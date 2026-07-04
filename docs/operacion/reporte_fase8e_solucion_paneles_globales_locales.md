# Reporte Fase 8E - Solucion global/local de paneles

Fecha: 2026-07-04

## 1. Causa real confirmada

El riesgo de cinco zonas provenia de dos sistemas de paneles coexistentes:

1. Sistema global:
   - Panel izquierdo/global asociado a `.side-nav`, `.side-nav-left`, `.with-side-nav` y la rehidratacion progresiva de navegacion.
   - Panel derecho/global creado por `renderRightPanel()` en `assets/js/right-panel.js` como `.side-panel-right`.

2. Sistema local comercial:
   - Panel izquierdo `.commerce-nav-panel`.
   - Panel central `.commerce-results`.
   - Panel derecho `.commerce-aside`.
   - Renderizado desde `assets/js/catalogo-global.js`.

En el estado actual de las paginas de linea no existia `.with-side-nav` en el HTML inicial, pero `navigation.js` podia rehidratar contenido progresivo y volver a llamar `renderRightPanel(true)` si el script global estaba disponible. Por eso se implemento una barrera explicita para que ambos sistemas no puedan coexistir.

## 2. Scripts globales involucrados

| Script | Responsabilidad | Estado final |
|---|---|---|
| `assets/js/navigation.js` | Cabecera, navegacion progresiva, WhatsApp flotante, footer/ubicacion y rehidratacion | Respeta `data-disable-global-sidebars="true"` antes de invocar `renderRightPanel(true)` |
| `assets/js/right-panel.js` | Crea `.side-panel-right` dentro de layouts `.with-side-nav` | Abortado en paginas comerciales locales; elimina `.side-panel-right` si encuentra alguno |
| `assets/js/audio-player.js` | Reproductor global | Conservado, no crea columnas |
| `assets/js/main.js` | Utilidades globales | Conservado, no crea columnas |

## 3. Scripts locales involucrados

| Script | Responsabilidad | Estado final |
|---|---|---|
| `assets/js/catalogo-global.js` | Render del catalogo comercial, paneles locales, filtros y resultados | Conservado como unica arquitectura de paneles en lineas |
| `assets/js/store.js` | CTA y comportamiento especifico de Store | Conservado |
| `assets/js/videos-destacados.js` | Videos destacados en paginas donde aplique | No participa en paneles comerciales |

## 4. Estrategia elegida

Se eligio la alternativa valida de menor riesgo:

**Desactivar paneles globales en paginas de linea y conservar el layout local comercial de tres paneles.**

Motivos:

- Las paginas de linea ya estaban migradas a `.commerce-shell`.
- Los filtros, resultados y acciones comerciales ya viven en `catalogo-global.js`.
- Cambiar a paneles globales habria requerido poblar contenido contextual nuevo en `right-panel.js` y mover responsabilidades comerciales ya resueltas.
- El bloqueo por bandera evita montajes accidentales futuros sin depender de rutas.

## 5. Cambios estructurales aplicados

Paginas actualizadas:

- `store/index.html`
- `educa/index.html`
- `innova/index.html`
- `salud/index.html`
- `interactive/index.html`
- `construye/index.html`
- `inox/index.html`
- `investiga/index.html`
- `disfruta/index.html`

Cada pagina ahora declara:

```html
<body data-layout-mode="commercial-local-panels" data-disable-global-sidebars="true">
<main data-commerce-panel-strategy="local" data-disable-global-sidebars="true">
```

`assets/js/right-panel.js` ahora aborta el montaje global si detecta esas banderas:

```js
if (globalSidebarsDisabled()) {
  document.querySelectorAll(".side-panel-right").forEach((panel) => panel.remove());
  return;
}
```

`assets/js/navigation.js` ahora evita la rehidratacion del panel derecho global en paginas comerciales locales.

## 6. Nodos eliminados o bloqueados

| Selector | Resultado |
|---|---|
| `.side-nav` | 0 en lineas |
| `.side-nav-left` | 0 en lineas |
| `.side-panel-right` | Bloqueado y removido si aparece |
| `.right-panel` | 0 en lineas |
| `.commerce-left-panel` | 0 en lineas |
| `.with-side-nav` | 0 en lineas |
| `[data-commerce-featured]` | 0 en lineas |
| `[data-commerce-offers]` | 0 en lineas |
| `.commerce-badge.is-featured` | 0 en tarjetas |

Ademas, en `store/index.html` el bloque informativo `store-hero-panel` dejo de ser `<aside>` y paso a ser `<div>`, para que el conteo real de `aside` refleje solo el panel derecho comercial.

