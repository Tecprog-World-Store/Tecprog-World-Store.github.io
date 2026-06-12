# Reporte de validacion de productos fase 7

Fecha: 2026-06-12

## Resultado

| Item | Archivo | Peso | Dimensiones | Estado |
|---|---|---:|---|---|
| tw-store-001 | `assets/img/store/productos/tw-store-001.webp` | 46.2 KB | 1200x1200 | OK |
| tw-store-008 | `assets/img/store/productos/tw-store-008.webp` | 161.0 KB | 1200x1200 | OK |
| tw-store-010 | `assets/img/store/productos/tw-store-010.webp` | 135.6 KB | 1200x1200 | OK |
| tw-store-014 | `assets/img/store/productos/tw-store-014.webp` | 55.9 KB | 1200x1200 | OK |
| tw-store-015 | `assets/img/store/productos/tw-store-015.webp` | 51.9 KB | 1200x1200 | OK |
| tw-educa-006 | `assets/img/store/productos/tw-educa-006.webp` | 109.3 KB | 1200x1200 | OK |
| tw-educa-007 | `assets/img/store/productos/tw-educa-007.webp` | 209.8 KB | 1200x1200 | OK |
| tw-innova-001 | `assets/img/store/productos/tw-innova-001.webp` | 84.2 KB | 1200x1200 | OK |
| tw-innova-004 | `assets/img/store/productos/tw-innova-004.webp` | 135.8 KB | 1200x1200 | OK |
| tw-salud-001 | `assets/img/store/productos/tw-salud-001.webp` | 100.5 KB | 1200x1200 | OK |
| tw-interactive-002 | `assets/img/store/productos/tw-interactive-002.webp` | 222.4 KB | 1200x1200 | OK |
| tw-construye-001 | `assets/img/store/productos/tw-construye-001.webp` | 143.4 KB | 1200x1200 | OK |
| tw-inox-001 | `assets/img/store/productos/tw-inox-001.webp` | 123.9 KB | 1200x1200 | OK |
| tw-disfruta-001 | `assets/img/store/productos/tw-disfruta-001.webp` | 137.3 KB | 1200x1200 | OK |
| tw-investiga-003 | `assets/img/store/productos/tw-investiga-003.webp` | 180.5 KB | 1200x1200 | OK |

## Validacion general

`python tools/validar_imagenes_tw.py` genero:

- OK: 33
- PENDIENTE: 70

Detalle por manifiesto:

- Banners de linea: 9 optimizado.
- Flyers de linea: 9 optimizado.
- Productos/items: 15 optimizado, 52 pendiente.
- OpenGraph: 9 pendiente.
- Carruseles: 9 pendiente.

## Observaciones

- Algunos WEBP quedaron por debajo de 120 KB aun con `quality=85`; se priorizo calidad visual y peso liviano para GitHub Pages.
- Se actualizo el validador para aceptar dimensiones alternativas declaradas en el manifiesto, por ejemplo `900x900 px o 1200x1200 px`.
- No se ejecuto `tools/asociar_imagenes_catalogo.py` porque asocia imagenes de forma global y podia salir del alcance cerrado de 15 IDs.
