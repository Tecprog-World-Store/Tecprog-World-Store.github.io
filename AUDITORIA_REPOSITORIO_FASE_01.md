# AUDITORÍA TÉCNICA DEL REPOSITORIO — FASE 01

Fecha de auditoría: 2026-07-28  
Repositorio: `C:\Users\ACER\Documents\GitHub\Tecprog-World-Store.github.io`  
Modalidad: solo lectura; no se eliminó, movió, renombró ni modificó ningún archivo preexistente.

## 1. Resumen ejecutivo

El proyecto es un sitio estático compatible con GitHub Pages, sin proceso de compilación obligatorio. Su punto de entrada es `index.html` y la ejecución pública depende principalmente de HTML, `assets/css/styles.css`, 14 scripts JavaScript activos, archivos JSON de `data/` y recursos multimedia de `assets/`.

Se analizaron 1,192 archivos en 338 carpetas, con un tamaño total de 432,091,559 bytes (412.07 MiB). El peso está concentrado en imágenes PNG (337.02 MB decimales), audio MP3 (50.11 MB) y recursos WebP (26.18 MB).

Hallazgos confirmados:

- 114 rutas del sitemap fueron solicitadas mediante HTTP local: 100 devolvieron 200 y 14 devolvieron 404.
- `sitemap.xml` no es XML válido: contiene secuencias literales `\n`; el analizador falla en la línea 1, columna 38.
- El sitemap contiene 14 URL de cursos cuyos directorios o `index.html` no existen.
- Se detectaron 12 páginas HTML operativas sin enlaces entrantes ni presencia válida en el sitemap.
- No se detectaron diferencias de mayúsculas/minúsculas en las referencias locales analizadas.
- Los 15 CSS/JS operativos están cargados desde al menos una página; no hay hojas CSS ni scripts activos totalmente desconectados.
- Se encontraron 33 grupos de archivos idénticos por SHA-256, 55 copias redundantes y 17,028,501 bytes repetidos.
- Se clasificaron 183 archivos como `NO REFERENCIADO`; son recursos posiblemente huérfanos, no autorizados para eliminación, porque algunos pueden participar en rutas dinámicas, Open Graph, procesos editoriales o futuras publicaciones.
- Se identificaron 448 candidatos conservadores a archivo y solo 10 candidatos a eliminación posterior.
- La búsqueda de indicadores de credenciales no encontró claves privadas, API keys, contraseñas ni secretos verificables. Las coincidencias de “token” y “secret” corresponden a contenido técnico de cursos o código de procesamiento.
- Las tres validaciones protegidas del repositorio terminaron correctamente.

Conclusión: el sitio funciona en sus rutas principales, pero el repositorio mezcla la publicación operativa con respaldos, fuentes editoriales, resultados generados, configuración de IDE y una gran cantidad de recursos alternativos. No debe realizarse una limpieza automática basándose solo en referencias estáticas.

## 2. Tecnología y arquitectura detectada

| Componente | Detección |
|---|---|
| Publicación | Sitio estático para GitHub Pages |
| HTML | 344 archivos totales; 114 fuera de `backups/` y `build/` |
| CSS | CSS propio; hoja operativa central `assets/css/styles.css` |
| JavaScript | JavaScript vanilla, sin empaquetador obligatorio |
| Datos | JSON consumido mediante `fetch()` y rutas calculadas |
| Generación | Scripts Python en `tools/` y `scripts/`; no son necesarios para servir el sitio ya generado |
| Framework | No se detectó React, Vue, Angular, Svelte, Next, Jekyll configurado ni otro framework de ejecución |
| Dependencias | No hay `package.json`, `requirements.txt` ni instalación necesaria para servir la versión actual |
| Automatización | Validadores y generadores Python; no existe `.github/workflows/` |
| GitHub Pages | Publicación directa de archivos estáticos; rutas absolutas compatibles con un sitio de usuario/organización en la raíz |
| SEO | `robots.txt`, canonicals, Open Graph, JSON-LD y `sitemap.xml` |
| Formularios | Dos formularios HTML: calculadora local y libro de reclamaciones con `action="#"`; no se detectó backend de recepción |
| Terceros | WhatsApp (`wa.me`), PayPal, YouTube/miniaturas, Facebook, LinkedIn, TikTok, Google Maps y enlaces de comparación comercial |
| Service worker | No detectado |

