# REPORTE FASE 02 — CORRECCIONES SEO Y LIMPIEZA SEGURA

Fecha: 2026-07-28  
Repositorio: `C:\Users\ACER\Documents\GitHub\Tecprog-World-Store.github.io`  
Rama local: `fase-02-correcciones-seo-limpieza-segura`

## 1. Resumen ejecutivo

La FASE 02 quedó completada sin modificar diseño, navegación, textos comerciales, precios, cursos, imágenes ni la arquitectura protegida.

Resultados:

- `sitemap.xml` pasó de un archivo XML inválido con 114 entradas a XML válido con 100 URL públicas únicas.
- Las 14 rutas inexistentes fueron retiradas; sus 14 alias cortos válidos ya estaban presentes y se conservaron.
- Las 100 URL finales del sitemap responden HTTP 200; no queda ningún 404.
- Se retiraron del manifiesto auxiliar `data/sitemap_comercial.json` las 14 entradas largas duplicadas e inexistentes.
- Se corrigieron dos apariciones de la ruta con tilde en `assets/js/detalle.js`.
- Se eliminaron exclusivamente los diez artefactos autorizados de JetBrains y caché Python.
- `.gitignore` conserva las reglas existentes y ahora ignora `.idea/`, `__pycache__/` y `*.py[cod]`.
- Los tres validadores protegidos finalizaron correctamente.
- Se probaron 25 páginas representativas en navegador sin errores ni advertencias de consola.
- Los 448 candidatos a archivo no fueron movidos.
- Ninguno de los 183 recursos no referenciados ni de los diez duplicados operativos fue eliminado.
- No se realizó commit ni push.

## 2. Estado inicial del repositorio

Estado inicial:

```text
## main...origin/main
?? AUDITORIA_REPOSITORIO_FASE_01.md
```

El único pendiente era el informe autorizado de FASE 01. No existían cambios rastreados previos ni otros archivos no rastreados.

Se leyó íntegramente `AUDITORIA_REPOSITORIO_FASE_01.md` y se reconfirmó:

- `sitemap.xml` inválido por secuencias literales `\n`;
- 114 URL declaradas, 14 de ellas inexistentes;
- dos apariciones de `catálogo-general-tw-educa.html`;
- siete archivos bajo `.idea/` y tres `.pyc` autorizados;
- ausencia de reglas globales para JetBrains y caché Python.

## 3. Rama local creada

Se creó y utilizó:

```text
fase-02-correcciones-seo-limpieza-segura
```

La rama parte de `main`. No se creó commit.

## 4. Archivos modificados

Archivos rastreados modificados: **4**.

- `.gitignore`
- `assets/js/detalle.js`
- `data/sitemap_comercial.json`
- `sitemap.xml`

Archivo documental nuevo de esta fase:

- `REPORTE_FASE_02_CORRECCIONES_Y_LIMPIEZA.md`

El informe de FASE 01 ya existía como archivo no rastreado antes de iniciar esta fase.

## 5. Archivos eliminados

Se eliminaron exclusivamente los diez archivos autorizados:

- `.idea/.gitignore`
- `.idea/inspectionProfiles/profiles_settings.xml`
- `.idea/misc.xml`
- `.idea/modules.xml`
- `.idea/Tecprog-World-Store.github.io.iml`
- `.idea/vcs.xml`
- `.idea/workspace.xml`
- `tools/__pycache__/convertir_catalogo_txt_a_json.cpython-314.pyc`
- `tools/__pycache__/generar_flyers_html_tw_store.cpython-314.pyc`
- `tools/__pycache__/revisar_catalogo_fuentes.cpython-314.pyc`

Las carpetas vacías `.idea/inspectionProfiles/`, `.idea/` y `tools/__pycache__/` fueron retiradas.

Git muestra nueve eliminaciones porque `.idea/workspace.xml` no estaba rastreado: la regla histórica `/workspace.xml` de `.idea/.gitignore` lo excluía. Su existencia fue confirmada al inicio y su ausencia al final.

