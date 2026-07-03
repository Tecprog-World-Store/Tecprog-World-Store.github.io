# Reporte Fase 8C - Layout comercial de líneas

## Páginas auditadas

- `/store/index.html`
- `/educa/index.html`
- `/innova/index.html`
- `/salud/index.html`
- `/interactive/index.html`
- `/construye/index.html`
- `/inox/index.html`
- `/investiga/index.html`
- `/disfruta/index.html`

## Cambios de layout aplicados

- El catálogo comercial ahora es la primera sección de cada página de línea.
- Se añadieron atributos declarativos `data-layout="comercial-3-paneles"` y `data-catalogo-scope`.
- Los heroes y videos quedaron debajo del catálogo para no desplazar la intención de compra.
- El panel central inicia con título corto, frase breve y buscador principal.

## Cambios CSS aplicados

- `.commerce-card-media` y `.store-card-media` usan `aspect-ratio: 1 / 1`.
- Las imágenes de cards usan `width: 100%`, `height: 100%`, `object-fit: cover` y `object-position: center`.
- Se añadió `.commerce-first-section` para compensar el header fijo.
- Se añadió `.commerce-central-search` para el buscador principal del panel central.

## Cambios JS aplicados

- `assets/js/catalogo-global.js` conserva el layout de tres paneles y agrega buscador central.
- El panel derecho ahora usa textos y enlaces coherentes por línea de negocio.
- La búsqueda central se integra con filtros existentes.
- Se mantuvo compatibilidad con modo Store global y líneas específicas.

## Correcciones UTF-8/mojibake

- Se corrigieron textos visibles dañados en HTML, JS y JSON público afectado durante la fase.
- Se restauraron rutas internas como `catalogo-global.js`, `catalogo/...` y el parámetro `catalogo`.
- Se restauró la clave `fecha_inicio_publica` en los cursos.

## Estado de cards 1:1

Validado en navegador: cards de catálogo con ratio visual `1.00` en TW Educa y en las páginas de línea probadas.

## Pruebas responsive

TW Educa validado en:

| Viewport | Overflow horizontal | Buscador central | Paneles | Ratio card |
|---|---|---|---|---|
| 390x844 | No | Sí | Sí | 1.00 |
| 768x1024 | No | Sí | Sí | 1.00 |
| 1366x768 | No | Sí | Sí | 1.00 |

## Páginas probadas

Se probaron las 9 páginas de línea en `http://localhost:8000/`, además de:

- Detalle producto: `detalle/item.html?id=tw-store-001`
- Detalle curso: `detalle/curso.html?id=tw-educa-curso-08&catalogo=tw-educa-vivo`
- Detalle servicio: `detalle/item.html?id=tw-innova-001`

## Problemas detectados

- El navegador podía mostrar versión cacheada sin querystring; con cache-busting se verificó el orden correcto.
- La terminal de PowerShell puede mostrar mojibake al imprimir UTF-8, aunque los archivos contienen caracteres correctos.

## Siguiente paso recomendado para ventas

Revisar copy comercial de cada panel derecho y priorizar campañas por línea: TW Educa con cronograma, TW Store con disponibilidad y las líneas de servicios con formularios o mensajes de WhatsApp por alcance.
