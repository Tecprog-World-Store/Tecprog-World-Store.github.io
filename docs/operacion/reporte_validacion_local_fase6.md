# Reporte de validacion local fase 6

Fecha: 2026-06-12

Servidor local: `python -m http.server 8000`

## Paginas probadas

| Pagina | Estado | Consola | Overflow movil | Banner |
|---|---|---|---:|---|
| `/index.html` | OK | Sin errores | 0 | OK |
| `/store/index.html` | OK | Sin errores | 0 | `tw-store.webp` |
| `/disfruta/index.html` | OK | Sin errores | 0 | `tw-disfruta.webp` |
| `/educa/index.html` | OK | Sin errores | 0 | `tw-educa.webp` |
| `/innova/index.html` | OK | Sin errores | 0 | `tw-innova.webp` |
| `/salud/index.html` | OK | Sin errores | 0 | `tw-salud.webp` |
| `/interactive/index.html` | OK | Sin errores | 0 | `tw-interactive.webp` |
| `/construye/index.html` | OK | Sin errores | 0 | `tw-construye.webp` |
| `/inox/index.html` | OK | Sin errores | 0 | `tw-inox.webp` |
| `/investiga/index.html` | OK | Sin errores | 0 | `tw-investiga.webp` |
| `/detalle/item.html?id=tw-store-001` | OK | Sin errores | 0 | fallback institucional |

## Rutas de imagen

- Referencias actuales de `data/catalogo_global.json`: 0 rutas locales faltantes.
- Rutas esperadas aun pendientes en `data/imagenes_pendientes.json`: 85.
  - Productos/items: 67.
  - OpenGraph: 9.
  - Carruseles: 9.

## Observaciones

- Los flyers WEBP no estan integrados como contenido visible en las paginas; por tanto no alteran el layout actual.
- Los banners finales siguen funcionando en las paginas de linea.
- No se detecto overflow horizontal en movil.
- No se detectaron errores de consola durante la navegacion.
- No se detectaron textos internos sensibles mediante revision automatica basica.
