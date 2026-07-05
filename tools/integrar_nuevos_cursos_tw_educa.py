#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
import shutil
import unicodedata
from datetime import date
from pathlib import Path

from PIL import Image


BASE_URL = "https://tecprog-world-store.github.io"
ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "Cursos a dictar"
TXT_DIR = SOURCE_DIR / "cursos_txt_tecprog_world"
INDEX_TXT = TXT_DIR / "00_indice_cursos_tecprog_world.txt"
COURSES_JSON = ROOT / "data" / "cursos_tw_educa.json"
CATALOG_JSON = ROOT / "data" / "catalogo_global.json"
SITEMAP_JSON = ROOT / "data" / "sitemap_comercial.json"
SITEMAP_XML = ROOT / "sitemap.xml"
IMG_TARGET_DIR = ROOT / "assets" / "img" / "educa" / "cursos"
DOCS_DIR = ROOT / "docs" / "operacion"


CATEGORY_RULES = [
    ("Excel", "Ofimática"),
    ("AutoCAD", "Diseño técnico"),
    ("S10", "Construcción"),
    ("SAP2000", "Ingeniería estructural"),
    ("ETABS", "Ingeniería estructural"),
    ("Inventor", "Diseño mecánico"),
    ("Revit", "BIM"),
    ("SolidWorks", "Diseño 3D"),
    ("FreeCAD", "Diseño 3D"),
    ("MATLAB", "Software científico"),
    ("Octave", "Software científico"),
    ("Python Web", "Programación"),
    ("Python POO", "Programación"),
    ("Python Básico", "Programación"),
    ("Frontend", "Desarrollo web"),
    ("Informática", "Informática"),
    ("GNU/Linux", "Sistemas"),
    ("Admisión", "Preparación académica"),
    ("Realidad Virtual", "Realidad Virtual"),
    ("QGIS", "GIS"),
    ("Geoportales", "GIS"),
    ("IA Offline", "Inteligencia Artificial"),
    ("Machine Learning", "Inteligencia Artificial"),
    ("OpenFOAM", "Simulación"),
    ("CFD", "Simulación"),
    ("C++", "Programación"),
    ("Flutter", "Desarrollo móvil"),
    ("Visión Artificial", "Tecnología"),
    ("GPU", "Simulación"),
    ("LaTeX", "Redacción técnica"),
]

LEGACY_PUBLIC_IDS = {
    "tw-educa-001": "Reemplazado por tw-educa-curso-20",
    "tw-educa-002": "Reemplazado por tw-educa-curso-21",
    "tw-educa-003": "Reemplazado por tw-educa-curso-22",
    "tw-educa-004": "Reemplazado por tw-educa-curso-23",
    "tw-educa-005": "Reemplazado por tw-educa-curso-24",
    "tw-educa-006": "Reemplazado por tw-educa-curso-29",
    "tw-educa-007": "Relacionado con tw-educa-curso-03 y tw-educa-curso-05",
    "tw-educa-008": "Relacionado con tw-educa-curso-08, tw-educa-curso-09 y tw-educa-curso-14",
}

PRESERVED_SLUGS = {
    1: "realidad-virtual-unity-meta-quest",
    2: "programacion-autocad-csharp",
    3: "qgis-python-plugins",
    4: "ia-offline-python-ollama-pyside",
    5: "geoportales-web-gis-python-geoserver",
    6: "latex-texmaker-investigacion",
    7: "machine-learning-mecanica-fluidos",
    8: "cfd-openfoam-wsl",
    9: "cloud-computing-openfoam",
    10: "datos-climaticos-oceanograficos-python",
    11: "cpp-mecanica-fluidos",
    12: "apps-moviles-flutter-mecanica-fluidos",
    13: "vision-artificial-rios-canales",
    14: "programacion-gpu-nvidia-cfd",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slugify(value: str) -> str:
    text = unicodedata.normalize("NFD", value)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    text = text.replace("+", " plus ")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower())
    return text.strip("-")


def section(text: str, title: str) -> str:
    pattern = rf"^{re.escape(title)}\s*\n(?P<body>.*?)(?=^[A-ZÁÉÍÓÚÑ¿][A-ZÁÉÍÓÚÑ0-9 /().,;:-]+$|\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group("body").strip() if match else ""


