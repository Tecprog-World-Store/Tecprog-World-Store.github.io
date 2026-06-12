# Auditoría técnica del sitio web

Fecha de auditoría: 2026-06-11  
Repositorio: `C:\Users\ACER\Documents\GitHub\Tecprog-World-Store.github.io`

## Resumen ejecutivo

El sitio ya tiene una base estática amplia y funcional: 81 páginas HTML, 31 archivos JSON, 11 scripts JavaScript, un CSS global, catálogos por línea, assets gráficos, PDFs, scripts operativos y una auditoría previa en `_auditoria_codex/`. La arquitectura actual combina páginas institucionales, catálogos educativos, páginas de líneas de negocio y TW Store.

El principal riesgo comercial detectado está en TW Store: la tarjeta pública renderizada por `assets/js/store.js` muestra datos internos o de abastecimiento como `Precio fuente` y `Margen sugerido`. Esto debe corregirse antes de escalar la tienda como catálogo comercial principal.

El segundo riesgo es de consistencia UX: la mayoría de páginas de línea usa `main.with-side-nav` y `assets/js/right-panel.js` para formar un layout de tres columnas, mientras que `store/index.html` usa `main.store-page` con un layout comercial independiente de una sola columna.

El tercer riesgo es de codificación: todos los HTML revisados incluyen `<meta charset="UTF-8">` y viewport responsive, pero el contenido ya contiene caracteres corruptos, por ejemplo `TecnologÃ­a`, `PerÃº`, `cotizaciÃ³n`, `Â¿`. Esto indica mojibake en datos o archivos fuente, no ausencia de meta tags.

## Estructura de carpetas observada

- `.git/`: control de versiones.
- `.idea/`: configuración local de IDE.
- `assets/`: CSS, JS, imágenes, iconos y PDFs publicados.
- `build/`: flyers HTML generados para TW Store.
- `catalogo/`: páginas de catálogo por cursos, materiales y líneas.
- `data/`: JSON y documentos operativos/comerciales.
- `detalle/`: páginas de detalle genéricas.
- `docs/`: documentación técnica y lineamientos existentes.
- `empresa/`: páginas institucionales.
- `herramientas/`: calculadora de precios.
- `legal/`: páginas legales.
- `lineas/`: páginas de unidades de negocio.
- `pagos/`: páginas de pagos Perú e internacionales.
- `scripts/`: scripts de generación, revisión y mantenimiento.
- `servicios/`: páginas de servicios especializados.
- `store/`: TW Store.
- `temario_cursos/`: contenidos de cursos.
- `tools/`: utilidades para convertir y revisar catálogos.
- `_auditoria_codex/`: auditoría previa generada.

## Páginas HTML principales

- Home: `index.html`.
- TW Store: `store/index.html`.
- Líneas existentes: `lineas/tw-educa.html`, `lineas/tw-innova.html`, `lineas/tw-salud.html`, `lineas/tw-interactive.html`, `lineas/tw-construye.html`, `lineas/tw-inox.html`, `lineas/tw-investiga.html`, más alias históricos `tw-protesis-ortesis`, `tw-salud-vida`, `tw-taller`, `tw-store`.
- Catálogos por línea: `catalogo/tw-salud.html`, `catalogo/tw-interactive.html`, `catalogo/tw-inox.html`, `catalogo/tw-innova.html`, `catalogo/tw-construye.html`.
- Educación: `catalogo/catalogo-general-tw-educa.html`, `catalogo/catalogo-general-tw-educa-pdf.html`, `catalogo/cursos-junio-2026.html`, `catalogo/cursos.html`, `catalogo/compendios.html`, `catalogo/guias.html`, `catalogo/descargas.html`.
- Empresa: `empresa/nosotros.html`, `empresa/contacto.html`, `empresa/mapa-del-sitio.html`.
- Legal: `legal/terminos-condiciones.html`, `legal/politicas-privacidad.html`, `legal/politicas-pagos-reembolsos.html`, `legal/libro-reclamaciones.html`.
- Pagos: `pagos/peru.html`, `pagos/internacionales.html`.

## CSS, JS, JSON, imágenes, banners y scripts

### CSS

