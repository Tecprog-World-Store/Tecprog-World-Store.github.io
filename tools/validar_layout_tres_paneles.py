from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_PAGES = [
    "index.html",
    "store/index.html",
    "educa/index.html",
    "disfruta/index.html",
    "innova/index.html",
    "salud/index.html",
    "interactive/index.html",
    "construye/index.html",
    "inox/index.html",
    "investiga/index.html",
    "pagos/peru.html",
    "pagos/internacionales.html",
]


def main() -> int:
    root = Path(".").resolve()
    errors: list[str] = []

    for rel in REQUIRED_PAGES:
        path = root / rel
        if not path.exists():
            errors.append(f"{rel}: no existe")
            continue
        text = path.read_text(encoding="utf-8")
        is_commerce = "data-commerce-catalog" in text and 'data-catalog-mode="home"' not in text
        is_global = "with-side-nav" in text
        has_central = "data-commerce-catalog" in text or "data-app-shell" in text or "page-main" in text or "<main" in text
        if not has_central:
            errors.append(f"{rel}: no se detecta panel/contenido central")
        if is_commerce:
            if text.count("data-commerce-catalog") != 1:
                errors.append(f"{rel}: debe tener un solo catalogo comercial central")
            if "data-commerce-panel-strategy=\"local\"" not in text:
                errors.append(f"{rel}: falta estrategia local de paneles")
            if "right-panel.js" in text:
                errors.append(f"{rel}: pagina comercial no debe cargar right-panel.js global")
        if is_global and text.count("class=\"side-nav") > 1:
            errors.append(f"{rel}: mas de un panel izquierdo inicial")
        if text.count("side-panel-right") > 1:
            errors.append(f"{rel}: mas de un panel derecho inicial")

    catalog_js = (root / "assets/js/catalogo-global.js").read_text(encoding="utf-8")
    if "root.dataset.twCatalogoGlobalReady" not in catalog_js:
        errors.append("assets/js/catalogo-global.js: init/render no es idempotente")
    right_panel_js = (root / "assets/js/right-panel.js").read_text(encoding="utf-8")
    if "globalSidebarsDisabled()" not in right_panel_js or "side-panel-right" not in right_panel_js:
        errors.append("assets/js/right-panel.js: panel derecho global sin control de duplicados")

    if errors:
        print("REGRESIONES DE LAYOUT:")
        print("\n".join(errors))
        return 1
    print("OK: paginas clave respetan maximo tres paneles y separan paneles locales/globales.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