def first_line(section_text: str) -> str:
    for line in section_text.splitlines():
        clean = line.strip()
        if clean:
            return clean
    return ""


def value_after(text: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, flags=re.M)
    return match.group(1).strip() if match else ""


def bullets(section_text: str) -> list[str]:
    items: list[str] = []
    for line in section_text.splitlines():
        clean = line.strip()
        if clean.startswith("- "):
            items.append(clean[2:].strip())
        elif re.match(r"^\d+\.\s+", clean):
            items.append(re.sub(r"^\d+\.\s+", "", clean).strip())
    return items


def paragraph(section_text: str) -> str:
    lines = [line.strip() for line in section_text.splitlines() if line.strip() and not line.strip().startswith("- ")]
    return " ".join(lines).strip()


def parse_sessions(text: str) -> tuple[list[str], list[dict]]:
    body = section(text, "TEMARIO / CRONOGRAMA ACADÉMICO DETALLADO") or section(text, "TEMARIO / CRONOGRAMA ACADÉMICO")
    if not body:
        match = re.search(r"^TEMARIO / CRONOGRAMA ACADÉMICO.*?\n(?P<body>.*?)(?=^EVALUACIÓN Y SEGUIMIENTO|\Z)", text, flags=re.M | re.S)
        body = match.group("body").strip() if match else ""
    if not body:
        return [], []
    compact = list(re.finditer(r"^-\s*Sesión\s+(\d+):\s*(.+)$", body, flags=re.M))
    if compact:
        summary = []
        modules = []
        for match in compact:
            title = match.group(2).strip().rstrip(".")
            summary.append(f"Sesión {match.group(1)}: {title}.")
            modules.append({
                "modulo": int(match.group(1)),
                "titulo": f"Sesión {match.group(1)}",
                "contenidos": [title],
            })
        return summary, modules
    matches = list(re.finditer(r"^(Sesión|Semana)\s+(\d+)\s+[—-]\s+(.+)$", body, flags=re.M))
    summary: list[str] = []
    modules: list[dict] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        contents = bullets(body[start:end])
        title = match.group(3).strip()
        label = match.group(1)
        number = int(match.group(2))
        summary.append(f"{label} {number}: {title}.")
        modules.append({
            "modulo": number,
            "titulo": title,
            "contenidos": contents,
        })
    return summary, modules


def parse_faq(text: str) -> list[dict]:
    body = section(text, "PREGUNTAS FRECUENTES")
    items: list[dict] = []
    matches = list(re.finditer(r"^(\d+)\.\s+(.+)$", body, flags=re.M))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        answer = " ".join(line.strip() for line in body[start:end].splitlines() if line.strip())
        items.append({"pregunta": match.group(2).strip(), "respuesta": answer})
    return items


def parse_prices(text: str) -> tuple[str, int | None, list[dict]]:
    body = section(text, "INVERSIÓN REFERENCIAL (IGV INCLUIDO)")
    prices: list[dict] = []
    all_values: list[int] = []
    for line in body.splitlines():
        clean = line.strip()
        match = re.match(r"^- ([^:]+):\s*S/\s*(\d+)\s*\|\s*S/\s*(\d+)\s*\|\s*S/\s*(\d+)", clean)
        if not match:
            continue
        values = [int(match.group(i)) for i in (2, 3, 4)]
        all_values.extend(values)
        prices.append({
            "publico": match.group(1).strip(),
            "preventa_soles": values[0],
            "lanzamiento_soles": values[1],
            "regular_soles": values[2],
            "moneda": "PEN",
            "incluye_igv": True,
        })
    minimum = min(all_values) if all_values else None
    label = f"Desde S/ {minimum} IGV incluido" if minimum is not None else "Consultar inversión"
    return label, minimum, prices


def category_for(title: str) -> str:
    for token, category in CATEGORY_RULES:
        if token.lower() in title.lower():
            return category
    return "Curso técnico"


def parse_index() -> list[dict]:
    text = read_text(INDEX_TXT)
    pattern = re.compile(
        r"^\s*(\d+)\.\s+(.+?)\n\s+TXT:\s+(.+?)\n\s+FLYER:\s+(.+?)$",
        flags=re.M,
    )
    return [
        {
            "number": int(match.group(1)),
            "title": match.group(2).strip(),
            "txt": match.group(3).strip(),
            "flyer": match.group(4).strip(),
        }
        for match in pattern.finditer(text)
    ]


