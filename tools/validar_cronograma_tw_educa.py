#!/usr/bin/env python3
"""Valida el cronograma cerrado de los 37 cursos publicados en TW Educa."""

from __future__ import annotations

import json
import math
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
SCHEDULE_ROOT = ROOT / "data" / "cronogramas"
BACKUP_REF = "pre-correccion-cronograma-37-cursos-20260729"
EXPECTED_COURSES = 37
EXPECTED_CONVOCATIONS = 444
EXPECTED_PERIODS = [
    "2026-08", "2026-09", "2026-10", "2026-11", "2026-12",
    "2027-01", "2027-02", "2027-03", "2027-04", "2027-05",
    "2027-06", "2027-07",
]
PRICE_STAGES = ("preventa", "lanzamiento", "regular")
AUTHORIZED_CONTENT_REPLACEMENTS = {"tw-educa-curso-02"}


def fail(message: str) -> None:
    raise AssertionError(message)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def git_file(ref: str, relative: str) -> str:
    return subprocess.run(
        ["git", "show", f"{ref}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout


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


def metrics(text: str) -> MetricsParser:
    parser = MetricsParser()
    parser.feed(text)
    return parser


def published_sources() -> tuple[list[str], list[dict], list[dict]]:
    closed = read_json(SCHEDULE_ROOT / "cursos_tw_educa_publicados.json")
    ids = closed.get("curso_ids", [])
    source = read_json(ROOT / "data" / "cursos_tw_educa.json")
    visible = [
        item for item in source
        if item.get("visible_cliente") is True and item.get("estado_publicacion") == "publicado"
    ]
    catalog = read_json(ROOT / "data" / "catalogo_global.json")
    catalog_visible = [
        item for item in catalog
        if item.get("linea_negocio") == "tw-educa"
        and item.get("tipo_item") == "curso"
        and item.get("visible_cliente") is True
        and item.get("estado_publicacion") == "publicado"
    ]
    if closed.get("total_cursos") != EXPECTED_COURSES or len(ids) != EXPECTED_COURSES:
        fail("La lista cerrada no contiene exactamente 37 IDs")
    if len(set(ids)) != EXPECTED_COURSES:
        fail("La lista cerrada contiene IDs duplicados")
    if [item["id"] for item in visible] != ids:
        fail("La lista cerrada no coincide con los 37 cursos publicados de la fuente comercial")
    if {item["id"] for item in catalog_visible} != set(ids) or len(catalog_visible) != EXPECTED_COURSES:
        fail("Los resultados visibles de educa/index.html no coinciden con la lista cerrada")
    return ids, visible, catalog_visible


def validate_price_profiles(ids: list[str], source: list[dict], canonical: list[dict]) -> None:
    source_map = {item["id"]: item for item in source}
    canonical_map = {item["id"]: item for item in canonical}
    usd_data = read_json(ROOT / "data" / "precios_internacionales_tw_educa.json")
    usd_map = {item["curso_id"]: item for item in usd_data.get("cursos", [])}
    rate = usd_data.get("configuracion", {}).get("pen_por_usd")
    if rate != 3.411 or usd_data.get("configuracion", {}).get("fecha_revision") != "2026-07-29":
        fail("La equivalencia USD no registra la referencia revisada")
    if set(usd_map) != set(ids) or usd_data.get("total_cursos") != EXPECTED_COURSES:
        fail("La tabla USD no cubre exactamente los 37 cursos")

    for course_id in ids:
        original = source_map[course_id].get("precios") or []
        pen = canonical_map[course_id].get("precios_pen") or []
        usd = canonical_map[course_id].get("precios_usd") or []
        usd_external = usd_map[course_id].get("perfiles") or []
        if pen != original:
            fail(f"Perfiles o etapas PEN alterados: {course_id}")
        if len(original) != len(usd) or usd != usd_external:
            fail(f"Tabla USD no equivalente a PEN: {course_id}")
        for pen_profile, usd_profile in zip(original, usd):
            if pen_profile["publico"] != usd_profile["publico"]:
                fail(f"Perfil USD inventado o alterado: {course_id}")
            for stage in PRICE_STAGES:
                expected = math.ceil(pen_profile[f"{stage}_soles"] / rate)
                if usd_profile.get(f"{stage}_usd") != expected:
                    fail(f"Conversión USD inválida: {course_id}/{stage}")


def validate_whatsapp(entry: dict, course: dict) -> None:
    parsed = urlparse(entry["enlace_inscripcion"])
    if parsed.netloc != "wa.me" or parsed.path.strip("/") != "51952354282":
        fail(f"WhatsApp inválido: {entry['id']}")
    message = parse_qs(parsed.query).get("text", [""])[0]
    required = (
        course["nombre"],
        entry["hora_inicio"],
        entry["hora_fin"],
        entry["modalidad"],
        "UTC-05:00",
        "tarifa aplicable",
        "perfil comercial",
        "modalidad de pago",
    )
    if not all(value in message for value in required):
        fail(f"WhatsApp incompleto: {entry['id']}")
    if "Precio:" in message or "S/ " in message or "USD " in message:
        fail(f"WhatsApp fija un precio único: {entry['id']}")


def validate_data() -> tuple[int, int]:
    ids, source, _ = published_sources()
    canonical_data = read_json(SCHEDULE_ROOT / "cursos.json")
    canonical = canonical_data.get("cursos", [])
    course_map = {course["id"]: course for course in canonical}
    current = read_json(SCHEDULE_ROOT / "actual.json")
    config = read_json(SCHEDULE_ROOT / "configuracion.json")
    if canonical_data.get("total_cursos") != EXPECTED_COURSES or len(canonical) != EXPECTED_COURSES:
        fail("La fuente canónica no contiene exactamente 37 cursos")
    if set(course_map) != set(ids):
        fail("La fuente canónica contiene cursos ajenos o excluye cursos publicados")
    if current.get("periodos_disponibles") != EXPECTED_PERIODS:
        fail("Periodo distinto de agosto 2026–julio 2027")
    if current.get("total_cursos") != EXPECTED_COURSES or current.get("total_convocatorias") != EXPECTED_CONVOCATIONS:
        fail("Totales incorrectos en actual.json")
    if config.get("zona_horaria") != "America/Lima" or config.get("utc") != "UTC-05:00":
        fail("Zona horaria canónica inválida")
    if config.get("minimo_general_inscritos") != 5:
        fail("El mínimo general debe ser 5")
    validate_price_profiles(ids, source, canonical)

    all_entries = []
    by_course = defaultdict(list)
    for period in EXPECTED_PERIODS:
        entries = read_json(SCHEDULE_ROOT / f"{period}.json").get("convocatorias", [])
        if len(entries) != EXPECTED_COURSES:
            fail(f"{period} no contiene 37 convocatorias")
        if {entry["curso_id"] for entry in entries} != set(ids):
            fail(f"{period} contiene cursos ajenos o incompletos")
        if len({entry["id"] for entry in entries}) != EXPECTED_COURSES:
            fail(f"IDs duplicados en {period}")
        if any(count > 2 for count in Counter((e["fecha_inicio"], e["hora_inicio"]) for e in entries).values()):
            fail(f"Más de dos inicios simultáneos en {period}")
        for entry in entries:
            course = course_map[entry["curso_id"]]
            if entry["periodo"] != period or not entry["fecha_inicio"].startswith(period):
                fail(f"Fecha fuera del periodo: {entry['id']}")
            start = datetime.strptime(entry["hora_inicio"], "%H:%M")
            end = datetime.strptime(entry["hora_fin"], "%H:%M")
            datetime.strptime(entry["fecha_inicio"], "%Y-%m-%d")
            if end <= start:
                fail(f"Horario inválido: {entry['id']}")
            if entry["zona_horaria"] != "America/Lima" or entry["utc"] != "UTC-05:00":
                fail(f"Zona horaria inválida: {entry['id']}")
            if entry["minimo_inscritos"] < 1 or entry["estado"] != "Inscripciones abiertas":
                fail(f"Mínimo o estado inválido: {entry['id']}")
            if entry["condicion"] != "Sujeto a mínimo de inscritos":
                fail(f"Condición inválida: {entry['id']}")
            if any(key in entry for key in ("precio_pen", "precio_usd", "precio_usd_fuente", "vacantes")):
                fail(f"Convocatoria con precio único o vacantes simuladas: {entry['id']}")
            validate_whatsapp(entry, course)
            all_entries.append(entry)
            by_course[entry["curso_id"]].append(entry)

    if len(all_entries) != EXPECTED_CONVOCATIONS or len({entry["id"] for entry in all_entries}) != EXPECTED_CONVOCATIONS:
        fail("Deben existir exactamente 444 convocatorias únicas")
    if len(by_course) != EXPECTED_COURSES or any(len(entries) != 12 for entries in by_course.values()):
        fail("Cada uno de los 37 cursos debe tener doce fechas")
    return len(canonical), len(all_entries)


def validate_preserved_content() -> int:
    _, courses, _ = published_sources()
    protected_tags = ("h1", "h2", "h3", "section", "article", "p", "li", "a", "img", "meta")
    for course in courses:
        relative = f"cursos/{course['slug']}/index.html"
        before_text = git_file(BACKUP_REF, relative)
        after_text = (ROOT / relative).read_text(encoding="utf-8-sig")
        before, after = metrics(before_text), metrics(after_text)
        for tag in protected_tags:
            if after.counts[tag] < before.counts[tag]:
                fail(f"Contenido reducido en {relative}: <{tag}>")
        if course["id"] not in AUTHORIZED_CONTENT_REPLACEMENTS:
            if not set(before.images).issubset(after.images):
                fail(f"Imagen retirada en {relative}")
            if not set(before.hrefs).issubset(after.hrefs):
                fail(f"Enlace retirado en {relative}")
            if not set(before.meta).issubset(after.meta):
                fail(f"Metadato retirado en {relative}")
        original_prices = course.get("precios") or []
        for profile in original_prices:
            for stage in PRICE_STAGES:
                token = f"S/ {profile[f'{stage}_soles']}"
                if token not in after_text:
                    fail(f"Precio PEN retirado en {relative}: {token}")
        required = ("data-course-schedule", "cronograma-tw-educa.js", "detalle.js")
        if not all(value in after_text for value in required):
            fail(f"Detalle incompleto en {relative}")
    before_source = json.loads(git_file(BACKUP_REF, "data/cursos_tw_educa.json"))
    after_source = read_json(ROOT / "data" / "cursos_tw_educa.json")
    preserved_before = [item for item in before_source if item.get("id") not in AUTHORIZED_CONTENT_REPLACEMENTS]
    preserved_after = [item for item in after_source if item.get("id") not in AUTHORIZED_CONTENT_REPLACEMENTS]
    if preserved_before != preserved_after:
        fail("Se alteró la fuente comercial o académica de los 37 cursos")
    return len(courses)


def validate_frontend_and_seo() -> None:
    js = (ROOT / "assets" / "js" / "cronograma-tw-educa.js").read_text(encoding="utf-8")
    forbidden = ("Zona detectada", "Conversión referencial", "En tu zona horaria", "priceText(", "precio_pen", "precio_usd")
    if any(value in js for value in forbidden):
        fail("El frontend conserva redundancias o precios únicos del cronograma incorrecto")
    required_js = (
        "Próximas fechas de inicio",
        "schedule-table",
        "zone === LIMA_ZONE",
        "root.dataset.scheduleLimit",
        "startDate(item) >= new Date()",
    )
    if not all(value in js for value in required_js):
        fail("El frontend no contiene la presentación compacta requerida")
    if 'insertAdjacentHTML("beforeend", compactSchedule(items))' in js:
        fail("Las tarjetas vuelven a insertar cronogramas extensos")
    detail_js = (ROOT / "assets" / "js" / "detalle.js").read_text(encoding="utf-8")
    required_pricing = (
        "precios_internacionales_tw_educa.json",
        "Precios internacionales — USD",
        "preventa_usd",
        "lanzamiento_usd",
        "regular_usd",
        "Pagos internacionales",
        "PayPal",
    )
    if not all(value in detail_js for value in required_pricing):
        fail("El detalle no incorpora la tabla USD paralela ni los pagos internacionales")

    annual = (ROOT / "catalogo" / "cronograma-anual-tw-educa.html").read_text(encoding="utf-8-sig")
    required_annual = (
        "exclusivamente a los 37 cursos actualmente publicados",
        'data-annual-schedule',
        'rel="canonical"',
        'property="og:title"',
    )
    if not all(value in annual for value in required_annual):
        fail("La página anual no declara el alcance cerrado o perdió SEO")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8-sig")
    if sitemap.count("<loc>") != 103 or "catalogo/cronograma-anual-tw-educa.html" not in sitemap:
        fail("Sitemap inválido")
    educa = (ROOT / "educa" / "index.html").read_text(encoding="utf-8-sig")
    if "Ver todas las fechas 2026–2027" not in educa:
        fail("TW Educa no enlaza correctamente el cronograma")
    css = (ROOT / "assets" / "css" / "styles.css").read_text(encoding="utf-8-sig")
    schedule_start = css.index("/* Cronograma canónico TW Educa */")
    schedule_end = css.index(".subpage-hero", schedule_start)
    schedule_css = css[schedule_start:schedule_end]
    if "transform: scale(" in schedule_css or re.search(r"\bzoom\s*:", schedule_css):
        fail("El cronograma usa escalado o zoom")


def validate_all_json() -> int:
    files = list(ROOT.rglob("*.json"))
    for path in files:
        read_json(path)
    return len(files)


def main() -> int:
    courses, convocations = validate_data()
    protected = validate_preserved_content()
    validate_frontend_and_seo()
    json_files = validate_all_json()
    print(
        "OK: cronograma TW Educa restringido; "
        f"{courses} cursos, {convocations} convocatorias, "
        f"{protected} páginas protegidas y {json_files} JSON válidos."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}")
        raise SystemExit(1)
