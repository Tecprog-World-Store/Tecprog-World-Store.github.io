# Reporte del cronograma anual TW Educa

Fecha de cierre: 29 de julio de 2026.

## 1. Resumen ejecutivo

Se implementó un sistema canónico, reutilizable y ampliable de convocatorias mensuales para los 243 cursos activos de TW Educa. Cada curso dispone de doce oportunidades de inicio tentativas, integradas en tarjetas, páginas de detalle y una página anual filtrable, sin backend y con JavaScript vanilla compatible con GitHub Pages.

## 2. Periodo cubierto

Del 1 de agosto de 2026 al 31 de julio de 2027, organizado en doce periodos mensuales consecutivos.

## 3. Cantidad de cursos

243 cursos activos y únicos:

- 194 cursos del catálogo general;
- 37 cursos con páginas comerciales dedicadas;
- 12 cursos publicados en páginas históricas que no estaban duplicados en las fuentes anteriores.

No se incluyeron materiales, compendios, servicios ni productos ajenos a la clasificación de curso.

## 4. Cantidad de convocatorias

2.916 convocatorias: 243 cursos × 12 meses. Todos los cursos tienen exactamente una convocatoria por periodo.

## 5. Reglas de distribución

Los cursos se clasificaron en cinco grupos: A, introductorios (25); B, programación y software (46); C, ingeniería y modelación (105); D, realidad virtual e intensivos (3); y E, especializados de apertura mensual (64). Las fechas se escalonaron durante cada mes, con un máximo validado de dos inicios en la misma fecha y hora. Se excluyeron el 1 de enero y el 25 de diciembre.

Todas las fechas son tentativas, el inicio exacto puede coordinarse con el grupo y ninguna convocatoria proyectada se declara confirmada.

## 6. Horarios utilizados

- Grupo A: martes y jueves; 19:00–21:00, 18:30–20:30 o 20:00–22:00.
- Grupo B: lunes y miércoles; 19:00–21:00, 18:30–20:30 o 20:00–22:00.
- Grupo C: martes, jueves o sábado; 20:00–22:00, 19:00–21:00 o 15:00–18:00.
- Grupo D: sábados; 15:00–18:00, 09:00–12:00 o 18:00–21:00.
- Grupo E: sábados o viernes; 09:00–12:00, 15:00–18:00 o 19:00–21:00.

## 7. Zona horaria

La referencia canónica es `America/Lima`, Perú, `UTC-05:00`. La hora oficial de Lima siempre permanece visible. El componente web usa `Intl.DateTimeFormat` para detectar la zona del navegador y mostrar una equivalencia local referencial sin sustituir la fecha oficial.

## 8. Modelo de mínimo de inscritos

El mínimo general configurable es de 5 participantes y puede sobrescribirse por curso. Todas las convocatorias proyectadas indican “Inscripciones abiertas” y “Sujeto a mínimo de inscritos”. No se simulan participantes, vacantes ni confirmaciones.

## 9. Tratamiento de PEN

Los precios vigentes en PEN se conservaron desde sus fuentes comerciales. PEN permanece como precio contractual principal cuando corresponde. No se modificaron promociones, descuentos ni opciones de pago.

## 10. Tratamiento de USD

Se conservaron los precios USD oficiales que ya existían. Para cursos sin USD oficial se aplicó una única equivalencia configurable de 3,411 PEN por USD, referencia del 24 de julio de 2026, con redondeo comercial hacia arriba al dólar entero. La fuente registrada es la cotización de venta publicada por la SBS con referencia de mercado BCRP.

El importe internacional se identifica como referencial; puede variar por conversión, PayPal o entidad financiera. No se añadieron comisiones al cálculo.

## 11. Archivos creados

19 archivos:

- `assets/js/cronograma-tw-educa.js`;
- `catalogo/cronograma-anual-tw-educa.html`;
- 15 archivos en `data/cronogramas/` (`configuracion.json`, `actual.json`, `cursos.json` y doce periodos);
- `tools/generar_cronograma_anual_tw_educa.py`;
- `tools/validar_cronograma_tw_educa.py`.

