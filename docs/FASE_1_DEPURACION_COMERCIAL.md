# Fase 1 de depuración comercial y visual

Fecha: 2026-09-07. Estado: completado localmente. Sin commit ni push.

## Cambios

- Eliminadas las barras secundarias desde HTML y generadores JS; conservado el menú global oscuro y su hamburguesa.
- Raíz presentada como TW Store, con catálogo global inmediato y acceso a las nueve líneas. `/store/index.html` conserva el catálogo y su ruta.
- Hero principal y cabeceras de las nueve líneas compactados; fondos existentes conservados.
- Pagos Perú: QR Yape intacto, cuenta BCP 19105494299095, CCI 00219110549429909559, comprobantes y envíos con Shalom. Números seleccionables para copiar; no se añadió dependencia JS.
- Pagos internacionales: PayPal principal, enlace solicitado por WhatsApp, pagos por hitos y comprobante electrónico separado.
- Eliminadas frases internas detectadas y CTAs repetidos. Tarjetas globales: máximo dos acciones, con Reservar, Solicitar o Consultar disponibilidad según tipo.
- Datos del catálogo, precios, canonicals, sitemap y Open Graph conservados. Versión uniforme de assets conservada: 20260902-01.

## Excepción autorizada

La solicitud explícita de esta fase reemplaza la exigencia anterior de navegación local horizontal contenida en `docs/restricciones_codex/ARQUITECTURA_APROBADA.md` y `CAMBIOS_PROTEGIDOS.md`. Se comunicó antes de editar. Se conserva una sola columna estructural central. El validador de paneles ahora exige ausencia de navegación secundaria en lugar de exigir su generador.

Respaldo de originales: `C:/Users/ACER/.codex/tmp/tw-fase1/backup-20260907-195609`.

## Validación

- Edge/Playwright: raíz, Store, Pagos Perú, Pagos Internacionales, Educa, Salud, Interactive e Innova; escritorio 1440×900 y móvil 390×900.
- 16 revisiones: sin menús secundarios, desbordamiento horizontal, errores JavaScript, respuestas HTTP fallidas ni textos prohibidos comprobados. Menú móvil abre y cierra.
- Inspección de capturas; hero de raíz de aproximadamente 324 px en escritorio, con catálogo visible debajo.
- Búsqueda, estado sin resultados, restauración de resultados y filtro por línea correctos.
- Rutas locales de enlaces/assets de HTML modificados y enlaces renderizados comprobadas, sin destinos inexistentes.
- PayPal, logo oficial y Shalom responden HTTP 200. BCP y CCI comprobados literalmente; QR cargado y archivo original intacto.
- Consola sin errores en las ocho páginas.
- Pasan los tres validadores requeridos y `git diff --check`.
- Evidencias locales: `C:/Users/ACER/.codex/tmp/tw-fase1/` (capturas y browser.json).

Logo obtenido del [centro oficial de PayPal](https://www.paypal.com/pe/webapps/mpp/logo-center); se referencia remotamente el recurso ofrecido por PayPal. Envíos enlazan al [sitio oficial de Shalom](https://shalom.com.pe/).

## Archivos modificados (lista exacta)

- `assets/css/styles.css`
- `assets/js/catalogo-global.js`
- `assets/js/catalogos-lineas.js`
- `assets/js/materiales.js`
- `assets/js/navigation.js`
- `assets/js/store.js`
- `assets/js/videos-destacados.js`
- `catalogo/catalogo-general-tw-educa-pdf.html`
- `catalogo/catalogo-general-tw-educa.html`
- `catalogo/catalogo-mensual.html`
- `catalogo/compendios.html`
- `catalogo/cronograma-anual-tw-educa.html`
- `catalogo/descargas.html`
- `catalogo/guias.html`
- `construye/index.html`
- `detalle/item.html`
- `disfruta/index.html`
- `educa/index.html`
- `empresa/contacto.html`
- `empresa/mapa-del-sitio.html`
- `empresa/nosotros.html`
- `index.html`
- `innova/corvus-ai-v4/index.html`
- `innova/corvus-ai-v4/manual.html`
- `innova/index.html`
- `inox/index.html`
- `interactive/index.html`
- `investiga/index.html`
- `legal/libro-reclamaciones.html`
- `lineas/tw-construye.html`
- `lineas/tw-educa.html`
- `lineas/tw-innova.html`
- `lineas/tw-inox.html`
- `lineas/tw-interactive.html`
- `lineas/tw-investiga.html`
- `lineas/tw-protesis-ortesis.html`
- `lineas/tw-salud-vida.html`
- `lineas/tw-salud.html`
- `lineas/tw-store.html`
- `pagos/internacionales.html`
- `pagos/peru.html`
- `salud/index.html`
- `store/index.html`
- `tools/validar_no_paneles_duplicados.py`
- `docs/FASE_1_DEPURACION_COMERCIAL.md` (nuevo informe)

## Pendiente para fase 2

Investigación y normalización de precios.
