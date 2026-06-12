from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUTS = [
    ROOT / "assets" / "img" / "banners",
    ROOT / "assets" / "img" / "store",
    ROOT / "assets" / "img" / "lineas",
]
OUT_DIR = ROOT / "build" / "imagenes_optimizadas"
REPORT = ROOT / "docs" / "operacion" / "reporte_optimizacion_imagenes.md"

try:
    from PIL import Image  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    Image = None


def iter_images(paths: list[Path]) -> list[Path]:
    allowed = {".png", ".jpg", ".jpeg", ".webp"}
    files: list[Path] = []
    for base in paths:
        if base.is_file() and base.suffix.lower() in allowed:
            files.append(base)
        elif base.is_dir():
            files.extend(path for path in base.rglob("*") if path.suffix.lower() in allowed)
    return sorted(set(files))


def output_path(source: Path) -> Path:
    rel = source.relative_to(ROOT)
    return (OUT_DIR / rel).with_suffix(".webp")


def write_report(lines: list[str]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Optimiza imágenes locales a WebP sin sobrescribir originales.")
    parser.add_argument("--quality", type=int, default=82, help="Calidad WebP entre 75 y 85. Valor por defecto: 82.")
    parser.add_argument("--input", nargs="*", help="Archivos o carpetas a procesar. Si se omite, usa rutas de imágenes del proyecto.")
    args = parser.parse_args()

    quality = max(75, min(85, args.quality))
    inputs = [ROOT / item for item in args.input] if args.input else DEFAULT_INPUTS
    report = [
        "# Reporte de optimización de imágenes",
        "",
        f"Calidad solicitada: {quality}",
        "",
    ]

    if Image is None:
        report.extend([
            "Pillow no está instalado.",
            "",
            "Instala la dependencia con:",
            "",
            "```bash",
            "pip install pillow",
            "```",
        ])
        write_report(report)
        print(f"Pillow no instalado. Reporte generado: {REPORT.relative_to(ROOT)}")
        return

    files = iter_images(inputs)
    report.extend(["| Archivo origen | Salida | Estado | Peso origen | Peso salida |", "|---|---|---|---:|---:|"])

    for source in files:
        target = output_path(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            before = source.stat().st_size / 1024
            with Image.open(source) as img:
                if img.mode not in ("RGB", "RGBA"):
                    img = img.convert("RGBA" if "A" in img.getbands() else "RGB")
                img.save(target, "WEBP", quality=quality, method=6)
            after = target.stat().st_size / 1024
            status = "OK"
        except Exception as exc:
            after = 0
            status = f"ERROR: {exc}"
        report.append(
            f"| `{source.relative_to(ROOT).as_posix()}` | `{target.relative_to(ROOT).as_posix()}` | {status} | {before:.1f} KB | {after:.1f} KB |"
        )

    write_report(report)
    print(f"Reporte generado: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
