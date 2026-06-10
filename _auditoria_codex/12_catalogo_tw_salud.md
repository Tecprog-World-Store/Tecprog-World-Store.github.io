# 12. Catalogo TW Salud

Fecha de ejecucion: 2026-06-10

## Objetivo aplicado

Se creo un catalogo robusto para la linea:

- Nombre completo: TW Salud y Vida - Protesis y Tecnologia Medica
- Nombre corto: TW Salud

El contenido se redacto con enfoque tecnico-comercial responsable: diseno, prototipado, soporte tecnico, accesibilidad e investigacion aplicada. No se presentan diagnosticos medicos, prescripciones, aprobaciones clinicas ni dispositivos listos para uso clinico.

## Archivos creados o actualizados

- `data/fuentes/catalogo_base_tw_salud.txt`
- `data/catalogo-tw-salud.json`
- `data/tw-salud.json`
- `lineas/tw-salud.html`
- `catalogo/tw-salud.html`
- `assets/js/catalogos-lineas.js`

## Estructura fuente

El archivo `data/fuentes/catalogo_base_tw_salud.txt` usa el encabezado solicitado:

```text
id | linea | categoria | servicio_producto | tipo | descripcion_corta | publico_objetivo | modalidad | entregables | precio_peru_desde_soles | precio_internacional_desde_usd | estado | requiere_validacion_profesional | nota_tecnica
```

Total de filas de servicios: 35.

## Categorias incluidas

- Protesis y ortesis
- Tecnologia medica y mantenimiento
- Vehiculos inclusivos
- Accesibilidad y asistencia tecnologica
- EEG y Brain Computer Interface
- Investigacion aplicada en salud

## Precios referenciales aplicados

Los servicios incluyen precios desde en soles y dolares. Se usaron rangos compatibles con los precios sugeridos:

- Asesoria tecnica inicial desde S/ 49
- Diagnostico tecnico simple desde S/ 79
- Modelado CAD basico desde S/ 149
- Prototipo educativo/no clinico desde S/ 299
- Prototipo personalizado desde S/ 699
- Proyecto biomedico a medida desde S/ 1,500
- Servicio internacional desde USD 49

## Nota obligatoria incorporada

Se incorporo en fuente, JSON, pagina de linea y catalogo dinamico:

> Los servicios de TW Salud se orientan a diseño, prototipado, soporte técnico, accesibilidad e investigación aplicada. La evaluación clínica, prescripción, adaptación médica y validación de uso deben realizarse con profesionales de salud competentes cuando corresponda.

## Criterios responsables usados

- Se evita afirmar diagnostico medico.
- Se evita afirmar prescripcion de dispositivos medicos.
- Se evita afirmar aprobacion clinica de prototipos.
- Se usan expresiones como prototipo, diseno tecnico, acompanamiento de ingenieria, validacion profesional y revision competente.
- Para equipos medicos se usa diagnostico tecnico, inventario, mantenimiento preventivo, limpieza externa, documentacion y derivacion a servicio autorizado cuando corresponda.
- Para EEG y BCI se presenta contenido como educativo, experimental o de investigacion aplicada, sin interpretacion diagnostica.
- Para dialisis y salud digital se presenta investigacion aplicada y monitoreo no clinico, sin propuestas de tratamiento.

## Validaciones ejecutadas

- `data/catalogo-tw-salud.json` valido como JSON.
- `data/tw-salud.json` valido como JSON.
- `assets/js/catalogos-lineas.js` valido con `node --check`.
- El TXT tiene el encabezado solicitado.
- Las 35 filas del TXT tienen 14 columnas delimitadas por pipes.
- Todas las categorias minimas solicitadas estan presentes.
- Todos los servicios tienen precio referencial en soles y USD.

## Advertencias y revision manual recomendada

- Las palabras prescripcion y evaluacion clinica aparecen dentro de la nota obligatoria y en aclaraciones restrictivas, no como promesa comercial.
- Antes de publicar piezas comerciales externas, revisar que no se agreguen claims como diagnostico medico, tratamiento, aprobacion clinica, certificacion sanitaria o fabricante autorizado.
- Si en el futuro se trabaja con profesionales, marcas, instituciones o autorizaciones, documentar evidencias antes de mencionarlas publicamente.