## 6. Corrección aplicada a sitemap.xml

Cambios:

- se sustituyeron los `\n` literales por saltos de línea reales;
- se mantuvo declaración XML UTF-8;
- se conservó el namespace de sitemap.org;
- se mantuvieron `loc`, `lastmod` y `priority` existentes;
- no se inventaron fechas;
- se conservaron el dominio público y las rutas válidas;
- se retiraron las 14 URL largas inexistentes;
- se conservaron sus 14 alias cortos ya presentes;
- se eliminaron duplicados resultantes;
- se comprobó que no existen URL de localhost, `127.0.0.1` ni rutas de Windows.

Resultado:

| Métrica | Antes | Después |
|---|---:|---:|
| Entradas | 114 | 100 |
| URL únicas | No comprobable como XML | 100 |
| Rutas 404 | 14 | 0 |
| XML válido | No | Sí |

`data/sitemap_comercial.json`, fuente auxiliar relacionada, pasó de 65 a 51 entradas únicas al retirar las mismas 14 rutas largas inválidas. Las rutas cortas correctas se conservaron.

## 7. Resultado del parser XML

Validación con `xml.etree.ElementTree`:

```text
XML_VALID|True|URLS|100|UNIQUE|100
INVALID_TARGETS|0
```

El archivo se sirve localmente con HTTP 200 y tipo `application/xml; charset=utf-8`.

## 8. Resolución individual de las 14 rutas 404

| Ruta 404 original | Página equivalente encontrada | Acción ejecutada | URL final válida | Evidencia HTTP |
|---|---|---|---|---|
| `cursos/curso-practico-de-apps-moviles-para-mecanica-de-fluidos-con-flutter-y-dart/` | `cursos/apps-moviles-flutter-mecanica-fluidos/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/apps-moviles-flutter-mecanica-fluidos/` | 200 |
| `cursos/curso-practico-de-c-plus-plus-aplicado-a-mecanica-de-fluidos/` | `cursos/cpp-mecanica-fluidos/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/cpp-mecanica-fluidos/` | 200 |
| `cursos/curso-practico-de-cfd-con-openfoam-en-windows-10-11-usando-wsl/` | `cursos/cfd-openfoam-wsl/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/cfd-openfoam-wsl/` | 200 |
| `cursos/curso-practico-de-cloud-computing-para-openfoam/` | `cursos/cloud-computing-openfoam/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/cloud-computing-openfoam/` | 200 |
| `cursos/curso-practico-de-datos-climaticos-y-oceanograficos-con-python/` | `cursos/datos-climaticos-oceanograficos-python/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/datos-climaticos-oceanograficos-python/` | 200 |
| `cursos/curso-practico-de-geoportales-web-gis-con-python-y-geoserver/` | `cursos/geoportales-web-gis-python-geoserver/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/geoportales-web-gis-python-geoserver/` | 200 |
| `cursos/curso-practico-de-latex-y-texmaker-para-investigacion-cientifica/` | `cursos/latex-texmaker-investigacion/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/latex-texmaker-investigacion/` | 200 |
| `cursos/curso-practico-de-machine-learning-aplicado-a-mecanica-de-fluidos/` | `cursos/machine-learning-mecanica-fluidos/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/machine-learning-mecanica-fluidos/` | 200 |
| `cursos/curso-practico-de-programacion-en-qgis-con-python-para-creacion-de-plugins/` | `cursos/qgis-python-plugins/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/qgis-python-plugins/` | 200 |
| `cursos/curso-practico-de-programacion-gpu-nvidia-aplicada-a-cfd/` | `cursos/programacion-gpu-nvidia-cfd/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/programacion-gpu-nvidia-cfd/` | 200 |
| `cursos/curso-practico-de-programacion-para-autocad-con-c-y-visual-studio/` | `cursos/programacion-autocad-csharp/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/programacion-autocad-csharp/` | 200 |
| `cursos/curso-practico-de-realidad-virtual-con-unity-para-meta-quest-2-y-3/` | `cursos/realidad-virtual-unity-meta-quest/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/realidad-virtual-unity-meta-quest/` | 200 |
| `cursos/curso-practico-de-software-de-ia-offline-con-python-ollama-y-pyside/` | `cursos/ia-offline-python-ollama-pyside/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/ia-offline-python-ollama-pyside/` | 200 |
| `cursos/curso-practico-de-vision-artificial-aplicada-a-rios-y-canales/` | `cursos/vision-artificial-rios-canales/` | Retirar larga; conservar alias | `https://tecprog-world-store.github.io/cursos/vision-artificial-rios-canales/` | 200 |

