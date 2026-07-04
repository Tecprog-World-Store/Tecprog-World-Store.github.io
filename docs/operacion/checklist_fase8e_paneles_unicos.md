# Checklist Fase 8E - Paneles unicos

Fecha: 2026-07-04

## Preparacion

- [x] Servidor local levantado con `python -m http.server 8000`.
- [x] Respaldo creado antes de modificar archivos: `backups/fase8e-paneles-global-local-20260704_100444/`.
- [x] Sin commit.
- [x] Sin push.
- [x] UTF-8 conservado.

## Implementacion

- [x] Bandera explicita agregada en `body`.
- [x] Bandera explicita agregada en `main`.
- [x] `right-panel.js` bloquea `.side-panel-right` en paginas comerciales locales.
- [x] `navigation.js` no rehidrata panel derecho global en paginas comerciales locales.
- [x] Store no suma un `<aside>` no comercial.
- [x] Tarjetas sin badge visual de destacados.
- [x] Querystring actualizado a `fase8e-20260704` en CSS/JS criticos.

## DOM obligatorio

- [x] 1 nodo fisico para panel izquierdo: `.commerce-nav-panel`.
- [x] 1 nodo fisico para panel central: `.commerce-results`.
- [x] 1 nodo fisico para panel derecho: `.commerce-aside`.
- [x] 0 `.side-nav`.
- [x] 0 `.side-nav-left`.
- [x] 0 `.side-panel-right`.
- [x] 0 `.right-panel`.
- [x] 0 `.commerce-left-panel`.
- [x] 0 grids destacados en lineas.
- [x] 0 grids ofertas en lineas.
- [x] 1 grid de resultados.
- [x] 1 buscador principal.
- [x] 1 toolbar/filtros.

## Viewports

- [x] 390x844 probado sin overflow horizontal.
- [x] 768x1024 probado sin overflow horizontal.
- [x] 1366x768 probado con tres columnas reales.
- [x] 1920x1080 probado con tres columnas reales.

## Paginas

- [x] Store
- [x] Educa
- [x] Innova
- [x] Salud
- [x] Interactive
- [x] Construye
- [x] Inox
- [x] Investiga
- [x] Disfruta

## Validaciones tecnicas

- [x] `node --check assets/js/catalogo-global.js`
- [x] `node --check assets/js/navigation.js`
- [x] `node --check assets/js/right-panel.js`
- [x] `node --check assets/js/audio-player.js`
- [x] `node --check assets/js/main.js`
- [x] JSON valido: `data/videos_destacados.json`
- [x] JSON valido: `data/cursos.json`
- [x] JSON valido: `data/catalogo_global.json`
- [x] HTTP 200 en paginas y assets criticos.

## Cache y publicacion

- [x] Querystring nueva aplicada localmente.
- [x] Validacion local con query temporal de auditoria.
- [ ] Validacion GitHub Pages incognito pendiente de commit/push.
- [ ] Hard refresh post-deploy pendiente de commit/push.

## Estado final

- [x] Apto para revision visual humana.
- [x] Apto para commit/push cuando el usuario lo autorice.
- [ ] Requiere validacion post-deploy despues de publicar.

