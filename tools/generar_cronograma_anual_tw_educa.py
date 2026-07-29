#!/usr/bin/env python3
"""Genera el cronograma móvil canónico de cursos TW Educa.

Uso:
  python tools/generar_cronograma_anual_tw_educa.py --inicio 2026-08 --meses 12 --dry-run
  python tools/generar_cronograma_anual_tw_educa.py --inicio 2026-08 --meses 12 --write
"""

from __future__ import annotations

import argparse
import calendar
import json
import math
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from html import unescape
from pathlib import Path
from typing import Any
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = DATA / "cronogramas"
WHATSAPP = "51952354282"
UPDATED_AT = "2026-07-29"
SCHEMA_VERSION = "1.0.0"
TIMEZONE = "America/Lima"
UTC_OFFSET = "UTC-05:00"
EXCHANGE_RATE = 3.411
EXCHANGE_DATE = "2026-07-24"

VALID_GROUPS = {"A", "B", "C", "D", "E"}
GROUP_RULES = {
    "A": {
        "nombre": "Cursos introductorios",
        "dias": "Martes y jueves",
        "preferred_weekdays": (1, 3),
        "times": (("19:00", "21:00"), ("18:30", "20:30"), ("20:00", "22:00")),
    },
    "B": {
        "nombre": "Programación y software",
        "dias": "Lunes y miércoles",
        "preferred_weekdays": (0, 2),
        "times": (("19:00", "21:00"), ("18:30", "20:30"), ("20:00", "22:00")),
    },
    "C": {
        "nombre": "Ingeniería y modelación",
        "dias": "Martes y jueves",
        "preferred_weekdays": (1, 3, 5),
        "times": (("20:00", "22:00"), ("19:00", "21:00"), ("15:00", "18:00")),
    },
    "D": {
        "nombre": "Realidad virtual y cursos prácticos intensivos",
        "dias": "Sábados",
        "preferred_weekdays": (5,),
        "times": (("15:00", "18:00"), ("09:00", "12:00"), ("18:00", "21:00")),
    },
    "E": {
        "nombre": "Cursos especializados de apertura mensual",
        "dias": "Sábados",
        "preferred_weekdays": (5, 4),
        "times": (("09:00", "12:00"), ("15:00", "18:00"), ("19:00", "21:00")),
    },
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFD", str(value or ""))
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")


def as_number(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)) and value > 0:
        return int(round(value))
    if isinstance(value, str):
        match = re.search(r"(?:S/\s*)?(\d+(?:[.,]\d+)?)", value)
        if match:
            return int(round(float(match.group(1).replace(",", "."))))
    return None


def clean_text(value: Any, fallback: str = "") -> str:
    return str(value or fallback).strip()


def group_for(course: dict[str, Any]) -> str:
    text = slugify(" ".join([
        course.get("nombre", ""),
        course.get("categoria", ""),
        course.get("descripcion", ""),
    ]))
    if any(key in text for key in (
        "realidad-virtual", "unity", "meta-quest", "vision-artificial",
        "taller", "demostracion", "prototip",
    )):
        return "D"
    if any(key in text for key in (
        "cfd", "openfoam", "qgis", "gis", "climatic", "oceanograf",
        "machine-learning", "gpu", "mecanica-de-fluidos", "hidraul",
        "estructur", "sap2000", "etabs", "delft", "modelacion",
    )):
        return "C"
    if any(key in text for key in (
        "python-poo", "c-plus", "csharp", "flutter", "desarrollo-web",
        "frontend", "software", "programacion", "plugins", "base-de-datos",
        "ingenieria-de-software", "algoritm", "aplicaciones-moviles",
    )):
        return "B"
    if any(key in text for key in (
        "excel", "python-basico", "latex", "ofimatica", "informatica-basica",
        "introduccion", "fundamentos", "nivel-i", "admision",
    )):
        return "A"
    return "E"


def international_price(pen: int, official_usd: Any) -> tuple[int, str]:
    official = as_number(official_usd)
    if official:
        return official, "precio_oficial_catalogo_general"
    return int(math.ceil(pen / EXCHANGE_RATE)), "equivalencia_comercial_configurada"


