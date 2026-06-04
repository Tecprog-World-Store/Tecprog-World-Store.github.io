from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("Pillow no está instalado. Ejecuta: pip install pillow")

ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "assets" / "img"
SKIP_PARTS = {"qr", "logos"}
SOURCE_EXTS = {".png", ".jpg", ".jpeg"}
BANNER_SOURCE = IMG_DIR / "banner_horizontal_tw" / "figuraHorizontal01.png"


def should_skip(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    return bool(parts & SKIP_PARTS) or path.suffix.lower() not in SOURCE_EXTS


def convert(path: Path) -> Path | None:
    if should_skip(path):
        return None
    target = path.with_suffix(".webp")
    if target.exists() and target.stat().st_mtime >= path.stat().st_mtime:
        return None
    with Image.open(path) as image:
        image.save(target, "WEBP", quality=82, method=6)
    return target


def main() -> None:
    created = []
    if BANNER_SOURCE.exists():
        target = BANNER_SOURCE.with_suffix(".webp")
        with Image.open(BANNER_SOURCE) as image:
            image.save(target, "WEBP", quality=85, method=6)
        created.append(target.relative_to(ROOT))
    for path in IMG_DIR.rglob("*"):
        if path == BANNER_SOURCE:
            continue
        if path.is_file():
            result = convert(path)
            if result:
                created.append(result.relative_to(ROOT))
    print(f"WebP creados o actualizados: {len(created)}")
    for item in created:
        print(item.as_posix())


if __name__ == "__main__":
    main()
