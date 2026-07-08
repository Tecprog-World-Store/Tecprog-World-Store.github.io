# Arquitectura Aprobada

Fecha de proteccion: 2026-07-08.

La arquitectura publica aprobada permite como maximo tres paneles visibles por pagina:

- Un panel lateral izquierdo.
- Un panel central de contenido o resultados.
- Un panel lateral derecho.

Reglas obligatorias:

- Los filtros, busqueda y ordenamiento del catalogo van dentro del panel central.
- No deben existir destacados duplicados.
- Las cards comerciales deben mantener proporcion visual 1:1 cuando aplique a grillas de catalogo.
- La busqueda principal del catalogo debe vivir en el centro, no en paneles laterales duplicados.
- Las paginas comerciales de linea usan paneles locales generados por `assets/js/catalogo-global.js`.
- Las paginas institucionales o de detalle pueden usar panel global derecho generado por `assets/js/right-panel.js`.
- No se permite cargar paneles globales y locales simultaneamente en una misma pagina comercial.