La arquitectura pública protegida es de máximo tres paneles: navegación izquierda, contenido central y panel derecho. Las páginas comerciales usan paneles locales generados por `assets/js/catalogo-global.js`; las institucionales o de detalle pueden usar `assets/js/right-panel.js`. Los validadores confirman que la separación se mantiene.

## 3. Árbol resumido del repositorio

Los conteos excluyen únicamente `.git/`.

```text
/
├── index.html                         entrada principal
├── assets/                    448 archivos / 349,352,036 B
├── backups/                   302 archivos /   5,725,249 B
├── build/                      43 archivos /     955,876 B
├── catalogo/                   36 archivos /     130,860 B
├── cursos/                     37 archivos /     468,965 B
├── Cursos a dictar/            76 archivos /  68,197,358 B
├── data/                       60 archivos /   3,621,761 B
├── detalle/                     9 archivos /      31,138 B
├── docs/                       78 archivos /   2,970,853 B
├── lineas/                     11 archivos /      56,512 B
├── tools/                      23 archivos /     219,527 B
├── scripts/                     9 archivos /      29,742 B
├── _auditoria_codex/           23 archivos /     178,428 B
├── temario_cursos/              1 archivo  /       2,267 B
├── store/, educa/, innova/, salud/, interactive/,
│   construye/, inox/, investiga/, disfruta/
├── empresa/, legal/, pagos/, servicios/, herramientas/
├── .idea/                       7 archivos /       3,457 B
├── sitemap.xml, robots.txt, site.webmanifest
└── README.md, AGENTS.md, LICENSE, .gitignore
```

Carpetas vacías detectadas:

- `assets/img/webp`
- `assets/img/store/banners`
- `assets/pdf/brochures`
- `backups/fase_precios_whatsapp_temarios_20260707_224747`
- `backups/cierre-visual-spots-youtube-20260628_011526/assets/img/videos`

## 4. Punto de entrada del sitio

El punto de entrada es `index.html`, publicado como `/` y `/index.html`. Desde allí se cargan:

- `assets/css/styles.css`
- `assets/js/navigation.js`
- `assets/js/main.js`
- `assets/js/audio-player.js`
- `assets/js/catalogo-global.js`
- `assets/js/videos-destacados.js`
- JSON de `data/`
- imágenes, iconos y audio de `assets/`

No existe una fase de build necesaria para la ejecución: `python -m http.server` o cualquier servidor estático equivalente puede servir el sitio.

## 5. Flujo de navegación entre páginas

```text
index.html
├── store/index.html
├── disfruta/index.html
├── educa/index.html
├── innova/index.html
├── salud/index.html
├── interactive/index.html
├── construye/index.html
├── inox/index.html
├── investiga/index.html
├── catalogo/*.html
│   ├── catalogo/cursos/*.html
│   ├── catalogo/guias/*.html
│   └── catalogo/compendios/*.html
├── cursos/*/index.html
├── detalle/*.html?id=...
├── lineas/*.html
├── empresa/*.html
├── pagos/*.html
├── legal/*.html
└── servicios/*.html
```

La navegación y los catálogos construyen enlaces y recursos dinámicamente. Por ello, una ausencia de `href` o `src` literal no demuestra que un archivo sea prescindible. Se cruzaron atributos HTML, `url()` CSS, `fetch()`, literales de rutas JS/JSON, sitemap, rutas calculadas conocidas y observación en navegador.

## 6. Inventario por tipo de archivo

