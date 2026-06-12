#!/usr/bin/env python3
"""
Genera flyers HTML verticales para TW Store.

Uso:
    python tools/generar_flyers_html_tw_store.py

Entradas:
    data/productos_store.json
    data/visual/visual_briefs_store.json

Salida:
    build/flyers_html/index.html
    build/flyers_html/<id-producto>-flyer.html

Este script no exporta PNG/WEBP ni descarga imagenes. Solo crea HTML estatico
de 1080x1920 px para revisar composicion visual antes de producir piezas finales.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_PATH = ROOT / "data" / "productos_store.json"
BRIEFS_PATH = ROOT / "data" / "visual" / "visual_briefs_store.json"
OUTPUT_DIR = ROOT / "build" / "flyers_html"

CONTACTO_WHATSAPP = "51952354282"
AVISO_COMERCIAL = "Producto sujeto a disponibilidad, confirmacion de precio, garantia y condiciones de entrega."

PLACEHOLDERS = {
    "celulares": "celular.svg",
    "laptop_gaming": "laptop.svg",
    "monitor_gaming": "monitor.svg",
    "audio_premium": "audifonos.svg",
    "realidad_virtual": "realidad-virtual.svg",
    "accesorios": "accesorio.svg",
    "general": "producto-generico.svg",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "flyer"


def money(value: Any) -> str:
    try:
        return f"S/ {float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (TypeError, ValueError):
        return "Consultar"


def normalize_repo_image_path(raw_path: str | None) -> Path | None:
    if not raw_path:
        return None

    clean = raw_path.replace("\\", "/")
    while clean.startswith("../"):
        clean = clean[3:]
    clean = clean.lstrip("/")
    return ROOT / clean


def rel_from_output(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def html_asset_path(path: Path) -> str:
    return "../../" + rel_from_output(path)


def placeholder_for(tipo_flyer: str) -> Path:
    filename = PLACEHOLDERS.get(tipo_flyer, PLACEHOLDERS["general"])
    return ROOT / "assets" / "img" / "store" / "placeholders" / filename


def image_for_product(product: dict[str, Any], brief: dict[str, Any]) -> Path:
    image_path = normalize_repo_image_path(product.get("imagen"))
    if image_path and image_path.exists():
        return image_path
    return placeholder_for(str(brief.get("tipo_flyer", "general")))


def pretty_label(value: str) -> str:
    labels = {
        "producto_bandera": "Producto bandera",
        "bajo_pedido": "Bajo pedido",
        "stock_por_confirmar": "Stock por confirmar",
        "oferta": "Oferta",
    }
    return labels.get(value, value.replace("_", " ").title())


def build_whatsapp_url(nombre: str) -> str:
    mensaje = f"Hola Tecprog World, deseo cotizar el producto: {nombre}. ¿Esta disponible para envio?"
    return f"https://wa.me/{CONTACTO_WHATSAPP}?text={quote(mensaje)}"


def render_tags(tags: list[str]) -> str:
    if not tags:
        return ""
    return "\n".join(f'<span class="tag tag-{html.escape(slugify(tag))}">{html.escape(pretty_label(tag))}</span>' for tag in tags[:4])


def render_flyer(product: dict[str, Any], brief: dict[str, Any]) -> str:
    title = str(brief.get("nombre") or product.get("nombre") or "Producto TW Store")
    category = str(brief.get("categoria") or product.get("categoria") or "Tecnologia")
    hook = str(brief.get("texto_secundario") or product.get("gancho") or "Tecnologia seleccionada para compra bajo cotizacion.")
    price = money(product.get("precio_publico"))
    source = str(product.get("fuente") or "Proveedor referencial")
    image_path = html_asset_path(image_for_product(product, brief))
    tags = list(product.get("etiquetas") or [])
    whatsapp_url = build_whatsapp_url(title)

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | Flyer TW Store</title>
  <style>
    :root {{
      --azul-noche: #07172f;
      --celeste: #0aa4d8;
      --blanco: #f8fbff;
      --gris: #d9e2ec;
      --amarillo: #f6c445;
      --verde: #23c483;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: #101827;
      font-family: Arial, Helvetica, sans-serif;
      color: var(--blanco);
    }}
    .flyer {{
      position: relative;
      width: 1080px;
      height: 1920px;
      overflow: hidden;
      background:
        radial-gradient(circle at 20% 12%, rgba(10, 164, 216, .34), transparent 28%),
        linear-gradient(160deg, #07172f 0%, #0b2548 48%, #06101f 100%);
      padding: 88px 84px;
    }}
    .brand-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 28px;
      min-height: 96px;
    }}
    .brand {{
      font-size: 58px;
      line-height: 1;
      font-weight: 900;
      letter-spacing: 0;
    }}
    .brand span {{ color: var(--celeste); }}
    .category {{
      border: 2px solid rgba(255,255,255,.24);
      border-radius: 999px;
      padding: 20px 30px;
      font-size: 28px;
      font-weight: 700;
      color: var(--gris);
      text-align: right;
    }}
    .safe-zone {{
      position: absolute;
      left: 0;
      top: 420px;
      width: 1080px;
      height: 1080px;
      display: grid;
      place-items: center;
      pointer-events: none;
    }}
    .product-stage {{
      width: 820px;
      height: 820px;
      display: grid;
      place-items: center;
      border-radius: 60px;
      background: rgba(255,255,255,.07);
      box-shadow: inset 0 0 0 2px rgba(255,255,255,.12), 0 46px 120px rgba(0,0,0,.32);
    }}
    .product-stage img {{
      width: 760px;
      height: 760px;
      object-fit: contain;
      filter: drop-shadow(0 32px 54px rgba(0,0,0,.38));
    }}
    .headline {{
      position: absolute;
      left: 84px;
      right: 84px;
      top: 210px;
    }}
    h1 {{
      margin: 0;
      max-width: 900px;
      font-size: 66px;
      line-height: 1.05;
      font-weight: 900;
      letter-spacing: 0;
    }}
    .hook {{
      margin-top: 28px;
      max-width: 760px;
      color: var(--gris);
      font-size: 34px;
      line-height: 1.28;
      font-weight: 600;
    }}
    .offer-panel {{
      position: absolute;
      left: 84px;
      right: 84px;
      bottom: 120px;
      display: grid;
      gap: 28px;
    }}
    .tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .tag {{
      display: inline-flex;
      align-items: center;
      min-height: 54px;
      padding: 13px 22px;
      border-radius: 999px;
      background: rgba(255,255,255,.1);
      color: var(--blanco);
      font-size: 24px;
      font-weight: 800;
    }}
    .tag-oferta {{
      background: var(--amarillo);
      color: #142033;
    }}
    .price-row {{
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 32px;
    }}
    .price-label {{
      font-size: 28px;
      color: var(--gris);
      font-weight: 700;
    }}
    .price {{
      margin-top: 8px;
      color: var(--amarillo);
      font-size: 78px;
      line-height: 1;
      font-weight: 900;
    }}
    .source {{
      color: rgba(255,255,255,.64);
      font-size: 22px;
      line-height: 1.2;
      text-align: right;
    }}
    .cta {{
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 92px;
      border-radius: 28px;
      background: var(--verde);
      color: #03150d;
      text-decoration: none;
      font-size: 34px;
      font-weight: 900;
      box-shadow: 0 22px 44px rgba(35, 196, 131, .28);
    }}
    .legal {{
      color: rgba(255,255,255,.68);
      font-size: 22px;
      line-height: 1.32;
      text-align: center;
    }}
    .watermark {{
      position: absolute;
      right: -110px;
      top: 770px;
      transform: rotate(-90deg);
      color: rgba(255,255,255,.08);
      font-size: 92px;
      font-weight: 900;
      letter-spacing: 0;
      white-space: nowrap;
    }}
  </style>
</head>
<body>
  <main class="flyer" aria-label="Flyer vertical TW Store">
    <div class="brand-row">
      <div class="brand">TW <span>Store</span></div>
      <div class="category">{html.escape(category)}</div>
    </div>

    <section class="headline">
      <h1>{html.escape(title)}</h1>
      <p class="hook">{html.escape(hook)}</p>
    </section>

    <section class="safe-zone" aria-label="Zona segura central 1080 por 1080">
      <div class="product-stage">
        <img src="{image_path}" alt="{html.escape(title)}">
      </div>
    </section>

    <section class="offer-panel">
      <div class="tags">{render_tags(tags)}</div>
      <div class="price-row">
        <div>
          <div class="price-label">Precio TW Store referencial</div>
          <div class="price">{html.escape(price)}</div>
        </div>
        <div class="source">Fuente referencial:<br>{html.escape(source)}</div>
      </div>
      <a class="cta" href="{whatsapp_url}">Cotiza por WhatsApp</a>
      <div class="legal">{html.escape(AVISO_COMERCIAL)}</div>
    </section>
    <div class="watermark">TECNOLOGIA BAJO COTIZACION</div>
  </main>
</body>
</html>
"""