def canonical_course(
    *,
    course_id: str,
    slug: str,
    name: str,
    category: str,
    modality: str,
    duration: str,
    pen: int,
    official_usd: Any,
    detail_url: str,
    source: str,
    description: str = "",
    minimum: int = 5,
) -> dict[str, Any]:
    usd, usd_source = international_price(pen, official_usd)
    course = {
        "id": course_id,
        "slug": slug,
        "nombre": name,
        "categoria": category or "Curso técnico",
        "modalidad": modality or "Online en vivo",
        "duracion": duration or "Consultar duración académica publicada",
        "precio_pen": pen,
        "precio_usd": usd,
        "precio_usd_fuente": usd_source,
        "minimo_inscritos": minimum,
        "url_detalle": detail_url,
        "fuente_canonica_contenido": source,
        "descripcion": description,
    }
    course["grupo_cronograma"] = group_for(course)
    return course


def load_general_courses() -> list[dict[str, Any]]:
    result = []
    for item in read_json(DATA / "catalogo-general-cursos.json"):
        pen = as_number(item.get("precio_peru_igv_soles"))
        if not pen:
            raise ValueError(f"Curso general sin precio PEN: {item.get('id')}")
        result.append(canonical_course(
            course_id=item["id"],
            slug=item["id"],
            name=item["curso"],
            category=item.get("categoria", ""),
            modality=item.get("modalidad", "Online en vivo"),
            duration=item.get("duracion_referencial", ""),
            pen=pen,
            official_usd=item.get("precio_internacional_usd"),
            detail_url=f"detalle/curso.html?id={quote(item['id'])}&catalogo=general",
            source="data/catalogo-general-cursos.json",
            description=item.get("descripcion_corta", ""),
        ))
    return result


def load_dedicated_courses() -> list[dict[str, Any]]:
    result = []
    for item in read_json(DATA / "cursos_tw_educa.json"):
        if item.get("visible_cliente") is False or item.get("estado_publicacion") != "publicado":
            continue
        pen = as_number(item.get("precio_soles"))
        if not pen:
            raise ValueError(f"Curso dedicado sin precio PEN: {item.get('id')}")
        result.append(canonical_course(
            course_id=item["id"],
            slug=item["slug"],
            name=item["nombre"],
            category=item.get("categoria", ""),
            modality="Online en vivo" if item.get("modalidad") == "Online" else item.get("modalidad", ""),
            duration=item.get("duracion", ""),
            pen=pen,
            official_usd=None,
            detail_url=item.get("url_detalle", f"cursos/{item['slug']}/"),
            source="data/cursos_tw_educa.json",
            description=item.get("descripcion_corta", ""),
            minimum=as_number(item.get("minimo_inscritos")) or 5,
        ))
    return result


def legacy_data_sources() -> dict[str, dict[str, Any]]:
    sources: dict[str, dict[str, Any]] = {}
    for item in read_json(DATA / "cursos.json"):
        sources[item["slug"]] = {
            "nombre": item.get("nombre", item["slug"]),
            "categoria": item.get("categoria", "Curso técnico"),
            "modalidad": item.get("modalidad", "Online en vivo"),
            "duracion": item.get("duracion", ""),
            "precio_pen": as_number(item.get("precio_peru_soles_igv") or item.get("precio_desde") or item.get("precio")),
            "precio_usd": item.get("precio_usd"),
            "descripcion": item.get("descripcion", ""),
            "fuente": "data/cursos.json",
        }
    for item in read_json(DATA / "cursos" / "2026-06.json"):
        sources[item["id"]] = {
            "nombre": item.get("titulo", item["id"]),
            "categoria": item.get("categoria", "Curso técnico"),
            "modalidad": "Online en vivo",
            "duracion": item.get("duracion", ""),
            "precio_pen": as_number(item.get("precio_peru_soles_igv") or item.get("precio_desde")),
            "precio_usd": item.get("precio_usd"),
            "descripcion": item.get("descripcion_corta", ""),
            "fuente": "data/cursos/2026-06.json",
        }
    main_js = (ROOT / "assets" / "js" / "main.js").read_text(encoding="utf-8-sig")
    pattern = re.compile(
        r'item\("(?P<id>[^"]+)",\s*"(?P<name>[^"]+)",\s*"TW Educa",\s*'
        r'"(?P<category>[^"]+)",\s*"(?P<description>[^"]*)",\s*"[^"]*",\s*'
        r'"(?P<price>[^"]+)",\s*"(?P<modality>[^"]+)"'
    )
    for match in pattern.finditer(main_js):
        course_id = match.group("id")
        sources.setdefault(course_id, {
            "nombre": match.group("name"),
            "categoria": match.group("category"),
            "modalidad": match.group("modality"),
            "duracion": "",
            "precio_pen": as_number(match.group("price")),
            "precio_usd": None,
            "descripcion": match.group("description"),
            "fuente": "assets/js/main.js",
        })
    return sources


