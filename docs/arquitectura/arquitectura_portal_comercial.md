# Arquitectura propuesta del portal comercial

## Principio rector

TW Store debe convertirse en el catálogo global comercial de Tecprog World E.I.R.L. Las líneas de negocio mantienen identidad propia, pero todas las ofertas pagables o cotizables deben poder indexarse en un catálogo común.

## Capas propuestas

### 1. Presentación

- `index.html`: buscador global comercial y destacados.
- `store/index.html`: catálogo global principal.
- `disfruta/index.html`, `educa/index.html`, `innova/index.html`, `salud/index.html`, `interactive/index.html`, `inox/index.html`, `construye/index.html`, `investiga/index.html`: páginas comerciales por línea.
- Páginas existentes en `lineas/` pueden mantenerse como páginas institucionales o redirigirse gradualmente al nuevo layout.

### 2. Datos

Archivos nuevos recomendados:

- `data/lineas_negocio.json`: definición canónica de líneas, slug, prioridad, descripción, página, banner e icono.
- `data/catalogo_global.json`: catálogo común de productos, servicios, cursos, proyectos, videojuegos y merchandising.
- `data/banners_lineas.json`: manifiesto de banners y fallback por línea.

Archivos existentes a migrar o mapear:

- `data/productos_store.json`
- `data/catalogo-tw-innova.json`
- `data/catalogo-tw-salud.json`
- `data/catalogo-tw-interactive.json`
- `data/catalogo-tw-inox.json`
- `data/catalogo-tw-construye.json`
- `data/cursos.json`
- `data/servicios.json`
- `data/software.json`
- `data/productos.json`
- `data/materiales.json`
- `data/compendios.json`

### 3. Lógica frontend

Archivo nuevo recomendado:

- `assets/js/catalogo-global.js`

Responsabilidades:

- Cargar `data/catalogo_global.json`.
- Normalizar texto para búsqueda.
- Buscar por nombre, descripción, categoría, tags y línea.
- Filtrar por línea.
- Filtrar por categoría.
- Filtrar por precio mínimo y máximo.
- Filtrar por moneda.
- Filtrar por estado.
- Ordenar por precio, nombre, destacados y ofertas.
- Renderizar tarjetas comerciales reutilizables.
- Evitar renderizar datos internos aunque existan en JSON.

### 4. Navegación

Actualizar `assets/js/navigation.js` como fuente principal del menú:

1. Inicio
2. TW Store
3. TW Disfruta
4. TW Educa
5. TW Innova
6. TW Salud
7. TW Interactive
8. TW Construye
9. TW Inox
10. TW Investiga
11. Empresa
12. Pagos Perú
13. Pagos Internacionales

### 5. Layout

Usar un layout comercial de tres zonas:

- Filtros a la izquierda.
- Catálogo y resultados en el centro.
- Conversión y confianza a la derecha.

Implementación compatible con lo existente:

- Reutilizar `.page-shell-three-columns`.
- Crear variantes CSS comerciales como `.commerce-shell`, `.commerce-filters`, `.commerce-results`, `.commerce-aside`.
- Mantener `right-panel.js` para páginas institucionales.
- Usar `catalogo-global.js` para páginas comerciales.

## Modelo de datos común

Campos mínimos por item:

```json
{
  "id": "tw-store-001",
  "linea_negocio": "tw-store",
  "categoria": "Celulares",
  "nombre": "Producto o servicio",
  "descripcion_corta": "Resumen comercial",
  "descripcion_larga": "Descripción completa",
  "precio_soles": 0,
  "precio_dolares": null,
  "moneda_principal": "PEN",
  "tipo_item": "producto",
  "estado": "bajo_pedido",
  "tags": ["oferta", "destacado"],
  "imagen": "assets/img/store/placeholders/producto-generico.svg",
  "banner": "assets/img/banners/banner-institucional.webp",
  "url_detalle": "detalle/producto.html?id=tw-store-001",
  "whatsapp_mensaje": "Hola, deseo cotizar...",
  "destacado": true,
  "oferta": true,
  "fecha_actualizacion": "2026-06-11",
  "visible_cliente": true
}
```

Campos internos permitidos solo fuera del render público:

```json
{
  "precio_interno_fuente": 0,
  "margen_interno": 0,
  "fuente_interna": "Proveedor",
  "url_fuente_interna": "https://..."
}
```

