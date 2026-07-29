# Reporte de corrección del layout central

## 1. Resumen

El 29 de julio de 2026 se migraron las páginas públicas de Tecprog World desde la estructura histórica de paneles laterales a una sola columna estructural central. Se conservaron la navegación superior, el contenido comercial, los precios, las políticas de pago, las rutas SEO, los canonicals, el sitemap, Open Graph, WhatsApp y los controles de audio.

La instrucción expresa de esta intervención autorizó sustituir la arquitectura de hasta tres paneles que figuraba en las restricciones anteriores. Antes del cambio se creó el tag `pre-correccion-layout-central-20260729` y la rama de respaldo `respaldo-pre-correccion-layout-central-20260729`.

## 2. Problema corregido

La composición de escritorio reservaba espacio permanente para navegación lateral y recursos comerciales laterales. Esto reducía el ancho útil del contenido, producía una jerarquía visual fragmentada y obligaba a mantener variantes estructurales distintas entre catálogos, páginas de detalle y páginas comerciales.

## 3. Origen técnico

La estructura anterior se originaba en una combinación de:

- marcado HTML con `side-nav`, `detail-sidebar`, `commerce-shell` y estrategias de panel;
- `assets/js/right-panel.js`, que insertaba dinámicamente la columna derecha;
- `assets/js/catalogo-global.js`, que generaba navegación y recursos en columnas laterales;
- reglas CSS de grilla destinadas a dos o tres columnas estructurales;
- lógica duplicada de navegación responsive entre `navigation.js` y `main.js`.

## 4. Elementos eliminados

- Panel lateral izquierdo como columna estructural.
- Panel lateral derecho como columna estructural.
- Barras laterales de resumen en páginas de detalle.
- Carga e implementación de `assets/js/right-panel.js`.
- Atributos y clases heredados destinados a estrategias de panel.
- Validador histórico `tools/validar_layout_tres_paneles.py`.
- Doble enlace de eventos del menú móvil.

## 5. Funciones reubicadas

- La navegación contextual pasó a una barra horizontal local dentro de la columna central.
- Los recursos relacionados y las acciones comerciales pasaron a secciones inferiores de la misma columna.
- Los resúmenes de detalle pasaron a bloques internos responsive, no a barras laterales.
- Los filtros, resultados, tarjetas y mensajes comerciales permanecen en el flujo principal.
- WhatsApp y audio conservaron sus funciones y disponibilidad.

## 6. Arquitectura final

La arquitectura pública aprobada queda formada por:

1. encabezado y navegación superior global de 13 destinos;
2. contenedor central de ancho máximo de 1440 px;
3. navegación contextual horizontal cuando corresponde;
4. héroe, contenido, catálogos y tarjetas en flujo vertical;
5. resúmenes, recursos relacionados y acciones como bloques internos o inferiores;
6. pie de página, WhatsApp y audio sin cambios funcionales.

Las tarjetas responden a 5, 4, 3, 2 o 1 columnas según el ancho disponible. En móvil, la navegación superior se transforma en menú desplegable accesible mediante `aria-expanded`.

## 7. Archivos modificados

El commit técnico modificó 138 archivos:

- 114 archivos HTML;
- 10 archivos JavaScript;
- 7 archivos Markdown;
- 6 archivos Python;
- 1 archivo CSS.

El balance del commit fue de 1153 inserciones y 1311 eliminaciones. Este informe es el único archivo adicional del commit de cierre.

## 8. Scripts modificados

- `assets/js/catalogo-global.js`: genera navegación local y recursos relacionados dentro del flujo central.
- `assets/js/catalogos-lineas.js`: genera navegación local horizontal.
- `assets/js/navigation.js`: normaliza los 13 enlaces superiores, estados activos y menú móvil accesible.
- `assets/js/main.js`: elimina la gestión duplicada del menú y adopta `data-local-nav`.
- `assets/js/detalle.js`, `guias.js`, `compendios.js`, `materiales.js` y `oferta-detalle.js`: generan resúmenes internos.
- `tools/generar_paginas_sociales_cursos.py`: conserva el nuevo patrón al regenerar páginas.
- `assets/js/right-panel.js`: eliminado.

