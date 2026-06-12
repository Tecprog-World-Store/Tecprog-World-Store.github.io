from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs" / "operacion" / "reporte_imagenes_tw.md"

try:
    from PIL import Image  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    Image = None


@dataclass
class ImageCheck:
    section: str
    key: str
    path: Path
    expected_size: str
    expected_weight: str
    status: str
    detail: str
    weight_kb: float | None = None
    dimensions: tuple[int, int] | None = None


def load_json(path: str) -> Any:
    with (ROOT / path).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def parse_weight_limit(text: str) -> tuple[int | None, int | None]:
    numbers = []
    for part in text.replace("KB", "").replace("kb", "").replace("a", " ").split():
        try:
            numbers.append(int(part))
        except ValueError:
            pass
    if len(numbers) >= 2:
        return numbers[0], numbers[1]
    if len(numbers) == 1:
        return None, numbers[0]
    return None, None


def expected_dimensions(text: str) -> tuple[int, int] | None:
    cleaned = text.lower().replace("px", "").replace(" ", "")
    for token in cleaned.replace("o", "|").split("|"):
        if "x" not in token:
            continue
        left, right = token.split("x", 1)
        if left.isdigit() and right.isdigit():
            return int(left), int(right)
    return None


def check_record(section: str, record: dict[str, Any]) -> ImageCheck:
    key = record.get("id") or record.get("linea_negocio") or "sin-id"
    rel = record.get("archivo_esperado", "")
    path = ROOT / rel
    expected_size = record.get("dimensiones_recomendadas", "")
    expected_weight = record.get("peso_recomendado", "")

    if not rel:
        return ImageCheck(section, key, path, expected_size, expected_weight, "REVISAR", "Sin archivo_esperado.")

    if not path.exists():
        return ImageCheck(section, key, path, expected_size, expected_weight, "PENDIENTE", "Archivo pendiente.")

    weight_kb = path.stat().st_size / 1024
    details = []
    status = "OK"

    if path.suffix.lower() != ".webp":
        status = "REVISAR"
        details.append("Extensión distinta de .webp.")

    _min_kb, max_kb = parse_weight_limit(expected_weight)
    if max_kb and weight_kb > max_kb:
        status = "OPTIMIZAR"
        details.append(f"Peso {weight_kb:.1f} KB supera recomendado {max_kb} KB.")

    dimensions = None
    if Image is None:
        details.append("Dimensiones no verificadas: instala Pillow.")
    else:
        try:
            with Image.open(path) as img:
                dimensions = img.size
            expected = expected_dimensions(expected_size)
            if expected:
                tolerance = 0.08
                width_ok = abs(dimensions[0] - expected[0]) <= expected[0] * tolerance
                height_ok = abs(dimensions[1] - expected[1]) <= expected[1] * tolerance
                if not (width_ok and height_ok):
                    status = "REVISAR" if status == "OK" else status
                    details.append(f"Dimensiones {dimensions[0]}x{dimensions[1]} difieren de {expected[0]}x{expected[1]}.")
        except Exception as exc:
            status = "REVISAR"
            details.append(f"No se pudo leer dimensiones: {exc}")

    return ImageCheck(
        section=section,
        key=str(key),
        path=path,
        expected_size=expected_size,
        expected_weight=expected_weight,
        status=status,
        detail=" ".join(details) or "Correcto.",
        weight_kb=weight_kb,
        dimensions=dimensions,
    )


def collect_manifest_checks() -> list[ImageCheck]:
    manifest = load_json("data/imagenes_pendientes.json")
    checks: list[ImageCheck] = []
    for section in ("banners_linea", "flyers_linea", "productos", "og_images", "carruseles"):
        for record in manifest.get(section, []):
            checks.append(check_record(section, record))
    return checks


def collect_cross_reference_warnings() -> list[str]:
    warnings: list[str] = []
    banners = load_json("data/banners_lineas.json")
    catalog = load_json("data/catalogo_global.json")

    for slug, config in banners.items():
        expected = config.get("banner_esperado") or config.get("banner")
        if expected and not (ROOT / expected).exists():
            warnings.append(f"Banner final pendiente para `{slug}`: `{expected}`.")

    for item in catalog:
        image = item.get("imagen", "")
        if image and not image.startswith("http") and not (ROOT / image).exists():
            warnings.append(f"Imagen referenciada no existe para `{item.get('id')}`: `{image}`.")

    return warnings


def render_report(checks: list[ImageCheck], warnings: list[str]) -> str:
    counts: dict[str, int] = {}
    for check in checks:
        counts[check.status] = counts.get(check.status, 0) + 1

    lines = [
        "# Reporte de imágenes Tecprog World",
        "",
        "Este reporte valida imágenes esperadas sin fallar cuando todavía están pendientes.",
        "",
        f"Pillow disponible: {'sí' if Image is not None else 'no'}",
        "",
        "## Resumen",
        "",
    ]
    for status in sorted(counts):
        lines.append(f"- {status}: {counts[status]}")

    lines.extend(["", "## Detalle", "", "| Sección | ID/Línea | Archivo | Estado | Peso | Dimensiones | Observación |", "|---|---|---|---|---:|---|---|"])
    for check in checks:
        rel = check.path.relative_to(ROOT).as_posix() if check.path.is_absolute() else str(check.path)
        weight = f"{check.weight_kb:.1f} KB" if check.weight_kb is not None else "-"
        dims = f"{check.dimensions[0]}x{check.dimensions[1]}" if check.dimensions else "-"
        lines.append(f"| {check.section} | {check.key} | `{rel}` | {check.status} | {weight} | {dims} | {check.detail} |")

    lines.extend(["", "## Cruces con datos", ""])
    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("- Sin advertencias de referencias.")

    return "\n".join(lines) + "\n"


def main() -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    checks = collect_manifest_checks()
    warnings = collect_cross_reference_warnings()
    REPORT.write_text(render_report(checks, warnings), encoding="utf-8")
    print(f"Reporte generado: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