## Rutas comerciales recomendadas

- `store/index.html`: catálogo global.
- `disfruta/index.html`: entretenimiento, videojuegos, assets, merchandising.
- `educa/index.html`: cursos, compendios y capacitación.
- `innova/index.html`: software, hardware, automatización y mantenimiento tecnológico.
- `salud/index.html`: tecnología médica, accesibilidad y equipos.
- `interactive/index.html`: consultoría de ingeniería.
- `construye/index.html`: construcción civil.
- `inox/index.html`: metalmecánica.
- `investiga/index.html`: investigación científica y tecnológica.

Las rutas existentes en `lineas/` pueden conservarse para SEO y compatibilidad, pero deben enlazar o converger hacia la experiencia comercial.

## Seguridad comercial

El frontend público debe aplicar una lista blanca de campos visibles. Si un item trae campos internos, simplemente no se renderizan.

Reglas:

- No mostrar fuente interna.
- No mostrar proveedor.
- No mostrar margen.
- No mostrar precio de compra.
- No prometer stock.
- No prometer garantía no confirmada.
- Mostrar siempre aviso de confirmación.

## Implementación aplicada en Fase 2

La arquitectura comercial quedó implementada con una primera versión funcional:

- `data/catalogo_global.json` centraliza items públicos de TW Store y de todas las líneas.
- `assets/js/catalogo-global.js` carga el catálogo, filtra, ordena y renderiza cards comerciales.
- `store/index.html` usa `data-catalog-mode="store"` y muestra filtros, resultados y panel comercial derecho.
- `index.html` usa `data-catalog-mode="home"` para mostrar un buscador global comercial.
- Las páginas por línea usan `data-catalog-line` para limitar resultados a su línea.
- `data/banners_lineas.json` permite aplicar banner específico y fallback por línea.

Comportamiento:

- Home y TW Store buscan en todo el catálogo global.
- Cada página comercial por línea filtra automáticamente por `linea_negocio`.
- Los botones de WhatsApp se generan desde `whatsapp_mensaje`.
- Las cards muestran precio público o `Cotizar` si no hay precio definido.

## Implementación aplicada en Fase 3

Se consolidó la arquitectura con una base de catálogo más robusta:

- El catálogo global contiene 67 items distribuidos en 9 líneas.
- TW Store conserva 15 productos tecnológicos iniciales.
- Las líneas comerciales tienen mínimos iniciales para búsqueda y validación.
- El modo home del catálogo muestra ofertas, destacados y resultados iniciales limitados.
- TW Store muestra el catálogo completo.
- Las páginas por línea muestran únicamente los items de su línea mediante `data-catalog-line`.

La arquitectura queda lista para crecer con:

- Banners finales por línea en formato `webp`.
- Páginas de detalle por item.
- SEO específico por línea.
- Separación futura de datos operativos internos en un backoffice o fuente privada.

## Implementación aplicada en Fase 4

La arquitectura incorpora detalle dinámico y preparación SEO/visual:

- `detalle/item.html` renderiza cualquier item por query string.
- `url_detalle` conecta cards con detalle.
- `data/imagenes_pendientes.json` registra imágenes futuras.
- `data/sitemap_comercial.json` formaliza rutas comerciales.
- `empresa/mapa-del-sitio.html` prioriza rutas comerciales nuevas.
- `docs/operacion/agregar_items_catalogo_global.md` define el flujo de alta de nuevos productos, cursos, servicios y proyectos.

Limitación conocida:

- Los metadatos de `detalle/item.html` se actualizan en cliente. Para SEO completo por item se recomienda una fase posterior de generación estática por item.

## Implementación aplicada en Fase 5

La arquitectura visual queda preparada para producción:

- Carpetas finales para banners, flyers, OG, carruseles, productos y líneas.
- `data/imagenes_pendientes.json` actúa como cola de producción visual.
- `tools/validar_imagenes_tw.py` genera control de calidad visual.
- `tools/optimizar_imagenes_webp_tw.py` permite salida optimizada en `build/imagenes_optimizadas/`.
- `tools/asociar_imagenes_catalogo.py` conecta imágenes específicas `ID.webp` con el catálogo.

El sitio sigue funcionando aunque falten imágenes finales porque conserva placeholders y fallbacks.
