# Reporte fase 8F - Auditoria de home

## Archivos revisados

- index.html
- assets/js/catalogo-global.js
- assets/js/navigation.js
- assets/js/right-panel.js
- assets/js/main.js
- assets/js/videos-destacados.js
- assets/css/styles.css

## Hallazgos

- La home tenia portada, buscador, banner, grilla extensa de lineas y multiples bloques destacados.
- El catalogo en modo home limitaba resultados iniciales y renderizaba bloques de ofertas/destacados duplicados.
- El script global de ubicacion podia agregar una seccion extra al final de la home.
- El frontis institucional existente estaba disponible en assets/img/banner_horizontal_tw/figuraHorizontal01.webp y .png.

## Cambios aplicados

- La portada usa el frontis institucional como primera seccion visible.
- El carrusel de lineas queda inmediatamente debajo de la portada.
- El buscador global y filtros quedan inmediatamente despues del carrusel.
- La home muestra una sola grilla global con todos los resultados.
- Canales oficiales queda como ultima seccion principal antes del footer e incluye redes y video institucional.
- Se desactivo la ubicacion comercial automatica solo en home para respetar el orden final.
- Se actualizo el cache busting de CSS y JS a fase8f-20260704.

## Bloques retirados del render de home

| Bloque | Destino o criterio |
| --- | --- |
| Capacidades tecnicas para problemas reales | Retirado de home; contenido institucional queda cubierto por Empresa y paginas de lineas. |
| Cursos destacados | Retirado de home; cursos se consultan en TW Educa y en la grilla global. |
| Videos destacados | Retirado como bloque destacado; video institucional se conserva dentro de Canales oficiales. |
| Software y soluciones digitales | Retirado de home; se accede por TW Innova y catalogo global. |
| Consultoria, modelamiento y desarrollo | Retirado de home; se accede por TW Interactive y catalogo global. |
| Prototipado biomedico y soluciones inclusivas | Retirado de home; se accede por TW Salud y catalogo global. |
| Tecnologia bajo pedido | Retirado como bloque independiente; TW Store queda en carrusel y grilla global. |
| Compendios y guias tecnicas | Retirado de home; se conserva en catalogo/compendios.html y catalogo/guias.html. |
| Innovacion con aplicacion real | Retirado de home; proyectos quedan en paginas internas y catalogos. |
| Solicita informacion, cotizacion o inscripcion | Retirado de home; acciones permanecen en cards, detalle, WhatsApp y footer. |
| Duplicados de lineas de negocio | Se elimino la grilla extensa; queda solo carrusel compacto. |
| Duplicados de redes sociales | Queda una sola seccion Canales oficiales. |

## Orden final

1. Frontis de Tecprog World.
2. Carrusel breve de lineas de negocio.
3. Buscador global y filtros.
4. Todos los resultados.
5. Canales oficiales / redes sociales.
6. Footer.
