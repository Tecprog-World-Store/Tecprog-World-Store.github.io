#!/usr/bin/env python3
"""Genera el cronograma móvil de los 37 cursos publicados en TW Educa."""

from __future__ import annotations

import argparse
import calendar
import json
import math
from collections import Counter
from copy import deepcopy
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = DATA / "cronogramas"
PUBLIC_LIST = OUTPUT / "cursos_tw_educa_publicados.json"
COURSE_SOURCE = DATA / "cursos_tw_educa.json"
USD_OUTPUT = DATA / "precios_internacionales_tw_educa.json"

SCHEMA_VERSION = "2.0.0"
UPDATED_AT = "2026-07-29"
TIMEZONE = "America/Lima"
UTC_OFFSET = "UTC-05:00"
WHATSAPP = "51952354282"
EXPECTED_COURSES = 37
EXCHANGE_RATE = 3.411
EXCHANGE_DATE = "2026-07-24"
EXCHANGE_REVIEW_DATE = "2026-07-29"
PRICE_STAGES = ("preventa", "lanzamiento", "regular")

GROUP_RULES = {
    "A": {
        "nombre": "Cursos introductorios",
        "dias": "Martes y jueves",
        "weekdays": (1, 3),
        "times": (("19:00", "21:00"), ("18:30", "20:30"), ("20:00", "22:00")),
    },
    "B": {
        "nombre": "Programación y software",
        "dias": "Lunes y miércoles",
        "weekdays": (0, 2),
        "times": (("19:00", "21:00"), ("18:30", "20:30"), ("20:00", "22:00")),
    },
    "C": {
        "nombre": "Ingeniería y modelación",
        "dias": "Martes y jueves",
        "weekdays": (1, 3, 5),
        "times": (("20:00", "22:00"), ("19:00", "21:00"), ("15:00", "18:00")),
    },
    "D": {
        "nombre": "Realidad virtual e intensivos",
        "dias": "Sábados",
        "weekdays": (5,),
        "times": (("15:00", "18:00"), ("09:00", "12:00"), ("18:00", "21:00")),
    },
    "E": {
        "nombre": "Cursos especializados",
        "dias": "Sábados",
        "weekdays": (5, 4),
        "times": (("09:00", "12:00"), ("15:00", "18:00"), ("19:00", "21:00")),
    },
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if not path.exists() or path.read_text(encoding="utf-8") != rendered:
        path.write_text(rendered, encoding="utf-8", newline="\n")


def published_ids() -> list[str]:
    payload = read_json(PUBLIC_LIST)
    ids = payload.get("curso_ids", [])
    if payload.get("total_cursos") != EXPECTED_COURSES or len(ids) != EXPECTED_COURSES:
        raise ValueError("La lista cerrada debe contener exactamente 37 IDs")
    if len(set(ids)) != EXPECTED_COURSES:
        raise ValueError("La lista cerrada contiene IDs duplicados")
    return ids


def group_for(course: dict[str, Any]) -> str:
    text = f"{course.get('nombre', '')} {course.get('categoria', '')}".lower()
    if any(word in text for word in ("realidad virtual", "meta quest", "visión artificial")):
        return "D"
    if any(word in text for word in (
        "python poo", "python web", "frontend", "flutter", "c++", "c#", "programación",
        "plugin", "gnu/linux", "ia offline",
    )):
        return "B"
    if any(word in text for word in (
        "excel", "informática básica", "latex", "autocad nivel i", "python básico",
    )):
        return "A"
    if any(word in text for word in (
        "openfoam", "cfd", "qgis", "climát", "ocean", "fluidos", "estructural",
        "sap2000", "etabs", "revit", "inventor", "solidworks", "freecad", "matlab",
        "gpu", "geoportal", "costos y presupuestos",
    )):
        return "C"
    return "E"


def usd_profile(course_id: str, profile: dict[str, Any]) -> dict[str, Any]:
    result = {"publico": profile["publico"]}
    for stage in PRICE_STAGES:
        pen_key = f"{stage}_soles"
        if pen_key in profile:
            result[f"{stage}_usd"] = int(math.ceil(profile[pen_key] / EXCHANGE_RATE))
    result["criterio"] = "conversion_configurada"
    result["fecha_referencia"] = EXCHANGE_DATE
    return result


def load_published_courses() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    ids = published_ids()
    source = read_json(COURSE_SOURCE)
    source_map = {item["id"]: item for item in source}
    visible_ids = [
        item["id"] for item in source
        if item.get("visible_cliente") is True and item.get("estado_publicacion") == "publicado"
    ]
    if visible_ids != ids:
        raise ValueError("La lista cerrada no coincide, en orden, con los 37 cursos visibles publicados")

    courses = []
    usd_courses = []
    for course_id in ids:
        item = source_map.get(course_id)
        if not item:
            raise ValueError(f"ID publicado inexistente: {course_id}")
        pen_profiles = deepcopy(item.get("precios") or [])
        if not pen_profiles:
            raise ValueError(f"Curso sin perfiles PEN: {course_id}")
        usd_profiles = [usd_profile(course_id, profile) for profile in pen_profiles]
        course = {
            "id": course_id,
            "slug": item["slug"],
            "nombre": item["nombre"],
            "categoria": item["categoria"],
            "imagen": item["imagen"],
            "modalidad": "Online en vivo" if item.get("modalidad") == "Online" else item.get("modalidad"),
            "estado_comercial": item.get("estado_publico", "Próxima convocatoria"),
            "duracion": item.get("duracion", ""),
            "minimo_inscritos": int(item.get("minimo_inscritos") or 5),
            "url_detalle": item["url_detalle"],
            "fuente_canonica_contenido": "data/cursos_tw_educa.json",
            "precios_pen": pen_profiles,
            "precios_usd": usd_profiles,
        }
        course["grupo_cronograma"] = group_for(course)
        courses.append(course)
        usd_courses.append({
            "curso_id": course_id,
            "moneda": "USD",
            "perfiles": usd_profiles,
            "criterio": "conversion_configurada",
            "fecha_referencia": EXCHANGE_DATE,
        })

    usd_data = {
        "schema_version": SCHEMA_VERSION,
        "fecha_actualizacion": UPDATED_AT,
        "configuracion": {
            "pen_por_usd": EXCHANGE_RATE,
            "fecha_referencia": EXCHANGE_DATE,
            "fecha_revision": EXCHANGE_REVIEW_DATE,
            "fuente": "SBS Perú, cotización de venta del dólar de N.A.; referencia de mercado BCRP",
            "url_fuente": "https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx",
            "criterio_redondeo": "Redondeo comercial hacia arriba al dólar entero.",
            "nota": "El importe internacional es referencial. PayPal o la entidad financiera pueden aplicar conversión o comisión.",
        },
        "total_cursos": len(usd_courses),
        "cursos": usd_courses,
    }
    return courses, usd_data


def add_months(start: str, count: int) -> list[str]:
    year, month = map(int, start.split("-"))
    periods = []
    for offset in range(count):
        absolute = year * 12 + month - 1 + offset
        periods.append(f"{absolute // 12:04d}-{absolute % 12 + 1:02d}")
    return periods


def month_name(period: str) -> str:
    year, month = map(int, period.split("-"))
    names = (
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
    )
    return f"{names[month - 1]} de {year}"


def weekday_name(value: date) -> str:
    return ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")[value.weekday()]


def candidate_slots(period: str, group: str) -> list[tuple[date, str, str]]:
    year, month = map(int, period.split("-"))
    rule = GROUP_RULES[group]
    dates = [
        date(year, month, day)
        for day in range(1, calendar.monthrange(year, month)[1] + 1)
        if date(year, month, day).weekday() in rule["weekdays"]
        and not (month == 1 and day == 1)
        and not (month == 12 and day == 25)
    ]
    dates.sort(key=lambda value: (0 if 5 <= value.day <= 21 else 1, value.day))
    return [(day, start, end) for day in dates for start, end in rule["times"]]


def whatsapp_url(course: dict[str, Any], period: str, start: date, start_time: str, end_time: str) -> str:
    message = (
        f'Hola, deseo información sobre el curso "{course["nombre"]}".\n\n'
        f"Convocatoria: {month_name(period)}.\n"
        f"Inicio tentativo: {weekday_name(start)} {start.day} de {month_name(period)}.\n"
        f"Horario: {GROUP_RULES[course['grupo_cronograma']]['dias'].lower()}, {start_time}–{end_time}.\n"
        "Hora de referencia: Lima, Perú, UTC-05:00.\n"
        f"Modalidad: {course['modalidad']}.\n\n"
        "Deseo confirmar vacante, tarifa aplicable, perfil comercial y modalidad de pago."
    )
    return f"https://wa.me/{WHATSAPP}?text={quote(message)}"


def preserved_manual_entries(period: str, valid_ids: set[str]) -> dict[str, dict[str, Any]]:
    path = OUTPUT / f"{period}.json"
    if not path.exists():
        return {}
    entries = read_json(path).get("convocatorias", [])
    return {
        entry["curso_id"]: entry
        for entry in entries
        if entry.get("bloqueado_manualmente") is True and entry.get("curso_id") in valid_ids
    }


def build_month(period: str, courses: list[dict[str, Any]]) -> dict[str, Any]:
    occupancy: Counter[tuple[str, str]] = Counter()
    positions: Counter[str] = Counter()
    manual = preserved_manual_entries(period, {course["id"] for course in courses})
    entries = []
    for course in courses:
        if course["id"] in manual:
            entry = deepcopy(manual[course["id"]])
            entry.pop("precio_pen", None)
            entry.pop("precio_usd", None)
            entry.pop("precio_usd_fuente", None)
            entries.append(entry)
            occupancy[(entry["fecha_inicio"], entry["hora_inicio"])] += 1
            continue

        group = course["grupo_cronograma"]
        slots = candidate_slots(period, group)
        start_index = positions[group] % len(slots)
        ordered = slots[start_index:] + slots[:start_index]
        selected = next(
            slot for slot in ordered
            if occupancy[(slot[0].isoformat(), slot[1])] < 2
        )
        positions[group] += 1
        start_date, start_time, end_time = selected
        occupancy[(start_date.isoformat(), start_time)] += 1
        entries.append({
            "id": f"{course['id']}--{period}",
            "curso_id": course["id"],
            "periodo": period,
            "fecha_inicio": start_date.isoformat(),
            "dias_clase": GROUP_RULES[group]["dias"],
            "hora_inicio": start_time,
            "hora_fin": end_time,
            "zona_horaria": TIMEZONE,
            "utc": UTC_OFFSET,
            "modalidad": course["modalidad"],
            "minimo_inscritos": course["minimo_inscritos"],
            "estado": "Inscripciones abiertas",
            "condicion": "Sujeto a mínimo de inscritos",
            "enlace_inscripcion": whatsapp_url(course, period, start_date, start_time, end_time),
            "nota_confirmacion": "Fecha y horario tentativos. Apertura sujeta al mínimo de inscritos.",
            "fecha_actualizacion": UPDATED_AT,
            "bloqueado_manualmente": False,
        })
    entries.sort(key=lambda item: (item["fecha_inicio"], item["hora_inicio"], item["curso_id"]))
    return {
        "schema_version": SCHEMA_VERSION,
        "periodo": period,
        "zona_horaria": TIMEZONE,
        "utc": UTC_OFFSET,
        "fecha_actualizacion": UPDATED_AT,
        "convocatorias": entries,
    }


def configuration() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "fecha_actualizacion": UPDATED_AT,
        "zona_horaria": TIMEZONE,
        "utc": UTC_OFFSET,
        "pais_referencia": "Perú",
        "modalidad_predeterminada": "Online en vivo",
        "minimo_general_inscritos": 5,
        "estado_inicial": "Inscripciones abiertas",
        "condicion_inicial": "Sujeto a mínimo de inscritos",
        "politica_confirmacion": "No se declara inicio confirmado sin alcanzar y verificar el mínimo de inscritos.",
        "politica_reprogramacion": "Si no se alcanza el mínimo, la reserva puede trasladarse a la siguiente convocatoria o coordinar una alternativa conforme a las condiciones comerciales vigentes.",
        "nota_fechas": "Las fechas y horarios son tentativos. La fecha exacta puede coordinarse con el grupo inscrito.",
        "nota_zona_horaria": "Los horarios se expresan en la hora de Lima, Perú (UTC-05:00). Si visitas la página desde otra zona horaria, se mostrará una equivalencia local orientativa.",
        "whatsapp": WHATSAPP,
        "correo_comercial": "grupotecprog@gmail.com",
        "moneda_local": "PEN",
        "moneda_internacional": "USD",
        "equivalencia_internacional": {
            "pen_por_usd": EXCHANGE_RATE,
            "fecha_referencia": EXCHANGE_DATE,
            "fecha_revision": EXCHANGE_REVIEW_DATE,
            "fuente": "SBS Perú, cotización de venta del dólar de N.A.; referencia de mercado BCRP",
            "url_fuente": "https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx",
            "criterio_redondeo": "Redondeo comercial hacia arriba al dólar entero.",
            "nota": "El importe internacional es referencial. PayPal o la entidad financiera pueden aplicar conversión o comisión.",
        },
        "grupos": GROUP_RULES,
    }


