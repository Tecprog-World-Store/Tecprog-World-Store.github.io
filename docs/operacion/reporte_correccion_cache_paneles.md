# Reporte De Correccion Cache Paneles

Fecha: 2026-07-08.

## Solucion aplicada

- Se normalizaron todas las referencias locales de CSS y JS en HTML publicos a `?v=20260708-01`.
- Se creo `tools/actualizar_version_assets.py` para repetir el cambio de version de forma controlada.
- Se reforzo `assets/js/catalogo-global.js` para evitar re-render del mismo root con `data-tw-catalogo-global-ready`.
- Se reforzo `assets/js/right-panel.js` para limpiar duplicados estructurales y retirar restos de panel global cuando la pagina declara paneles locales.
- Se crearon validadores de no regresion en `tools/`.

## Estrategia de cache final

- GitHub Pages sigue sirviendo archivos estaticos.
- No se agrego service worker.
- La invalidacion se hace por query string uniforme en CSS/JS: `v=20260708-01`.
- Futuras publicaciones deben actualizar la version con `tools/actualizar_version_assets.py`.

## Pruebas ejecutadas

- `python tools/validar_version_assets.py`: OK.
- `python tools/validar_no_paneles_duplicados.py`: OK.
- `python tools/validar_layout_tres_paneles.py`: OK.
- `python -m py_compile tools/actualizar_version_assets.py tools/validar_version_assets.py tools/validar_no_paneles_duplicados.py tools/validar_layout_tres_paneles.py`: OK.
- Prueba local en navegador integrado con servidor `http://127.0.0.1:8008`: OK en `/`, `/store/`, `/educa/`, `/pagos/peru.html` para 390x844 y 1366x768. Sin errores de consola, sin overflow horizontal, sin IDs duplicados y sin assets fuera de `v=20260708-01`.

## Resultado

Los HTML publicos ya apuntan a una unica version de assets. La primera carga debe solicitar CSS/JS con `v=20260708-01`, evitando que se reutilicen scripts de paneles antiguos por URL identica.

## Pendientes

No se ejecuto prueba manual real en Chrome/Edge incognito desde esta sesion. La validacion automatica cubrio estructura estatica, versionado y primera carga local en navegador integrado.
