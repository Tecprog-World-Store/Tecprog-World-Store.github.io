# Cambios Protegidos

Fecha: 2026-07-08.

Cambios aprobados:

- Arquitectura de una sola columna estructural central.
- Navegacion superior global y navegacion local horizontal.
- Catalogos comerciales con filtros y busqueda dentro del panel central.
- Eliminacion de paneles laterales duplicados.
- Versionado uniforme de CSS y JS con `v=20260729-04`.
- Idempotencia en `assets/js/catalogo-global.js` para evitar re-render del mismo root.
- Eliminacion del generador `assets/js/right-panel.js`.

Archivos criticos:

- `assets/css/styles.css`
- `assets/js/catalogo-global.js`
- `assets/js/navigation.js`
- `index.html`
- `store/index.html`
- `educa/index.html`
- `disfruta/index.html`
- `innova/index.html`
- `salud/index.html`
- `interactive/index.html`
- `construye/index.html`
- `inox/index.html`
- `investiga/index.html`
- `pagos/peru.html`
- `pagos/internacionales.html`

Validaciones obligatorias:

- `python tools/validar_layout_columna_central.py`
- `python tools/validar_no_paneles_duplicados.py`
- `python tools/validar_version_assets.py`

Restriccion: no modificar esta arquitectura sin instruccion explicita del usuario.