| Extensión | Archivos | Tamaño total |
|---|---:|---:|
| `.html` | 344 | 1,990,616 B |
| `.png` | 187 | 337,016,113 B |
| `.webp` | 154 | 26,184,918 B |
| `.md` | 104 | 404,608 B |
| `.svg` | 96 | 309,025 B |
| `.json` | 89 | 6,839,494 B |
| `.txt` | 54 | 532,274 B |
| `.js` | 52 | 734,629 B |
| `.py` | 30 | 231,934 B |
| `.gitkeep` | 20 | 20 B |
| `.css` | 11 | 553,719 B |
| `.jpg` | 10 | 4,970,383 B |
| `.xml` | 10 | 77,619 B |
| `.pdf` | 9 | 2,034,695 B |
| `.mp3` | 6 | 50,109,641 B |
| `.bat` | 3 | 434 B |
| `.pyc` | 3 | 48,219 B |
| `.puml` | 3 | 4,963 B |
| `.bak` | 2 | 46,184 B |
| `.gitignore` | 2 | 141 B |
| sin extensión | 1 | 1,097 B |
| `.webmanifest` | 1 | 508 B |
| `.iml` | 1 | 325 B |
| **Total** | **1,192** | **432,091,559 B** |

## 7. Tabla de clasificación de archivos

La clasificación es exhaustiva y mutuamente excluyente. Cada archivo pertenece a la primera regla aplicable, en el orden mostrado. “Ruta relativa” expresa un conjunto exacto mediante patrón; los conteos suman los 1,192 archivos. El tamaño es el agregado del conjunto.

| Ruta relativa | Tipo | Tamaño | Referenciado desde | Categoría | Nivel de confianza | Acción propuesta | Justificación |
|---|---|---:|---|---|---|---|---|
| Páginas públicas, SEO, CSS/JS operativos y JSON esenciales | HTML/CSS/JS/JSON/XML | 3,635,043 B | Entrada, navegación, sitemap o carga directa | CRÍTICO | Alto | Conservar | Necesarios para servir rutas públicas y construir la interfaz |
| Recursos con referencia estática/dinámica confirmada y herramientas activas | Multimedia/datos/Python | 106,825,456 B | HTML, CSS, JS, JSON o flujo de mantenimiento | UTILIZADO | Alto | Conservar | Uso confirmado por referencia o proceso operativo |
| Recursos sin confirmación concluyente, fuentes editoriales y auxiliares | Mixto | 68,363,089 B | Uso indirecto o no demostrable | POSIBLEMENTE UTILIZADO | Medio/Bajo | Revisar manualmente | Puede existir consumo dinámico, editorial o futuro |
| 183 rutas enumeradas por los grupos del apartado 9 | Multimedia/JSON | 226,414,274 B | No se encontró referencia activa | NO REFERENCIADO | Medio | Revisar manualmente | Ausencia de referencia no equivale a seguridad de eliminación |
| 10 segundas copias operativas exactas del apartado 10 | PNG/TXT | 16,579,238 B | Rutas alternativas | DUPLICADO | Alto | Optimizar posteriormente | SHA-256 idéntico; confirmar cuál ruta canónica conservar |
| `backups/**` y cuatro JSON `*.backup*` de `data/` | Mixto | 6,064,411 B | Fuera del sitio operativo | RESPALDO O HISTÓRICO | Alto | Archivar posteriormente | Versiones y instantáneas anteriores |
| `build/**`, `.idea/**`, `tools/__pycache__/*.pyc` | Generado/IDE/caché | 1,007,552 B | No requerido por el sitio servido | TEMPORAL O GENERADO | Alto | Archivar o eliminar posteriormente | Salidas reproducibles o metadatos locales |
| `docs/**`, `_auditoria_codex/**`, Markdown y archivos descriptivos | Documentación | 3,202,496 B | Mantenimiento humano | DOCUMENTACIÓN | Alto | Conservar | No ejecuta el sitio, pero documenta reglas y decisiones |
| **Total** |  | **432,091,559 B** |  |  |  |  | **1,192 archivos** |

Conteo por categoría:

| Categoría | Cantidad |
|---|---:|
| CRÍTICO | 150 |
| UTILIZADO | 258 |
| POSIBLEMENTE UTILIZADO | 115 |
| NO REFERENCIADO | 183 |
| DUPLICADO | 10 |
| RESPALDO O HISTÓRICO | 306 |
| TEMPORAL O GENERADO | 53 |
| DOCUMENTACIÓN | 117 |
| **Total** | **1,192** |

Etiquetas secundarias, que pueden solaparse conceptualmente con la categoría primaria:

- `CANDIDATO A ARCHIVO`: 448 archivos, 75,396,073 B.
- `CANDIDATO A ELIMINACIÓN`: 10 archivos, 51,676 B.

## 8. Recursos críticos

Conservar sin cambios hasta disponer de pruebas de regresión:

- `index.html`
- `assets/css/styles.css`
- `assets/js/navigation.js`
- `assets/js/main.js`
- `assets/js/catalogo-global.js`
- `assets/js/right-panel.js`
- `assets/js/audio-player.js`
- `assets/js/detalle.js`
- `assets/js/guias.js`
- `assets/js/compendios.js`
- `assets/js/materiales.js`
- `assets/js/catalogos-lineas.js`
- `assets/js/catalogo-general-cursos.js`
- `assets/js/oferta-detalle.js`
- `assets/js/store.js`
- `assets/js/videos-destacados.js`
- HTML público bajo `store/`, `educa/`, `disfruta/`, `innova/`, `salud/`, `interactive/`, `construye/`, `inox/`, `investiga/`, `catalogo/`, `cursos/`, `detalle/`, `lineas/`, `empresa/`, `legal/`, `pagos/` y `servicios/`
- `data/catalogo_global.json`
- `data/cursos_tw_educa.json`
- `data/catalogo-general-cursos.json`
- `data/catalogo-tw-*.json`
- `data/banners_lineas.json`
- `data/pagos.json`
- JSON consumidos por páginas de detalle
- `robots.txt`, `sitemap.xml`, `site.webmanifest`
- recursos de `assets/` referenciados por los componentes anteriores

Todos los 15 archivos CSS/JS operativos están cargados por al menos una página. No se detectó un CSS o JavaScript activo completamente desconectado.

## 9. Recursos no referenciados

Se clasificaron 183 archivos como `NO REFERENCIADO`. Distribución exacta por conjunto:

| Conjunto de rutas | Cantidad |
|---|---:|
| `assets/img/store/**` | 69 |
| `assets/img/og/**` | 17 |
| `assets/img/banners/**` | 15 |
| `assets/img/cursos/**` | 15 |
| `assets/img/educa/**` | 14 |
| `assets/img/servicios/**` | 11 |
| `assets/img/flyers/**` | 9 |
| `assets/img/guias/**` | 8 |
| `assets/img/compendios/**` | 2 |
| `assets/audio/Pista01_00.mp3` | 1 |
| `assets/audio/Pista02__00.mp3` | 1 |
| `assets/audio/Pista03__00.mp3` | 1 |
| `assets/icons/favicon.svg` | 1 |
| `assets/icons/workshop.svg` | 1 |
| `assets/img/logos/tecprog-logo.svg` | 1 |
| `assets/img/qr/QR_Yape_00.svg` | 1 |
| JSON no consumidos listados debajo | 16 |
| **Total** | **183** |

JSON sin consumo confirmado:

- `data/campanias/top_productos_semana.json`
- `data/descargas.json`
- `data/home-destacados.json`
- `data/imagenes_pendientes.json`
- `data/lineas.json`
- `data/ofertas.json`
- `data/politica_precios_tw_educa.json`
- `data/precios.json`
- `data/productos.json`
- `data/productos_store.json`
- `data/servicios.json`
- `data/software.json`
- `data/tw-interactive.json`
- `data/tw-salud.json`
- `data/visual/prioridad_imagenes_productos.json`
- `data/visual/visual_briefs_store.json`

Estos archivos deben revisarse manualmente contra procesos de publicación, herramientas Python, Open Graph y campañas antes de proponer su archivo. En particular, las imágenes PNG suelen coexistir con WebP y pueden ser fuentes maestras o fallback.

Páginas HTML sin enlaces entrantes y sin entrada válida propia en el sitemap:

- `catalogo/cursos/admision-unac.html`
- `catalogo/cursos/desarrollo-web-con-html-css-php-y-mysql.html`
- `catalogo/cursos/hp50g.html`
- `catalogo/cursos/latex.html`
- `catalogo/cursos/odoo-erp.html`
- `catalogo/cursos/ofimatica-para-emprendedores.html`
- `catalogo/cursos/openfoam-basico-para-simulacion-cfd.html`
- `catalogo/cursos/openfoam-cfd.html`
- `catalogo/cursos/programacion-de-plugins-para-qgis.html`
- `catalogo/cursos/python-para-cientificos-de-datos.html`
- `catalogo/cursos/python-poo.html`
- `catalogo/cursos/qgis-aplicado-a-cuencas-hidrograficas.html`

