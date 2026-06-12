from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
except Exception as exc:  # pragma: no cover - dependency guidance
    raise SystemExit("Pillow no esta instalado. Ejecuta: pip install pillow") from exc


ROOT = Path(__file__).resolve().parents[1]
BANNERS_DIR = ROOT / "assets" / "img" / "banners"
REPORT = ROOT / "docs" / "operacion" / "reporte_conversion_banners_webp.md"

TARGET_SIZE = (1920, 640)
TARGET_RATIO = TARGET_SIZE[0] / TARGET_SIZE[1]
MIN_KB = 150
MAX_KB = 450
QUALITIES = (85, 82, 80, 78, 75)

BANNERS = (
    "tw-store",
    "tw-disfruta",
    "tw-educa",
    "tw-innova",
    "tw-salud",
    "tw-interactive",
    "tw-construye",
    "tw-inox",
    "tw-investiga",
)


@dataclass
class ConversionResult:
    name: str
    source: Path
    output: Path
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


def save_webp_with_target_weight(image: Image.Image, output: Path) -> tuple[int, float, str]:
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
    elif chosen_weight < MIN_KB:
        detail = f"Peso bajo {MIN_KB} KB con quality={chosen_quality}; se priorizo calidad visual."

    return chosen_quality, chosen_weight, detail


def convert_banner(name: str) -> ConversionResult:
    source = BANNERS_DIR / f"{name}.png"
    output = BANNERS_DIR / f"{name}.webp"

    if not source.exists():
        return ConversionResult(
            name=name,
            source=source,
            output=output,
            original_size=None,
            final_size=None,
            quality=None,
            weight_kb=None,
            status="PENDIENTE",
            detail="No existe el PNG fuente.",
        )

    with Image.open(source) as original:
        original_size = original.size
        image = original.convert("RGB")
        cropped = image.crop(cover_crop_box(*image.size))
        resized = cropped.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        quality, weight_kb, detail = save_webp_with_target_weight(resized, output)

    with Image.open(output) as final:
        final_size = final.size

    status = "OK"
    if final_size != TARGET_SIZE:
        status = "REVISAR"
        detail = f"Dimensiones finales {final_size[0]}x{final_size[1]} difieren de 1920x640."
    elif weight_kb > MAX_KB:
        status = "OPTIMIZAR"
    elif weight_kb < MIN_KB:
        status = "OK_BAJO_PESO"

    return ConversionResult(
        name=name,
        source=source,
        output=output,
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
        "# Reporte de conversion de banners a WEBP",
        "",
        f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "Proceso aplicado: recorte seguro tipo cover a relacion 3:1, redimensionado exacto a 1920x640 px y exportacion WEBP sin sobrescribir PNG originales.",
        "",
        "| Banner | PNG fuente | WEBP final | Estado | Calidad | Peso | Dimensiones originales | Dimensiones finales | Observacion |",
        "|---|---|---|---|---:|---:|---|---|---|",
    ]

    for result in results:
        original = f"{result.original_size[0]}x{result.original_size[1]}" if result.original_size else "-"
        final = f"{result.final_size[0]}x{result.final_size[1]}" if result.final_size else "-"
        quality = str(result.quality) if result.quality is not None else "-"
        weight = f"{result.weight_kb:.1f} KB" if result.weight_kb is not None else "-"
        lines.append(
            f"| {result.name} | `{relative(result.source)}` | `{relative(result.output)}` | {result.status} | {quality} | {weight} | {original} | {final} | {result.detail} |"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    results = [convert_banner(name) for name in BANNERS]
    REPORT.write_text(render_report(results), encoding="utf-8")

    for result in results:
        weight = f"{result.weight_kb:.1f} KB" if result.weight_kb is not None else "-"
        final = f"{result.final_size[0]}x{result.final_size[1]}" if result.final_size else "-"
        print(f"{result.name}: {result.status} | {weight} | {final}")
    print(f"Reporte generado: {relative(REPORT)}")


if __name__ == "__main__":
    main()
