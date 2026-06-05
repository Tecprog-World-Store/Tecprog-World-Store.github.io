from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PRIMARY = ROOT / "data" / "fuentes" / "catalogo_base_cursos_tw_educa.txt"
SOURCE_LEGACY = ROOT / "data" / "fuente" / "catalogo_base_cursos_tw_educa.txt"
OUTPUT = ROOT / "data" / "catalogo-general-cursos.json"


def slugify(text: str) -> str:
    replacements = str.maketrans(
        "áéíóúñüÁÉÍÓÚÑÜ",
        "aeiounuAEIOUNU",
    )
    clean = text.translate(replacements).lower()
    clean = re.sub(r"[^a-z0-9]+", "-", clean).strip("-")
    return clean


def read_source() -> Path:
    SOURCE_PRIMARY.parent.mkdir(parents=True, exist_ok=True)
    if not SOURCE_PRIMARY.exists() and SOURCE_LEGACY.exists():
        shutil.copyfile(SOURCE_LEGACY, SOURCE_PRIMARY)
    if not SOURCE_PRIMARY.exists():
        raise FileNotFoundError(f"No existe {SOURCE_PRIMARY}")
    return SOURCE_PRIMARY


def parse_number(value: str) -> int:
    digits = re.sub(r"[^0-9]", "", value or "")
    return int(digits) if digits else 0


def module_count(hours: int) -> int:
    if 80 <= hours <= 120:
        return 8
    if hours >= 48:
        return 6
    if hours >= 32:
        return 5
    if hours >= 20:
        return 4
    return 3


def topic_family(title: str, category: str) -> tuple[str, list[str]]:
    text = f"{title} {category}".lower()
    if any(word in text for word in ["qgis", "gis", "geoespacial", "territorio"]):
        return "GIS y analisis territorial", ["capas", "CRS", "mapas", "geoprocesamiento"]
    if any(word in text for word in ["openfoam", "cfd", "fluidos", "hidraul", "delft"]):
        return "modelamiento y simulacion", ["modelo", "malla", "condiciones de borde", "resultados"]
    if any(word in text for word in ["python", "programacion", "software", "base de datos", "web", "sistemas"]):
        return "software y sistemas", ["requerimientos", "datos", "codigo", "validacion"]
    if any(word in text for word in ["inteligencia artificial", "machine learning", "aprendizaje", "datos"]):
        return "datos e inteligencia artificial", ["datasets", "modelos", "metricas", "automatizacion"]
    if any(word in text for word in ["electron", "circuit", "control", "automatizacion"]):
        return "electronica y automatizacion", ["circuitos", "sensores", "control", "diagnostico"]
    return "fundamentos tecnicos", ["conceptos", "herramientas", "casos", "entregables"]


def build_syllabus(title: str, category: str, hours: int) -> list[dict]:
    count = module_count(hours)
    family, terms = topic_family(title, category)
    templates = [
        ("Fundamentos y contexto aplicado", ["Objetivos del curso", f"Conceptos clave de {family}", "Flujo de trabajo recomendado"]),
        ("Herramientas y configuracion inicial", ["Entorno de trabajo", f"Uso de {terms[0]} y {terms[1]}", "Buenas practicas de organizacion"]),
        ("Desarrollo de ejercicios guiados", ["Caso base paso a paso", f"Aplicacion de {terms[2]}", "Revision de errores frecuentes"]),
        ("Analisis de resultados y entregables", ["Interpretacion tecnica", f"Documentacion de {terms[3]}", "Presentacion de resultados"]),
        ("Proyecto aplicado integrador", ["Definicion del alcance", "Construccion del proyecto", "Criterios de evaluacion tecnica"]),
        ("Optimización, automatizacion y soporte", ["Mejoras del flujo", "Automatizacion de tareas", "Soporte y mantenimiento del entregable"]),
        ("Gestion del aprendizaje y portafolio", ["Evidencias de avance", "Organizacion de archivos", "Preparacion de portafolio tecnico"]),
        ("Cierre profesional", ["Retroalimentacion final", "Recomendaciones de continuidad", "Rutas de especializacion"]),
    ]
    return [
        {
            "modulo": index + 1,
            "titulo": templates[index][0],
            "contenidos": templates[index][1],
        }
        for index in range(count)
    ]


def load_existing_ids() -> set[str]:
    ids: set[str] = set()
    for rel in ["data/cursos/2026-06.json", "data/cursos.json"]:
        path = ROOT / rel
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for item in data:
            if item.get("id"):
                ids.add(item["id"])
            elif item.get("nombre"):
                ids.add(slugify(item["nombre"]))
            elif item.get("titulo"):
                ids.add(slugify(item["titulo"]))
    return ids


def parse_catalog(source: Path) -> list[dict]:
    rows = []
    header_seen = False
    for raw in source.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or "|" not in line:
            continue
        parts = [part.strip() for part in line.split("|")]
        if parts[0] == "id":
            header_seen = True
            continue
        if not header_seen or len(parts) < 13:
            continue
        rows.append(parts[:13])

    existing_ids = load_existing_ids()
    catalog = []
    seen = set()
    for parts in rows:
        (
            course_id,
            line,
            category,
            course,
            source_base,
            modality,
            hours,
            duration,
            price_pen,
            price_usd,
            level,
            priority,
            short_description,
        ) = parts
        course_id = course_id or slugify(course)
        if course_id in seen:
            continue
        seen.add(course_id)
        hour_count = parse_number(hours)
        price_pen_number = parse_number(price_pen)
        price_usd_number = parse_number(price_usd)
        item = {
            "id": course_id,
            "linea": line or "TW Educa",
            "categoria": category,
            "curso": course,
            "fuente_base": source_base,
            "modalidad": modality,
            "horas_certificables": hour_count,
            "duracion_referencial": duration,
            "precio_peru_igv_soles": price_pen_number,
            "precio_internacional_usd": price_usd_number,
            "nivel": level,
            "prioridad_web": priority,
            "descripcion_corta": short_description,
            "descripcion_larga": (
                f"Curso tecnico de {course} orientado a formacion aplicada para estudiantes, "
                "profesionales, equipos tecnicos e instituciones. El contenido se adapta al nivel, "
                "la duracion referencial y los objetivos comerciales definidos por Tecprog World E.I.R.L."
            ),
            "temario_base": build_syllabus(course, category, hour_count),
            "publico_objetivo": [
                "Estudiantes de ingenieria, software, ciencias o carreras tecnicas.",
                "Profesionales que requieren actualizar herramientas aplicadas.",
                "Equipos de empresas o instituciones que necesitan capacitacion a medida.",
            ],
            "incluye": [
                "Sesiones virtuales o grabadas segun modalidad coordinada.",
                "Material de apoyo digital preparado por Tecprog World.",
                "Orientacion por WhatsApp o correo durante el periodo acordado.",
            ],
            "certificacion": "Constancia o certificado de participacion emitido por Tecprog World E.I.R.L. segun modalidad y cumplimiento acordado.",
            "url_detalle": f"detalle/curso.html?id={course_id}&catalogo=general",
            "imagen": "assets/img/cursos/capacitacion-empresarial.svg",
            "whatsapp_message": f"Hola, deseo informacion sobre el curso {course} del catalogo general TW Educa.",
        }
        if course_id in existing_ids:
            item["origen_complementario"] = ["catalogo_base_cursos_tw_educa.txt"]
        catalog.append(item)
    return catalog


def main() -> int:
    source = read_source()
    catalog = parse_catalog(source)
    OUTPUT.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generados {len(catalog)} cursos en {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
