# Reporte Fase 3 - Validación y pulido del portal comercial

Fecha: 2026-06-12  
Entorno probado: `http://localhost:8000/`

## Archivos revisados

- `index.html`
- `store/index.html`
- `assets/js/navigation.js`
- `assets/js/catalogo-global.js`
- `assets/js/store.js`
- `assets/css/styles.css`
- `data/lineas_negocio.json`
- `data/catalogo_global.json`
- `data/banners_lineas.json`
- `disfruta/index.html`
- `educa/index.html`
- `innova/index.html`
- `salud/index.html`
- `interactive/index.html`
- `construye/index.html`
- `inox/index.html`
- `investiga/index.html`

## Validación de datos

- `data/catalogo_global.json` es JSON válido.
- `data/lineas_negocio.json` es JSON válido.
- `data/banners_lineas.json` es JSON válido.
- El catálogo global quedó con 67 items públicos:
  - TW Store: 15
  - TW Disfruta: 6
  - TW Educa: 8
  - TW Innova: 8
  - TW Salud: 6
  - TW Interactive: 6
  - TW Construye: 6
  - TW Inox: 6
  - TW Investiga: 6

## Errores encontrados

- La home aún mostraba `7 líneas de negocio`; se corrigió a `9`.
- El catálogo global inicial tenía pocos items fuera de TW Store; se expandió por línea.
- La home no destacaba ofertas y destacados dentro del buscador global; se agregó esa estructura.
- El manifiesto de banners no indicaba nombres esperados para banners finales; se agregó `banner_esperado`.

## Problemas responsive

- El menú superior tiene muchos enlaces. Se ajustó el CSS para reducir espacio del brand, permitir `flex-wrap` controlado en desktop y conservar hamburguesa en móvil.
- En viewport móvil `390x844`, TW Store no presentó overflow horizontal.
- El layout comercial colapsa a una sola columna en móvil.

## Problemas visuales

- La home podía sentirse demasiado extensa al renderizar todo el catálogo inicial. Se limitó la grilla inicial del modo home a 12 resultados cuando no hay filtros activos.
- Se mantuvieron ofertas y destacados como secciones visibles para reforzar conversión.

## Problemas de navegación

- El orden del menú se verificó como:
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

## Accesibilidad básica

- Las páginas nuevas incluyen `lang="es"`, `meta charset="UTF-8"` y viewport.
- El botón hamburguesa incluye texto `sr-only`.
- Las imágenes de cards se renderizan con `alt` basado en el nombre del item.
- Los CTAs son enlaces reales a WhatsApp o detalle.

## Tarjetas públicas

No se detectaron en vistas públicas:

- Precio fuente
- Margen sugerido
- Precio proveedor
- Proveedor
- URL fuente
- Costo interno
- `precio_fuente`
- `margen_sugerido`
- `url_fuente`

Campos visibles confirmados:

- Imagen o placeholder.
- Nombre.
- Línea de negocio.
- Categoría.
- Descripción corta.
- Precio público o `Cotizar`.
- Estado.
- Etiquetas oferta/destacado.
- Botón `Cotizar por WhatsApp`.
- Botón `Ver detalle` cuando existe URL.
- Aviso de confirmación.

## Pruebas realizadas

- Home: `http://localhost:8000/index.html`
- TW Store: `http://localhost:8000/store/index.html`
- Línea Innova: `http://localhost:8000/innova/index.html`
- Responsive móvil: `390x844`
- Consola del navegador: sin warnings ni errores.

Resultados de búsqueda en home:

- `Excel`: 3 resultados de TW Educa.
- `seguridad`: incluye cámaras de seguridad y servicios relacionados.
- `videojuego`: 4 resultados de TW Disfruta.
- `hidrológica`: consultoría hidrológica.
- `acero`: resultados de TW Inox.
- `protesis`: resultados de TW Salud.
- `remodelacion`: resultados de TW Construye.

## Tareas corregidas

- Indicador de líneas en home.
- Footer de home con rutas comerciales nuevas.
- Menú superior con `Pagos Perú`.
- Catálogo global ampliado.
- Manifiesto de banners preparado para imágenes finales.
- Modo home del catálogo con ofertas, destacados y resultados iniciales limitados.
- CSS del header y layout comercial.

## Tareas pendientes

- Crear imágenes finales `webp` por línea cuando existan recursos visuales definitivos.
- Migrar gradualmente datos operativos antiguos hacia una estructura separada de backoffice.
- Ampliar páginas de detalle por item.
- Mejorar SEO por línea con metadatos OpenGraph específicos.
- Agregar pruebas automatizadas de regresión para catálogo y navegación.

