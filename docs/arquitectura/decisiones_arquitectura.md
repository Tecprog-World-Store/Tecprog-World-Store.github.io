# Decisiones de arquitectura

## ADR-001: TW Store como catálogo global comercial

Estado: propuesta para aplicar en fase 2.

Decisión: TW Store debe funcionar como e-commerce principal o catálogo global de todas las líneas de negocio, no solo como tienda tecnológica.

Motivo: el usuario necesita que cualquier producto, servicio, curso, proyecto, videojuego, contenido digital o merchandising pagable/cotizable pueda buscarse desde TW Store.

Impacto:

- Crear `data/catalogo_global.json`.
- Crear `assets/js/catalogo-global.js`.
- Migrar o mapear los catálogos existentes al modelo común.
- Mantener `data/productos_store.json` como fuente operativa temporal hasta normalizar.

## ADR-002: Layout comercial de tres zonas en lugar de copiar el patrón institucional

Estado: propuesta recomendada.

Decisión: no adaptar TW Store de forma literal al patrón institucional actual. En su lugar, crear un layout comercial superior para TW Store y todas las líneas.

Justificación:

- El patrón existente de tres columnas es útil, pero está orientado a navegación contextual y recursos institucionales.
- TW Store necesita conversión: búsqueda, filtros, ofertas, destacados y WhatsApp.
- Un layout comercial de tres zonas mantiene consistencia visual y mejora ventas.

Aplicación propuesta:

- Izquierda: filtros comerciales.
- Centro: buscador, banners, ofertas, destacados y catálogo.
- Derecha: WhatsApp, pagos, disponibilidad, garantías sujetas a confirmación y accesos rápidos.

## ADR-003: Navegación priorizada por venta

Estado: pendiente de implementación.

Decisión: reordenar menú superior para poner TW Store y líneas comerciales antes de Empresa y Pagos.

Orden:

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

Implementación recomendada: modificar `assets/js/navigation.js` como fuente central.

## ADR-004: Separación entre datos públicos e internos

Estado: urgente.

Decisión: el frontend público debe renderizar solo campos comerciales públicos.

Campos públicos:

- `precio_publico_soles`
- `precio_publico_dolares`
- `precio_soles`
- `precio_dolares`
- `precio_anterior`
- `precio_oferta`
- `estado`
- `garantia_texto`
- `disponibilidad_texto`
- `whatsapp_mensaje`

Campos internos:

- `precio_fuente`
- `precio_interno_fuente`
- `precio_proveedor`
- `precio_compra`
- `margen_sugerido`
- `margen_interno`
- `fuente`
- `url_fuente`

Regla: los campos internos pueden existir para operación, pero no deben llegar a la tarjeta pública.

## ADR-005: UTF-8 real y corrección de mojibake

Estado: pendiente de implementación.

Decisión: mantener `<meta charset="UTF-8">` y corregir el contenido corrupto en HTML, JS y JSON.

Motivo: los meta tags existen, por lo que el problema está en cadenas guardadas con mojibake.

Implementación recomendada:

- Corregir primero archivos públicos: `index.html`, `store/index.html`, `assets/js/store.js`, `assets/js/catalogos-lineas.js`, `data/productos_store.json`.
- Luego revisar todo el sitio con `scripts/revisar_utf8.py`.
- Evitar conversiones masivas sin diff revisable.

## ADR-006: Banners por manifiesto

Estado: pendiente de implementación.

Decisión: crear `data/banners_lineas.json` como fuente de banners por línea.

Motivo: permite que home, store y páginas de línea lean banners de forma consistente sin hardcodear rutas.

Regla: si no existe banner específico, usar fallback institucional.

## ADR-007: Compatibilidad de rutas

Estado: propuesta.

Decisión: no borrar páginas existentes. Crear nuevas rutas comerciales por carpeta cuando falten y conservar rutas `lineas/` como compatibilidad o contenido institucional.

Motivo: evita romper enlaces existentes, PDFs, redes sociales o indexación.