## 7. Nodos conservados

| Selector | Motivo |
|---|---|
| `.commerce-shell` | Grilla comercial unica |
| `.commerce-nav-panel` | Panel izquierdo unico |
| `.commerce-results` | Panel central unico |
| `.commerce-aside` | Panel derecho unico |
| `[data-commerce-results]` | Grilla unica de resultados |
| `[data-commerce-search-main]` | Buscador unico |
| `[data-commerce-controls]` | Toolbar/filtros unicos |
| `.site-nav` | Navegacion principal del header, no panel comercial |
| `.audio-widget` | Audio global, no ocupa columna |
| `.whatsapp-float` | CTA flotante, no ocupa columna |

## 8. Orden de ejecucion

1. HTML inicial carga `styles.css?v=fase8e-20260704`.
2. `assets/js/catalogo-global.js?v=fase8e-20260704` renderiza la arquitectura comercial local dentro de `.commerce-shell`.
3. Scripts especificos como `store.js` o videos ejecutan funcionalidades puntuales.
4. `assets/js/navigation.js?v=fase8e-20260704` rehidrata navegacion global, pero no invoca `renderRightPanel(true)` cuando detecta `data-disable-global-sidebars="true"`.
5. `assets/js/audio-player.js` monta el audio global.
6. `assets/js/main.js` ejecuta utilidades generales.
7. Si `assets/js/right-panel.js` esta disponible, `renderRightPanel()` aborta en paginas comerciales locales.

## 9. Resultado DOM por pagina

| Pagina | `aside` | `.side-nav` | `.side-panel-right` | `.commerce-aside` | `.commerce-left-panel` | `.commerce-shell` | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| Store | 1 | 0 | 0 | 1 | 0 | 1 | OK |
| Educa | 1 | 0 | 0 | 1 | 0 | 1 | OK |
| Innova | 1 | 0 | 0 | 1 | 0 | 1 | OK |
| Salud | 1 | 0 | 0 | 1 | 0 | 1 | OK |
| Interactive | 1 | 0 | 0 | 1 | 0 | 1 | OK |
| Construye | 1 | 0 | 0 | 1 | 0 | 1 | OK |
| Inox | 1 | 0 | 0 | 1 | 0 | 1 | OK |
| Investiga | 1 | 0 | 0 | 1 | 0 | 1 | OK |
| Disfruta | 1 | 0 | 0 | 1 | 0 | 1 | OK |

## 10. Resultado visual por viewport

| Viewport | Resultado |
|---|---|
| 390x844 | Sin overflow horizontal. Panel izquierdo compacto, centro unico y panel derecho local sin duplicados. |
| 768x1024 | Sin overflow horizontal. Misma estructura compacta. |
| 1366x768 | Tres columnas reales: 220px / centro flexible / 240px. |
| 1920x1080 | Tres columnas reales: 220px / centro amplio / 240px. |

## 11. Cache y publicacion

Se actualizo versionado de cache:

- `styles.css?v=fase8e-20260704`
- `catalogo-global.js?v=fase8e-20260704`
- `navigation.js?v=fase8e-20260704`

La validacion local uso URLs con query temporal de auditoria para forzar recarga. No se hizo commit ni push, por lo tanto la verificacion real de GitHub Pages en incognito/hard refresh queda pendiente para despues del despliegue. El sitio queda preparado para esa validacion porque los assets criticos ya tienen nueva querystring.

## 12. Pruebas ejecutadas

- `node --check assets/js/catalogo-global.js`
- `node --check assets/js/navigation.js`
- `node --check assets/js/right-panel.js`
- `node --check assets/js/audio-player.js`
- `node --check assets/js/main.js`
- Validacion JSON:
  - `data/videos_destacados.json`
  - `data/cursos.json`
  - `data/catalogo_global.json`
- HTTP 200 local:
  - 9 paginas de linea
  - `assets/js/catalogo-global.js`
  - `assets/js/navigation.js`
  - `assets/js/right-panel.js`
  - `assets/css/styles.css`
  - `data/catalogo_global.json`

## 13. Riesgos pendientes

- Validacion real en GitHub Pages requiere commit, push y prueba post-deploy en incognito/hard refresh.
- Revision visual humana final recomendada en Store y Educa por ser las paginas con mas tarjetas.

## Conclusion

La solucion no oculta paneles con CSS. Bloquea estructuralmente la creacion de sidebars globales en paginas que declaran paneles locales, conserva una sola grilla comercial y deja tres nodos fisicos reales para la experiencia comercial.

