# Reporte de generacion de paginas sociales de cursos

Fecha: 2026-07-04

## Resultado

- Cursos procesados: 14
- Directorio generado: `cursos/<slug>/index.html`
- Open Graph escrito en HTML inicial.
- Enlaces publicos actualizados en `data/cursos_tw_educa.json` y `data/catalogo_global.json`.
- Sitemap comercial y `sitemap.xml` actualizados.

## URLs generadas

| ID | URL estatica | Imagen Open Graph | Dimensiones |
|---|---|---|---|
| `tw-educa-curso-01` | `https://tecprog-world-store.github.io/cursos/realidad-virtual-unity-meta-quest/` | `assets/img/educa/cursos/curso-practico-de-realidad-virtual-con-unity-para-meta-quest-2-y-3.webp` | 1200x1200 |
| `tw-educa-curso-02` | `https://tecprog-world-store.github.io/cursos/programacion-autocad-csharp/` | `assets/img/educa/cursos/curso-practico-de-programacion-para-autocad-con-csharp-y-visual-studio.webp` | 1200x1200 |
| `tw-educa-curso-03` | `https://tecprog-world-store.github.io/cursos/qgis-python-plugins/` | `assets/img/educa/cursos/curso-practico-de-programacion-en-qgis-con-python-para-creacion-de-plugins.webp` | 1200x1200 |
| `tw-educa-curso-04` | `https://tecprog-world-store.github.io/cursos/ia-offline-python-ollama-pyside/` | `assets/img/educa/cursos/curso-practico-de-software-de-ia-offline-con-python-ollama-y-pyside.webp` | 1200x1200 |
| `tw-educa-curso-05` | `https://tecprog-world-store.github.io/cursos/geoportales-web-gis-python-geoserver/` | `assets/img/educa/cursos/curso-practico-de-geoportales-web-gis-con-python-y-geoserver.webp` | 1200x1200 |
| `tw-educa-curso-06` | `https://tecprog-world-store.github.io/cursos/latex-texmaker-investigacion/` | `assets/img/educa/cursos/curso-practico-de-latex-y-texmaker-para-investigacion-cientifica.webp` | 1200x1200 |
| `tw-educa-curso-07` | `https://tecprog-world-store.github.io/cursos/machine-learning-mecanica-fluidos/` | `assets/img/educa/cursos/curso-practico-de-machine-learning-aplicado-a-mecanica-de-fluidos.webp` | 1200x1200 |
| `tw-educa-curso-08` | `https://tecprog-world-store.github.io/cursos/cfd-openfoam-wsl/` | `assets/img/educa/cursos/curso-practico-de-cfd-con-openfoam-en-windows-10-11-usando-wsl.webp` | 1200x1200 |
| `tw-educa-curso-09` | `https://tecprog-world-store.github.io/cursos/cloud-computing-openfoam/` | `assets/img/educa/cursos/curso-practico-de-cloud-computing-para-openfoam.webp` | 1200x1200 |
| `tw-educa-curso-10` | `https://tecprog-world-store.github.io/cursos/datos-climaticos-oceanograficos-python/` | `assets/img/educa/cursos/curso-practico-de-datos-climaticos-y-oceanograficos-con-python.webp` | 1200x1200 |
| `tw-educa-curso-11` | `https://tecprog-world-store.github.io/cursos/cpp-mecanica-fluidos/` | `assets/img/educa/cursos/curso-practico-de-cpp-aplicado-a-mecanica-de-fluidos.webp` | 1200x1200 |
| `tw-educa-curso-12` | `https://tecprog-world-store.github.io/cursos/apps-moviles-flutter-mecanica-fluidos/` | `assets/img/educa/cursos/curso-practico-de-apps-moviles-para-mecanica-de-fluidos-con-flutter-y-dart.webp` | 1200x1200 |
| `tw-educa-curso-13` | `https://tecprog-world-store.github.io/cursos/vision-artificial-rios-canales/` | `assets/img/educa/cursos/curso-practico-de-vision-artificial-aplicada-a-rios-y-canales.webp` | 1200x1200 |
| `tw-educa-curso-14` | `https://tecprog-world-store.github.io/cursos/programacion-gpu-nvidia-cfd/` | `assets/img/educa/cursos/curso-practico-de-programacion-gpu-nvidia-aplicada-a-cfd.webp` | 1200x1200 |

## Extension a productos y servicios

El generador deja separadas las funciones de lectura de datos, metadatos, plantilla HTML y sitemap. Para productos y servicios se debe crear un mapeo equivalente desde `data/catalogo_global.json`, definir `productos/<slug>/` o `servicios/<slug>/`, y reutilizar la misma regla: metadatos absolutos en HTML inicial, no por JavaScript.
