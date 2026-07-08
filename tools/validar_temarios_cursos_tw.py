#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSES_JSON = ROOT / "data" / "cursos_tw_educa.json"


def main() -> int:
    errors: list[str] = []
    courses = json.loads(COURSES_JSON.read_text(encoding="utf-8"))
    ids = set()
    for course in courses:
        if course["id"] in ids:
            errors.append(f"ID duplicado: {course['id']}")
        ids.add(course["id"])
        modules = course.get("temario_por_sesion") or []
        expected = int(course.get("numero_sesiones") or len(modules))
        if len(modules) != expected:
            errors.append(f"Numero de sesiones inconsistente en {course['id']}: {len(modules)} vs {expected}")
        if not course.get("proyecto_final"):
            errors.append(f"Curso sin proyecto final: {course['id']}")
        for module in modules:
            contents = module.get("contenidos") or []
            if len(contents) < 4:
                errors.append(f"Sesion con menos de 4 temas en {course['id']} modulo {module.get('modulo')}")
            for key in ("titulo", "proposito", "practica", "resultado"):
                if not module.get(key):
                    errors.append(f"Sesion sin {key} en {course['id']} modulo {module.get('modulo')}")
    if errors:
        print("\n".join(errors))
        return 1
    print("OK: temarios TW Educa validados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