## 10. Archivos duplicados

El hash SHA-256 detectó 33 grupos idénticos, 55 copias adicionales y 17,028,501 B redundantes. Gran parte corresponde a respaldos, lo cual es esperable.

Duplicados operativos claros:

- `assets/img/store/flyers/tw-interactive-portada.png` duplica `assets/img/flyers/tw-interactive-portada.png`
- `assets/img/store/flyers/tw-educa-portada.png` duplica `assets/img/flyers/tw-educa-portada.png`
- `assets/img/store/flyers/tw-salud-portada.png` duplica `assets/img/flyers/tw-salud-portada.png`
- `assets/img/store/flyers/tw-store-portada.png` duplica `assets/img/flyers/tw-store-portada.png`
- `assets/img/store/flyers/tw-inox-portada.png` duplica `assets/img/flyers/tw-inox-portada.png`
- `assets/img/store/flyers/tw-construye-portada.png` duplica `assets/img/flyers/tw-construye-portada.png`
- `assets/img/store/flyers/tw-innova-portada.png` duplica `assets/img/flyers/tw-innova-portada.png`
- `assets/img/store/flyers/tw-investiga-portada.png` duplica `assets/img/flyers/tw-investiga-portada.png`
- `assets/img/store/flyers/tw-disfruta-portada.png` duplica `assets/img/flyers/tw-disfruta-portada.png`
- `data/fuentes/catalogo_base_cursos_tw_educa.txt` duplica `data/fuente/catalogo_base_cursos_tw_educa.txt`

No se propone eliminar estas copias en FASE 01: las rutas consumidoras deben unificarse primero.

## 11. Respaldos y versiones antiguas

Respaldos identificados:

- Todos los 302 archivos bajo `backups/**`.
- `data/catalogo_global.backup_fase7.json`
- `data/catalogo_global.backup_fase8f.json`
- `data/cursos_tw_educa.backup_fase8f.json`
- `data/imagenes_pendientes.backup-fase8-cierre-20260612-204801.json`

Estas 306 piezas se clasifican como `RESPALDO O HISTÓRICO`. Los respaldos bajo la raíz pueden ser publicados por GitHub Pages y aumentar el tamaño de clonación/despliegue. Deben archivarse fuera del árbol publicado después de validar su política de retención.

## 12. Archivos temporales o generados

- `build/**`: 43 archivos; resultados generados.
- `.idea/**`: 7 archivos; configuración local de JetBrains.
- `tools/__pycache__/*.pyc`: 3 archivos; caché reproducible de Python.
- Cinco carpetas vacías enumeradas en el apartado 3.

El `.gitignore` actual solo ignora auxiliares de LaTeX. Debería evaluarse agregar en FASE 02:

```gitignore
.idea/
__pycache__/
*.py[cod]
```

No se recomienda ignorar `build/` ni `backups/` automáticamente hasta decidir si contienen entregables o retención histórica necesaria.

## 13. Archivos pesados