- `assets/css/styles.css` es el CSS global. Contiene variables de marca, header, navegación, layout de tres columnas, paneles laterales, cards, catálogos, store, footer y media queries.

### JavaScript

- `assets/js/navigation.js`: datos oficiales, navegación superior estándar, WhatsApp flotante, footer institucional, helpers de rutas y PayPal.
- `assets/js/right-panel.js`: transforma páginas `with-side-nav` en layout de tres columnas con navegación izquierda, contenido central y panel derecho.
- `assets/js/main.js`: renderizado de carruseles, líneas de negocio y comportamiento general.
- `assets/js/store.js`: carga `data/productos_store.json`, filtra TW Store y renderiza tarjetas. Actualmente expone datos internos.
- `assets/js/catalogos-lineas.js`: renderiza catálogos por línea con filtros por categoría, tipo, madurez y prioridad.
- Otros scripts: detalle, guías, materiales, compendios, oferta-detalle, catálogo general de cursos.

### JSON y datos

- `data/lineas.json`: contiene 7 líneas; no incluye aún TW Store ni TW Disfruta en el modelo pedido.
- `data/productos_store.json`: catálogo tecnológico de TW Store; contiene precio fuente, precios por margen, fuente y URL fuente.
- `data/catalogo-tw-*.json`: catálogos por línea para Salud, Innova, Interactive, Inox y Construye.
- `data/home-destacados.json`: referencias de destacados por sección.
- `data/productos.json`, `data/servicios.json`, `data/software.json`, `data/cursos.json`, `data/materiales.json`, `data/compendios.json`, `data/guias.json`: datos por tipo de oferta.
- No existe aún `data/catalogo_global.json`.
- No existe aún `data/lineas_negocio.json`.
- No existe aún `data/banners_lineas.json`.

### Imágenes y banners

- Existen banners por varias líneas: `assets/img/banners/tw-educa/`, `tw-innova/`, `tw-salud/`, `tw-interactive/`, `tw-construye/`, `tw-inox/`, `tw-investiga/`.
- No se detectó banner dedicado para `tw-store` ni `tw-disfruta`.
- Existen placeholders de tienda en `assets/img/store/placeholders/`.

### Scripts operativos

- `scripts/revisar_utf8.py` y `scripts/revisar_utf8.bat`.
- Generadores de catálogos LaTeX/HTML.
- `tools/convertir_catalogo_txt_a_json.py`, `tools/revisar_catalogo_fuentes.py`, `tools/generar_flyers_html_tw_store.py`.

## Navegación superior

La navegación se centraliza en `assets/js/navigation.js` mediante `renderStandardTopNav()`, que sobrescribe el contenido de cada `.site-nav` salvo que tenga `data-skip-standard-nav="true"`.

Orden actual renderizado:

1. Inicio
2. Empresa
3. TW Investiga
4. TW Innova
5. TW Educa
6. TW Interactive
7. TW Construye
8. TW Inox
9. TW Salud
10. TW Store
11. Pagos Peru
12. Pagos Internacionales

Orden solicitado:

1. Inicio
2. TW Store
3. TW Disfruta
4. TW Educa
5. TW Innova
6. TW Salud
7. TW Interactive
8. TW Construye
9. TW Inox
10. TW Investiga
11. Empresa
12. Pagos Perú
13. Pagos Internacionales

Diagnóstico: conviene actualizar principalmente `assets/js/navigation.js`. Las páginas que tienen navegación inicial duplicada pueden mantenerse como fallback, pero en una segunda fase se recomienda normalizar headers para reducir duplicación.

## Duplicación detectada

- Headers y marcas se repiten en HTML, aunque el nav se sobrescribe por JS.
- Páginas de línea repiten estructura de `main.with-side-nav`, hero, secciones y CTA.
- Catálogos por línea usan un renderizador común parcial en `assets/js/catalogos-lineas.js`, pero no cubren todas las líneas.
- TW Store usa `assets/js/store.js`, distinto del renderizador de catálogos por línea.
- Hay duplicidad conceptual entre `data/lineas.json`, páginas `lineas/`, catálogos `catalogo/` y archivos `data/catalogo-tw-*.json`.