Cada página equivalente contiene canonical y `og:url` coherentes con la ruta corta. No se crearon páginas duplicadas ni redirecciones incompatibles con GitHub Pages.

## 9. Corrección de assets/js/detalle.js

Se corrigieron las dos apariciones activas:

```text
../catalogo/catálogo-general-tw-educa.html
```

por:

```text
../catalogo/catalogo-general-tw-educa.html
```

Las apariciones correspondían a:

- `backHref` de los cursos normalizados;
- enlace de retorno cuando un curso no se encuentra.

Prueba:

- curso válido `detalle/curso.html?id=qgis-basico`: carga correcta;
- identificador inexistente: muestra el fallback y el enlace final apunta a `../catalogo/catalogo-general-tw-educa.html`;
- destino del enlace: HTTP 200.

## 10. Resultado de la búsqueda de referencias similares

Después de la corrección:

```text
TILDE_REMAINING_ACTIVE: 0
BAD_SLUGS_IN_ACTIVE_RUNTIME: 0
CASE_MISMATCHES: 0
```

Las rutas largas pueden permanecer en documentación histórica, respaldos y el informe de FASE 01 como evidencia. No se modificaron esas fuentes.

El análisis de 1,404 atributos HTML locales no encontró referencias físicas rotas confirmadas. Cuatro coincidencias restantes en `detalle/item.html` son plantillas dinámicas `${...}`, no rutas literales.

## 11. Cambios aplicados a .gitignore

Se conservaron todas las reglas LaTeX y se añadieron:

```gitignore
# JetBrains IDEs
.idea/

# Python cache and bytecode
__pycache__/
*.py[cod]
```

`git check-ignore -v` confirmó:

- `.idea/workspace.xml` ignorado por `.idea/`;
- `tools/__pycache__/sample.pyc` ignorado por `__pycache__/`;
- `tools/cache.pyc` ignorado por `*.py[cod]`.

No se añadieron reglas para `assets/`, `data/`, `build/`, `backups/`, `docs/`, `Cursos a dictar/`, sitemap, HTML ni JSON operativos.

## 12. Resultado de los tres validadores protegidos

```text
OK: paginas clave respetan maximo tres paneles y separan paneles locales/globales.
OK: no hay paneles estructurales duplicados ni referencias legacy en HTML publico.
OK: assets CSS/JS locales usan v=20260708-01 sin duplicados por pagina.
EXIT_CODES|layout=0|duplicates=0|assets=0
```

## 13. Resultado de la prueba local

Servidor:

```text
http://127.0.0.1:8765/
```

Cobertura:

- página principal;
- Store y ocho líneas comerciales;
- catálogos general, cursos, guías y TW Innova;
- cuatro páginas estáticas de cursos;
- detalle de curso válido y fallback;
- muestra de detalle de producto;
- empresa;
- pagos Perú e internacionales;
- dos páginas legales;
- `robots.txt`;
- `sitemap.xml`;
- todas las rutas incluidas en el sitemap.

Resultados de navegador:

