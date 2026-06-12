from __future__ import annotations

import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
except Exception as exc:  # pragma: no cover - dependency guidance
    raise SystemExit("Pillow no esta instalado. Ejecuta: pip install pillow") from exc


ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_DIR = ROOT / "assets" / "img" / "store" / "flyers"
LEGACY_DIR = ROOT / "assets" / "img" / "flyers"
REPORT = ROOT / "docs" / "operacion" / "reporte_conversion_flyers_webp.md"

TARGET_SIZE = (1080, 1920)
TARGET_RATIO = TARGET_SIZE[0] / TARGET_SIZE[1]
MAX_KB = 600
QUALITIES = (85, 82, 80, 78, 75)

FLYERS = (
    "tw-store-portada",
    "tw-disfruta-portada",
    "tw-educa-portada",
    "tw-innova-portada",
    "tw-salud-portada",
    "tw-interactive-portada",
    "tw-construye-portada",
    "tw-inox-portada",
    "tw-investiga-portada",
)


@dataclass
class ConversionResult:
    name: str
    source: Path
    official_png: Path
    output: Path
    source_origin: str
    original_size: tuple[int, int] | None
    final_size: tuple[int, int] | None
    quality: int | None
    weight_kb: float | None
    status: str
    detail: str


def cover_crop_box(width: int, height: int) -> tuple[int, int, int, int]:
    current_ratio = width / height
    if current_ratio > TARGET_RATIO:
        crop_width = round(height * TARGET_RATIO)
        left = (width - crop_width) // 2
        return left, 0, left + crop_width, height

    crop_height = round(width / TARGET_RATIO)
    top = (height - crop_height) // 2
    return 0, top, width, top + crop_height


def source_for(name: str) -> tuple[Path, str] | None:
    official = OFFICIAL_DIR / f"{name}.png"
    legacy = LEGACY_DIR / f"{name}.png"
    if official.exists():
        return official, "oficial"
    if legacy.exists():
        return legacy, "legacy"
    return None


def save_webp(image: Image.Image, output: Path) -> tuple[int, float, str]:
    chosen_quality = QUALITIES[-1]
    chosen_weight = 0.0
    detail = "Peso dentro del rango recomendado."

    for quality in QUALITIES:
        image.save(output, "WEBP", quality=quality, method=6)
        weight_kb = output.stat().st_size / 1024
        chosen_quality = quality
        chosen_weight = weight_kb
        if weight_kb <= MAX_KB:
            break

    if chosen_weight > MAX_KB:
        detail = f"Peso sobre {MAX_KB} KB aun con quality={chosen_quality}."

    return chosen_quality, chosen_weight, detail


def convert_flyer(name: str) -> ConversionResult:
    OFFICIAL_DIR.mkdir(parents=True, exist_ok=True)
    official_png = OFFICIAL_DIR / f"{name}.png"
    output = OFFICIAL_DIR / f"{name}.webp"
    located = source_for(name)

    if located is None:
        return ConversionResult(
            name=name,
            source=official_png,
            official_png=official_png,
            output=output,
            source_origin="no encontrado",
            original_size=None,
            final_size=None,
            quality=None,
            weight_kb=None,
            status="PENDIENTE",
            detail="No existe PNG fuente en ruta oficial ni legacy.",
        )

    source, source_origin = located
    if source != official_png:
        shutil.copy2(source, official_png)
        source = official_png
        source_origin = "legacy copiado a oficial"

    with Image.open(source) as original:
        original_size = original.size
        image = original.convert("RGB")
        cropped = image.crop(cover_crop_box(*image.size))
        resized = cropped.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        quality, weight_kb, detail = save_webp(resized, output)

    with Image.open(output) as final:
        final_size = final.size

    status = "OK"
    if final_size != TARGET_SIZE:
        status = "REVISAR"
        detail = f"Dimensiones finales {final_size[0]}x{final_size[1]} difieren de 1080x1920."
    elif weight_kb > MAX_KB:
        status = "OPTIMIZAR"

    return ConversionResult(
        name=name,
        source=source,
        official_png=official_png,
        output=output,
        source_origin=source_origin,
        original_size=original_size,
        final_size=final_size,
        quality=quality,
        weight_kb=weight_kb,
        status=status,
        detail=detail,
    )


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def render_report(results: list[ConversionResult]) -> str:
    lines = [
        "# Reporte de conversion de flyers a WEBP",
        "",
        f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "Ruta oficial: `assets/img/store/flyers/`.",
        "Ruta legacy consultada solo como fuente: `assets/img/flyers/`.",
        "",
        "Proceso aplicado: copia segura de PNG legacy si falta en ruta oficial, recorte cover a relacion 9:16, redimensionado exacto a 1080x1920 px y exportacion WEBP sin borrar PNG originales.",
        "",
        "| Flyer | Origen | PNG oficial | WEBP final | Estado | Calidad | Peso | Dimensiones originales | Dimensiones finales | Observacion |",
        "|---|---|---|---|---|---:|---:|---|---|---|",
    ]

    for result in results:
        original = f"{result.original_size[0]}x{result.original_size[1]}" if result.original_size else "-"
        final = f"{result.final_size[0]}x{result.final_size[1]}" if result.final_size else "-"
        quality = str(result.quality) if result.quality is not None else "-"
        weight = f"{result.weight_kb:.1f} KB" if result.weight_kb is not None else "-"
        lines.append(
            f"| {result.name} | {result.source_origin} | `{relative(result.official_png)}` | `{relative(result.output)}` | {result.status} | {quality} | {weight} | {original} | {final} | {result.detail} |"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    results = [convert_flyer(name) for name in FLYERS]
    REPORT.write_text(render_report(results), encoding="utf-8")

    for result in results:
        weight = f"{result.weight_kb:.1f} KB" if result.weight_kb is not None else "-"
        final = f"{result.final_size[0]}x{result.final_size[1]}" if result.final_size else "-"
        print(f"{result.name}: {result.status} | {weight} | {final} | {result.source_origin}")
    print(f"Reporte generado: {relative(REPORT)}")


if __name__ == "__main__":
    main()