## Patrón de tres paneles

El patrón existe mediante:

- CSS: `.page-shell-three-columns` con columnas `230px minmax(0, 1fr) 280px`.
- CSS: `.side-nav-left`, `.side-panel-right`, `.page-main`.
- JS: `assets/js/right-panel.js`, que toma páginas con `main.with-side-nav` y las envuelve en `.page-shell.page-shell-three-columns`.

Páginas de línea como `lineas/tw-innova.html` y `lineas/tw-educa.html` usan `main.with-side-nav`, por lo que reciben el patrón de tres columnas. `store/index.html` usa `main.store-page`, por lo que no recibe panel izquierdo ni panel derecho.

## Comparación con TW Store

TW Store tiene un layout comercial más directo:

- Hero propio `store-hero`.
- Panel informativo dentro del hero.
- Toolbar de búsqueda y filtros por categoría.
- Grid de productos.
- Aviso comercial y pasos de compra.

Ventaja: es más enfocado a conversión que las páginas institucionales.

Problema: rompe la consistencia visual respecto a las páginas que usan tres columnas y no aprovecha el panel derecho para acciones rápidas, recursos y pagos.

## Problemas responsive

- El CSS tiene media queries para navegación móvil y colapso de tres columnas.
- La navegación superior puede saturarse en desktop por cantidad de enlaces; el orden pedido agrega TW Disfruta y mantiene 13 enlaces.
- `.site-nav.is-static` fuerza display flex en móvil; debe revisarse al actualizar el menú.
- `filter-panel` usa cinco columnas en desktop y debe validarse en móvil para nuevas búsquedas globales.
- Las tarjetas de Store tienen media queries específicas; deben mantenerse al migrar a un catálogo global.

## UTF-8 y caracteres

Todos los HTML revisados tienen `<meta charset="UTF-8">` y viewport responsive.

Problemas observados:

- `index.html`: `TecnologÃ­a`, `PerÃº`, `LÃ­neas`, `cotizaciÃ³n`, `prÃ³tesis`, `tÃ©cnica`.
- `store/index.html`: `TecnologÃ­a`, `CatÃ¡logo`, `cotizaciÃ³n`, `garantÃ­a`, `envÃ­o`.
- `data/productos_store.json`: nombres y ganchos con `cÃ¡mara`, `creaciÃ³n`, `econÃ³mico`.
- `assets/js/store.js`: mensajes con `Â¿`, `confirmaciÃ³n`, `garantÃ­a`.
- `assets/js/catalogos-lineas.js`: `diseÃ±o`, `tÃ©cnico`, `investigaciÃ³n`.

Conclusión: la corrección debe hacerse sobre contenido y datos, no solo sobre metatags.

## Datos internos visibles al cliente

Riesgo confirmado en `assets/js/store.js`:

- Renderiza `Precio fuente`.
- Renderiza `Precio TW Store`.
- Renderiza `Margen sugerido`.
- Incluye `product.fuente` dentro del texto buscable.

Datos internos existen en `data/productos_store.json`:

- `precio_fuente`
- `precio_tw_8`
- `precio_tw_12`
- `precio_tw_18`
- `fuente`
- `url_fuente`

Recomendación: mantener esos datos solo para operación interna si son necesarios, pero cambiar el render público a `precio_publico_soles`, `precio_publico_dolares`, `precio_anterior`, `precio_oferta`, `estado`, `visible_cliente` y mensajes de cotización.

## Hallazgos prioritarios

1. P0 comercial: TW Store muestra precio fuente y margen sugerido al cliente.
2. P1 UX: TW Store no comparte el patrón de tres columnas ni el futuro layout comercial global.
3. P1 arquitectura: no existe catálogo global común para productos, servicios, cursos, proyectos y merchandising.
4. P1 navegación: orden del menú no prioriza venta y falta TW Disfruta.
5. P2 datos: `data/lineas.json` no refleja las nueve líneas comerciales solicitadas.
6. P2 contenido: mojibake extendido en HTML, JS y JSON.
7. P2 banners: no existe manifiesto central de banners por línea.
8. P3 mantenimiento: headers y estructuras se repiten en múltiples HTML.

