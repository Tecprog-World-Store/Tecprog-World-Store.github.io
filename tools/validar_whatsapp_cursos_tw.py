#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
COURSES_JSON = ROOT / "data" / "cursos_tw_educa.json"
DETAIL_JS = ROOT / "assets" / "js" / "detalle.js"
CATALOG_JS = ROOT / "assets" / "js" / "catalogo-global.js"
STATIC_DIR = ROOT / "cursos"
FORBIDDEN = [
    "material introductorio",
    "acceder gratis",
    "contenido gratuito",
    "descargar material",
    "quiero el material",
    "solicitar material",
]


def main() -> int:
    errors: list[str] = []
    courses = json.loads(COURSES_JSON.read_text(encoding="utf-8"))
    for course in courses:
        message = course.get("whatsapp_mensaje") or ""
        lower = message.lower()
        if course.get("nombre") not in message:
            errors.append(f"WhatsApp sin nombre exacto del curso: {course.get('id')}")
        if any(term in lower for term in FORBIDDEN) or "gratis" in lower:
            errors.append(f"WhatsApp con CTA gratuito prohibido: {course.get('id')}")
        href = f"https://wa.me/51952354282?text={quote(message)}"
        if "51952354282" not in href or "%20" not in href:
            errors.append(f"Enlace WhatsApp no codificado correctamente: {course.get('id')}")
    for path in [DETAIL_JS, CATALOG_JS, *STATIC_DIR.glob("*/index.html")]:
        text = path.read_text(encoding="utf-8").lower()
        for term in FORBIDDEN:
            if term in text:
                errors.append(f"Texto prohibido '{term}' en {path.relative_to(ROOT)}")
    if errors:
        print("\n".join(errors))
        return 1
    print("OK: WhatsApp TW Educa validado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
