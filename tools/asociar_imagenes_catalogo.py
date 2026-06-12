from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalogo_global.json"
PRODUCTS_DIR = ROOT / "assets" / "img" / "store" / "productos"
REPORT = ROOT / "docs" / "operacion" / "reporte_asociacion_imagenes_catalogo.md"


def main() -> None:
    items = json.loads(CATALOG.read_text(encoding="utf-8"))
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = CATALOG.with_suffix(f".backup-{stamp}.json")
    shutil.copy2(CATALOG, backup)

    updates = []
    for item in items:
        expected = PRODUCTS_DIR / f"{item['id']}.webp"
        rel = expected.relative_to(ROOT).as_posix()
        if expected.exists() and item.get("imagen") != rel:
            updates.append((item["id"], item.get("imagen", ""), rel))
            item["imagen"] = rel

    if updates:
        CATALOG.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Reporte de asociación de imágenes al catálogo",
        "",
        f"Backup creado: `{backup.relative_to(ROOT).as_posix()}`",
        "",
        f"Actualizaciones: {len(updates)}",
        "",
        "| Item | Imagen anterior | Imagen nueva |",
        "|---|---|---|",
    ]
    if updates:
        lines.extend(f"| {item_id} | `{old}` | `{new}` |" for item_id, old, new in updates)
    else:
        lines.append("| - | - | No se encontraron imágenes nuevas para asociar. |")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Reporte generado: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
