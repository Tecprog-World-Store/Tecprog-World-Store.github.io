from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_VERSION = "20260729-06"
SKIP_DIRS = {"backups", "build", "_auditoria_codex", ".git", ".idea", "__pycache__"}
ASSET_RE = re.compile(
    r'(?P<prefix><(?:link|script)\b[^>]*(?:href|src)=["\'])(?P<url>[^"\']*assets/(?:css|js)/[^"\']+\.(?:css|js)(?:\?[^"\']*)?)(?P<suffix>["\'])',
    re.IGNORECASE,
)


def iter_html(root: Path):
    for path in root.rglob("*.html"):
      if not any(part in SKIP_DIRS for part in path.parts):
        yield path


def is_local_asset(url: str) -> bool:
    return not re.match(r"^(?:https?:)?//", url, re.IGNORECASE) and "assets/" in url.replace("\\", "/")


def normalize_url(url: str, version: str) -> str:
    if not is_local_asset(url):
        return url
    base = url.split("?", 1)[0]
    if not re.search(r"assets/(?:css|js)/", base.replace("\\", "/")):
        return url
    return f"{base}?v={version}"


def update_file(path: Path, version: str, write: bool) -> tuple[bool, list[str]]:
    original = path.read_text(encoding="utf-8")
    changes: list[str] = []

    def repl(match: re.Match[str]) -> str:
        old = match.group("url")
        new = normalize_url(old, version)
        if old != new:
            changes.append(f"{old} -> {new}")
        return f"{match.group('prefix')}{new}{match.group('suffix')}"

    updated = ASSET_RE.sub(repl, original)
    changed = updated != original
    if changed and write:
        path.write_text(updated, encoding="utf-8", newline="")
    return changed, changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Actualiza versiones locales de CSS y JS en HTML publicos.")
    parser.add_argument("--version", default=DEFAULT_VERSION)
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    touched = []
    for path in iter_html(root):
        changed, changes = update_file(path, args.version, not args.dry_run)
        if changed:
            touched.append((path.relative_to(root), changes))

    mode = "simulado" if args.dry_run else "aplicado"
    print(f"Version objetivo: {args.version}")
    print(f"Modo: {mode}")
    print(f"HTML modificados: {len(touched)}")
    for path, changes in touched:
        print(f"- {path}")
        for change in changes:
            print(f"  {change}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