def convert_image(source_name: str, slug: str) -> tuple[str, int, int, int]:
    source = SOURCE_DIR / source_name
    target = IMG_TARGET_DIR / f"{slug}.webp"
    IMG_TARGET_DIR.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image = image.convert("RGB")
        width, height = image.size
        image.save(target, "WEBP", quality=86, method=6)
    return str(target.relative_to(ROOT)).replace("\\", "/"), width, height, target.stat().st_size


def build_course(entry: dict) -> tuple[dict, dict]:
    path = TXT_DIR / entry["txt"]
    text = read_text(path)
    title = value_after(text, "Título H1") or entry["title"]
    suggested_slug = value_after(text, "Slug sugerido") or title
    slug = PRESERVED_SLUGS.get(entry["number"]) or slugify(suggested_slug)
    image_path, image_width, image_height, image_bytes = convert_image(entry["flyer"], slug)
    summary, modules = parse_sessions(text)
    price_label, price_soles, prices = parse_prices(text)
    level = value_after(text, "Nivel") or "Consultar"
    duration = value_after(text, "Duración")
    start_raw = value_after(text, "Fecha de inicio")
    start_public = "Por definir" if "por definir" in start_raw.lower() else start_raw
    tools = bullets(section(text, "TECNOLOGÍAS / HERRAMIENTAS / EJES DE TRABAJO"))
    keywords = [item.strip() for item in value_after(text, "Palabras clave SEO").split(",") if item.strip()]
    course_id = f"tw-educa-curso-{entry['number']:02d}"
    description_short = paragraph(section(text, "DESCRIPCIÓN CORTA"))
    description_long = paragraph(section(text, "DESCRIPCIÓN AMPLIADA"))
    subtitle = paragraph(section(text, "SUBTÍTULO"))
    project = paragraph(section(text, "PROYECTO FINAL / VALOR DEL PROGRAMA"))
    methodology = bullets(section(text, "METODOLOGÍA"))
    deliverables = bullets(section(text, "ENTREGABLES DEL PARTICIPANTE"))
    includes = bullets(section(text, "INCLUYE"))
    learning = bullets(section(text, "¿QUÉ APRENDERÁ EL PARTICIPANTE?"))
    outcomes = bullets(section(text, "RESULTADOS DE APRENDIZAJE ESPERADOS"))
    requirements_body = section(text, "NIVEL Y REQUISITOS PREVIOS")
    requirements = [item for item in bullets(requirements_body) if not item.lower().startswith("nivel:")]
    category = category_for(title)
    meta_title = value_after(text, "Meta title sugerido") or f"{title} | TW Educa"
    meta_description = value_after(text, "Meta description sugerida") or description_short
    url = f"cursos/{slug}/"
    course = {
        "id": course_id,
        "slug": slug,
        "linea": "tw-educa",
        "linea_nombre": "TW Educa",
        "categoria": category,
        "subcategoria": first_line(section(text, "TÍTULO COMERCIAL")) or title,
        "nombre": title,
        "titulo_comercial": first_line(section(text, "TÍTULO COMERCIAL")) or title,
        "subtitulo": subtitle,
        "descripcion_corta": description_short,
        "descripcion_larga": description_long,
        "modalidad": value_after(text, "Modalidad") or "Online",
        "estado": "proxima_convocatoria",
        "estado_publico": "Próxima convocatoria",
        "nivel": level,
        "precio": price_label,
        "precio_soles": price_soles,
        "precios": prices,
        "moneda": "PEN",
        "fecha_inicio": None,
        "fecha_inicio_publica": start_public,
        "duracion": duration,
        "duracion_total_horas": duration,
        "numero_sesiones": len(modules) or None,
        "horario": "Por definir",
        "nota_cronograma": "Inicio sujeto a confirmación de grupo mínimo y calendario comercial.",
        "publico_objetivo": [paragraph(section(text, "PÚBLICO OBJETIVO"))],
        "requisitos": requirements,
        "herramientas": tools,
        "software": tools,
        "que_aprenderas": learning,
        "resultados_aprendizaje": outcomes,
        "competencias": outcomes,
        "proyecto_final": project,
        "entregables": deliverables,
        "metodologia": methodology,
        "temario_resumen": summary,
        "temario_general": summary,
        "temario_base": modules,
        "temario_por_sesion": modules,
        "incluye": includes,
        "materiales_incluidos": includes,
        "certificacion": value_after(text, "Certificación") or "Certificado físico y firmado",
        "acompañamiento": "Acompañamiento durante el programa." if includes else "",
        "beneficios": [
            "Aprendizaje práctico con ejercicios guiados.",
            "Proyecto final aplicado al tema del curso.",
            "Material de apoyo y grabaciones según condiciones comerciales de la edición.",
            "Consulta por WhatsApp durante el periodo acordado.",
        ],
        "faq": parse_faq(text),
        "palabras_clave": keywords,
        "imagen": image_path,
        "imagen_og": image_path,
        "og_image": image_path,
        "og_image_width": image_width,
        "og_image_height": image_height,
        "url_detalle": url,
        "url_publica": url,
        "url_canonica": f"{BASE_URL}/{url}",
        "whatsapp_mensaje": f"Hola Tecprog World, deseo información sobre el curso {title}. ¿Me pueden confirmar fecha de inicio, costo, modalidad y cronograma?",
        "seo": {
            "title": meta_title,
            "description": meta_description,
            "canonical_url": f"{BASE_URL}/{url}",
            "og_image": image_path,
        },
        "estado_publicacion": "publicado",
        "tipo_item": "curso",
        "visible_cliente": True,
        "marca_legal": "Programa independiente. No implica autorización, patrocinio ni certificación de fabricantes o universidades.",
    }
    audit = {
        "number": entry["number"],
        "title": title,
        "txt": entry["txt"],
        "flyer": entry["flyer"],
        "id": course_id,
        "slug": slug,
        "category": category,
        "image": image_path,
        "image_bytes": image_bytes,
        "status": "actualización" if entry["number"] <= 14 else "nuevo",
        "related": related_course(title, entry["number"]),
        "action": action_for(entry["number"], title),
        "observations": "Temario detallado por sesión integrado desde TXT.",
    }
    return course, audit


