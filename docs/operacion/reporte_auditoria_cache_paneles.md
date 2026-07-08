# Reporte De Auditoria Cache Paneles

Fecha: 2026-07-08.

## Causa raiz

La causa principal fue versionado inconsistente de assets CSS/JS entre paginas publicas. La auditoria encontro referencias mezcladas a `fase8e-20260704`, `fase8f-20260704`, `fase8g-20260704`, `tres-paneles-20260627`, `videos-20260628`, `img-final-20260628` y tambien referencias sin version.

Con ese estado, un navegador, GitHub Pages o CDN podia servir HTML nuevo con CSS/JS viejo, o HTML viejo con JS/CSS nuevo. Esa mezcla explicaba que aparecieran paneles laterales antiguos o duplicados en primera carga y que F5 corrigiera al forzar revalidacion de recursos.

## Evidencia

- `index.html` usaba `assets/css/styles.css?v=fase8f-20260704` y JS `fase8f`.
- Paginas comerciales como `store/index.html`, `educa/index.html`, `disfruta/index.html`, `innova/index.html`, `salud/index.html`, `interactive/index.html`, `construye/index.html`, `inox/index.html` e `investiga/index.html` usaban `fase8e-20260704`.
- Paginas de cursos usaban `fase8g-20260704` para `styles.css` y `detalle.js`, pero `fase8e-20260704` para `navigation.js`.
- Muchas paginas institucionales y de catalogo cargaban `styles.css`, `navigation.js` y `right-panel.js` sin version.
- No existe `service-worker.js`, `sw.js` ni registro `navigator.serviceWorker`; solo existe `site.webmanifest`.

## Responsables de paneles

- Panel izquierdo global: HTML inicial con `.side-nav` y reorganizacion en `assets/js/right-panel.js`.
- Panel derecho global: `assets/js/right-panel.js`, funcion `renderRightPanel`.
- Paneles locales comerciales: `assets/js/catalogo-global.js`, funciones `leftPanel`, `resultsPanel` y `rightPanel`.
- Paginas comerciales bloquean paneles globales con `data-layout-mode="commercial-local-panels"`, `data-disable-global-sidebars="true"` y `data-commerce-panel-strategy="local"`.

## Diagnostico

- No se encontro service worker ni cache persistente programatico.
- No se detecto carga doble de CSS/JS tras normalizar assets.
- El problema corresponde a cache persistente/CDN mas versionado inconsistente, con riesgo adicional de doble inicializacion JS.
- El F5 corregia porque el navegador revalidaba HTML y/o assets y terminaba usando la combinacion actual.
