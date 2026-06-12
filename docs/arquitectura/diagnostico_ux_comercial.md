# Diagnóstico UX comercial

## Objetivo comercial

Tecprog World E.I.R.L. debe evolucionar desde una web institucional hacia un portal comercial centralizado. La prioridad de la experiencia debe ser:

1. Buscar.
2. Filtrar.
3. Ver precio o condición de cotización.
4. Entender disponibilidad y alcance.
5. Contactar por WhatsApp.
6. Cerrar por canales de pago.

## Estado actual de la experiencia

La home funciona como presentación institucional con líneas de negocio, carruseles y llamadas a WhatsApp. TW Store funciona como catálogo tecnológico bajo pedido. Las páginas de líneas explican servicios y redirigen a catálogos o WhatsApp.

El sitio ya tiene identidad visual consistente: azul oscuro, dorado, cyan, cards con radio bajo, botones claros y footer institucional. Sin embargo, la experiencia comercial está fragmentada: los productos de tienda, cursos, servicios y catálogos por línea se renderizan con modelos distintos.

## Problema del patrón de layout

Las páginas de línea usan tres zonas:

- Panel izquierdo: índice contextual.
- Centro: contenido principal.
- Panel derecho: acciones rápidas, recursos, redes y enlaces.

TW Store usa una sola columna comercial. Esto la hace más directa para vender, pero visualmente distinta. Adaptarla literalmente al patrón institucional de tres columnas resolvería consistencia, pero puede reducir foco comercial si el panel derecho compite con búsqueda, filtros y cards.

## Decisión UX recomendada

Crear un layout comercial superior para todas las líneas, basado en el patrón de tres zonas pero adaptado a venta:

- Columna izquierda: filtros, categorías, línea, moneda, estado y rango de precio.
- Centro: buscador, banners, ofertas, destacados y grid comercial.
- Columna derecha: CTA de WhatsApp, pagos, garantías sujetas a confirmación, políticas comerciales y accesos rápidos.

En móvil, las columnas deben convertirse en:

- Buscador arriba.
- Filtros como panel colapsable o bloque compacto.
- Cards en una columna.
- CTA de WhatsApp persistente.

## Por qué no adaptar TW Store de forma literal

El patrón actual de tres columnas fue pensado para navegación institucional y recursos rápidos. TW Store necesita una jerarquía comercial:

1. Búsqueda global.
2. Ofertas.
3. Destacados.
4. Filtros.
5. Cards con precio público.
6. Cotización por WhatsApp.

Por eso conviene tomar la estructura de tres zonas, pero redefinir el contenido de los paneles para comercio. Esta solución mantiene consistencia visual y mejora conversión.

## Problemas UX detectados

- TW Store muestra datos internos: precio fuente y margen sugerido.
- El menú superior no prioriza TW Store.
- Home no tiene buscador global comercial.
- No hay filtros globales por línea de negocio, moneda, estado y precio.
- No existe un catálogo global común.
- Las secciones por línea no comparten aún una experiencia comercial homogénea.
- Hay textos con caracteres corruptos que afectan percepción profesional.
- No existe TW Disfruta como destino visible.
- Algunas etiquetas están sin tilde por normalización previa; esto es menos grave que mojibake, pero debe corregirse con UTF-8 real.

## Tarjeta comercial recomendada

Campos visibles:

- Imagen o placeholder.
- Nombre.
- Línea de negocio.
- Categoría.
- Descripción corta.
- Precio público en soles.
- Precio público en dólares si existe.
- Estado: Disponible, Bajo pedido, Cotizar, Próximamente.
- Etiqueta: Oferta, Destacado.
- CTA: Cotizar por WhatsApp.
- CTA secundaria: Ver detalle.

Campos no visibles:

- Precio fuente.
- Precio proveedor.
- Precio de compra.
- Margen sugerido.
- Margen interno.
- URL de fuente.
- Datos de scraping.

## Home recomendada

La home debe funcionar como entrada comercial:

- Hero con búsqueda global.
- Filtros rápidos por línea.
- Ofertas destacadas.
- Productos y servicios destacados.
- Acceso a TW Store como catálogo global.
- Acceso a pagos al final de la navegación.
- Mensaje claro: precios, disponibilidad y alcance sujetos a confirmación.

## TW Store recomendada

TW Store debe ser el catálogo comercial global. Aunque inicialmente priorice tecnología, debe poder listar cualquier item pagable o cotizable:

- Productos tecnológicos.
- Servicios.
- Cursos.
- Consultorías.
- Proyectos.
- Videojuegos.
- Merchandising.
- Contenido digital.

La búsqueda en TW Store debe consultar todo `data/catalogo_global.json`.

## Líneas de negocio recomendadas

Cada línea debe tener una página comercial con:

- Banner.
- Breve explicación.
- Buscador limitado a la línea.
- Filtros por categoría, precio, moneda y estado.
- Ordenamiento.
- Cards comerciales.
- WhatsApp.
- Aviso comercial.

## Riesgos de confianza

- Mostrar proveedor o precio fuente puede inducir al cliente a comparar contra el costo interno.
- Mostrar margen sugerido deteriora percepción de valor.
- Prometer stock o garantía sin confirmación genera riesgo operativo.
- Mojibake reduce confianza y profesionalismo.

## Avance aplicado en Fase 2

Se corrigió el riesgo principal de TW Store en la nueva vista pública: las cards comerciales ya no muestran precio fuente, margen sugerido, proveedor ni URL de fuente. La tienda se conecta al catálogo global público y presenta precio, estado, descripción, etiquetas de oferta/destacado y CTA de WhatsApp.

La home ya incorpora un buscador global comercial y conserva el contenido institucional posterior. Las nuevas páginas comerciales por línea ofrecen una experiencia homogénea con búsqueda, filtros, ordenamiento y aviso de confirmación.

## Avance aplicado en Fase 3

La home se pulió para reforzar el objetivo comercial:

- El indicador principal ahora refleja 9 líneas de negocio.
- El buscador global muestra ofertas, destacados y una selección inicial en vez de saturar con todo el catálogo.
- El menú mantiene todas las líneas, pero se ajustó visualmente para reducir saturación.
- TW Store presenta 67 items públicos como catálogo global.
- Las páginas por línea ya tienen suficientes items de prueba para validar búsqueda, filtros y ordenamiento.

Validaciones UX realizadas:

- Búsquedas clave por línea funcionan.
- No hay datos internos visibles en las vistas públicas revisadas.
- No hay overflow horizontal en móvil.
- El menú hamburguesa aparece en móvil.

## Avance aplicado en Fase 4

La experiencia comercial ahora permite pasar de exploración a detalle:

- Cada tarjeta puede mostrar `Ver detalle`.
- El detalle muestra contenido público, precio o cotización, estado, tags, actualización y CTA WhatsApp.
- El usuario puede volver a TW Store o a la línea correspondiente.
- El mapa del sitio organiza las rutas comerciales nuevas y preserva rutas anteriores.
- La preparación visual queda lista para banners y flyers sin crear imágenes todavía.