| Posición | Ruta relativa | Tamaño |
|---:|---|---:|
| 1 | `assets/audio/Pista02__00.mp3` | 32,530,530 B |
| 2 | `assets/audio/Pista01_00.mp3` | 8,515,070 B |
| 3 | `assets/audio/Pista03__00.mp3` | 6,118,242 B |
| 4 | `assets/img/store/productos/tw-interactive-004.png` | 2,670,027 B |
| 5 | `assets/img/og/compendios/qgis-basico-ingenieria-gestion-territorial-og.png` | 2,625,626 B |
| 6 | `assets/img/store/productos/tw-interactive-001.png` | 2,521,999 B |
| 7 | `assets/img/compendios/miniaturas/qgis-basico-ingenieria-gestion-territorial.png` | 2,496,822 B |
| 8 | `assets/img/store/productos/tw-interactive-002.png` | 2,374,199 B |
| 9 | `assets/img/store/og/tw-interactive-og.png` | 2,348,253 B |
| 10 | `assets/img/store/carruseles/tw-interactive-01.png` | 2,339,773 B |
| 11 | `assets/img/store/productos/tw-educa-007.png` | 2,319,912 B |
| 12 | `assets/img/store/productos/tw-construye-003.png` | 2,309,873 B |
| 13 | `assets/img/store/flyers/tw-interactive-portada.png` | 2,295,224 B |
| 14 | `assets/img/flyers/tw-interactive-portada.png` | 2,295,224 B |
| 15 | `assets/img/store/productos/tw-interactive-003.png` | 2,288,595 B |
| 16 | `assets/img/store/productos/tw-construye-005.png` | 2,280,130 B |
| 17 | `assets/img/store/productos/tw-construye-006.png` | 2,275,034 B |
| 18 | `assets/img/store/productos/tw-interactive-005.png` | 2,270,593 B |
| 19 | `Cursos a dictar/Curso_practico_de_datos_climáticos_y_oceanográficos_con_Python.png` | 2,270,144 B |
| 20 | `assets/img/store/carruseles/tw-construye-01.png` | 2,263,769 B |

El mayor ahorro potencial está en:

1. decidir si los MP3 con sufijos `_00`/`__00` son fuentes maestras u obsoletas;
2. archivar `Cursos a dictar/`;
3. retirar PNG duplicados solo después de migrar referencias a WebP o una ruta canónica;
4. conservar tamaños adecuados para Open Graph cuando correspondan.

## 14. Rutas y enlaces rotos

### 14.1 Rutas 404 confirmadas por HTTP

El sitemap declara 14 rutas inexistentes:

- `cursos/curso-practico-de-apps-moviles-para-mecanica-de-fluidos-con-flutter-y-dart/index.html`
- `cursos/curso-practico-de-c-plus-plus-aplicado-a-mecanica-de-fluidos/index.html`
- `cursos/curso-practico-de-cfd-con-openfoam-en-windows-10-11-usando-wsl/index.html`
- `cursos/curso-practico-de-cloud-computing-para-openfoam/index.html`
- `cursos/curso-practico-de-datos-climaticos-y-oceanograficos-con-python/index.html`
- `cursos/curso-practico-de-geoportales-web-gis-con-python-y-geoserver/index.html`
- `cursos/curso-practico-de-latex-y-texmaker-para-investigacion-cientifica/index.html`
- `cursos/curso-practico-de-machine-learning-aplicado-a-mecanica-de-fluidos/index.html`
- `cursos/curso-practico-de-programacion-en-qgis-con-python-para-creacion-de-plugins/index.html`
- `cursos/curso-practico-de-programacion-gpu-nvidia-aplicada-a-cfd/index.html`
- `cursos/curso-practico-de-programacion-para-autocad-con-c-y-visual-studio/index.html`
- `cursos/curso-practico-de-realidad-virtual-con-unity-para-meta-quest-2-y-3/index.html`
- `cursos/curso-practico-de-software-de-ia-offline-con-python-ollama-y-pyside/index.html`
- `cursos/curso-practico-de-vision-artificial-aplicada-a-rios-y-canales/index.html`

Varios tienen alias más cortos que sí existen, por ejemplo `cursos/apps-moviles-flutter-mecanica-fluidos/`, `cursos/cfd-openfoam-wsl/` y `cursos/programacion-autocad-csharp/`. La corrección debe decidir entre actualizar el sitemap o generar las rutas canónicas faltantes sin romper SEO.

### 14.2 Referencias literales para revisar

- `assets/js/detalle.js` contiene `../catalogo/catálogo-general-tw-educa.html`; el archivo existente usa `catalogo-general-tw-educa.html` sin tilde.
- `data/imagenes_pendientes.json` declara ocho imágenes inexistentes de `tw-inox-004..006` y `tw-investiga-001,002,004..006`. Al estar explícitamente marcadas como pendientes, son hallazgos editoriales y no errores de ejecución confirmados.

### 14.3 Mayúsculas/minúsculas

