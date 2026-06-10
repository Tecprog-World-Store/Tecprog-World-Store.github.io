# 13. Catalogo TW Interactive

Fecha de ejecucion: 2026-06-10

## Objetivo aplicado

Se creo la linea tecnica:

- Nombre completo: TW Interactive - Ingenieros Consultores
- Nombre corto: TW Interactive
- Enfoque: servicios de ingenieria mecanica de fluidos, consultoria, simulacion, modelamiento y documentacion tecnica para aplicaciones en Peru.

La linea se conserva como marca historica o fanpage posiblemente inactiva, pero queda normalizada dentro del sitio como unidad de servicios tecnicos de ingenieria.

## Archivos creados

- `data/fuentes/catalogo_base_tw_interactive.txt`
- `data/catalogo-tw-interactive.json`
- `data/tw-interactive.json`
- `catalogo/tw-interactive.html`
- `_auditoria_codex/13_catalogo_tw_interactive.md`

## Archivos actualizados

- `lineas/tw-interactive.html`
- `assets/js/catalogos-lineas.js`
- `assets/js/right-panel.js`
- `assets/js/navigation.js`
- `assets/js/oferta-detalle.js`
- `assets/js/main.js`
- `data/lineas.json`
- `index.html`
- `empresa/mapa-del-sitio.html`
- `README.md`

## Estructura fuente

El archivo `data/fuentes/catalogo_base_tw_interactive.txt` usa el encabezado solicitado:

```text
id | linea | rama | servicio | tipo | descripcion_corta | publico_objetivo | entregables | software_herramientas | precio_peru_desde_soles | precio_internacional_desde_usd | estado | nota_tecnica
```

Total de filas de servicios: 47.

## Ramas incluidas

- Hidraulica e hidrologia
- Hidraulica fluvial
- CFD y simulacion
- Termofluidos
- Turbomaquinas y energia
- Aerodinamica
- Ingenieria aplicada y documentacion

## Servicios y precios

Todos los servicios incluyen precio referencial desde en soles y USD. Se aplicaron rangos compatibles con:

- Asesoria tecnica puntual desde S/ 49
- Revision de informacion tecnica desde S/ 99
- Informe tecnico breve desde S/ 199
- Procesamiento GIS/hidrologico basico desde S/ 299
- Simulacion preliminar desde S/ 499
- Estudio tecnico especializado desde S/ 900
- Proyecto institucional desde S/ 1,500
- Servicio internacional desde USD 80

## Cambios visibles

- Se agrego el boton `Servicios de ingenieria` en el hero de inicio.
- Se agrego `Servicios de ingenieria` en el panel lateral derecho.
- Se agrego `Catalogo TW Interactive` al panel derecho y al footer institucional.
- Se agrego `Catalogo TW Interactive` al mapa del sitio.
- La tarjeta de inicio de TW Interactive ahora describe hidrologia, hidraulica, CFD, termofluidos, energia, aerodinamica y Python.
- El detalle dinamico `detalle/oferta.html?id=...&linea=tw-interactive` carga desde `data/catalogo-tw-interactive.json`.

## Nota tecnica general

Servicio tecnico de ingenieria y consultoria. Los resultados son referenciales segun datos disponibles, alcance contratado, supuestos de calculo, normativa aplicable y revision profesional competente cuando corresponda.

## Validaciones ejecutadas

- JSON valido en `data/catalogo-tw-interactive.json`, `data/tw-interactive.json` y `data/lineas.json`.
- Sintaxis JavaScript valida en `assets/js/catalogos-lineas.js`, `assets/js/main.js`, `assets/js/navigation.js`, `assets/js/right-panel.js` y `assets/js/oferta-detalle.js`.
- TXT con encabezado exacto solicitado.
- 47 filas con 13 columnas delimitadas por pipes.
- Todas las ramas minimas solicitadas estan presentes.
- Todos los servicios tienen precio referencial en soles y USD.
- Enlaces locales validos en `lineas/tw-interactive.html`, `catalogo/tw-interactive.html`, `index.html` y `empresa/mapa-del-sitio.html`.

## Revision manual recomendada

- Verificar si la fanpage historica de TW Interactive debe enlazarse publicamente o mantenerse sin enlace por estar inactiva.
- Confirmar si algunos servicios especializados requieren firma, colegiatura, visita de campo, topografia, laboratorio, geotecnia, licencia de software o coordinacion con terceros.
- Revisar futuras piezas comerciales para evitar promesas de aprobacion institucional, resultados garantizados o reemplazo de revision oficial.
