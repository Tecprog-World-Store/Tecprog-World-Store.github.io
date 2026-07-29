#!/usr/bin/env python3
"""Valida cobertura, integridad y presentación del cronograma TW Educa."""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
SCHEDULE_ROOT = ROOT / "data" / "cronogramas"
BACKUP_REF = "pre-cronograma-anual-tw-educa-20260729"
EXPECTED_PERIODS = [
    "2026-08", "2026-09", "2026-10", "2026-11", "2026-12",
    "2027-01", "2027-02", "2027-03", "2027-04", "2027-05",
    "2027-06", "2027-07",
]
VALID_STATES = {
    "Inscripciones abiertas",
    "Cupos disponibles",
    "Próxima apertura",
    "Sujeto a mínimo de inscritos",
    "Inicio confirmado",
    "Inscripciones cerradas",
    "Reprogramado",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_generator():
    path = ROOT / "tools" / "generar_cronograma_anual_tw_educa.py"
    spec = importlib.util.spec_from_file_location("tw_schedule_generator", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class MetricsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.counts = Counter()
        self.hrefs = []
        self.images = []
        self.meta = []

    def handle_starttag(self, tag, attrs):
        self.counts[tag] += 1
        data = dict(attrs)
        if tag == "a" and data.get("href"):
            self.hrefs.append(data["href"])
        if tag == "img" and data.get("src"):
            self.images.append(data["src"])
        if tag == "meta":
            self.meta.append((data.get("name") or data.get("property"), data.get("content")))


def html_metrics(text: str) -> MetricsParser:
    parser = MetricsParser()
    parser.feed(text)
    return parser


def git_file(ref: str, relative: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{ref}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout


def validate_preserved_content() -> int:
    paths = sorted((ROOT / "cursos").glob("*/index.html"))
    paths += sorted((ROOT / "catalogo" / "cursos").glob("*.html"))
    protected_tags = ("h1", "h2", "h3", "h4", "section", "article", "p", "li", "a", "button", "img", "meta")
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        before_text = git_file(BACKUP_REF, relative)
        after_text = path.read_text(encoding="utf-8-sig")
        before = html_metrics(before_text)
        after = html_metrics(after_text)
        for tag in protected_tags:
            if after.counts[tag] < before.counts[tag]:
                fail(f"Contenido reducido en {relative}: <{tag}> {before.counts[tag]} -> {after.counts[tag]}")
        if not set(before.images).issubset(after.images):
            fail(f"Se retiraron imágenes en {relative}")
        if not set(before.hrefs).issubset(after.hrefs):
            fail(f"Se retiraron enlaces en {relative}")
        if not set(before.meta).issubset(after.meta):
            fail(f"Se retiraron metadatos en {relative}")
        price_tokens = set(re.findall(r"(?:S/\s*\d+|USD\s*\d+)", before_text))
        if not price_tokens.issubset(set(re.findall(r"(?:S/\s*\d+|USD\s*\d+)", after_text))):
            fail(f"Se alteraron o retiraron precios publicados en {relative}")
        if "data-course-schedule" not in after_text or "cronograma-tw-educa.js" not in after_text:
            fail(f"Página de curso sin integración de cronograma: {relative}")
    return len(paths)


def validate_whatsapp(entry: dict, course: dict) -> None:
    parsed = urlparse(entry["enlace_inscripcion"])
    if parsed.netloc != "wa.me" or parsed.path.strip("/") != "51952354282":
        fail(f"WhatsApp inválido: {entry['id']}")
    message = parse_qs(parsed.query).get("text", [""])[0]
    year, month = map(int, entry["periodo"].split("-"))
    month_name = (
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
    )[month - 1]
    required = (course["nombre"], f"{month_name} de {year}", "UTC-05:00", "sujeta al mínimo")
    if not all(value in message for value in required):
        fail(f"Mensaje de WhatsApp incompleto: {entry['id']}")


def validate_data() -> tuple[int, int]:
    generator = load_generator()
    audited = generator.audit_courses()
    canonical = read_json(SCHEDULE_ROOT / "cursos.json")
    config = read_json(SCHEDULE_ROOT / "configuracion.json")
    current = read_json(SCHEDULE_ROOT / "actual.json")
    courses = canonical["cursos"]
    course_map = {course["id"]: course for course in courses}

    if len(audited) != 243 or len(courses) != len(audited):
        fail(f"Cantidad de cursos inesperada: auditados={len(audited)}, canónicos={len(courses)}")
    if {course["id"] for course in audited} != set(course_map):
        fail("La fuente canónica no coincide con la auditoría de cursos activos")
    if current["periodos_disponibles"] != EXPECTED_PERIODS:
        fail("Los doce periodos disponibles no cubren agosto 2026–julio 2027")
    if current["zona_horaria"] != "America/Lima" or current["utc"] != "UTC-05:00":
        fail("Metadatos de zona horaria inválidos")
    if config["minimo_general_inscritos"] != 5:
        fail("El mínimo general debe ser 5")
    if config["equivalencia_internacional"]["pen_por_usd"] != 3.411:
        fail("Tipo de cambio comercial inesperado")

    all_entries = []
    by_course = defaultdict(list)
    for period in EXPECTED_PERIODS:
        month = read_json(SCHEDULE_ROOT / f"{period}.json")
        entries = month["convocatorias"]
        if len(entries) != len(courses):
            fail(f"Cobertura incompleta en {period}: {len(entries)}")
        slots = Counter((entry["fecha_inicio"], entry["hora_inicio"]) for entry in entries)
        if any(count > 2 for count in slots.values()):
            fail(f"Más de dos inicios al mismo día y hora en {period}")
        seen_courses = set()
        seen_ids = set()
        for entry in entries:
            if entry["id"] in seen_ids or entry["curso_id"] in seen_courses:
                fail(f"Duplicado en {period}: {entry['id']}")
            seen_ids.add(entry["id"])
            seen_courses.add(entry["curso_id"])
            course = course_map.get(entry["curso_id"])
            if not course:
                fail(f"Curso inexistente en {entry['id']}")
            if entry["periodo"] != period or not entry["fecha_inicio"].startswith(period):
                fail(f"Periodo/fecha inconsistente en {entry['id']}")
            start = datetime.strptime(entry["hora_inicio"], "%H:%M")
            end = datetime.strptime(entry["hora_fin"], "%H:%M")
            datetime.strptime(entry["fecha_inicio"], "%Y-%m-%d")
            if end <= start:
                fail(f"Horario inválido en {entry['id']}")
            if entry["zona_horaria"] != "America/Lima" or entry["utc"] != "UTC-05:00":
                fail(f"Zona horaria inválida en {entry['id']}")
            if not isinstance(entry["minimo_inscritos"], int) or entry["minimo_inscritos"] < 1:
                fail(f"Mínimo inválido en {entry['id']}")
            if entry["estado"] not in VALID_STATES or entry["estado"] == "Inicio confirmado":
                fail(f"Estado no permitido para proyección sin inscritos: {entry['id']}")
            if entry["condicion"] != "Sujeto a mínimo de inscritos":
                fail(f"Condición comercial inválida en {entry['id']}")
            if entry.get("vacantes") is not None:
                fail(f"Vacantes simuladas en {entry['id']}")
            if entry["precio_pen"] != course["precio_pen"] or entry["precio_pen"] <= 0:
                fail(f"Precio PEN inconsistente en {entry['id']}")
            if not isinstance(entry.get("precio_usd"), int) or entry["precio_usd"] <= 0:
                fail(f"Precio USD ausente en {entry['id']}")
            validate_whatsapp(entry, course)
            all_entries.append(entry)
            by_course[entry["curso_id"]].append(entry)
        if seen_courses != set(course_map):
            fail(f"Faltan cursos en {period}")

    if len(all_entries) != 2916 or len({entry["id"] for entry in all_entries}) != 2916:
        fail("La cantidad total de convocatorias debe ser 2916 y sus IDs deben ser únicos")
    if any(len(items) != 12 for items in by_course.values()) or len(by_course) != 243:
        fail("Cada curso debe tener exactamente doce convocatorias")
    return len(courses), len(all_entries)


def validate_frontend_and_seo() -> None:
    annual = ROOT / "catalogo" / "cronograma-anual-tw-educa.html"
    text = annual.read_text(encoding="utf-8-sig")
    required = (
        'data-annual-schedule',
        'rel="canonical"',
        'property="og:title"',
        "Programación proyectada desde agosto de 2026 hasta julio de 2027",
        "cronograma-tw-educa.js",
    )
    if not all(value in text for value in required):
        fail("La página anual no contiene todos los elementos requeridos")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8-sig")
    if sitemap.count("<loc>") != 101 or "catalogo/cronograma-anual-tw-educa.html" not in sitemap:
        fail("Sitemap sin la nueva URL anual o cantidad distinta de 101")
    commercial = read_json(ROOT / "data" / "sitemap_comercial.json")
    if not any(item.get("ruta") == "catalogo/cronograma-anual-tw-educa.html" for item in commercial):
        fail("data/sitemap_comercial.json no incluye el cronograma anual")
    if "cronograma-anual-tw-educa.html" not in (ROOT / "educa" / "index.html").read_text(encoding="utf-8-sig"):
        fail("TW Educa no enlaza al cronograma anual")
    dynamic_detail = (ROOT / "detalle" / "curso.html").read_text(encoding="utf-8-sig")
    if "cronograma-tw-educa.js" not in dynamic_detail:
        fail("La página dinámica de detalle no carga el cronograma")


def validate_all_json() -> int:
    files = list(ROOT.rglob("*.json"))
    for path in files:
        read_json(path)
    return len(files)


def main() -> int:
    courses, convocations = validate_data()
    preserved_pages = validate_preserved_content()
    validate_frontend_and_seo()
    json_files = validate_all_json()
    print(
        "OK: cronograma TW Educa válido; "
        f"{courses} cursos, {convocations} convocatorias, "
        f"{preserved_pages} páginas protegidas y {json_files} JSON válidos."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