def html_text(pattern: str, html: str) -> str:
    match = re.search(pattern, html, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    return re.sub(r"<[^>]+>", "", unescape(match.group(1))).strip()


def load_legacy_pages(existing_ids: set[str]) -> list[dict[str, Any]]:
    sources = legacy_data_sources()
    result = []
    for path in sorted((ROOT / "catalogo" / "cursos").glob("*.html")):
        course_id = path.stem
        if course_id in existing_ids:
            continue
        html = path.read_text(encoding="utf-8-sig")
        known = sources.get(course_id, {})
        name = known.get("nombre") or html_text(r"<h1[^>]*>(.*?)</h1>", html) or html_text(r"<title>(.*?)</title>", html)
        category = known.get("categoria") or html_text(r'class="eyebrow"[^>]*>(.*?)</', html) or "Curso técnico"
        pen = known.get("precio_pen")
        if not pen:
            prices = [int(value) for value in re.findall(r"S/\s*(\d+)", html)]
            pen = min(prices) if prices else None
        if not pen:
            raise ValueError(f"Página de curso sin precio PEN verificable: {path.relative_to(ROOT)}")
        result.append(canonical_course(
            course_id=course_id,
            slug=course_id,
            name=name,
            category=category,
            modality=known.get("modalidad", "Online en vivo"),
            duration=known.get("duracion", ""),
            pen=pen,
            official_usd=known.get("precio_usd"),
            detail_url=path.relative_to(ROOT).as_posix(),
            source=known.get("fuente", path.relative_to(ROOT).as_posix()),
            description=known.get("descripcion", ""),
        ))
    return result


def audit_courses() -> list[dict[str, Any]]:
    courses = load_general_courses()
    ids = {course["id"] for course in courses}
    for course in load_dedicated_courses():
        if course["id"] in ids:
            raise ValueError(f"ID de curso duplicado: {course['id']}")
        courses.append(course)
        ids.add(course["id"])
    courses.extend(load_legacy_pages(ids))
    courses.sort(key=lambda item: (item["categoria"], item["nombre"], item["id"]))
    duplicates = [key for key, count in Counter(item["id"] for item in courses).items() if count > 1]
    if duplicates:
        raise ValueError(f"IDs duplicados: {duplicates}")
    return courses


def add_months(start: str, count: int) -> list[str]:
    year, month = map(int, start.split("-"))
    result = []
    for offset in range(count):
        absolute = year * 12 + month - 1 + offset
        result.append(f"{absolute // 12:04d}-{absolute % 12 + 1:02d}")
    return result


def candidate_slots(period: str, group: str) -> list[tuple[date, str, str]]:
    year, month = map(int, period.split("-"))
    rule = GROUP_RULES[group]
    days = [
        date(year, month, day)
        for day in range(1, calendar.monthrange(year, month)[1] + 1)
        if date(year, month, day).weekday() in rule["preferred_weekdays"]
        and not (month == 1 and day == 1)
        and not (month == 12 and day == 25)
    ]
    # Semanas iniciales y medias primero; después se utiliza todo el mes.
    days.sort(key=lambda value: (0 if 5 <= value.day <= 21 else 1, value.day))
    return [(day, start, end) for day in days for start, end in rule["times"]]


def fallback_slots(period: str) -> list[tuple[date, str, str]]:
    year, month = map(int, period.split("-"))
    times = (
        ("18:00", "20:00"), ("18:30", "20:30"), ("19:00", "21:00"),
        ("19:30", "21:30"), ("20:00", "22:00"), ("20:30", "22:30"),
    )
    result = []
    for day_number in range(1, calendar.monthrange(year, month)[1] + 1):
        day = date(year, month, day_number)
        if day.weekday() == 6 or (month == 1 and day_number == 1) or (month == 12 and day_number == 25):
            continue
        result.extend((day, start, end) for start, end in times)
    return result


def month_name(period: str) -> str:
    year, month = map(int, period.split("-"))
    names = (
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
    )
    return f"{names[month - 1]} de {year}"


def weekday_name(value: date) -> str:
    return ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")[value.weekday()]


def whatsapp_url(course: dict[str, Any], period: str, start: date, rule: dict[str, Any]) -> str:
    price = f"S/ {course['precio_pen']} PEN | USD {course['precio_usd']}"
    message = (
        f'Hola, deseo información e inscribirme en el curso "{course["nombre"]}".\n\n'
        f"Convocatoria: {month_name(period)}.\n"
        f"Inicio tentativo: {weekday_name(start)} {start.day} de {month_name(period)}.\n"
        f"Horario: {rule['dias'].lower()}, {rule['hora_inicio']}–{rule['hora_fin']}.\n"
        f"Hora oficial: Lima, Perú, UTC-05:00.\n"
        f"Modalidad: {course['modalidad']}.\n"
        f"Precio: {price}.\n"
        "Comprendo que la apertura está sujeta al mínimo de inscritos."
    )
    return f"https://wa.me/{WHATSAPP}?text={quote(message)}"


def preserved_manual_entries(period: str) -> dict[str, dict[str, Any]]:
    path = OUTPUT / f"{period}.json"
    if not path.exists():
        return {}
    data = read_json(path)
    entries = data.get("convocatorias", []) if isinstance(data, dict) else []
    return {
        entry["curso_id"]: entry
        for entry in entries
        if entry.get("bloqueado_manualmente") is True
    }


def build_month(period: str, courses: list[dict[str, Any]]) -> dict[str, Any]:
    occupancy: Counter[tuple[str, str]] = Counter()
    manual = preserved_manual_entries(period)
    convocations = []
    candidates_by_group = {group: candidate_slots(period, group) for group in VALID_GROUPS}
    fallback = fallback_slots(period)
    group_positions: Counter[str] = Counter()

    for course in courses:
        if course["id"] in manual:
            entry = manual[course["id"]]
            key = (entry["fecha_inicio"], entry["hora_inicio"])
            occupancy[key] += 1
            convocations.append(entry)
            continue

        group = course["grupo_cronograma"]
        candidates = candidates_by_group[group]
        start_index = group_positions[group] % max(len(candidates), 1)
        ordered = candidates[start_index:] + candidates[:start_index] + fallback
        selected = None
        for start_date, start_time, end_time in ordered:
            key = (start_date.isoformat(), start_time)
            if occupancy[key] < 2:
                selected = (start_date, start_time, end_time)
                occupancy[key] += 1
                break
        if not selected:
            raise ValueError(f"No hay horario disponible para {course['id']} en {period}")
        group_positions[group] += 1
        start_date, start_time, end_time = selected
        rule = GROUP_RULES[group]
        public_rule = {
            "dias": rule["dias"],
            "hora_inicio": start_time,
            "hora_fin": end_time,
        }
        convocation_id = f"{course['id']}--{period}"
        convocations.append({
            "id": convocation_id,
            "curso_id": course["id"],
            "periodo": period,
            "fecha_inicio": start_date.isoformat(),
            "fecha_fin_estimada": None,
            "dias_clase": rule["dias"],
            "hora_inicio": start_time,
            "hora_fin": end_time,
            "zona_horaria": TIMEZONE,
            "utc": UTC_OFFSET,
            "modalidad": course["modalidad"],
            "minimo_inscritos": course["minimo_inscritos"],
            "estado": "Inscripciones abiertas",
            "condicion": "Sujeto a mínimo de inscritos",
            "vacantes": None,
            "precio_pen": course["precio_pen"],
            "precio_usd": course["precio_usd"],
            "precio_usd_fuente": course["precio_usd_fuente"],
            "enlace_inscripcion": whatsapp_url(course, period, start_date, public_rule),
            "nota_confirmacion": "Apertura sujeta al mínimo de inscritos. Fecha y horario tentativos; la fecha exacta puede coordinarse con el grupo inscrito.",
            "fecha_actualizacion": UPDATED_AT,
            "bloqueado_manualmente": False,
        })

    return {
        "schema_version": SCHEMA_VERSION,
        "periodo": period,
        "zona_horaria": TIMEZONE,
        "utc": UTC_OFFSET,
        "fecha_actualizacion": UPDATED_AT,
        "convocatorias": sorted(convocations, key=lambda item: (item["fecha_inicio"], item["hora_inicio"], item["curso_id"])),
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
        "nota_zona_horaria": "Los horarios se presentan en la hora oficial de Lima, Perú (UTC-05:00). Los participantes internacionales deben verificar la equivalencia con su zona horaria.",
        "whatsapp": WHATSAPP,
        "correo_comercial": "grupotecprog@gmail.com",
        "moneda_local": "PEN",
        "moneda_internacional": "USD",
        "equivalencia_internacional": {
            "pen_por_usd": EXCHANGE_RATE,
            "fecha_referencia": EXCHANGE_DATE,
            "fuente": "SBS Perú, cotización de venta del dólar de N.A.; fuente de mercado BCRP",
            "url_fuente": "https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx",
            "criterio_redondeo": "Redondeo comercial hacia arriba al dólar entero para cursos sin precio USD oficial.",
            "nota": "El importe internacional es referencial y puede variar por conversión de moneda, comisión de PayPal o entidad financiera. No se agregan comisiones al cálculo mostrado.",
        },
        "grupos": GROUP_RULES,
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == rendered:
        return
    path.write_text(rendered, encoding="utf-8", newline="\n")


def validate_generated(periods: list[str], courses: list[dict[str, Any]], months: list[dict[str, Any]]) -> None:
    expected_ids = {course["id"] for course in courses}
    for month in months:
        entries = month["convocatorias"]
        ids = [entry["curso_id"] for entry in entries]
        if len(entries) != len(courses) or set(ids) != expected_ids or len(ids) != len(set(ids)):
            raise ValueError(f"Cobertura inválida en {month['periodo']}")
        slots = Counter((entry["fecha_inicio"], entry["hora_inicio"]) for entry in entries)
        if any(count > 2 for count in slots.values()):
            raise ValueError(f"Más de dos inicios simultáneos en {month['periodo']}")
        for entry in entries:
            datetime.strptime(entry["fecha_inicio"], "%Y-%m-%d")
            datetime.strptime(entry["hora_inicio"], "%H:%M")
            datetime.strptime(entry["hora_fin"], "%H:%M")
            if entry["zona_horaria"] != TIMEZONE or entry["utc"] != UTC_OFFSET:
                raise ValueError(f"Zona horaria inválida en {entry['id']}")
            if entry["estado"] == "Inicio confirmado":
                raise ValueError(f"Confirmación no permitida sin inscritos verificables: {entry['id']}")
    if [month["periodo"] for month in months] != periods:
        raise ValueError("Los periodos generados no coinciden con la solicitud")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inicio", default="2026-08", help="Periodo inicial YYYY-MM")
    parser.add_argument("--meses", type=int, default=12)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    datetime.strptime(args.inicio, "%Y-%m")
    if args.meses < 1:
        parser.error("--meses debe ser mayor que cero")

    courses = audit_courses()
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
