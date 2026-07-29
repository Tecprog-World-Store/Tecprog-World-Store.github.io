from __future__ import annotations

import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


SKIP_DIRS = {"backups", "build", "_auditoria_codex", ".git", ".idea", "__pycache__"}
CENTRAL_CLASSES = {
    "central-page",
    "central-page-shell",
    "central-catalog-layout",
    "commerce-results",
    "local-nav",
    "commerce-local-nav",
    "commerce-related",
    "detail-summary",
}
LEGACY_RE = re.compile(
    r"(legacy-panel|old-panel|panel-antiguo|layout-legacy|sidebar-legacy|"
    r"side-panel-right|side-nav-left|page-shell-three-columns|commerce-aside)",
    re.I,
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: Counter[str] = Counter()
        self.classes: Counter[str] = Counter()
        self.scripts: Counter[str] = Counter()
        self.styles: Counter[str] = Counter()

    def handle_starttag(self, tag, attrs) -> None:
        attrs_dict = dict(attrs)
        if "id" in attrs_dict:
            self.ids[attrs_dict["id"]] += 1
        for cls in attrs_dict.get("class", "").split():
            if cls in CENTRAL_CLASSES:
                self.classes[cls] += 1
        if tag == "script" and attrs_dict.get("src"):
            self.scripts[attrs_dict["src"].split("?", 1)[0].replace("\\", "/")] += 1
        if tag == "link" and attrs_dict.get("rel") == "stylesheet" and attrs_dict.get("href"):
            self.styles[attrs_dict["href"].split("?", 1)[0].replace("\\", "/")] += 1


def iter_html(root: Path):
    for path in root.rglob("*.html"):
        if not any(part in SKIP_DIRS for part in path.parts):
            yield path


def main() -> int:
    root = Path(".").resolve()
    errors: list[str] = []

    for path in iter_html(root):
        text = path.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(text)
        rel = path.relative_to(root)

        for item_id, count in parser.ids.items():
            if count > 1:
                errors.append(f"{rel}: id duplicado #{item_id} ({count})")
        for cls, count in parser.classes.items():
            if cls in {"central-page", "central-page-shell", "central-catalog-layout"} and count > 1:
                errors.append(f"{rel}: contenedor estructural duplicado .{cls} ({count})")
        for src, count in parser.scripts.items():
            if count > 1:
                errors.append(f"{rel}: JS duplicado {src} ({count})")
        for href, count in parser.styles.items():
            if count > 1:
                errors.append(f"{rel}: CSS duplicado {href} ({count})")
        if LEGACY_RE.search(text):
            errors.append(f"{rel}: referencia de panel lateral obsoleto")

    catalog_js = (root / "assets/js/catalogo-global.js").read_text(encoding="utf-8")
    for generator in ("function localNavigation", "function relatedResources", "function resultsPanel"):
        if catalog_js.count(generator) != 1:
            errors.append(f"assets/js/catalogo-global.js: generador inconsistente {generator}")
    if "<aside" in catalog_js:
        errors.append("assets/js/catalogo-global.js: no debe generar aside comercial")

    if errors:
        print("REGRESIONES DE PANELES:")
        print("\n".join(errors))
        return 1
    print("OK: no hay paneles laterales, contenedores centrales duplicados ni referencias legacy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
