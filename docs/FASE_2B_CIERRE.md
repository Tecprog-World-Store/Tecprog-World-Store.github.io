# Cierre de FASE 2B

Fecha: 2026-09-09. Estado inicial: árbol limpio, HEAD `ed92499`.
Se valida la implementación existente sin investigar, convertir ni modificar precios. La revisión visual detectó tarifas PEN incrustadas en flyers de cursos: las tarjetas del catálogo global y las líneas usan ahora la ilustración existente de capacitación, sin tarifas. Se conservan los archivos originales.

- Edge/Playwright: TW Store (105 tarjetas), TW Educa (37), TW Interactive (14) y TW Salud (6), en escritorio 1440×900 y móvil 390×844.
- Tarjetas: precios USD; cursos con Matrícula abierta; precios variables con Desde USD; una sola acción Ver más. Sin precios PEN, Precio a consultar ni Próxima convocatoria. AWS/Azure no es una referencia monetaria.
- Búsqueda por nombre y sin resultados; filtros mínimo/máximo USD entre 100 y 300 y restauración de resultados: correctos.
- Todos los enlaces de las tarjetas probadas responden HTTP 200. Fichas de producto, curso, Interactive y Salud renderizadas en ambos tamaños con título y precio USD correctos.
- Sin errores de consola, respuestas HTTP fallidas ni imágenes rotas en las cuatro páginas probadas.
- Comprobación decimal independiente: precio publicado >= (base + 0.30) / 0.946 en las nueve muestras siguientes. No se modificó ningún importe.

| Tipo | ID | Base USD | Publicado USD |
| --- | --- | ---: | ---: |
| Producto | tw-store-001 | 899.67 | 959 |
| Producto | tw-store-002 | 866.34 | 919 |
| Producto | tw-store-003 | 176.34 | 189 |
| Curso | tw-educa-001 | 24 | 29 |
| Curso | tw-educa-002 | 30 | 39 |
| Curso | tw-educa-003 | 35 | 39 |
| Servicio | tw-disfruta-002 | 200 | 219 |
| Servicio | tw-innova-001 | 100 | 109 |
| Servicio | tw-innova-002 | 200 | 219 |

Validadores existentes correctos: layout de columna central, ausencia de paneles duplicados, versiones de assets, precios de cursos, WhatsApp y temarios TW Educa. `git diff --check` correcto.

Evidencia local fuera del repositorio: `C:/Users/ACER/AppData/Local/Temp/tw-fase2b/cierre-validacion.json` y capturas `cierre-*` / `card-*`.
Este cierre incorpora esta constancia y la corrección de imagen de tarjetas; sin cambios de precios ni push.
