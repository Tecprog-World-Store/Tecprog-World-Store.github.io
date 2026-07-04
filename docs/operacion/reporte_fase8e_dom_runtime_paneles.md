# Reporte Fase 8E - Auditoria runtime DOM de paneles

Fecha: 2026-07-04

## Alcance

Paginas auditadas con `python -m http.server 8000`:

- `store/index.html`
- `educa/index.html`
- `innova/index.html`
- `salud/index.html`
- `interactive/index.html`
- `construye/index.html`
- `inox/index.html`
- `investiga/index.html`
- `disfruta/index.html`

Viewports auditados en navegador:

- 390x844
- 768x1024
- 1366x768
- 1920x1080

## Resultado principal

La doble capa global/local queda bloqueada en runtime con bandera explicita:

- `body[data-layout-mode="commercial-local-panels"]`
- `body[data-disable-global-sidebars="true"]`
- `main[data-commerce-panel-strategy="local"]`
- `main[data-disable-global-sidebars="true"]`

En las 9 paginas se conserva una sola arquitectura comercial:

- Panel izquierdo unico: `.commerce-nav-panel`
- Panel central unico: `.commerce-results`
- Panel derecho unico: `.commerce-aside`

No se detectaron nodos globales duplicados:

- `.side-nav`: 0
- `.side-nav-left`: 0
- `.side-panel-right`: 0
- `.right-panel`: 0
- `.commerce-left-panel`: 0

## Tabla de nodos e inyectores

| Selector / nodo | Archivo / script origen | HTML inicial | Inyectado por JS | Ocupa columna real | Conservar en lineas | Eliminar / bloquear en lineas |
|---|---|---:|---:|---:|---:|---:|
| `.commerce-shell` | HTML de cada linea | Si | No | Si | Si | No |
| `.commerce-nav-panel` | `assets/js/catalogo-global.js` | No | Si | Si, panel izquierdo local | Si | No |
| `.commerce-results` | `assets/js/catalogo-global.js` | No | Si | Si, panel central | Si | No |
| `.commerce-aside` | `assets/js/catalogo-global.js` | No | Si | Si, panel derecho local | Si | No |
| `[data-commerce-results]` | `assets/js/catalogo-global.js` | No | Si | Dentro del centro | Si | No |
| `[data-commerce-featured]` | `assets/js/catalogo-global.js` modo home | No | No en lineas | No | No en lineas | Si |
| `[data-commerce-offers]` | `assets/js/catalogo-global.js` modo home | No | No en lineas | No | No en lineas | Si |
| `.side-nav` | HTML legacy / `ofertas.js` / paginas con `.with-side-nav` | No en lineas | No en lineas | No | No | Si |
| `.side-nav-left` | Navegacion lateral legacy | No en lineas | No en lineas | No | No | Si |
| `.side-panel-right` | `assets/js/right-panel.js` | No | Bloqueado por bandera | No | No | Si |
| `.right-panel` | Legacy / variantes | No | No | No | No | Si |
| `.commerce-left-panel` | Variante anterior del catalogo | No | No | No | No | Si |
| `.with-side-nav` | Layout global legacy | No | No | No | No | Si |
| `.site-nav` | HTML + `assets/js/navigation.js` | Si | Rehidratable | Header, no columna comercial | Si | No |
| `.whatsapp-float` | `assets/js/navigation.js` | No | Si | No, fixed | Si | No |
| `.audio-widget` | `assets/js/audio-player.js` | No | Si | No, fixed | Si | No |
| `header.site-header` | HTML + CSS | Si | No | No, sticky header | Si | No |

## Caso principal: TW Educa

Auditoria runtime sobre `/educa/index.html`:

| Selector | Conteo | Estado |
|---|---:|---|
| `aside` | 1 | Solo `.commerce-aside` |
| `nav` | 2 | `.site-nav` de cabecera + `.commerce-nav-panel` comercial |
| `.side-nav` | 0 | Sin sidebar global izquierdo |
| `.side-panel-right` | 0 | Sin panel derecho global |
| `.commerce-aside` | 1 | Panel derecho local unico |
| `.commerce-left-panel` | 0 | Variante antigua ausente |
| `.commerce-shell` | 1 | Una sola grilla comercial |
| `[data-commerce-results]` | 1 | Una sola grilla de resultados |
| `[data-commerce-featured]` | 0 | Sin bloque destacados |
| `[data-commerce-offers]` | 0 | Sin bloque ofertas |
| `.commerce-badge.is-featured` | 0 | Sin etiqueta visible de destacados |

## Resultado por pagina

Los conteos siguientes fueron consistentes en los 4 viewports probados.

| Pagina | `aside` | `.side-nav` | `.side-panel-right` | `.commerce-aside` | `.commerce-left-panel` | Grillas resultados | Destacados | Ofertas | Overflow X |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Store | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |
| Educa | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |
| Innova | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |
| Salud | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |
| Interactive | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |
| Construye | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |
| Inox | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |
| Investiga | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |
| Disfruta | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | No |

## Resultado por viewport

| Viewport | Columnas CSS reales | Estado visual |
|---|---:|---|
| 390x844 | 2 tracks compactos | Panel izquierdo compacto + centro; panel derecho local se conserva sin overflow |
| 768x1024 | 2 tracks compactos | Panel izquierdo compacto + centro; panel derecho local se conserva sin overflow |
| 1366x768 | 3 tracks | Izquierda 220px, centro flexible, derecha 240px |
| 1920x1080 | 3 tracks | Izquierda 220px, centro amplio, derecha 240px |

## Nodos sticky/fixed detectados

Los nodos `position: fixed` o `position: sticky` detectados no generan columnas adicionales:

- `header.site-header`: cabecera fija/sticky del sitio.
- `a.whatsapp-float`: CTA flotante global.
- `div.audio-widget`: reproductor global.
- En desktop, `.commerce-nav-panel` y `.commerce-aside` pueden ser sticky, pero son los paneles comerciales conservados, no duplicados.

## Conclusion DOM

La correccion es estructural: los scripts globales no montan sidebars en paginas marcadas como layout comercial local. No depende de ocultar paneles duplicados con CSS.