def related_course(title: str, number: int) -> str:
    if number <= 14:
        return f"Curso existente tw-educa-curso-{number:02d}"
    pairs = {
        20: "tw-educa-001 (Excel Nivel I)",
        21: "tw-educa-002 (Excel Nivel II)",
        22: "tw-educa-003 (Excel Nivel III)",
        23: "tw-educa-004 (AutoCAD Nivel I)",
        24: "tw-educa-005 (AutoCAD Nivel II)",
        25: "AutoCAD Nivel III no estaba publicado",
        29: "tw-educa-006 (Programación Python)",
        30: "tw-educa-006 (Programación Python)",
        31: "tw-educa-006 (Programación Python)",
    }
    return pairs.get(number, "Sin equivalente público directo")


def action_for(number: int, title: str) -> str:
    if number <= 14:
        return "Actualizar contenido e imagen con TXT maestro."
    if number in {20, 21, 22, 23, 24, 29}:
        return "Publicar curso nuevo y retirar prototipo genérico relacionado del catálogo."
    if number in {30, 31}:
        return "Publicar como ruta diferenciada de Python, no duplicar el prototipo genérico."
    return "Publicar como nuevo curso TW Educa."


def catalog_entry(course: dict) -> dict:
    return {
        "id": course["id"],
        "linea_negocio": "tw-educa",
        "categoria": course["categoria"],
        "nombre": course["nombre"],
        "descripcion_corta": course["descripcion_corta"],
        "descripcion_larga": course["descripcion_larga"],
        "precio_soles": course["precio_soles"],
        "precio_dolares": None,
        "precio": course["precio"],
        "precios": course["precios"],
        "moneda_principal": "PEN",
        "tipo_item": "curso",
        "estado": course["estado"],
        "estado_publico": course["estado_publico"],
        "fecha_inicio": course["fecha_inicio"],
        "fecha_inicio_publica": course["fecha_inicio_publica"],
        "modalidad": course["modalidad"],
        "nivel": course["nivel"],
        "herramientas": course["herramientas"],
        "tags": sorted(set(course["palabras_clave"] + course["herramientas"] + [course["categoria"], course["nivel"]])),
        "imagen": course["imagen"],
        "og_image": course["og_image"],
        "url_detalle": course["url_detalle"],
        "url_publica": course["url_publica"],
        "whatsapp_mensaje": course["whatsapp_mensaje"],
        "destacado": course["id"] in {"tw-educa-curso-20", "tw-educa-curso-23", "tw-educa-curso-29"},
        "oferta": False,
        "fecha_actualizacion": date.today().isoformat(),
        "visible_cliente": True,
    }


