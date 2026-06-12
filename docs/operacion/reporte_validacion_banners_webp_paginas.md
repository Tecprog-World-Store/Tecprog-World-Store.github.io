# Reporte de validacion visual de banners WEBP

Fecha: 2026-06-12

Servidor local usado: `python -m http.server 8000`

## Alcance

Se revisaron las 9 paginas de lineas comerciales en escritorio `1280x720` y movil `390x844`.

## Resultado

| Pagina | Banner esperado | Escritorio | Movil | Consola | Overflow movil |
|---|---|---|---|---|---:|
| `/store/index.html` | `assets/img/banners/tw-store.webp` | OK | OK | Sin errores | 0 |
| `/disfruta/index.html` | `assets/img/banners/tw-disfruta.webp` | OK | OK | Sin errores | 0 |
| `/educa/index.html` | `assets/img/banners/tw-educa.webp` | OK | OK | Sin errores | 0 |
| `/innova/index.html` | `assets/img/banners/tw-innova.webp` | OK | OK | Sin errores | 0 |
| `/salud/index.html` | `assets/img/banners/tw-salud.webp` | OK | OK | Sin errores | 0 |
| `/interactive/index.html` | `assets/img/banners/tw-interactive.webp` | OK | OK | Sin errores | 0 |
| `/construye/index.html` | `assets/img/banners/tw-construye.webp` | OK | OK | Sin errores | 0 |
| `/inox/index.html` | `assets/img/banners/tw-inox.webp` | OK | OK | Sin errores | 0 |
| `/investiga/index.html` | `assets/img/banners/tw-investiga.webp` | OK | OK | Sin errores | 0 |

## Verificaciones realizadas

- La seccion `.commerce-hero` existe en cada pagina.
- El fondo calculado usa el WEBP final correspondiente.
- La metadata `og:image` apunta al WEBP final correspondiente.
- `background-size` queda como `cover`, sin deformar la imagen.
- El titulo `h1` permanece visible y por encima del banner.
- No se detecto overflow horizontal en movil.
- No se detectaron errores de consola durante la navegacion.

## Observaciones

- Los banners usan una capa lineal oscura encima de la imagen para conservar legibilidad del texto HTML.
- `TW Store` tiene un hero mas alto en movil porque su maqueta incluye un panel comercial adicional dentro del primer bloque.
