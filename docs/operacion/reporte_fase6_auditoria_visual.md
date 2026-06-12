# Reporte fase 6 - auditoria visual

Fecha: 2026-06-12

## Carpetas revisadas

| Carpeta | Estado | Archivos encontrados |
|---|---|---:|
| `assets/img/flyers/` | Existe, ruta legacy/temporal | 9 PNG |
| `assets/img/store/flyers/` | Existe, ruta oficial | 9 PNG, 9 WEBP, `.gitkeep` |
| `assets/img/store/productos/` | Existe | 8 SVG base |
| `assets/img/store/og/` | Existe | `.gitkeep` |
| `assets/img/store/carruseles/` | Existe | `.gitkeep` |
| `assets/img/banners/` | Existe | banners finales WEBP, PNG fuente y assets legacy |

## Rutas esperadas segun manifiesto

`data/imagenes_pendientes.json` define estas rutas esperadas:

- Banners de linea: `assets/img/banners/*.webp`
- Flyers de linea: `assets/img/store/flyers/*-portada.webp`
- Productos/items: `assets/img/store/productos/*.webp`
- OpenGraph: `assets/img/store/og/*-og.webp`
- Carruseles: `assets/img/store/carruseles/*-01.webp`

## Rutas reales encontradas

Los 9 PNG de flyers fueron colocados inicialmente en:

- `assets/img/flyers/tw-store-portada.png`
- `assets/img/flyers/tw-disfruta-portada.png`
- `assets/img/flyers/tw-educa-portada.png`
- `assets/img/flyers/tw-innova-portada.png`
- `assets/img/flyers/tw-salud-portada.png`
- `assets/img/flyers/tw-interactive-portada.png`
- `assets/img/flyers/tw-construye-portada.png`
- `assets/img/flyers/tw-inox-portada.png`
- `assets/img/flyers/tw-investiga-portada.png`

Luego fueron copiados de forma segura a la ruta oficial:

- `assets/img/store/flyers/*.png`

Y convertidos a:

- `assets/img/store/flyers/*.webp`

## Diferencias detectadas

- La ruta real inicial `assets/img/flyers/` no coincide con la ruta esperada del manifiesto.
- La ruta `assets/img/store/flyers/` ya existia, pero solo tenia `.gitkeep`.
- No se borraron los PNG originales en `assets/img/flyers/`.
- No se movieron archivos destructivamente; se copiaron los PNG a la ruta oficial.

## Decision de ruta unica

Ruta oficial para flyers:

`assets/img/store/flyers/`

Justificacion:

- Coincide con `data/imagenes_pendientes.json`.
- Agrupa todos los recursos comerciales de tienda dentro de `assets/img/store/`.
- Evita mezclar piezas finales con carpetas temporales.
- Mantiene una estructura coherente con `productos`, `og` y `carruseles`.

`assets/img/flyers/` queda documentada como carpeta legacy/temporal de origen. Puede limpiarse en una fase posterior si se aprueba, pero no se elimina en esta fase.
