# Reporte Fase 8B - Integración de cursos TW Educa

## Cursos detectados

Se detectaron 14 cursos en `Cursos a dictar/cursos_txt_tecprog_world/`, con 14 flyers PNG asociados en `Cursos a dictar/`.

## Cursos integrados

Los 14 cursos se integraron como items nuevos `tw-educa-curso-01` a `tw-educa-curso-14` en `data/catalogo_global.json` y como fichas enriquecidas en `data/cursos_tw_educa.json`.

## Cursos con fecha original

Todos los cursos tienen fecha original en su archivo fuente.

## Cursos con fecha tentativa asignada

No se asignaron fechas tentativas porque todos los cursos traen fecha de inicio.

## Criterio de cronograma

Se respetó el cronograma académico de 4 sesiones en vivo indicado en cada TXT. El horario público se normalizó como jueves de 7:00 p. m. a 9:00 p. m. hora Perú, consistente con las fechas originales.

## Archivos modificados

- `data/catalogo_global.json`
- `assets/js/detalle.js`
- `assets/js/catalogo-global.js`
- `assets/css/styles.css`

## Archivos creados

- `data/cursos_tw_educa.json`
- `docs/operacion/reporte_fase8b_auditoria_cursos_tw_educa.md`
- `docs/operacion/reporte_fase8b_integracion_cursos_tw_educa.md`
- `docs/operacion/cursos_tw_educa_cronograma_publico.md`

## Imágenes copiadas/convertidas

Se generaron 14 im?genes WebP en `assets/img/educa/cursos/`, conservando los PNG originales en `Cursos a dictar/`.

## Tabla de integraci?n

| Curso | Categoría | Estado | Fecha | Horario | Imagen | Detalle |
|---|---|---|---|---|---|---|
| Curso práctico de Realidad Virtual con Unity para Meta Quest 2 y 3 | Realidad Virtual | Inscripciones abiertas | 16/07/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-realidad-virtual-con-unity-para-meta-quest-2-y-3.webp` | `detalle/curso.html?id=tw-educa-curso-01&catalogo=tw-educa-vivo` |
| Curso práctico de Programación para AutoCAD con C# y Visual Studio | AutoCAD | Inscripciones abiertas | 30/07/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-programacion-para-autocad-con-csharp-y-visual-studio.webp` | `detalle/curso.html?id=tw-educa-curso-02&catalogo=tw-educa-vivo` |
| Curso práctico de Programación en QGIS con Python para creación de plugins | GIS | Inscripciones abiertas | 06/08/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-programacion-en-qgis-con-python-para-creacion-de-plugins.webp` | `detalle/curso.html?id=tw-educa-curso-03&catalogo=tw-educa-vivo` |
| Curso práctico de Software de IA Offline con Python, Ollama y PySide | Inteligencia Artificial | Inscripciones abiertas | 13/08/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-software-de-ia-offline-con-python-ollama-y-pyside.webp` | `detalle/curso.html?id=tw-educa-curso-04&catalogo=tw-educa-vivo` |
| Curso práctico de Geoportales Web GIS con Python y GeoServer | GIS | Inscripciones abiertas | 27/08/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-geoportales-web-gis-con-python-y-geoserver.webp` | `detalle/curso.html?id=tw-educa-curso-05&catalogo=tw-educa-vivo` |
| Curso práctico de LaTeX y Texmaker para Investigación Científica | Redacci?n técnica | Inscripciones abiertas | 20/08/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-latex-y-texmaker-para-investigacion-cientifica.webp` | `detalle/curso.html?id=tw-educa-curso-06&catalogo=tw-educa-vivo` |
| Curso práctico de Machine Learning aplicado a Mecánica de Fluidos | Inteligencia Artificial | Inscripciones abiertas | 10/09/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-machine-learning-aplicado-a-mecanica-de-fluidos.webp` | `detalle/curso.html?id=tw-educa-curso-07&catalogo=tw-educa-vivo` |
| Curso práctico de CFD con OpenFOAM en Windows 10/11 usando WSL | Simulaci?n | Inscripciones abiertas | 24/09/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-cfd-con-openfoam-en-windows-10-11-usando-wsl.webp` | `detalle/curso.html?id=tw-educa-curso-08&catalogo=tw-educa-vivo` |
| Curso práctico de Cloud Computing para OpenFOAM | Simulaci?n | Inscripciones abiertas | 15/10/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-cloud-computing-para-openfoam.webp` | `detalle/curso.html?id=tw-educa-curso-09&catalogo=tw-educa-vivo` |
| Curso práctico de Datos Climáticos y Oceanográficos con Python | Programaci?n | Inscripciones abiertas | 05/11/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-datos-climaticos-y-oceanograficos-con-python.webp` | `detalle/curso.html?id=tw-educa-curso-10&catalogo=tw-educa-vivo` |
| Curso práctico de C++ aplicado a Mecánica de Fluidos | Programaci?n | Inscripciones abiertas | 26/11/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-cpp-aplicado-a-mecanica-de-fluidos.webp` | `detalle/curso.html?id=tw-educa-curso-11&catalogo=tw-educa-vivo` |
| Curso práctico de Apps Móviles para Mecánica de Fluidos con Flutter y Dart | Desarrollo móvil | Inscripciones abiertas | 10/12/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-apps-moviles-para-mecanica-de-fluidos-con-flutter-y-dart.webp` | `detalle/curso.html?id=tw-educa-curso-12&catalogo=tw-educa-vivo` |
| Curso práctico de Visión Artificial aplicada a Ríos y Canales | Tecnolog?a | Inscripciones abiertas | 17/12/2026 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-vision-artificial-aplicada-a-rios-y-canales.webp` | `detalle/curso.html?id=tw-educa-curso-13&catalogo=tw-educa-vivo` |
| Curso práctico de Programación GPU NVIDIA aplicada a CFD | Simulaci?n | Inscripciones abiertas | 07/01/2027 | Jueves, 7:00 p. m. a 9:00 p. m. hora Perú | `assets/img/educa/cursos/curso-practico-de-programacion-gpu-nvidia-aplicada-a-cfd.webp` | `detalle/curso.html?id=tw-educa-curso-14&catalogo=tw-educa-vivo` |

## Validaciones realizadas

- JSON válido: `data/catalogo_global.json`, `data/cursos_tw_educa.json`, `data/banners_lineas.json`.
- JS válido con `node --check`: `assets/js/detalle.js`, `assets/js/catalogo-global.js`.
- Rutas de imágenes de los 14 cursos verificadas.
- Servidor local iniciado con `python -m http.server 8000`.
- Páginas probadas: `index.html`, `educa/index.html`, `store/index.html`.
- Detalles probados: `tw-educa-curso-01`, `tw-educa-curso-02`, `tw-educa-curso-03`, `tw-educa-curso-08`, `tw-educa-curso-14`.
- Búsqueda probada en TW Educa con `OpenFOAM`, con resultados de cursos relacionados.
- Revisión responsive de TW Educa en 390 px y 1280 px sin overflow horizontal.
- Consola del navegador sin errores durante la revisión de páginas base.

## Problemas detectados

La terminal de PowerShell puede mostrar mojibake al imprimir algunos archivos existentes, pero los TXT fuente fueron leídos y los artefactos nuevos escritos como UTF-8.

## Recomendaci?n para publicaci?n

Publicar despu?s de validar navegaci?n local, revisar textos comerciales finales y confirmar si los precios de preventa deben mantenerse como inversi?n pública o pasar a consulta por WhatsApp.
