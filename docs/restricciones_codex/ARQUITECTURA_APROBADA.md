# Arquitectura Aprobada

Fecha de proteccion original: 2026-07-08.
Actualizacion autorizada: 2026-07-29.

La arquitectura publica aprobada utiliza una sola columna estructural central:

- Encabezado global y navegacion superior.
- Navegacion local horizontal cuando sea necesaria.
- Contenido principal central adaptable.
- Secciones relacionadas debajo del contenido.
- Footer, WhatsApp flotante y reproductor de audio flotante.

Reglas obligatorias:

- Los filtros, busqueda y ordenamiento del catalogo van dentro del panel central.
- No deben existir destacados duplicados.
- Las cards comerciales deben mantener proporcion visual 1:1 cuando aplique a grillas de catalogo.
- La busqueda principal del catalogo debe vivir en el centro, no en paneles laterales duplicados.
- Las paginas comerciales usan navegacion local horizontal generada por `assets/js/catalogo-global.js`.
- No se permiten paneles laterales verticales globales, locales ni comerciales.
- Los grids internos de tarjetas, heroes y bloques informativos no cuentan como columnas estructurales.