def render_index(files: list[tuple[str, str]]) -> str:
    links = "\n".join(
        f'<li><a href="{html.escape(filename)}">{html.escape(title)}</a></li>' for filename, title in files
    )
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Flyers HTML TW Store</title>
  <style>
    body {{ margin: 0; font-family: Arial, sans-serif; background: #07172f; color: #f8fbff; padding: 32px; }}
    h1 {{ margin-top: 0; }}
    a {{ color: #0aa4d8; font-weight: 700; }}
    li {{ margin: 10px 0; }}
    .note {{ max-width: 760px; color: #d9e2ec; line-height: 1.5; }}
  </style>
</head>
<body>
  <h1>Flyers HTML TW Store</h1>
  <p class="note">Vista previa estatica. Cada archivo simula un flyer vertical de 1080x1920 px; no se generaron imagenes finales.</p>
  <ul>
    {links}
  </ul>
</body>
</html>
"""


def main() -> None:
    products = load_json(PRODUCTS_PATH)
    briefs = load_json(BRIEFS_PATH)

    product_by_id = {str(product.get("id")): product for product in products}
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    generated: list[tuple[str, str]] = []
    for brief in briefs:
        product_id = str(brief.get("id_producto"))
        product = product_by_id.get(product_id)
        if not product:
            print(f"[aviso] Producto no encontrado para brief: {product_id}")
            continue

        filename = f"{slugify(product_id)}-flyer.html"
        output_path = OUTPUT_DIR / filename
        output_path.write_text(render_flyer(product, brief), encoding="utf-8")
        generated.append((filename, str(product.get("nombre") or product_id)))

    (OUTPUT_DIR / "index.html").write_text(render_index(generated), encoding="utf-8")
    print(f"Flyers HTML generados: {len(generated)}")
    print(f"Indice: {OUTPUT_DIR / 'index.html'}")


if __name__ == "__main__":
    main()
