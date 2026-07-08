#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSES_JSON = ROOT / "data" / "cursos_tw_educa.json"
CATALOG_JSON = ROOT / "data" / "catalogo_global.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    courses = read_json(COURSES_JSON)
    catalog = read_json(CATALOG_JSON)
    if len(courses) != 37:
        errors.append(f"Se esperaban 37 cursos TW Educa, encontrados {len(courses)}.")
    seen_slugs: set[str] = set()
    for course in courses:
        slug = course.get("slug")
        if slug in seen_slugs:
            errors.append(f"Slug duplicado: {slug}")
        seen_slugs.add(slug)
        if course.get("precio_soles") in (0, 1) or "S/ 1 IGV" in str(course.get("precio")):
            errors.append(f"Precio critico en {course.get('id')}: {course.get('precio')}")
        prices = course.get("precios") or []
        if not prices:
            errors.append(f"Curso sin estructura de precios: {course.get('id')}")
        for price in prices:
            for key in ("preventa_soles", "lanzamiento_soles", "regular_soles"):
                value = price.get(key)
                if not isinstance(value, int) or value <= 1:
                    errors.append(f"Precio invalido {key}={value} en {course.get('id')}")
        if not course.get("imagen"):
            errors.append(f"Curso sin imagen: {course.get('id')}")
        if course.get("fuente_interna") and "fuente_interna" in json.dumps(catalog, ensure_ascii=False):
            errors.append("Campo interno fuente_interna expuesto en catalogo_global.json")
    if errors:
        print("\n".join(errors))
        return 1
    print("OK: precios TW Educa validados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
