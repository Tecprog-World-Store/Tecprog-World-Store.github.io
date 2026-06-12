# Reporte Fase 4 - Detalle, SEO y preparación visual

Fecha: 2026-06-12

## Qué se creó

- `detalle/item.html`: página dinámica estática para renderizar cualquier item de `data/catalogo_global.json`.
- `data/imagenes_pendientes.json`: manifiesto de banners, flyers e imágenes de productos pendientes.
- `data/visual/prompts_banners_lineas_tw.md`: prompts base para banners horizontales por línea.
- `data/visual/prompts_flyers_productos_tw.md`: prompts base para flyers verticales por tipo de oferta.
- `data/sitemap_comercial.json`: sitemap comercial estructurado.
- `docs/operacion/agregar_items_catalogo_global.md`: flujo operativo para agregar nuevos items.

## Qué se modificó

- `data/catalogo_global.json`: cada item ahora tiene `url_detalle` con la forma `detalle/item.html?id=ID`.
- `index.html`, `store/index.html` y páginas comerciales por línea: metadatos SEO/Open Graph básicos.
- `empresa/mapa-del-sitio.html`: mapa actualizado con rutas comerciales nuevas y rutas anteriores preservadas.
- `assets/css/styles.css`: estilos para página de detalle.
- Documentación de arquitectura, decisiones, diagnóstico UX y checklist.

## Cómo funciona `detalle/item.html`

La página recibe un parámetro:

```text
detalle/item.html?id=tw-store-001
```

Luego carga `../data/catalogo_global.json`, busca el item por `id`, verifica `visible_cliente` y renderiza únicamente datos públicos. Si falta el ID o no existe, muestra un mensaje amable y enlaces de regreso.

## Cómo se enlazan las cards

Cada item del catálogo tiene:

```json
"url_detalle": "detalle/item.html?id=tw-store-001"
```

`assets/js/catalogo-global.js` resuelve rutas relativas desde home, TW Store y páginas por línea.

## Datos internos

La página de detalle no renderiza precio fuente, margen, proveedor, URL fuente, costo interno ni campos de scraping.

## SEO básico

Se agregaron o normalizaron `title`, `meta description`, `og:title`, `og:description`, `og:type`, `og:image`, `og:url` y `twitter:card`.

## Pendiente para imágenes finales

No se generaron imágenes en esta fase. Quedan pendientes banners `.webp` por línea, flyers verticales, imágenes específicas por item y optimización WebP.

## Pendiente para SEO avanzado

Los metadatos de `detalle/item.html` se actualizan en cliente. Para SEO completo por item se recomienda generar páginas HTML estáticas por item, además de `sitemap.xml`, `robots.txt` y JSON-LD.