- 25 páginas HTML representativas probadas;
- todas cargaron `main`, CSS y JavaScript;
- canonicals y Open Graph presentes en la muestra;
- cero imágenes locales cargadas con error;
- cero errores o advertencias de consola;
- enlace corregido de detalle verificado en ejecución.

`robots.txt` y `sitemap.xml` respondieron HTTP 200.

## 14. Cantidad total de rutas probadas

Rutas finales extraídas del sitemap y probadas por HTTP: **100**.

Adicionalmente se probaron 25 vistas HTML representativas en navegador. Algunas pertenecen al conjunto de 100 y no se suman para evitar inflar la métrica principal.

## 15. Cantidad de respuestas HTTP 200

Sitemap final:

```text
HTTP 200: 100
```

## 16. Cantidad de respuestas HTTP 404

Sitemap final:

```text
HTTP 404: 0
Otros estados: 0
```

## 17. Errores y advertencias de consola

```text
Errores: 0
Advertencias: 0
```

No se detectaron regresiones nuevas en la muestra.

## 18. Matriz resumida de los 448 candidatos a archivo

No se movió ningún archivo. Destino externo propuesto:

```text
C:\Users\ACER\Documents\GitHub\Tecprog-World-Store-archivo
```

| Conjunto | Archivos | Tamaño | Tipo de contenido | Posible dependencia | Evidencia no ejecutable pública | Riesgo | Destino propuesto | Restauración | Validación posterior |
|---|---:|---:|---|---|---|---|---|---|---|
| `backups/**` | 302 | 5,725,249 B | Instantáneas históricas | Recuperación manual | Ninguna referencia `href/src/fetch/import` operativa | Medio | `...\backups\` | Copiar de vuelta preservando rutas | Validadores, diff y prueba HTTP |
| `_auditoria_codex/**` | 23 | 178,428 B | Auditorías y JSON de diagnóstico | Consulta humana | Sin carga desde páginas o JS | Bajo | `...\auditorias-historicas\` | Copiar carpeta completa | Comprobar documentación requerida |
| `Cursos a dictar/**` | 76 | 68,197,358 B | Fuentes editoriales e imágenes | Posibles fuentes maestras | Sin carga desde HTML/JS público | Alto | `...\fuentes-editoriales\Cursos a dictar\` | Restaurar carpeta completa | Revisar proceso editorial y hashes |
| `build/**` | 43 | 955,876 B | Resultados generados | Publicaciones PDF/LaTeX potenciales | Sin referencias de ejecución pública | Medio | `...\builds-generados\` | Restaurar o regenerar | Comparar entregables y ejecutar validadores |
| `data/catalogo_global.backup_fase7.json` | 1 | 67,143 B | Snapshot JSON | Recuperación de catálogo | No consumido por `fetch()` activo | Bajo | `...\snapshots-data\` | Copiar a `data/` | Validar JSON y catálogo |
| `data/catalogo_global.backup_fase8f.json` | 1 | 114,834 B | Snapshot JSON | Recuperación de catálogo | No consumido por `fetch()` activo | Bajo | `...\snapshots-data\` | Copiar a `data/` | Validar JSON y catálogo |
| `data/cursos_tw_educa.backup_fase8f.json` | 1 | 90,914 B | Snapshot JSON | Recuperación de cursos | No consumido por `fetch()` activo | Bajo | `...\snapshots-data\` | Copiar a `data/` | Validar JSON, cursos y precios |
| `data/imagenes_pendientes.backup-fase8-cierre-20260612-204801.json` | 1 | 66,271 B | Snapshot editorial | Control histórico de imágenes | No consumido por ejecución pública | Bajo | `...\snapshots-data\` | Copiar a `data/` | Validar JSON y proceso visual |
| **Total** | **448** | **75,396,073 B** |  |  |  |  |  |  |  |

Método reversible recomendado para FASE 03:

1. crear o verificar el destino externo;
2. copiar conservando estructura y timestamps;
3. comparar cantidad, tamaño y SHA-256;
4. probar restauración de una muestra;
5. solo después retirar los originales;
6. ejecutar validadores y prueba HTTP;
7. conservar un manifiesto de origen, destino y hash.

## 19. Riesgos pendientes

- `Cursos a dictar/**` concentra 68.2 MB y puede contener fuentes editoriales únicas; requiere aprobación humana antes de mover.
- Los 183 recursos no referenciados siguen necesitando una matriz de consumo dinámico y editorial.
- Los diez duplicados operativos no fueron tocados; unificación futura exige migrar referencias primero.
- Documentación y backups conservan rutas largas antiguas como evidencia histórica.
- `detalle/producto.html?id=tw-store-001` mostró el fallback “Curso no encontrado” en la muestra. No se modificó porque no pertenece al alcance SEO solicitado y requiere diagnóstico separado de la plantilla/identificador.
- El servidor HTTP simple sirve `robots.txt` como `application/octet-stream`; GitHub Pages puede aplicar un tipo distinto. El contenido responde 200 y no se modificó.
- La prueba local en Windows no sustituye una comprobación final en el entorno case-sensitive de GitHub Pages, aunque el escaneo no detectó diferencias de mayúsculas/minúsculas.

## 20. Recomendación precisa para la FASE 03

Ejecutar un archivado reversible por lotes, empezando por `_auditoria_codex/**` y los cuatro JSON de respaldo de bajo riesgo. Antes de mover `backups/**`, `build/**` o `Cursos a dictar/**`, generar un manifiesto SHA-256, confirmar retención y dependencia editorial, copiar al destino externo, verificar los 448 archivos y probar restauración. Mantener fuera de alcance los 183 no referenciados y los diez duplicados hasta una fase específica.

## 21. Evidencia de git diff

Antes de crear este reporte:

```text
4 archivos rastreados modificados
9 eliminaciones rastreadas
10 eliminaciones físicas autorizadas
513 inserciones y 125 eliminaciones de líneas
```

La diferencia entre nueve eliminaciones rastreadas y diez físicas corresponde a `.idea/workspace.xml`, ignorado y no rastreado desde el inicio.

Resumen:

```text
M  .gitignore
M  assets/js/detalle.js
M  data/sitemap_comercial.json
M  sitemap.xml
D  .idea/.gitignore
D  .idea/Tecprog-World-Store.github.io.iml
D  .idea/inspectionProfiles/profiles_settings.xml
D  .idea/misc.xml
D  .idea/modules.xml
D  .idea/vcs.xml
D  tools/__pycache__/convertir_catalogo_txt_a_json.cpython-314.pyc
D  tools/__pycache__/generar_flyers_html_tw_store.cpython-314.pyc
D  tools/__pycache__/revisar_catalogo_fuentes.cpython-314.pyc
```

Todos los cambios pueden revisarse con `git diff`. No se ejecutó `git add`, commit ni push.

## 22. Estado final de git status

Estado esperado al cierre:

```text
## fase-02-correcciones-seo-limpieza-segura
 M .gitignore
 D .idea/.gitignore
 D .idea/Tecprog-World-Store.github.io.iml
 D .idea/inspectionProfiles/profiles_settings.xml
 D .idea/misc.xml
 D .idea/modules.xml
 D .idea/vcs.xml
 M assets/js/detalle.js
 M data/sitemap_comercial.json
 M sitemap.xml
 D tools/__pycache__/convertir_catalogo_txt_a_json.cpython-314.pyc
 D tools/__pycache__/generar_flyers_html_tw_store.cpython-314.pyc
 D tools/__pycache__/revisar_catalogo_fuentes.cpython-314.pyc
?? AUDITORIA_REPOSITORIO_FASE_01.md
?? REPORTE_FASE_02_CORRECCIONES_Y_LIMPIEZA.md
```

El servidor local debe quedar detenido antes de la entrega.