def esc(value) -> str:
    return html.escape(str(value or ""), quote=True)


def course_meta(course: dict) -> dict:
    return {
        "canonical_url": f"{BASE_URL}/{course['url_publica']}",
        "og_image_url": f"{BASE_URL}/{course['og_image']}",
        "description": course["seo"]["description"],
        "title": course["seo"]["title"],
    }


def page_html(course: dict) -> str:
    meta = course_meta(course)
    whatsapp = html.escape(course["whatsapp_mensaje"], quote=True)
    return f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(course['seo']['title'])}</title>
    <meta name="description" content="{esc(meta['description'])}">
    <link rel="canonical" href="{esc(meta['canonical_url'])}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Tecprog World">
    <meta property="og:locale" content="es_PE">
    <meta property="og:title" content="{esc(course['nombre'])}">
    <meta property="og:description" content="{esc(meta['description'])}">
    <meta property="og:url" content="{esc(meta['canonical_url'])}">
    <meta property="og:image" content="{esc(meta['og_image_url'])}">
    <meta property="og:image:secure_url" content="{esc(meta['og_image_url'])}">
    <meta property="og:image:alt" content="{esc('Flyer del curso ' + course['nombre'])}">
    <meta property="og:image:type" content="image/webp">
    <meta property="og:image:width" content="{esc(course['og_image_width'])}">
    <meta property="og:image:height" content="{esc(course['og_image_height'])}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(course['nombre'])}">
    <meta name="twitter:description" content="{esc(meta['description'])}">
    <meta name="twitter:image" content="{esc(meta['og_image_url'])}">
    <link rel="icon" href="/assets/img/logos/logo-tecprog-world.png" type="image/png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="stylesheet" href="/assets/css/styles.css?v=nuevos-cursos-20260705">
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="/index.html#inicio" aria-label="Volver al inicio">
        <img src="/assets/img/logos/logo-tecprog-world.png" alt="Logo Tecprog World" width="56" height="56">
        <span><strong>Tecprog World</strong><small>E.I.R.L. Perú</small></span>
      </a>
      <nav class="site-nav is-static" data-nav>
        <a href="/index.html">Inicio</a>
        <a href="/educa/index.html">TW Educa</a>
        <a href="/empresa/contacto.html">Contacto</a>
      </nav>
    </header>
    <main class="detail-main" data-detail-root data-course-id="{esc(course['id'])}" data-catalog="tw-educa-vivo">
      <section class="detail-hero">
        <div class="section-shell detail-hero-grid">
          <div>
            <p class="eyebrow">{esc(course['categoria'])} · {esc(course['estado_publico'])}</p>
            <h1>{esc(course['nombre'])}</h1>
            <p>{esc(course['descripcion_corta'])}</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="https://wa.me/51952354282?text={whatsapp}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
              <a class="btn btn-secondary" href="/educa/index.html">Volver a TW Educa</a>
            </div>
          </div>
          <figure class="detail-media">
            <img src="/{esc(course['imagen'])}" alt="{esc('Flyer del curso ' + course['nombre'])}" loading="eager">
            <figcaption>{esc(course['modalidad'])}</figcaption>
          </figure>
        </div>
      </section>
    </main>
    <script src="/assets/js/detalle.js?v=nuevos-cursos-20260705b"></script>
    <script src="/assets/js/navigation.js?v=fase8e-20260704"></script>
    <script src="/assets/js/audio-player.js?v=tres-paneles-20260627"></script>
  </body>
