#!/usr/bin/env python3
"""
Convierte el catalogo TXT de reventa TW Store a JSON.

Uso desde la raiz del repositorio:

    python tools/convertir_catalogo_txt_a_json.py

Opciones:

    python tools/convertir_catalogo_txt_a_json.py --input data/catalogos/tecprog_world_store_catalogo_reventa.txt --output data/productos_store.json

Notas:
- No descarga imagenes.
- No usa credenciales.
- Si el TXT no se puede parsear, genera una plantilla manual con productos bandera.
- Valida que el JSON final pueda leerse correctamente.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Iterable


DEFAULT_INPUT = Path("data/catalogos/tecprog_world_store_catalogo_reventa.txt")
DEFAULT_OUTPUT = Path("data/productos_store.json")
DEFAULT_IMAGE = "../assets/img/store/productos/producto-generico.webp"
DEFAULT_REVISION = "2026-06-11"

SOURCE_URLS = {
    "Coolbox": "https://www.coolbox.pe/",
    "Memory Kings": "https://www.memorykings.pe/",
    "Masplay": "https://masplay.pe/",
}

CATEGORY_MAP = {
    "celulares": "Celulares",
    "audifonos": "Audio",
    "audífonos": "Audio",
    "audio apple": "Apple",
    "parlantes pc": "Audio",
    "parlantes karaoke": "Audio",
    "laptop gaming": "Laptops",
    "monitor gaming": "Monitores",
    "ordenadores apple": "Apple",
    "smartwatch": "Apple",
    "ipad/tablets": "Apple",
    "realidad virtual": "Realidad Virtual",
    "accesorios premium": "Accesorios",
    "accesorios apple": "Accesorios",
}


def money_to_decimal(value: str) -> Decimal:
    """Convierte textos como 'S/ 2,699.00' a Decimal('2699.00')."""
    cleaned = value.replace("S/", "").replace(",", "").strip()
    cleaned = re.sub(r"[^0-9.]", "", cleaned)
    if not cleaned:
        raise ValueError(f"Precio invalido: {value!r}")
    return Decimal(cleaned).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def round_money(value: Decimal) -> float:
    return float(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def slugify(value: str) -> str:
    replacements = str.maketrans(
        "áéíóúÁÉÍÓÚñÑüÜ",
        "aeiouAEIOUnNuU",
    )
    text = value.translate(replacements).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "producto"


def normalize_category(raw: str) -> str:
    key = raw.strip().lower()
    return CATEGORY_MAP.get(key, raw.strip())


def source_from_heading(heading: str) -> str:
    upper = heading.upper()
    if "COOLBOX" in upper:
        return "Coolbox"
    if "MEMORY KINGS" in upper:
        return "Memory Kings"
    if "MASPLAY" in upper:
        return "Masplay"
    return "Proveedor por confirmar"


def etiquetas_for(product: dict, index: int) -> list[str]:
    etiquetas: list[str] = ["bajo_pedido"]
    if product["categoria"] in {"Apple", "Realidad Virtual", "Laptops"}:
        etiquetas.insert(0, "producto_bandera")
    if index <= 10 or product["categoria"] in {"Celulares", "Audio"}:
        etiquetas.append("oferta")
    if product["estado"] == "stock_por_confirmar":
        etiquetas.append("stock_por_confirmar")
    return list(dict.fromkeys(etiquetas))


def parse_product_blocks(text: str) -> list[tuple[int, str]]:
    matches = list(re.finditer(r"(?m)^(\d{2})\s+\|\s+Categoría:", text))
    blocks: list[tuple[int, str]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        blocks.append((int(match.group(1)), text[start:end].strip()))
    return blocks


def current_source_for_block(text_before_block: str) -> str:
    headings = re.findall(r"(?m)^=+\n([A-Z]\.\s+[^\n]+)\n=+", text_before_block)
    if not headings:
        return "Proveedor por confirmar"
    return source_from_heading(headings[-1])


def parse_products(text: str) -> list[dict]:
    products: list[dict] = []
    blocks = parse_product_blocks(text)
    for index, block in blocks:
        before = text[: text.find(block)]
        fuente = current_source_for_block(before)

        categoria_match = re.search(r"Categoría:\s*(.+)", block)
        nombre_match = re.search(r"Producto fuente:\s*(.+)", block)
        precio_match = re.search(r"Precio fuente:\s*S/\s*([0-9,.]+)", block)
        gancho_match = re.search(r"Gancho de flyer:\s*(.+)", block)
        stock_match = re.search(r"Stock fuente:\s*(.+)", block)

        if not (categoria_match and nombre_match and precio_match):
            continue

        precio = money_to_decimal(precio_match.group(1))
        categoria = normalize_category(categoria_match.group(1))
        estado = "stock_por_confirmar" if stock_match else "stock_por_confirmar"
        product = {
            "id": f"tw-store-{index:03d}",
            "nombre": nombre_match.group(1).strip(),
            "categoria": categoria,
            "precio_fuente": round_money(precio),
            "precio_tw_8": round_money(precio * Decimal("1.08")),
            "precio_tw_12": round_money(precio * Decimal("1.12")),
            "precio_tw_18": round_money(precio * Decimal("1.18")),
            "precio_publico": round_money(precio * Decimal("1.12")),
            "fuente": fuente,
            "url_fuente": SOURCE_URLS.get(fuente, ""),
            "estado": estado,
            "etiquetas": [],
            "imagen": DEFAULT_IMAGE,
            "gancho": gancho_match.group(1).strip() if gancho_match else "Producto tecnologico bajo cotizacion.",
            "ultima_revision": DEFAULT_REVISION,
        }
        product["etiquetas"] = etiquetas_for(product, index)
        products.append(product)
    return products


def manual_flagship_template() -> list[dict]:
    """Fallback manual si el TXT cambia demasiado de formato."""
    raw_products = [
        ("tw-store-001", "PICO 4 ULTRA 256GB + 12GB RAM", "Realidad Virtual", Decimal("3199.00"), "Masplay", "Realidad virtual para entretenimiento, inmersion y demostraciones tecnologicas."),
        ("tw-store-002", "MacBook Air 13 Chip M5 512GB 16GB RAM", "Apple", Decimal("4499.00"), "Masplay", "Laptop ultraligera para estudio, trabajo y movilidad."),
        ("tw-store-003", "iPhone 16e 5G 128GB", "Celulares", Decimal("2699.00"), "Coolbox", "iPhone 16e 5G para trabajo, estudio y creacion de contenido."),
        ("tw-store-004", "ASUS TUF Gaming F16 RTX 5050", "Laptops", Decimal("4819.50"), "Memory Kings", "Alto rendimiento para gaming, ingenieria y edicion."),
        ("tw-store-005", "AirPods Pro 3 2025", "Apple", Decimal("869.00"), "Masplay", "Audio premium para concentracion y productividad."),
    ]
    products = []
    for index, (product_id, nombre, categoria, precio, fuente, gancho) in enumerate(raw_products, start=1):
        product = {
            "id": product_id,
            "nombre": nombre,
            "categoria": categoria,
            "precio_fuente": round_money(precio),
            "precio_tw_8": round_money(precio * Decimal("1.08")),
            "precio_tw_12": round_money(precio * Decimal("1.12")),
            "precio_tw_18": round_money(precio * Decimal("1.18")),
            "precio_publico": round_money(precio * Decimal("1.12")),
            "fuente": fuente,
            "url_fuente": SOURCE_URLS.get(fuente, ""),
            "estado": "stock_por_confirmar",
            "etiquetas": ["producto_bandera", "bajo_pedido", "stock_por_confirmar"],
            "imagen": DEFAULT_IMAGE,
            "gancho": gancho,
            "ultima_revision": DEFAULT_REVISION,
        }
        if index == 3:
            product["etiquetas"].append("oferta")
        products.append(product)
    return products


def validate_products(products: Iterable[dict]) -> None:
    required = {
        "id",
        "nombre",
        "categoria",
        "precio_fuente",
        "precio_tw_8",
        "precio_tw_12",
        "precio_tw_18",
        "precio_publico",
        "fuente",
        "url_fuente",
        "estado",
        "etiquetas",
        "imagen",
        "gancho",
        "ultima_revision",
    }
    seen: set[str] = set()
    for product in products:
        missing = required - set(product)
        if missing:
            raise ValueError(f"Producto incompleto {product.get('id')}: {sorted(missing)}")
        if product["id"] in seen:
            raise ValueError(f"ID duplicado: {product['id']}")
        seen.add(product["id"])
        json.dumps(product, ensure_ascii=False)


def convert(input_path: Path, output_path: Path) -> list[dict]:
    if not input_path.exists():
        print(f"No se encontro {input_path}. Se generara plantilla manual.")
        products = manual_flagship_template()
    else:
        text = input_path.read_text(encoding="utf-8")
        products = parse_products(text)
        if not products:
            print("No se pudo parsear automaticamente el TXT. Se generara plantilla manual.")
            products = manual_flagship_template()

    validate_products(products)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(products, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Validacion final: leer el archivo escrito y parsearlo nuevamente.
    json.loads(output_path.read_text(encoding="utf-8"))
    return products


def main() -> None:
    parser = argparse.ArgumentParser(description="Convierte catalogo TXT TW Store a JSON.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Ruta del TXT fuente.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Ruta JSON destino.")
    args = parser.parse_args()

    products = convert(args.input, args.output)
    print(f"JSON generado: {args.output}")
    print(f"Productos exportados: {len(products)}")
    print("Imagenes: no se descargaron imagenes automaticamente.")


if __name__ == "__main__":
    main()
