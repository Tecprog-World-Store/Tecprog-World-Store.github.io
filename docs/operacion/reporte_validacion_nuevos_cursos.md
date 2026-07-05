# Reporte de validación de nuevos cursos

Fecha: 2026-07-05

## Resultado

- JSON válido: `data/cursos_tw_educa.json`, `data/catalogo_global.json` y `data/sitemap_comercial.json`.
- JavaScript válido: `node --check assets/js/detalle.js` y `node --check assets/js/catalogo-global.js`.
- Python válido: `python -m py_compile` para herramientas Python revisadas.
- Open Graph validado: `python tools/validar_open_graph_tw.py` reportó OK para los 37 cursos.
- Imágenes: las 37 rutas WebP referenciadas existen y cargan localmente.
- URLs estáticas: las 37 páginas `cursos/<slug>/index.html` existen.
- Duplicados: el catálogo público TW Educa muestra 37 cursos visibles; los 8 prototipos legacy quedaron con `visible_cliente: false`.
- Búsqueda: en navegador local, `Excel` devolvió 5 cards, `Python` 9 cards y `AutoCAD` 4 cards.
- Responsive: probado en 390x844, 768x1024, 1366x768 y 1920x1080 sin overflow horizontal, sin imágenes rotas y sin errores de consola.
- Detalle enriquecido: probado `curso-practico-de-excel-nivel-i` con temario, inversión, resultados de aprendizaje, imagen y Open Graph HTTPS absoluto.

## Pendientes

- Confirmar calendario comercial definitivo antes de publicar fechas concretas.
- Revisar condiciones comerciales finales si los precios referenciales cambian antes de campaña.
