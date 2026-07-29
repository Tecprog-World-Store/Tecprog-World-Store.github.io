#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote

BASE_URL = "https://tecprog-world-store.github.io"
ROOT = Path(__file__).resolve().parents[1]
COURSES_JSON = ROOT / "data" / "cursos_tw_educa.json"
CATALOGO_JSON = ROOT / "data" / "catalogo_global.json"
SITEMAP_JSON = ROOT / "data" / "sitemap_comercial.json"
SITEMAP_XML = ROOT / "sitemap.xml"
REPORT = ROOT / "docs" / "operacion" / "reporte_generacion_paginas_sociales_cursos.md"
USD_PRICES_JSON = ROOT / "data" / "precios_internacionales_tw_educa.json"

SLUGS = {
    "tw-educa-curso-01": "realidad-virtual-unity-meta-quest",
    "tw-educa-curso-02": "programacion-autocad-csharp",
    "tw-educa-curso-03": "qgis-python-plugins",
    "tw-educa-curso-04": "ia-offline-python-ollama-pyside",
    "tw-educa-curso-05": "geoportales-web-gis-python-geoserver",
    "tw-educa-curso-06": "latex-texmaker-investigacion",
    "tw-educa-curso-07": "machine-learning-mecanica-fluidos",
    "tw-educa-curso-08": "cfd-openfoam-wsl",
    "tw-educa-curso-09": "cloud-computing-openfoam",
    "tw-educa-curso-10": "datos-climaticos-oceanograficos-python",
    "tw-educa-curso-11": "cpp-mecanica-fluidos",
    "tw-educa-curso-12": "apps-moviles-flutter-mecanica-fluidos",
    "tw-educa-curso-13": "vision-artificial-rios-canales",
    "tw-educa-curso-14": "programacion-gpu-nvidia-cfd",
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def esc(value) -> str:
    return html.escape(str(value or ""), quote=True)


def slugify(value: str) -> str:
    text = value.lower()
    replacements = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n",
        "ü": "u", "ç": "c",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def absolute_url(path: str) -> str:
    clean = str(path or "").lstrip("/")
    return f"{BASE_URL}/{clean}"


def image_type(path: str) -> str:
    suffix = Path(path).suffix.lower().lstrip(".")
    return {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "webp": "image/webp",
        "svg": "image/svg+xml",
    }.get(suffix, "image/webp")


def list_html(items: list[str]) -> str:
    clean_items = [item for item in items if item]
    return "<ul>" + "".join(f"<li>{esc(item)}</li>" for item in clean_items) + "</ul>" if clean_items else "<p>Consultar en la convocatoria.</p>"


def investment_html(course: dict) -> str:
    prices = course.get("precios") or []
    if not prices:
        return "<p>Inversion: consultar proxima convocatoria.</p>"
    rows = []
    for item in prices:
        rows.append(
            "<tr>"
            f"<td>{esc(item.get('publico'))}</td>"
            f"<td>S/ {esc(item.get('preventa_soles'))}</td>"
            f"<td>S/ {esc(item.get('lanzamiento_soles'))}</td>"
            f"<td>S/ {esc(item.get('regular_soles'))}</td>"
            "</tr>"
        )
    return (
        "<table><thead><tr><th>Modalidad</th><th>Preventa</th><th>Lanzamiento</th><th>Regular</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
        "<p>Precios referenciales en PEN. Confirma vacantes, etapa vigente y forma de pago por WhatsApp.</p>"
    )


def investment_usd_html(course: dict) -> str:
    data = read_json(USD_PRICES_JSON)
    pricing = next((item for item in data.get("cursos", []) if item.get("curso_id") == course["id"]), None)
    profiles = pricing.get("perfiles", []) if pricing else []
    if not profiles:
        return ""
    rows = []
    for item in profiles:
        rows.append(
            "<tr>"
            f"<td>{esc(item.get('publico'))}</td>"
            f"<td>USD {esc(item.get('preventa_usd'))}</td>"
            f"<td>USD {esc(item.get('lanzamiento_usd'))}</td>"
            f"<td>USD {esc(item.get('regular_usd'))}</td>"
            "</tr>"
        )
    return (
        "<article class=\"detail-block international-price-card\">"
        "<h2>Precios internacionales — USD</h2>"
        "<div class=\"table-scroll\"><table><thead><tr><th>Publico</th><th>Preventa</th><th>Lanzamiento</th><th>Regular</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table></div>"
        "<p>Equivalencia internacional referencial. Confirma la etapa y el importe final antes de pagar.</p>"
        "</article>"
        "<article class=\"detail-block international-payment-card\">"
        "<h2>Pagos internacionales</h2>"
        "<ul><li>PayPal.</li><li>Enlace de pago coordinado.</li><li>Conversión y comisión según PayPal o entidad financiera.</li><li>Confirmación comercial antes del pago.</li></ul>"
        "<a class=\"btn btn-small btn-gold\" href=\"https://www.paypal.com/paypalme/grupotecprog\" target=\"_blank\" rel=\"noopener noreferrer\">Solicitar pago PayPal</a>"
        "</article>"
    )


def syllabus_html(course: dict) -> str:
    modules = course.get("temario_por_sesion") or course.get("temario_base") or []
    if not modules:
        return "<p>Temario sujeto a confirmacion academica.</p>"
    blocks = []
    for module in modules:
        proposito = f"<p>{esc(module.get('proposito'))}</p>" if module.get("proposito") else ""
        practica = f"<p><strong>Practica:</strong> {esc(module.get('practica'))}</p>" if module.get("practica") else ""
        resultado = f"<p><strong>Resultado:</strong> {esc(module.get('resultado'))}</p>" if module.get("resultado") else ""
        blocks.append(
            "<article class=\"detail-block\">"
            f"<h3>Sesion {esc(module.get('modulo'))}: {esc(module.get('titulo'))}</h3>"
            f"{proposito}"
            f"{list_html(module.get('contenidos') or [])}"
            f"{practica}"
            f"{resultado}"
            "</article>"
        )
    return "".join(blocks)


def webp_size(path: Path) -> tuple[int, int] | tuple[None, None]:
    data = path.read_bytes()
    if len(data) < 30 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return (None, None)
    offset = 12
    while offset + 8 <= len(data):
        chunk = data[offset:offset + 4]
        size = int.from_bytes(data[offset + 4:offset + 8], "little")
        payload = offset + 8
        if chunk == b"VP8X" and payload + 10 <= len(data):
            width = 1 + int.from_bytes(data[payload + 4:payload + 7], "little")
            height = 1 + int.from_bytes(data[payload + 7:payload + 10], "little")
            return (width, height)
        if chunk == b"VP8 " and payload + 10 <= len(data):
            width = int.from_bytes(data[payload + 6:payload + 8], "little") & 0x3fff
            height = int.from_bytes(data[payload + 8:payload + 10], "little") & 0x3fff
            return (width, height)
        if chunk == b"VP8L" and payload + 5 <= len(data):
            b0, b1, b2, b3 = data[payload + 1:payload + 5]
            width = 1 + (((b1 & 0x3F) << 8) | b0)
            height = 1 + (((b3 & 0x0F) << 10) | (b2 << 2) | ((b1 & 0xC0) >> 6))
            return (width, height)
        offset += 8 + size + (size % 2)
    return (None, None)


def course_meta(course: dict) -> dict:
    slug = SLUGS.get(course["id"]) or course.get("slug") or slugify(course["nombre"])
    url_publica = f"cursos/{slug}/"
    seo = course.setdefault("seo", {})
    title = seo.get("title") or f"{course['nombre']} | TW Educa"
    description = seo.get("description") or course.get("descripcion_corta") or course["nombre"]
    image = seo.get("og_image") or course.get("og_image") or course.get("imagen")
    width, height = webp_size(ROOT / image) if image else (None, None)
    return {
        "id": course["id"],
        "slug": slug,
        "url_publica": url_publica,
        "title": title,
        "description": description,
        "canonical_url": absolute_url(url_publica),
        "og_image": image,
        "og_image_url": absolute_url(image),
        "og_image_width": width or 1200,
        "og_image_height": height or 1200,
        "og_image_type": image_type(image),
        "og_type": "website",
        "twitter_card": "summary_large_image",
    }


def page_html(course: dict, meta: dict) -> str:
    title = course["nombre"]
    desc = meta["description"]
    image_alt = f"Flyer del curso {title}"
    whatsapp = quote(course.get("whatsapp_mensaje") or f"Hola, deseo información sobre {title}.")
    learning = list_html(course.get("resultados_aprendizaje") or course.get("que_aprenderas") or [])
    requirements = list_html(course.get("requisitos") or [])
    tools = list_html(course.get("herramientas") or course.get("software") or [])
    deliverables = list_html(course.get("entregables") or [])
    methodology = list_html(course.get("metodologia") or [])
    return f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)} | Tecprog World Educa</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="canonical" href="{esc(meta['canonical_url'])}">
    <meta property="og:type" content="{esc(meta['og_type'])}">
    <meta property="og:site_name" content="Tecprog World">
    <meta property="og:locale" content="es_PE">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{esc(meta['canonical_url'])}">
    <meta property="og:image" content="{esc(meta['og_image_url'])}">
    <meta property="og:image:secure_url" content="{esc(meta['og_image_url'])}">
    <meta property="og:image:alt" content="{esc(image_alt)}">
    <meta property="og:image:type" content="{esc(meta['og_image_type'])}">
    <meta property="og:image:width" content="{esc(meta['og_image_width'])}">
    <meta property="og:image:height" content="{esc(meta['og_image_height'])}">
    <meta name="twitter:card" content="{esc(meta['twitter_card'])}">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(desc)}">
    <meta name="twitter:image" content="{esc(meta['og_image_url'])}">
    <link rel="icon" href="/assets/img/logos/logo-tecprog-world.png" type="image/png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="stylesheet" href="/assets/css/styles.css?v=20260729-07">
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="/index.html#inicio" aria-label="Volver al inicio">
        <img src="/assets/img/logos/logo-tecprog-world.png" alt="Logo Tecprog World" width="56" height="56">
        <span><strong>Tecprog World</strong><small>E.I.R.L. Perú</small></span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-nav-toggle><span></span><span></span><span></span><span class="sr-only">Abrir menu</span></button>
      <nav id="site-nav" class="site-nav" data-nav></nav>
    </header>
    <main class="detail-main" data-detail-root data-course-id="{esc(course['id'])}" data-catalog="tw-educa-vivo">
      <section class="detail-hero">
        <div class="section-shell detail-hero-grid">
          <div>
            <p class="eyebrow">TW Educa · Curso online</p>
            <h1>{esc(title)}</h1>
            <p>{esc(course.get('descripcion_corta') or desc)}</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="https://wa.me/51952354282?text={whatsapp}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
              <a class="btn btn-secondary" href="/educa/index.html">Volver a TW Educa</a>
            </div>
          </div>
          <figure class="detail-media">
            <img src="/{esc(meta['og_image'])}" alt="{esc(image_alt)}" loading="eager">
            <figcaption>{esc(course.get('modalidad') or 'Curso online')}</figcaption>
          </figure>
        </div>
      </section>
      <section class="section section-alt">
        <div class="section-shell" data-course-schedule data-course-id="{esc(course['id'])}"></div>
      </section>
      <section class="section">
        <div class="section-shell detail-layout">
          <div class="detail-content">
            <article class="detail-block">
              <h2>Inversion publicada</h2>
              {investment_html(course)}
            </article>
            {investment_usd_html(course)}
            <article class="detail-block">
              <h2>Temario por sesion</h2>
            </article>
            {syllabus_html(course)}
            <article class="detail-block">
              <h2>Resultados de aprendizaje</h2>
              {learning}
            </article>
            <article class="detail-block">
              <h2>Proyecto final</h2>
              <p>{esc(course.get('proyecto_final') or 'Proyecto aplicado integrador.')}</p>
            </article>
            <article class="detail-block">
              <h2>Entregables</h2>
              {deliverables}
            </article>
            <article class="detail-block">
              <h2>Herramientas</h2>
              {tools}
            </article>
            <article class="detail-block">
              <h2>Metodologia</h2>
              {methodology}
            </article>
            <article class="detail-block">
              <h2>Requisitos</h2>
              {requirements}
            </article>
            <article class="detail-block">
              <h2>Certificacion</h2>
              <p>{esc(course.get('certificacion') or 'Certificado fisico y firmado segun condiciones de la convocatoria.')}</p>
            </article>
          </div>
          <section class=\"detail-summary\">
            <article class="price-panel">
              <h2>Inscripcion</h2>
              <p>{esc(course.get('precio') or 'Consultar inversion')}</p>
              <div class="catalog-actions">
                <a class="btn btn-small btn-primary" href="https://wa.me/51952354282?text={whatsapp}" target="_blank" rel="noopener noreferrer">Inscribirme por WhatsApp</a>
                <a class="btn btn-small" href="/educa/index.html">Ver catalogo TW Educa</a>
              </div>
            </article>
          </section>
        </div>
      </section>
    </main>
    <script src="/assets/js/cronograma-tw-educa.js?v=20260729-07"></script>
    <script src="/assets/js/detalle.js?v=20260729-07"></script>
    <script src="/assets/js/navigation.js?v=20260729-07"></script>
    <script src="/assets/js/audio-player.js?v=20260729-07"></script>
  </body>