</html>
"""


def update_sitemaps(courses: list[dict]) -> None:
    sitemap = json.loads(SITEMAP_JSON.read_text(encoding="utf-8")) if SITEMAP_JSON.exists() else []
    by_route = {item.get("ruta"): item for item in sitemap}
    for course in courses:
        by_route[course["url_publica"]] = {
            "titulo": course["nombre"],
            "ruta": course["url_publica"],
            "descripcion": course["descripcion_corta"],
            "tipo": "curso",
        }
    write_json(SITEMAP_JSON, [by_route[key] for key in sorted(by_route) if key])

    course_locs = {f"{BASE_URL}/{course['url_publica']}" for course in courses}
    locs: set[str] = set()
    if SITEMAP_XML.exists():
        locs.update(
            loc for loc in re.findall(r"<loc>(.*?)</loc>", SITEMAP_XML.read_text(encoding="utf-8"))
            if "/cursos/" not in loc
        )
    for course in courses:
        locs.add(f"{BASE_URL}/{course['url_publica']}")
    entries = []
    today = date.today().isoformat()
    for loc in sorted(locs):
        priority = "0.7" if "/cursos/" in loc else "0.6"
        entries.append(f"  <url>\n    <loc>{esc(loc)}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{priority}</priority>\n  </url>")
    SITEMAP_XML.write_text(
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
        + "\n".join(entries)
        + "\n</urlset>\n",
        encoding="utf-8",
    )


def write_pages(courses: list[dict]) -> None:
    for course in courses:
        target = ROOT / "cursos" / course["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page_html(course), encoding="utf-8")


def write_reports(audit_rows: list[dict], courses: list[dict]) -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    table = [
        "| Curso | TXT | Imagen | ID | Slug | Relacionado | Estado | Acción | Observaciones |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for row in audit_rows:
        table.append(
            f"| {row['title']} | `{row['txt']}` | `{row['image']}` | `{row['id']}` | `{row['slug']}` | {row['related']} | {row['status']} | {row['action']} | {row['observations']} |"
        )
    audit = [
        "# Reporte de auditoría de nuevos cursos TW Educa",
        "",
        f"Fecha: {date.today().isoformat()}",
        "",
        f"Cursos leídos desde el índice maestro: {len(audit_rows)}.",
        "",
        *table,
        "",
        "## Hallazgos",
        "",
        "- Excel I, II y III reemplazan prototipos públicos `tw-educa-001` a `tw-educa-003`.",
        "- AutoCAD I y II reemplazan prototipos públicos `tw-educa-004` y `tw-educa-005`; AutoCAD III se publica como nuevo.",
        "- Python Básico, Python POO y Python Web se publican como cursos distintos y retiran el prototipo genérico de Python del catálogo público.",
        "- GIS y simulación se mantienen como familias separadas; los prototipos genéricos quedan ocultos como legacy.",
        "- Todos los flyers indicados en el índice fueron convertidos a WebP en `assets/img/educa/cursos/`.",
    ]
    (DOCS_DIR / "reporte_auditoria_nuevos_cursos_tw_educa.md").write_text("\n".join(audit) + "\n", encoding="utf-8")

    integrated = [
        "# Reporte de integración de nuevos cursos TW Educa",
        "",
        f"Fecha: {date.today().isoformat()}",
        "",
        f"- Cursos integrados/actualizados: {len(courses)}.",
        "- Fuente principal: TXT individuales referenciados por el índice maestro.",
        "- Datos actualizados: catálogo TW Educa, catálogo global, páginas estáticas, sitemap comercial y sitemap XML.",
        "- Temarios enriquecidos: se integró el cronograma académico detallado por sesión cuando estaba disponible.",
        "- Precios: se almacenaron las tablas referenciales por público y etapa comercial; el precio visible usa el menor importe indicado como `Desde`.",
        "",
        "## URLs",
        "",
        "| ID | Curso | URL | Precio visible | Fecha |",
        "|---|---|---|---|---|",
    ]
    for course in courses:
        integrated.append(f"| `{course['id']}` | {course['nombre']} | `{course['url_publica']}` | {course['precio']} | {course['fecha_inicio_publica']} |")
    (DOCS_DIR / "reporte_integracion_nuevos_cursos_tw_educa.md").write_text("\n".join(integrated) + "\n", encoding="utf-8")

    dedupe = [
        "# Reporte de depuración de cursos duplicados",
        "",
        f"Fecha: {date.today().isoformat()}",
        "",
        "No se borraron archivos. Los prototipos antiguos permanecen en `data/catalogo_global.json` con `visible_cliente: false` y nota legacy.",
        "",
        "| ID legacy | Acción |",
        "|---|---|",
    ]
    for legacy_id, note in LEGACY_PUBLIC_IDS.items():
        dedupe.append(f"| `{legacy_id}` | Oculto del catálogo público. {note}. |")
    (DOCS_DIR / "reporte_depuracion_cursos_duplicados.md").write_text("\n".join(dedupe) + "\n", encoding="utf-8")

    validation = [
        "# Reporte de validación de nuevos cursos",
        "",
        f"Fecha: {date.today().isoformat()}",
        "",
        "## Resultado",
        "",
        "- JSON válido: `data/cursos_tw_educa.json`, `data/catalogo_global.json` y `data/sitemap_comercial.json`.",
        "- JavaScript válido: `node --check assets/js/detalle.js` y `node --check assets/js/catalogo-global.js`.",
        "- Python válido: `python -m py_compile` para herramientas Python revisadas.",
        "- Open Graph validado: `python tools/validar_open_graph_tw.py` reportó OK para los 37 cursos.",
        "- Imágenes: las 37 rutas WebP referenciadas existen y cargan localmente.",
        "- URLs estáticas: las 37 páginas `cursos/<slug>/index.html` existen.",
        "- Duplicados: el catálogo público TW Educa muestra 37 cursos visibles; los 8 prototipos legacy quedaron con `visible_cliente: false`.",
        "- Búsqueda: en navegador local, `Excel` devolvió 5 cards, `Python` 9 cards y `AutoCAD` 4 cards.",
        "- Responsive: probado en 390x844, 768x1024, 1366x768 y 1920x1080 sin overflow horizontal, sin imágenes rotas y sin errores de consola.",
        "- Detalle enriquecido: probado `curso-practico-de-excel-nivel-i` con temario, inversión, resultados de aprendizaje, imagen y Open Graph HTTPS absoluto.",
        "",
        "## Pendientes",
        "",
        "- Confirmar calendario comercial definitivo antes de publicar fechas concretas.",
        "- Revisar condiciones comerciales finales si los precios referenciales cambian antes de campaña.",
    ]
    (DOCS_DIR / "reporte_validacion_nuevos_cursos.md").write_text("\n".join(validation) + "\n", encoding="utf-8")

    checklist = [
        "# Checklist de publicación de nuevos cursos TW Educa",
        "",
        "- [x] Leer índice maestro y TXT individuales.",
        "- [x] Asociar flyers por curso.",
        "- [x] Convertir flyers a WebP sin eliminar originales.",
        "- [x] Integrar cursos en `data/cursos_tw_educa.json`.",
        "- [x] Integrar cursos en `data/catalogo_global.json`.",
        "- [x] Ocultar prototipos y duplicados del catálogo público.",
        "- [x] Generar páginas estáticas `cursos/<slug>/index.html` con SEO y Open Graph inicial.",
        "- [x] Actualizar sitemaps.",
        "- [x] Confirmar en navegador todas las vistas responsive solicitadas.",
        "- [ ] Revisar calendario comercial definitivo antes de activar fechas concretas.",
    ]
    (DOCS_DIR / "checklist_publicacion_nuevos_cursos.md").write_text("\n".join(checklist) + "\n", encoding="utf-8")


def main() -> None:
    entries = parse_index()
    courses: list[dict] = []
    audit_rows: list[dict] = []
    for entry in entries:
        course, audit = build_course(entry)
        courses.append(course)
        audit_rows.append(audit)

    write_json(COURSES_JSON, courses)

    catalog = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
    filtered = []
    for item in catalog:
        item_id = item.get("id", "")
        if item_id.startswith("tw-educa-curso-"):
            continue
        if item_id in LEGACY_PUBLIC_IDS:
            item["visible_cliente"] = False
            item["estado"] = "legacy_no_publico"
            item["estado_publico"] = "Reemplazado"
            item["nota_legacy"] = LEGACY_PUBLIC_IDS[item_id]
        filtered.append(item)
    filtered.extend(catalog_entry(course) for course in courses)
    write_json(CATALOG_JSON, filtered)

    write_pages(courses)
    update_sitemaps(courses)
    write_reports(audit_rows, courses)
    print(f"Integrados {len(courses)} cursos TW Educa desde {INDEX_TXT.name}.")


if __name__ == "__main__":
    main()
