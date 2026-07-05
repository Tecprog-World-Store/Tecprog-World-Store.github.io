# Reporte Fase 8G - Open Graph por curso

Fecha: 2026-07-04

## Resultado

Se generaron 14 paginas estaticas para cursos TW Educa. Cada pagina contiene metadatos sociales estaticos en el HTML inicial y reutiliza `assets/js/detalle.js` solo para enriquecer la ficha visible al usuario.

## URLs e imagenes Open Graph

| Curso | URL estatica | Imagen Open Graph |
|---|---|---|
| Realidad Virtual con Unity para Meta Quest | `/cursos/realidad-virtual-unity-meta-quest/` | `assets/img/educa/cursos/curso-practico-de-realidad-virtual-con-unity-para-meta-quest-2-y-3.webp` |
| Programacion para AutoCAD con C# | `/cursos/programacion-autocad-csharp/` | `assets/img/educa/cursos/curso-practico-de-programacion-para-autocad-con-csharp-y-visual-studio.webp` |
| QGIS con Python para plugins | `/cursos/qgis-python-plugins/` | `assets/img/educa/cursos/curso-practico-de-programacion-en-qgis-con-python-para-creacion-de-plugins.webp` |
| IA Offline con Python, Ollama y PySide | `/cursos/ia-offline-python-ollama-pyside/` | `assets/img/educa/cursos/curso-practico-de-software-de-ia-offline-con-python-ollama-y-pyside.webp` |
| Geoportales Web GIS con Python y GeoServer | `/cursos/geoportales-web-gis-python-geoserver/` | `assets/img/educa/cursos/curso-practico-de-geoportales-web-gis-con-python-y-geoserver.webp` |
| LaTeX y Texmaker para investigacion | `/cursos/latex-texmaker-investigacion/` | `assets/img/educa/cursos/curso-practico-de-latex-y-texmaker-para-investigacion-cientifica.webp` |
| Machine Learning aplicado a Mecanica de Fluidos | `/cursos/machine-learning-mecanica-fluidos/` | `assets/img/educa/cursos/curso-practico-de-machine-learning-aplicado-a-mecanica-de-fluidos.webp` |
| CFD con OpenFOAM en Windows WSL | `/cursos/cfd-openfoam-wsl/` | `assets/img/educa/cursos/curso-practico-de-cfd-con-openfoam-en-windows-10-11-usando-wsl.webp` |
| Cloud Computing para OpenFOAM | `/cursos/cloud-computing-openfoam/` | `assets/img/educa/cursos/curso-practico-de-cloud-computing-para-openfoam.webp` |
| Datos Climaticos y Oceanograficos con Python | `/cursos/datos-climaticos-oceanograficos-python/` | `assets/img/educa/cursos/curso-practico-de-datos-climaticos-y-oceanograficos-con-python.webp` |
| C++ aplicado a Mecanica de Fluidos | `/cursos/cpp-mecanica-fluidos/` | `assets/img/educa/cursos/curso-practico-de-cpp-aplicado-a-mecanica-de-fluidos.webp` |
| Apps Moviles para Mecanica de Fluidos | `/cursos/apps-moviles-flutter-mecanica-fluidos/` | `assets/img/educa/cursos/curso-practico-de-apps-moviles-para-mecanica-de-fluidos-con-flutter-y-dart.webp` |
| Vision Artificial aplicada a Rios y Canales | `/cursos/vision-artificial-rios-canales/` | `assets/img/educa/cursos/curso-practico-de-vision-artificial-aplicada-a-rios-y-canales.webp` |
| Programacion GPU NVIDIA aplicada a CFD | `/cursos/programacion-gpu-nvidia-cfd/` | `assets/img/educa/cursos/curso-practico-de-programacion-gpu-nvidia-aplicada-a-cfd.webp` |

## Confirmaciones

- Los metadatos Open Graph no dependen de JavaScript.
- Todas las URLs OG son absolutas HTTPS.
- Todas las imagenes OG apuntan a flyers especificos existentes.
- `data/catalogo_global.json` y `data/cursos_tw_educa.json` apuntan a URLs estaticas.
- `sitemap.xml` conserva URLs anteriores y añade las paginas de cursos.

## Productos y servicios

La estrategia equivalente queda preparada para:

- `/productos/<slug>/`
- `/servicios/<slug>/`

Debe usarse `data/catalogo_global.json` como fuente, filtrando por `tipo_item` o linea, y generando HTML estatico con los mismos campos OG absolutos.

