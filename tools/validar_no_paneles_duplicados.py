from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path


SKIP_DIRS = {"backups", "build", "_auditoria_codex", ".git", ".idea", "__pycache__"}
STRUCTURAL_CLASSES = {
    "side-nav",
    "side-nav-left",
    "side-panel-right",
    "commerce-nav-panel",
    "commerce-aside",
    "commerce-results",
    "page-shell-three-columns",
}
LEGACY_RE = re.compile(r"(legacy-panel|old-panel|panel-antiguo|layout-legacy|sidebar-legacy)", re.I)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids: Counter[str] = Counter()
        self.classes: Counter[str] = Counter()
        self.scripts: Counter[str] = Counter()
        self.styles: Counter[str] = Counter()
        self.body_attrs: dict[str, str] = {}
        self.main_attrs: list[dict[str, str]] = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "body":
            self.body_attrs.update(attrs_dict)
        if tag == "main":
            self.main_attrs.append(attrs_dict)
        if "id" in attrs_dict:
            self.ids[attrs_dict["id"]] += 1
        for cls in attrs_dict.get("class", "").split():
            if cls in STRUCTURAL_CLASSES:
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
            if count > 1:
                errors.append(f"{rel}: clase estructural duplicada .{cls} ({count})")
        for src, count in parser.scripts.items():
            if count > 1:
                errors.append(f"{rel}: JS duplicado {src} ({count})")
        for href, count in parser.styles.items():
            if count > 1:
                errors.append(f"{rel}: CSS duplicado {href} ({count})")
        if LEGACY_RE.search(text):
            errors.append(f"{rel}: referencia legacy de panel/layout")

        is_commerce = "data-commerce-catalog" in text and 'data-catalog-mode="home"' not in text
        local_strategy = "data-commerce-panel-strategy=\"local\"" in text
        disabled = "data-disable-global-sidebars=\"true\"" in text
        if is_commerce and not (local_strategy and disabled):
            errors.append(f"{rel}: catalogo comercial sin estrategia local y bloqueo de sidebars globales")

    js_text = Path("assets/js/catalogo-global.js").read_text(encoding="utf-8")
    if js_text.count("function leftPanel") != 1 or js_text.count("function rightPanel") != 1:
        errors.append("assets/js/catalogo-global.js: debe existir un solo generador local leftPanel/rightPanel")
    right_panel_text = Path("assets/js/right-panel.js").read_text(encoding="utf-8")
    if "globalSidebarsDisabled()" not in right_panel_text:
        errors.append("assets/js/right-panel.js: falta bloqueo de sidebars globales")

    if errors:
        print("REGRESIONES DE PANELES:")
        print("\n".join(errors))
        return 1
    print("OK: no hay paneles estructurales duplicados ni referencias legacy en HTML publico.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
