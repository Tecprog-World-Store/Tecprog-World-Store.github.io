#!/usr/bin/env python3
"""
Revision semanal conservadora de fuentes para TW Store.

Uso:
    python tools/revisar_catalogo_fuentes.py

Objetivo:
    Leer las URLs publicas registradas en data/productos_store.json y generar
    data/operacion/reporte_revision_catalogo.md como apoyo manual.

Reglas:
    - No automatiza compras.
    - No envia mensajes.
    - No descarga imagenes.
    - No evade bloqueos.
    - No hace scraping agresivo.
    - Deduplica URLs para no consultar repetidamente la misma fuente.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_PATH = ROOT / "data" / "productos_store.json"
REPORT_PATH = ROOT / "data" / "operacion" / "reporte_revision_catalogo.md"

USER_AGENT = "TW-Store-Revision-Semanal/1.0 (+manual review; no aggressive scraping)"
DEFAULT_TIMEOUT = 12
DEFAULT_DELAY = 2.5


@dataclass
class FetchResult:
    ok: bool
    url: str
    status_code: int | None
    text: str
    observation: str


def load_products() -> list[dict[str, Any]]:
    with PRODUCTS_PATH.open("r", encoding="utf-8-sig") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("data/productos_store.json debe contener una lista de productos.")
    return data


def clean_text(value: Any) -> str:
    text = str(value or "").strip()
    if any(mark in text for mark in ("Ã", "Â", "â")):
        try:
            text = text.encode("latin-1").decode("utf-8")
        except UnicodeError:
            pass
    return text


def money(value: Any) -> str:
    try:
        return f"S/ {float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (TypeError, ValueError):
        return "Sin precio registrado"


def fetch_url(url: str, timeout: int) -> FetchResult:
    if not url.startswith(("http://", "https://")):
        return FetchResult(False, url, None, "", "URL no valida para revision automatica.")

    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})
    try:
        with urlopen(request, timeout=timeout) as response:
            content_type = response.headers.get("Content-Type", "")
            raw = response.read(500_000)
            if "text/html" not in content_type and "application/xhtml" not in content_type:
                return FetchResult(False, url, response.status, "", f"Contenido no HTML: {content_type}")
            text = raw.decode("utf-8", errors="ignore")
            return FetchResult(True, url, response.status, text, "Fuente leida para revision preliminar.")
    except HTTPError as exc:
        return FetchResult(False, url, exc.code, "", f"HTTP {exc.code}; requiere revision manual.")
    except URLError as exc:
        return FetchResult(False, url, None, "", f"No se pudo leer la fuente: {exc.reason}")
    except TimeoutError:
        return FetchResult(False, url, None, "", "Timeout; requiere revision manual.")
    except Exception as exc:  # noqa: BLE001 - reporte operativo, no debe romper toda la revision
        return FetchResult(False, url, None, "", f"Error no esperado: {exc}")


def is_general_source_url(url: str) -> bool:
    """
    Evita tomar precios de homepages o portadas como si fueran precios de producto.
    Lo ideal es registrar URLs especificas de producto en data/productos_store.json.
    """
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    return not path or path.lower() in {"catalogo", "tienda", "store", "productos"}


def detect_price(text: str) -> float | None:
    """
    Deteccion basica y prudente de precios en soles.
    No interpreta JavaScript ni intenta evadir protecciones.
    """
    patterns = [
        r"S/\s*([0-9]{1,3}(?:[.,][0-9]{3})*(?:[.,][0-9]{2})?)",
        r"soles?\s*([0-9]{1,3}(?:[.,][0-9]{3})*(?:[.,][0-9]{2})?)",
    ]
    candidates: list[float] = []
    for pattern in patterns:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            raw = match.group(1)
            normalized = raw.replace(".", "").replace(",", ".")
            try:
                value = float(normalized)
            except ValueError:
                continue
            if 10 <= value <= 50_000:
                candidates.append(value)
    return min(candidates) if candidates else None


def classify_price(registered: Any, reviewed: float | None, fetch: FetchResult) -> tuple[str, str]:
    if not fetch.ok:
        return "requiere_revision_manual", fetch.observation
    if reviewed is None:
        return "requiere_revision_manual", "Fuente leida, pero no se detecto precio de forma confiable."

    try:
        registered_value = float(registered)
    except (TypeError, ValueError):
        return "requiere_revision_manual", "No hay precio registrado comparable."

    difference = abs(reviewed - registered_value)
    if difference <= max(5.0, registered_value * 0.02):
        return "ok", "Precio detectado cercano al precio fuente registrado."
    return "cambio_detectado", f"Precio detectado difiere del registrado por S/ {difference:.2f}."


def build_report(products: list[dict[str, Any]], fetches: dict[str, FetchResult]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Reporte de revision de catalogo TW Store",
        "",
        f"Generado: {now}",
        "",
        "Este reporte es un apoyo operativo. No reemplaza la revision humana de precio, stock, garantia y envio.",
        "",
        "| Producto | Fuente | URL | Precio actual registrado | Precio revisado si se detecta | Estado | Observacion |",
        "|---|---|---|---:|---:|---|---|",
    ]

    for product in products:
        name = clean_text(product.get("nombre"))
        source = clean_text(product.get("fuente"))
        url = clean_text(product.get("url_fuente"))
        registered = product.get("precio_fuente")
        fetch = fetches.get(url) or FetchResult(False, url, None, "", "URL no revisada.")
        reviewed = detect_price(fetch.text) if fetch.ok else None
        status, observation = classify_price(registered, reviewed, fetch)
        reviewed_text = money(reviewed) if reviewed is not None else "No detectado"
        lines.append(
            "| {producto} | {fuente} | {url} | {registrado} | {revisado} | {estado} | {observacion} |".format(
                producto=name.replace("|", "/"),
                fuente=source.replace("|", "/"),
                url=url.replace("|", "/"),
                registrado=money(registered),
                revisado=reviewed_text,
                estado=status,
                observacion=observation.replace("|", "/"),
            )
        )

    lines.extend(
        [
            "",
            "## Reglas aplicadas",
            "",
            "- Solo se leyeron URLs publicas ya registradas en `data/productos_store.json`.",
            "- No se automatizaron compras, mensajes ni publicaciones.",
            "- No se descargaron imagenes.",
            "- Las URLs repetidas se consultaron una sola vez.",
            "- Si el precio no se detecto de forma confiable, el producto queda para revision manual.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera reporte semanal de revision de fuentes TW Store.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Timeout por URL en segundos.")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY, help="Pausa entre URLs en segundos.")
    parser.add_argument("--sin-red", action="store_true", help="Genera reporte sin consultar URLs; todo queda para revision manual.")
    args = parser.parse_args()

    products = load_products()
    urls = []
    for product in products:
        url = clean_text(product.get("url_fuente"))
        if url and url not in urls:
            urls.append(url)

    fetches: dict[str, FetchResult] = {}
    for index, url in enumerate(urls):
        if args.sin_red:
            fetches[url] = FetchResult(False, url, None, "", "Revision sin red; requiere revision manual.")
            continue
        if is_general_source_url(url):
            fetches[url] = FetchResult(
                False,
                url,
                None,
                "",
                "URL de portada o fuente general; registrar URL especifica de producto para detectar precio.",
            )
            continue
        fetches[url] = fetch_url(url, timeout=args.timeout)
        if index < len(urls) - 1:
            time.sleep(max(0.0, args.delay))

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_report(products, fetches), encoding="utf-8")
    print(f"Reporte generado: {REPORT_PATH}")


if __name__ == "__main__":
    main()
