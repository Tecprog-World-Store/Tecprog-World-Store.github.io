# Fase 8D - Auditoria de paneles duplicados

Fecha: 2026-07-04

## Origen de los cinco paneles aparentes

La revision encontro que las paginas de linea cargaban un unico contenedor HTML (`.commerce-shell`), pero `assets/js/catalogo-global.js` lo expandia en tres zonas internas:

- `.commerce-filters commerce-left-panel`: panel izquierdo con buscador, filtros, cotizacion y aviso comercial.
- `.commerce-results`: panel central con buscador principal, contador, bloque de destacados y bloque de resultados.
- `.commerce-aside`: panel derecho con recursos de la linea y confianza comercial.

Ademas, el sistema global de navegacion del sitio ya tiene patrones para panel izquierdo institucional (`.side-nav`, `.side-nav-left`) y panel derecho general (`.side-panel-right`) en paginas con `with-side-nav`. Aunque las paginas de linea no usaban directamente `with-side-nav`, la suma visual de filtros laterales, catalogo central y panel derecho especifico generaba una experiencia comparable a cinco columnas: navegacion institucional, filtros, resultados, recursos globales y recursos de linea.

## Que se conserva

- Se conserva un unico panel izquierdo, ahora dedicado a navegacion comercial contextual.
- Se conserva un unico panel central, con titulo, descripcion, buscador, filtros, contador y una sola grilla.
- Se conserva un unico panel derecho, fusionando acciones comerciales, recursos de linea, pagos y confianza.
- Se conservan cards 1:1, imagenes, precios, fechas, rutas, datos comerciales y metadatos SEO.

## Que se elimina

- Se elimina el segundo panel izquierdo de filtros.
- Se elimina el render de bloques duplicados de destacados/ofertas en paginas de linea y store.
- Se elimina el segundo buscador en filtros.
- Se eliminan espacios sobrantes entre `Destacados` y `Resultados` al dejar una sola grilla.

## Que se fusiona

- WhatsApp, correo, copiar enlace, compartir pagina, cotizar, recursos de linea, pagos y confianza comercial se agrupan en una sola instancia de `.commerce-aside`.
- En TW Educa se priorizan WhatsApp, correo, cronograma publico, guias, cursos, pagos y confianza comercial mediante `LINE_PANEL_COPY["tw-educa"]`.

## Riesgos de regresion

- El modo `home` de `catalogo-global.js` conserva bloques de ofertas/destacados porque la home puede depender de esa seleccion editorial.
- El orden `destacados` se mantiene como valor interno de sort para no romper datos existentes, aunque su etiqueta visible se cambio a prioridad comercial.
- Las paginas con `with-side-nav` fuera del alcance pueden seguir usando `right-panel.js`; esta fase se concentra en las paginas de linea indicadas.
- Si se agregan nuevos filtros en el futuro, deben integrarse en `.commerce-toolbar` del panel central, no como sidebar adicional.