</html>
"""


def update_data(courses: list[dict], metas: list[dict]) -> None:
    by_id = {m["id"]: m for m in metas}
    for course in courses:
        meta = by_id[course["id"]]
        course["slug"] = meta["slug"]
        course["url_publica"] = meta["url_publica"]
        course["url_detalle"] = meta["url_publica"]
        course["og_image"] = meta["og_image"]
        course["og_image_width"] = meta["og_image_width"]
        course["og_image_height"] = meta["og_image_height"]
        course["og_type"] = meta["og_type"]
        course["twitter_card"] = meta["twitter_card"]
        course.setdefault("seo", {})
        course["seo"]["canonical_url"] = meta["canonical_url"]
        course["seo"]["og_image"] = meta["og_image"]
    write_json(COURSES_JSON, courses)

    catalog = read_json(CATALOGO_JSON)
    for item in catalog:
        if item.get("id") in by_id:
            item["slug"] = by_id[item["id"]]["slug"]
            item["url_publica"] = by_id[item["id"]]["url_publica"]
            item["url_detalle"] = by_id[item["id"]]["url_publica"]
            item["og_image"] = by_id[item["id"]]["og_image"]
    write_json(CATALOGO_JSON, catalog)


def update_sitemaps(courses: list[dict], metas: list[dict]) -> None:
    sitemap = read_json(SITEMAP_JSON) if SITEMAP_JSON.exists() else []
    existing = {item.get("ruta"): item for item in sitemap}
    for course, meta in zip(courses, metas):
        existing[meta["url_publica"]] = {
            "titulo": course["nombre"],
            "ruta": meta["url_publica"],
            "descripcion": meta["description"],
            "tipo": "curso",
        }
    ordered = [existing[key] for key in sorted(existing)]
    write_json(SITEMAP_JSON, ordered)

    if SITEMAP_XML.exists():
        xml_before = SITEMAP_XML.read_text(encoding="utf-8")
        locs = set(re.findall(r"<loc>(.*?)</loc>", xml_before))
        for item in ordered:
            ruta = item.get("ruta", "").lstrip("/")
            if ruta:
                locs.add(f"{BASE_URL}/{ruta}")
        entries = []
        for loc in sorted(locs):
            priority = "0.7" if "/cursos/" in loc else "0.6"
            entries.append(f"  <url>\n    <loc>{esc(loc)}</loc>\n    <lastmod>{date.today().isoformat()}</lastmod>\n    <priority>{priority}</priority>\n  </url>")
        xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(entries) + "\n</urlset>\n"
        SITEMAP_XML.write_text(xml, encoding="utf-8")


def generate_pages(courses: list[dict], metas: list[dict]) -> None:
    for course, meta in zip(courses, metas):
        target = ROOT / "cursos" / meta["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page_html(course, meta), encoding="utf-8")


def write_report(courses: list[dict], metas: list[dict]) -> None:
    lines = [
        "# Reporte de generacion de paginas sociales de cursos",
        "",
        f"Fecha: {date.today().isoformat()}",
        "",
        "## Resultado",
        "",
        f"- Cursos procesados: {len(courses)}",
        "- Directorio generado: `cursos/<slug>/index.html`",
        "- Open Graph escrito en HTML inicial.",
        "- Enlaces publicos actualizados en `data/cursos_tw_educa.json` y `data/catalogo_global.json`.",
        "- Sitemap comercial y `sitemap.xml` actualizados.",
        "",
        "## URLs generadas",
        "",
        "| ID | URL estatica | Imagen Open Graph | Dimensiones |",
        "|---|---|---|---|",
    ]
    for course, meta in zip(courses, metas):
        lines.append(
            f"| `{course['id']}` | `{meta['canonical_url']}` | `{meta['og_image']}` | {meta['og_image_width']}x{meta['og_image_height']} |"
        )
    lines.extend([
        "",
        "## Extension a productos y servicios",
        "",
        "El generador deja separadas las funciones de lectura de datos, metadatos, plantilla HTML y sitemap. Para productos y servicios se debe crear un mapeo equivalente desde `data/catalogo_global.json`, definir `productos/<slug>/` o `servicios/<slug>/`, y reutilizar la misma regla: metadatos absolutos en HTML inicial, no por JavaScript.",
        "",
    ])
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    courses = read_json(COURSES_JSON)
    metas = [course_meta(course) for course in courses]
    update_data(courses, metas)
    generate_pages(courses, metas)
    update_sitemaps(courses, metas)
    write_report(courses, metas)
    print(f"Generadas {len(courses)} paginas sociales de cursos.")


if __name__ == "__main__":
    main()