No se encontraron referencias cuyo único problema sea la diferencia de mayúsculas/minúsculas. Esto reduce, pero no elimina, el riesgo de diferencias entre Windows y GitHub Pages.

### 14.4 Sitemap inválido

`sitemap.xml` contiene `\n` literales en vez de saltos de línea. `xml.etree.ElementTree` informó:

```text
ParseError: not well-formed (invalid token): line 1, column 38
```

Este es un error SEO independiente de las 14 rutas 404.

## 15. Errores encontrados durante la prueba local

Servidor utilizado: `http://127.0.0.1:8765/`

Pruebas de navegador:

- Portada cargada con título, `main`, H1, 293 enlaces y 99 imágenes declaradas.
- Se revisaron `store/`, las ocho líneas comerciales adicionales, una página de detalle, pagos y empresa.
- No se registraron errores ni advertencias de consola.
- Las solicitudes observadas inicialmente fueron 231 respuestas HTTP 200.
- Varias imágenes con carga diferida mostraron `naturalWidth=0` por no estar en viewport; al cruzarlas con el sistema de archivos, todas las rutas locales existían. No se contabilizaron como 404.
- La miniatura externa `https://img.youtube.com/...` no pudo verificarse como dependencia local y queda sujeta a disponibilidad de terceros.
- La URL de detalle probada con un identificador no existente mostró “Curso no encontrado”; esto valida el manejo de ausencia, no demuestra un fallo de plantilla.

Prueba completa del sitemap:

- Rutas probadas: 114.
- HTTP 200: 100.
- HTTP 404: 14.
- Consola del navegador: 0 errores/advertencias registrados.

Errores confirmados totales para esta fase: **15** (14 rutas 404 + 1 sitemap XML inválido). Las nueve referencias literales adicionales quedan como hallazgos de revisión y no se suman a errores confirmados.

## 16. Riesgos de eliminar archivos incorrectamente

- Los JSON contienen rutas dinámicas que no siempre aparecen en HTML.
- `catalogo-global.js`, `detalle.js` y scripts relacionados construyen URL en tiempo de ejecución.
- Imágenes PNG pueden ser fuentes maestras, fallback, Open Graph o material de campañas aunque exista WebP.
- Archivos sin enlace entrante pueden estar indexados externamente o conservar valor SEO.
- Los directorios `Cursos a dictar/`, `data/fuente/`, `data/fuentes/` y `temario_cursos/` pueden alimentar generadores fuera del flujo de navegación.
- Los respaldos pueden ser necesarios para recuperación, aunque no deban publicarse.
- Mover archivos rompe rutas absolutas, canonicals, sitemap, Open Graph y datos JSON si no se hace una migración coordinada.
- El sitio integra recursos externos; su ausencia no puede resolverse eliminando archivos locales.
- GitHub Pages es sensible a mayúsculas/minúsculas y a la ubicación raíz.

## 17. Propuesta preliminar de estructura mínima

Propuesta conceptual; no ejecutar todavía:

```text
/
├── index.html
├── assets/
│   ├── css/
│   ├── js/
│   ├── img/
│   ├── audio/
│   └── pdf/
├── data/
├── catalogo/
├── cursos/
├── detalle/
├── lineas/
├── store/
├── educa/ disfruta/ innova/ salud/ interactive/
├── construye/ inox/ investiga/
├── empresa/ legal/ pagos/ servicios/ herramientas/
├── robots.txt
├── sitemap.xml
└── site.webmanifest
```

Fuera del árbol publicable deberían quedar, una vez validados:

- respaldos;
- auditorías históricas;
- fuentes editoriales pesadas;
- resultados generados;
- configuración de IDE;
- caché Python;
- herramientas de mantenimiento, si el método de despliegue permite separar fuente y publicación.

## 18. Propuesta de carpeta para archivar contenido no operativo

Propuesta fuera del árbol publicado:

```text
../Tecprog-World-Store-archivo/
├── backups/
├── auditorias-historicas/
├── fuentes-editoriales/
│   └── Cursos a dictar/
├── builds-generados/
└── snapshots-data/
```

No debe crearse dentro del repositorio público en FASE 01. Si se necesita conservar en Git, conviene usar un repositorio privado o almacenamiento de respaldo separado.

