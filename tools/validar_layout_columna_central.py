from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path


SKIP_DIRS = {"backups", "build", "_auditoria_codex", ".git", ".idea", "__pycache__"}
BANNED_MARKERS = (
    "with-side-nav",
    "side-nav",
    "side-nav-left",
    "side-panel-right",
    "page-shell-three-columns",
    "commerce-shell",
    "commerce-nav-panel",
    "commerce-aside",
    "detail-sidebar",
    "data-commerce-panel-strategy",
    "data-disable-global-sidebars",
    "commercial-local-panels",
    "comercial-3-paneles",
    "right-panel.js",
)
REQUIRED_NAV_PATHS = (
    "index.html",
    "store/index.html",
    "disfruta/index.html",
    "educa/index.html",
    "innova/index.html",
    "salud/index.html",
    "interactive/index.html",
    "construye/index.html",
    "inox/index.html",
    "investiga/index.html",
    "empresa/nosotros.html",
    "pagos/peru.html",
    "pagos/internacionales.html",
)


class LayoutParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.main_count = 0
        self.structural_asides: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        attrs_dict = dict(attrs)
        if tag == "main":
            self.main_count += 1
        if tag == "aside":
            classes = attrs_dict.get("class", "")
            if re.search(r"(?:side|sidebar|navigation|commerce-aside)", classes, re.I):
                self.structural_asides.append(classes)


def iter_html(root: Path):
    for path in root.rglob("*.html"):
        if not any(part in SKIP_DIRS for part in path.parts):
            yield path


def main() -> int:
    root = Path(".").resolve()
    errors: list[str] = []

    for path in iter_html(root):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        parser = LayoutParser()
        parser.feed(text)
        if parser.main_count != 1:
            errors.append(f"{rel}: debe existir exactamente un main ({parser.main_count})")
        if parser.structural_asides:
            errors.append(f"{rel}: aside estructural lateral: {', '.join(parser.structural_asides)}")
        for marker in BANNED_MARKERS:
            if marker in text:
                errors.append(f"{rel}: marcador lateral obsoleto {marker}")

    css = (root / "assets/css/styles.css").read_text(encoding="utf-8")
    if "--tw-shell-width: min(calc(100% - 32px), var(--layout-max-width))" not in css:
        errors.append("assets/css/styles.css: falta ancho central adaptable canonico")
    if "--layout-max-width: 1440px" not in css:
        errors.append("assets/css/styles.css: el contenedor central no usa maximo 1440px")
    for marker in BANNED_MARKERS[:8]:
        if re.search(rf"\.{re.escape(marker)}\b", css):
            errors.append(f"assets/css/styles.css: selector lateral obsoleto .{marker}")
    if re.search(r"\.local-nav\s*\{[^}]*overflow-y", css, re.S):
        errors.append("assets/css/styles.css: navegacion local con scrollbar vertical")
    if not re.search(r"\.central-catalog-layout\s*\{[^}]*grid-template-columns:\s*minmax\(0,\s*1fr\)", css, re.S):
        errors.append("assets/css/styles.css: catalogo no usa una columna estructural")
    if not re.search(r"\.detail-layout\s*\{[^}]*grid-template-columns:\s*minmax\(0,\s*1fr\)", css, re.S):
        errors.append("assets/css/styles.css: detalle no usa una columna estructural")

    navigation_js = (root / "assets/js/navigation.js").read_text(encoding="utf-8")
    for path in REQUIRED_NAV_PATHS:
        if path not in navigation_js:
            errors.append(f"assets/js/navigation.js: falta acceso superior a {path}")
    if 'aria-expanded' not in navigation_js or "setupTopNavigation" not in navigation_js:
        errors.append("assets/js/navigation.js: menu adaptable sin control ARIA")

    catalog_js = (root / "assets/js/catalogo-global.js").read_text(encoding="utf-8")
    if "root.dataset.twCatalogoGlobalReady" not in catalog_js:
        errors.append("assets/js/catalogo-global.js: inicializacion no idempotente")
    for marker in ("leftPanel", "rightPanel", "commerce-aside", "commerce-nav-panel"):
        if marker in catalog_js:
            errors.append(f"assets/js/catalogo-global.js: generador lateral obsoleto {marker}")
    if not (root / "assets/js/right-panel.js").exists():
        pass
    else:
        errors.append("assets/js/right-panel.js: el generador lateral debe permanecer eliminado")

    if errors:
        print("REGRESIONES DE COLUMNA CENTRAL:")
        print("\n".join(errors))
        return 1
    print("OK: paginas publicas usan una sola columna estructural central sin paneles laterales.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