Este reporte es el vigésimo archivo creado y se incorpora en el commit final de documentación.

## 12. Archivos modificados

125 archivos existentes fueron modificados en el commit técnico. Los cambios corresponden a integración del cronograma, estilos, fuentes comerciales, sitemap, generadores existentes y actualización uniforme de assets a `?v=20260729-06`.

## 13. Automatización implementada

`tools/generar_cronograma_anual_tw_educa.py` admite:

```text
python tools/generar_cronograma_anual_tw_educa.py --inicio 2026-08 --meses 12 --dry-run
python tools/generar_cronograma_anual_tw_educa.py --inicio 2026-08 --meses 12 --write
```

El modo `--dry-run` no escribe archivos. El modo `--write` preserva convocatorias marcadas con `bloqueado_manualmente: true`, actualiza el periodo móvil y produce resultados idempotentes. Dos ejecuciones consecutivas generaron el mismo SHA-256 del conjunto canónico.

## 14. Resultado de validadores

- Cronograma: correcto; 243 cursos, 2.916 convocatorias, 52 páginas protegidas y 43 JSON válidos.
- Columna central: correcto.
- Paneles duplicados: correcto.
- Versión de assets: correcta y uniforme (`20260729-06`).
- Sintaxis de los cinco JavaScript modificados: correcta.
- `git diff --check`: correcto.

El nombre histórico `tools/validar_layout_tres_paneles.py` no existe en el estado actual del repositorio; se ejecutó el validador vigente indicado en el encargo, `tools/validar_layout_columna_central.py`.

## 15. Resultado HTTP

Validación local:

- 101 URL del sitemap;
- 243 registros canónicos de cursos;
- 307 URL activas únicas;
- 307 respuestas HTTP 200;
- 0 respuestas HTTP 404;
- 76 recursos locales CSS/JS activos comprobados, todos con HTTP 200.

Validación pública en GitHub Pages:

- 307 URL activas únicas;
- 307 respuestas HTTP 200;
- 0 respuestas HTTP 404;
- sin otros códigos HTTP.

## 16. Resultado de consola

0 errores y 0 advertencias en las páginas públicas comprobadas. También se validaron las resoluciones 1920×1080, 1366×768, 1024×768, 768×1024, 430×932, 390×844 y 360×800 sin desplazamiento horizontal atribuible al cronograma.

## 17. Comprobación de contenido preservado

El validador comparó 52 páginas de cursos contra el respaldo previo. No disminuyeron encabezados, secciones, artículos, párrafos, listas, botones, enlaces, imágenes, metadatos ni tokens de precio. Se conservaron temarios, duración, modalidad, beneficios, requisitos, certificación, métodos de pago, contacto y SEO.

## 18. Resultado del push

El commit técnico `2960ee7a6af8c424370774ecd1f539fde9169aa5` se publicó correctamente en `origin/main` mediante avance normal, sin force push.

## 19. Hash final

El hash técnico desplegado y validado es `2960ee7a6af8c424370774ecd1f539fde9169aa5`. El hash final absoluto del repositorio es el commit que contiene este reporte y se comunica al cierre; no puede autorreferenciarse dentro de su propio contenido sin alterar su hash.

## 20. Estado de GitHub Pages

El flujo `pages build and deployment` número 30429243120 terminó con conclusión `success` para el commit técnico. Se comprobaron públicamente TW Educa, el cronograma anual, los dos catálogos, diez cursos representativos, una página de detalle dinámica, filtros, PEN, USD, WhatsApp, zona horaria, vista móvil, sitemap y consola.

## 21. Riesgos o datos comerciales pendientes

- Las fechas y horarios son proyecciones tentativas y requieren confirmación comercial cuando cada grupo alcance el mínimo.
- La equivalencia USD debe revisarse cuando cambie la política comercial o el tipo de cambio de referencia.
- Las conversiones horarias del navegador son orientativas; la hora contractual sigue siendo la de Lima.
- La fuente anual completa suma aproximadamente 4,4 MB en JSON; es adecuada para el sitio estático actual, pero conviene vigilar el rendimiento móvil si aumenta sustancialmente el catálogo.
