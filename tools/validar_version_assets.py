from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


EXPECTED_VERSION = "20260729-07"
SKIP_DIRS = {"backups", "build", "_auditoria_codex", ".git", ".idea", "__pycache__"}
ASSET_RE = re.compile(r'<(?:link|script)\b[^>]*(?:href|src)=["\'](?P<url>[^"\']*assets/(?:css|js)/[^"\']+\.(?:css|js)(?:\?[^"\']*)?)["\']', re.I)


def iter_html(root: Path):
    for path in root.rglob("*.html"):
        if not any(part in SKIP_DIRS for part in path.parts):
            yield path


def asset_key(url: str) -> str:
    return url.split("?", 1)[0].replace("\\", "/")


def version(url: str) -> str | None:
    if "?" not in url:
        return None
    query = url.split("?", 1)[1]
    for part in query.split("&"):
        key, _, value = part.partition("=")
        if key == "v":
            return value
    return None


def main() -> int:
    root = Path(".").resolve()
    errors: list[str] = []
    all_versions = defaultdict(set)

    for path in iter_html(root):
        text = path.read_text(encoding="utf-8")
        per_page = defaultdict(int)
        for match in ASSET_RE.finditer(text):
            url = match.group("url")
            key = asset_key(url)
            if re.match(r"^(?:https?:)?//", url, re.I):
                continue
            per_page[key] += 1
            found_version = version(url)
            all_versions[key].add(found_version or "SIN_VERSION")
            if found_version != EXPECTED_VERSION:
                errors.append(f"{path.relative_to(root)}: {url} usa version {found_version or 'SIN_VERSION'}")
        for key, count in per_page.items():
            if count > 1:
                errors.append(f"{path.relative_to(root)}: carga duplicada de {key} ({count} veces)")

    mixed = {key: values for key, values in all_versions.items() if len(values) > 1}
    for key, values in mixed.items():
        errors.append(f"{key}: versiones mezcladas {', '.join(sorted(values))}")

    if errors:
        print("REGRESIONES DE VERSIONADO:")
        print("\n".join(errors))
        return 1
    print(f"OK: assets CSS/JS locales usan v={EXPECTED_VERSION} sin duplicados por pagina.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
