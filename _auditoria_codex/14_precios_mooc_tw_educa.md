# 14. Precios MOOC TW Educa

Fecha de ejecucion: 2026-06-10

## Objetivo aplicado

Se actualizo la estrategia comercial de TW Educa hacia un modelo freemium:

- Material introductorio o acceso MOOC gratuito para atraer trafico.
- Certificacion, evaluacion, clases en vivo, acceso completo, acompanamiento especializado y capacitacion institucional con costo.

Frase obligatoria aplicada:

> Puedes revisar material introductorio gratuito. La certificación, evaluación, clases en vivo o acompañamiento especializado tienen costo.

## Archivos creados

- `data/politica_precios_tw_educa.json`
- `_auditoria_codex/14_precios_mooc_tw_educa.md`

## Archivos actualizados

- `data/catalogo-general-cursos.json`
- `data/cursos.json`
- `data/cursos/2026-06.json`
- `data/ofertas.json`
- `catalogo/catalogo-general-tw-educa.html`
- `lineas/tw-educa.html`
- `detalle/curso.html`
- `assets/js/catalogo-general-cursos.js`
- `assets/js/detalle.js`
- `assets/js/main.js`

## Politica creada

La politica `data/politica_precios_tw_educa.json` define:

- MOOC gratuito: S/ 0
- Certificado digital basico: desde S/ 19
- Certificado con evaluacion: desde S/ 49
- Curso en vivo economico: desde S/ 59 a S/ 99
- Curso tecnico especializado: desde S/ 99 a S/ 149
- Programa de especializacion: desde S/ 199 a S/ 399
- Capacitacion institucional: desde S/ 500

Tambien registra horas certificables sugeridas:

- Microcurso: 8 a 12 horas
- Curso corto: 16 a 24 horas
- Curso estandar: 32 a 40 horas
- Curso avanzado: 60 horas
- Especializacion: 80 a 120 horas

## Campos agregados a cursos

Los cursos fueron enriquecidos con campos como:

- `acceso_mooc_gratuito`
- `precio_mooc_soles`
- `mooc_texto`
- `boton_mooc`
- `certificado_desde_soles`
- `certificado_texto`
- `certificado_digital_basico_desde_soles`
- `certificado_con_evaluacion_desde_soles`
- `curso_en_vivo_desde_soles`
- `curso_tecnico_especializado_desde_soles`
- `programa_especializacion_desde_soles`
- `capacitacion_institucional_desde_soles`
- `modalidad_tags`
- `tipo_horas_certificables`
- `horas_certificables_sugeridas`
- `nota_precio_mooc`

## Cambios visibles

- El catalogo general muestra `Acceso MOOC: Gratis`.
- El catalogo general muestra `Certificado desde S/ ...`.
- Se agrego boton `Acceder gratis`.
- El detalle de curso incluye bloque `Acceso gratuito y certificacion`.
- La ficha del curso separa acceso MOOC, certificado y acceso completo.
- TW Educa explica que lo gratuito es introductorio y que certificacion/evaluacion/en vivo/acompanamiento tienen costo.
- Los cursos destacados del inicio muestran acceso MOOC gratuito y certificado desde.

## Filtros agregados

En `catalogo/catalogo-general-tw-educa.html`, mediante `assets/js/catalogo-general-cursos.js`, se agrego el filtro comercial:

- MOOC gratuito
- Certificado pagado
- En vivo
- Grabado
- Especializacion

## Conteos validados

Catalogo general:

- Total de cursos: 194
- MOOC gratuito: 194
- Certificado pagado: 194
- En vivo: 194
- Grabado: 194
- Especializacion: 66

Otros archivos:

- `data/cursos.json`: 6 registros enriquecidos.
- `data/cursos/2026-06.json`: 2 registros enriquecidos.

## Validaciones ejecutadas

- JSON valido en `data/politica_precios_tw_educa.json`.
- JSON valido en `data/catalogo-general-cursos.json`.
- JSON valido en `data/cursos.json`.
- JSON valido en `data/cursos/2026-06.json`.
- JSON valido en `data/ofertas.json`.
- Sintaxis JavaScript valida en `assets/js/catalogo-general-cursos.js`, `assets/js/detalle.js` y `assets/js/main.js`.
- Todos los cursos revisados muestran `Acceso MOOC: Gratis`.
- Todos los cursos revisados muestran `Certificado desde S/ ...`.
- Todos los cursos revisados incluyen la frase de aclaracion sobre costos.

## Advertencias

- El acceso MOOC gratuito no debe comunicarse como curso completo gratuito con certificado.
- La certificacion, evaluacion, clases en vivo, acompanamiento especializado y capacitacion institucional deben mantenerse como opciones pagadas.
- Si se agregan nuevos cursos, deben heredar los campos de politica MOOC para evitar mensajes ambiguos.
