# Fase 8D - Paneles y resultados

Fecha: 2026-07-04

## Causa del problema

Las paginas comerciales usaban `data-commerce-catalog` como un contenedor unico, pero `assets/js/catalogo-global.js` renderizaba dentro de ese contenedor un panel izquierdo de filtros, un panel central y un panel derecho de recursos. Visualmente eso se sumaba a la navegacion institucional y al concepto de panel derecho global del sitio, generando hasta cinco zonas aparentes.

Tambien se renderizaban bloques separados de destacados/ofertas y resultados. En lineas con pocos items, ese patron duplicaba visualmente el catalogo.

## Componentes eliminados

- Panel lateral izquierdo de filtros (`commerce-filters commerce-left-panel`) en paginas de linea y store.
- Segundo buscador dentro de filtros (`data-commerce-search`).
- Bloques `data-commerce-featured` y `data-commerce-offers` en paginas de linea y store.
- Titulos visibles `Destacados`, `Ofertas destacadas` y `Productos y servicios destacados` en paginas de linea y store.

El modo home conserva sus bloques editoriales porque puede depender de la propiedad `destacado`.

## Paneles fusionados

El panel derecho ahora agrupa una sola instancia de:

- WhatsApp.
- Enviar correo.
- Copiar enlace.
- Compartir pagina.
- Cotizar.
- Recursos de la linea.
- Pagos Peru e internacionales.
- Confianza comercial.

En TW Educa se conservan cronograma publico, guias, cursos, pagos y confianza comercial desde `LINE_PANEL_COPY["tw-educa"]`.

## Filtros en el centro

El panel central queda ordenado asi:

1. Titulo corto.
2. Frase breve.
3. Buscador principal unico.
4. Filtros integrados en `.commerce-toolbar`.
5. Contador.
6. Grilla unica de resultados.

Los filtros disponibles son categoria, moneda, estado, precio minimo, precio maximo y ordenar. En store tambien se conserva filtro por linea.

## Una sola grilla

Cada pagina de linea y store renderiza una sola grilla `data-commerce-results`. No hay grilla de destacados ni grilla de ofertas en esas paginas.

## Pruebas responsive

Paginas probadas:

- `/store/index.html`
- `/educa/index.html`
- `/innova/index.html`
- `/salud/index.html`
- `/interactive/index.html`
- `/construye/index.html`
- `/inox/index.html`
- `/investiga/index.html`
- `/disfruta/index.html`

Viewports:

- 390x844: sin overflow despues del ajuste de ancho responsive.
- 768x1024: sin overflow.
- 1366x768: tres columnas reales.
- 1920x1080: tres columnas reales.

Resultados comunes:

- 1 panel izquierdo.
- 1 panel central.
- 1 panel derecho.
- 1 buscador.
- 1 toolbar de filtros.
- 1 grilla de resultados.
- 0 grillas de destacados/ofertas.
- Cards con media 1:1.
- Sin duplicados de items detectados.

## Validacion TW Educa

Consultas probadas:

- OpenFOAM: devuelve cursos OpenFOAM/CFD relacionados.
- QGIS: devuelve cursos QGIS/GIS relacionados.
- Realidad Virtual: devuelve curso de realidad virtual.
- AutoCAD: devuelve cursos AutoCAD.
- Python: devuelve cursos Python y relacionados.

Filtros probados:

- Categoria Programacion.
- Rango de precio 100 a 1000.
- Orden precio menor a mayor.
- Enlaces de detalle presentes en tarjetas filtradas.
- Enlaces de WhatsApp presentes en tarjetas filtradas.

## Errores de consola

No se detectaron errores de consola en las rutas y viewports validados.

## Estado para publicar

La Fase 8D queda apta para revision visual humana y lista para commit/push tecnico si el usuario aprueba el resultado visual.