## 9. Validadores

Resultado final: 3 de 3 validadores obligatorios aprobados.

- `python tools/validar_layout_columna_central.py`: aprobado.
- `python tools/validar_no_paneles_duplicados.py`: aprobado.
- `python tools/validar_version_assets.py`: aprobado con versión uniforme `?v=20260729-04`.

También se aprobaron `node --check` en los JavaScript modificados, la validación de 28 archivos JSON y `git diff --check`.

## 10. Resultados responsive

Se ejecutaron 54 comprobaciones exactas sobre 6 páginas críticas en 9 viewports, además de una revisión visual de 30 páginas.

| Viewport | Tarjetas observadas en tienda | Resultado |
| --- | ---: | --- |
| 1920 × 1080 | 5 | Aprobado |
| 1600 × 900 | 5 | Aprobado |
| 1366 × 768 | 5 | Aprobado |
| 1280 × 800 | 4 | Aprobado |
| 1024 × 768 | 3 | Aprobado |
| 768 × 1024 | 2 | Aprobado |
| 430 × 932 | 1 | Aprobado |
| 390 × 844 | 1 | Aprobado |
| 360 × 800 | 1 | Aprobado |

No se detectaron desbordamientos horizontales, solapamientos de encabezado, paneles heredados ni botones recortados después del ajuste final. El menú móvil se verificó con clic, teclado, cambio de `aria-expanded` y cierre tras seleccionar un destino.

## 11. Validación de 100 URLs

El `sitemap.xml` público contiene 100 URLs únicas. Tras la publicación del commit técnico:

- URLs solicitadas: 100;
- respuestas HTTP 200: 100;
- respuestas HTTP 404: 0;
- otras respuestas: 0;
- referencias a paneles heredados en HTML público: 0.

## 12. Validación de recursos

La inspección local resolvió 129 referencias activas sin errores. En producción se deduplicaron y solicitaron 65 recursos locales activos:

- recursos HTTP 200: 65;
- recursos HTTP 404: 0;
- otros errores de recursos: 0;
- versión pública detectada: `?v=20260729-04`.

## 13. Consola

Las páginas críticas publicadas no produjeron errores de consola atribuibles al sitio. Durante una revisión local de un PDF embebido apareció una incidencia aislada de instrumentación del navegador sobre `MutationObserver`, sin URL de origen y sin correspondencia en el código del repositorio. La repetición en producción devolvió una consola vacía.

## 14. Capturas y descripción visual

Se generaron capturas temporales de la tienda en 1920 × 1080, 1366 × 768, 768 × 1024 y 390 × 844. Confirmaron encabezado estable, héroe antes del catálogo, navegación contextual horizontal, contenido central continuo, tarjetas responsive y ausencia de columnas laterales. Las capturas se eliminaron del directorio temporal al terminar la revisión y no se incorporaron al repositorio.

## 15. Push

El commit técnico `b6d2b5b37eb5537de9f0912a99e82e09520fe6c9` se envió correctamente a `origin/main`.

## 16. Hash de referencia

Hash que contiene la corrección técnica completa:

`b6d2b5b37eb5537de9f0912a99e82e09520fe6c9`

El hash final del segundo commit se comunica en la entrega porque un commit no puede incluir de forma autorreferencial su propio hash.

## 17. Estado de GitHub Pages

El flujo `pages build and deployment` número `30426681674` terminó con estado `completed` y conclusión `success` para el commit técnico. Después del commit de este informe se ejecutará y verificará una segunda publicación.

## 18. Riesgos residuales

- Los futuros generadores o nuevas páginas deben mantener `central-page`, `local-nav` y `detail-summary` y no reintroducir columnas laterales.
- Toda referencia local a CSS o JavaScript debe conservar una versión `?v=` uniforme.
- Los cambios futuros en el número de destinos globales deben actualizar conjuntamente navegación y validadores.
- Las validaciones visuales automatizadas pueden verse afectadas por extensiones del navegador; por eso se combinaron inspección visual, DOM, consola, HTTP y validadores estáticos.
- No quedan riesgos funcionales críticos conocidos ni errores públicos detectados en el alcance revisado.