## Registro de implementación Fase 2

Fecha: 2026-06-12.

Cambios aplicados:

- Se creó `data/lineas_negocio.json` como modelo canónico de nueve líneas comerciales.
- Se creó `data/catalogo_global.json` como catálogo público común para TW Store, cursos, servicios, consultorías, proyectos y entretenimiento.
- Se creó `data/banners_lineas.json` con rutas específicas y fallback institucional.
- Se creó `assets/js/catalogo-global.js` como motor reusable de búsqueda, filtros, ordenamiento y tarjetas comerciales.
- Se actualizó `assets/js/navigation.js` con el nuevo orden comercial del menú.
- Se actualizó `store/index.html` para operar como catálogo global principal con tres zonas comerciales.
- Se actualizó `index.html` para incluir buscador comercial global en la parte superior del flujo.
- Se crearon rutas comerciales por carpeta para `disfruta`, `educa`, `innova`, `salud`, `interactive`, `construye`, `inox` e `investiga`.

Separación público/interno:

- El catálogo global solo usa campos comerciales públicos.
- El render público no lee ni imprime `precio_fuente`, `margen_sugerido`, `fuente`, `url_fuente`, proveedor ni costo interno.
- `data/productos_store.json` puede conservar datos operativos, pero TW Store ya no lo renderiza directamente.

## Registro de implementación Fase 3

Fecha: 2026-06-12.

Cambios aplicados:

- Se validó la base comercial creada en Fase 2.
- Se amplió `data/catalogo_global.json` a 67 items públicos.
- Se corrigió el indicador de home a 9 líneas comerciales.
- Se ajustó el modo home del catálogo para mostrar ofertas, destacados y una grilla inicial limitada.
- Se mejoró el CSS del header para reducir saturación del menú en desktop y conservar hamburguesa en móvil.
- Se agregó `banner_esperado` en `data/banners_lineas.json` para preparar banners finales.
- Se creó `docs/arquitectura/reporte_fase3_validacion.md`.
- Se creó `docs/arquitectura/checklist_portal_comercial.md`.

Decisión adicional:

- La home no debe renderizar todo el catálogo como primera impresión. En estado inicial muestra una selección de resultados, ofertas y destacados; al buscar o filtrar, muestra el resultado completo correspondiente.

## Registro de implementación Fase 4

Fecha: 2026-06-12.

Cambios aplicados:

- Se creó `detalle/item.html` como página dinámica estática para cualquier item del catálogo global.
- Se normalizó `url_detalle` en los 67 items de `data/catalogo_global.json`.
- Se agregaron metadatos SEO/Open Graph básicos en home, TW Store y páginas comerciales por línea.
- Se creó `data/imagenes_pendientes.json`.
- Se crearon prompts base para banners y flyers.
- Se creó `data/sitemap_comercial.json`.
- Se actualizó `empresa/mapa-del-sitio.html` con rutas comerciales.
- Se documentó el flujo de operación en `docs/operacion/agregar_items_catalogo_global.md`.

Decisión:

- Para compatibilidad con GitHub Pages se mantiene una sola página dinámica por query string. Para SEO avanzado futuro, conviene generar páginas HTML estáticas por item.

## Registro de implementación Fase 5

Fecha: 2026-06-12.

Cambios aplicados:

- Se creó estructura final para banners, flyers, productos, OG, carruseles y líneas.
- Se normalizó `data/imagenes_pendientes.json`.
- Se creó `tools/validar_imagenes_tw.py`.
- Se creó `tools/optimizar_imagenes_webp_tw.py`.
- Se creó `tools/asociar_imagenes_catalogo.py`.
- Se documentaron convenciones y flujo de producción visual.
- Se generaron reportes iniciales de validación y optimización.

Decisión:

- Las imágenes finales no se generan ni descargan desde Codex. El repositorio queda preparado para recibir imágenes externas autorizadas, convertirlas/optimizarles localmente y asociarlas al catálogo de forma controlada.