## 19. Lista exacta de archivos que podrían archivarse

La selección exacta está definida por la unión de estos conjuntos, sin incluir ningún otro archivo:

1. Los 302 archivos actualmente contenidos bajo `backups/**`.
2. Los 23 archivos actualmente contenidos bajo `_auditoria_codex/**`.
3. Los 76 archivos actualmente contenidos bajo `Cursos a dictar/**`.
4. Los 43 archivos actualmente contenidos bajo `build/**`.
5. `data/catalogo_global.backup_fase7.json`.
6. `data/catalogo_global.backup_fase8f.json`.
7. `data/cursos_tw_educa.backup_fase8f.json`.
8. `data/imagenes_pendientes.backup-fase8-cierre-20260612-204801.json`.

Total exacto: **448 archivos**, 75,396,073 B.

Condición previa: revisar retención histórica, confirmar que `build/` es reproducible y comprobar que `Cursos a dictar/` no es la única fuente maestra.

## 20. Lista exacta de archivos que podrían eliminarse después de una revisión

Solo se proponen estos 10 artefactos de IDE/caché:

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

Total exacto: **10 archivos**, 51,676 B.

No se propone eliminar todavía ninguno de los 183 archivos no referenciados ni ninguno de los 10 duplicados operativos.

## 21. Recomendaciones para la FASE 02

Orden recomendado:

1. Corregir la generación de `sitemap.xml` para producir XML válido.
2. Resolver las 14 rutas 404: escoger alias canónico, redirección compatible con GitHub Pages o generación de las páginas faltantes; actualizar canonicals y sitemap de forma coordinada.
3. Revisar la ruta con tilde de `assets/js/detalle.js`.
4. Crear una matriz de consumo para los 183 recursos no referenciados, incluyendo herramientas Python, campañas, Open Graph y fuentes maestras.
5. Mover los 448 candidatos a un archivo externo mediante una rama o backup verificable, no borrarlos directamente.
6. Eliminar únicamente los 10 artefactos de IDE/caché tras confirmar el alcance y ampliar `.gitignore`.
7. Unificar las nueve parejas de flyers PNG duplicados y la doble carpeta `data/fuente`/`data/fuentes` solo después de migrar referencias.
8. Optimizar primero PNG grandes y audio duplicado; medir el sitio antes y después.
9. Ejecutar nuevamente validadores, prueba HTTP de las 114 rutas, revisión de consola, enlaces, canonicals, Open Graph y `git diff`.

## 22. Evidencias de comandos y pruebas realizadas

Comandos principales de solo lectura:

```powershell
Get-ChildItem docs/restricciones_codex -File
git status --porcelain=v1 --untracked-files=all
git ls-files
rg --files -uu -g '!.git/**'
Get-ChildItem -Recurse -File
Get-FileHash -Algorithm SHA256
rg -n para href, src, fetch, url(), rutas, terceros y posibles secretos
python -m http.server 8765 --bind 127.0.0.1
python tools/validar_layout_tres_paneles.py
python tools/validar_no_paneles_duplicados.py
python tools/validar_version_assets.py
```

También se indexó el repositorio en un grafo temporal de código, sin persistencia en el proyecto:

- 5,356 nodos.
- 12,535 relaciones.
- 635 archivos de código indexados.
- 344 HTML, 52 JavaScript, 30 Python y 11 CSS detectados por el indexador.

Resultados de validadores:

```text
OK: paginas clave respetan maximo tres paneles y separan paneles locales/globales.
OK: no hay paneles estructurales duplicados ni referencias legacy en HTML publico.
OK: assets CSS/JS locales usan v=20260708-01 sin duplicados por pagina.
```

Validación JSON/XML:

```text
site.webmanifest: VÁLIDO
sitemap.xml: INVÁLIDO — ParseError, línea 1, columna 38
```

Estado Git inicial:

```text
git status --porcelain=v1 --untracked-files=all
(sin salida: árbol limpio)
```

Validación final esperada después de crear este informe:

```text
?? AUDITORIA_REPOSITORIO_FASE_01.md
```

El servidor local debe quedar detenido antes de la entrega. No se ejecutó `git add`, `git commit` ni `git push`.