def validate_generated(periods: list[str], courses: list[dict[str, Any]], months: list[dict[str, Any]]) -> None:
    valid_ids = {course["id"] for course in courses}
    if len(courses) != EXPECTED_COURSES:
        raise ValueError("Deben existir exactamente 37 cursos")
    for month in months:
        entries = month["convocatorias"]
        ids = [entry["curso_id"] for entry in entries]
        if len(entries) != EXPECTED_COURSES or set(ids) != valid_ids or len(ids) != len(set(ids)):
            raise ValueError(f"Cobertura inválida en {month['periodo']}")
        if any(count > 2 for count in Counter((e["fecha_inicio"], e["hora_inicio"]) for e in entries).values()):
            raise ValueError(f"Más de dos inicios simultáneos en {month['periodo']}")
        for entry in entries:
            datetime.strptime(entry["fecha_inicio"], "%Y-%m-%d")
            datetime.strptime(entry["hora_inicio"], "%H:%M")
            datetime.strptime(entry["hora_fin"], "%H:%M")
            if entry["zona_horaria"] != TIMEZONE or entry["utc"] != UTC_OFFSET:
                raise ValueError(f"Zona horaria inválida: {entry['id']}")
            if any(key in entry for key in ("precio_pen", "precio_usd", "precio_usd_fuente")):
                raise ValueError(f"Precio simplificado incrustado en convocatoria: {entry['id']}")
    if len(months) * EXPECTED_COURSES != 444 or [m["periodo"] for m in months] != periods:
        raise ValueError("El cronograma debe contener 444 convocatorias en los doce periodos solicitados")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inicio", default="2026-08")
    parser.add_argument("--meses", type=int, default=12)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    datetime.strptime(args.inicio, "%Y-%m")
    if args.meses != 12:
        parser.error("--meses debe ser 12 para el periodo publicado")

    courses, usd_data = load_published_courses()
    periods = add_months(args.inicio, args.meses)
    months = [build_month(period, courses) for period in periods]
    validate_generated(periods, courses, months)
    result = {
        "modo": "write" if args.write else "dry-run",
        "periodo_inicial": periods[0],
        "periodo_final": periods[-1],
        "cursos": len(courses),
        "convocatorias": sum(len(month["convocatorias"]) for month in months),
        "periodos": len(periods),
        "grupos": dict(Counter(course["grupo_cronograma"] for course in courses)),
    }
    if args.write:
        write_json(OUTPUT / "configuracion.json", configuration())
        write_json(OUTPUT / "cursos.json", {
            "schema_version": SCHEMA_VERSION,
            "fecha_actualizacion": UPDATED_AT,
            "total_cursos": len(courses),
            "cursos": courses,
        })
        write_json(USD_OUTPUT, usd_data)
        for month in months:
            write_json(OUTPUT / f"{month['periodo']}.json", month)
        write_json(OUTPUT / "actual.json", {
            "schema_version": SCHEMA_VERSION,
            "fecha_actualizacion": UPDATED_AT,
            "periodo_vigente": periods[0],
            "periodo_final": periods[-1],
            "periodos_disponibles": periods,
            "zona_horaria": TIMEZONE,
            "utc": UTC_OFFSET,
            "total_cursos": len(courses),
            "total_convocatorias": sum(len(month["convocatorias"]) for month in months),
        })
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
