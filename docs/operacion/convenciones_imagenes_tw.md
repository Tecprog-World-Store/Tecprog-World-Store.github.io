# Convenciones de imágenes Tecprog World

## Banners por línea

- Formato: 1920x640 px.
- Archivo: `.webp`.
- Peso recomendado: 150 KB a 450 KB.
- Zona segura: centro de la imagen.
- Ruta: `assets/img/banners/`.
- Nombres:
  - `tw-store.webp`
  - `tw-disfruta.webp`
  - `tw-educa.webp`
  - `tw-innova.webp`
  - `tw-salud.webp`
  - `tw-interactive.webp`
  - `tw-construye.webp`
  - `tw-inox.webp`
  - `tw-investiga.webp`

Si el banner final no existe, el sitio usa el fallback institucional definido en `data/banners_lineas.json`. Si también faltara el fallback, el frontend debe conservar un degradado CSS.

## Flyers

- Formato: 1080x1920 px.
- Archivo: `.webp`.
- Peso recomendado: 200 KB a 600 KB.
- Zona segura: cuadrado central 1080x1080 px.
- Ruta: `assets/img/store/flyers/`.
- Uso: campañas, redes sociales y productos bandera.

## Imágenes de producto o item

- Formato: 900x900 px o 1200x1200 px.
- Archivo: `.webp`.
- Peso recomendado: 80 KB a 250 KB.
- Ruta: `assets/img/store/productos/`.
- Convención recomendada: `ID.webp`.
- Ejemplo: `assets/img/store/productos/tw-store-001.webp`.

Cuando exista una imagen específica de producto, ejecuta:

```bash
python tools/asociar_imagenes_catalogo.py
```

El script actualiza `data/catalogo_global.json` solo si el archivo existe y crea respaldo.

## OpenGraph

- Formato recomendado: 1200x630 px.
- Ruta: `assets/img/store/og/`.
- Peso recomendado: 100 KB a 350 KB.
- Nombres sugeridos:
  - `tw-store-og.webp`
  - `tw-educa-og.webp`
  - `tw-innova-og.webp`

Si no existe imagen OG específica, usar banner de línea. Si tampoco existe, usar fallback institucional.

## Carruseles

- Formato sugerido: 1600x700 px.
- Archivo: `.webp`.
- Peso recomendado: 120 KB a 400 KB.
- Ruta: `assets/img/store/carruseles/`.

## Reglas de nombres

- Usar minúsculas.
- Usar guiones.
- No usar espacios.
- No usar tildes.
- No usar caracteres especiales.
- Evitar duplicados.

## Reglas legales y comerciales

- No usar imágenes con copyright sin autorización.
- No usar logos de marcas externas sin permiso.
- No prometer stock.
- No prometer garantía sin confirmación.
- No subir archivos pesados si no son necesarios.

## Validación

Ejecutar:

```bash
python tools/validar_imagenes_tw.py
```

El reporte se genera en:

```text
docs/operacion/reporte_imagenes_tw.md
```

## Optimización

Ejecutar:

```bash
python tools/optimizar_imagenes_webp_tw.py
```

La salida se genera en:

```text
build/imagenes_optimizadas/
```

Los originales no se sobrescriben.

