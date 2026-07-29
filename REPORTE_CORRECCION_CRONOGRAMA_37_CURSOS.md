# Reporte de corrección del cronograma de 37 cursos

Fecha de cierre: 2026-07-29  
Repositorio: `Tecprog-World-Store.github.io`  
Rama: `main`

## 1. Problema corregido

La primera versión del cronograma anual incorporó 243 registros procedentes de fuentes generales e históricas. Ese universo no coincidía con la oferta visible y publicada de TW Educa. La corrección restringe todo el flujo —datos, generador, interfaz y validación— a una lista cerrada de exactamente 37 cursos.

## 2. Cursos detectados antes de la corrección

El cronograma anterior contenía 243 cursos.

## 3. Cursos retirados del alcance

Se retiraron 206 cursos ajenos a la oferta publicada actual: `243 - 37 = 206`. Ninguno permanece en los JSON mensuales, la vista anual, las tarjetas de TW Educa ni las páginas de detalle.

## 4. Lista válida de 37 cursos

La fuente cerrada y auditable es `data/cronogramas/cursos_tw_educa_publicados.json`. Los 37 slugs autorizados son:

1. `realidad-virtual-unity-meta-quest`
2. `programacion-autocad-csharp`
3. `qgis-python-plugins`
4. `ia-offline-python-ollama-pyside`
5. `geoportales-web-gis-python-geoserver`
6. `latex-texmaker-investigacion`
7. `machine-learning-mecanica-fluidos`
8. `cfd-openfoam-wsl`
9. `cloud-computing-openfoam`
10. `datos-climaticos-oceanograficos-python`
11. `cpp-mecanica-fluidos`
12. `apps-moviles-flutter-mecanica-fluidos`
13. `vision-artificial-rios-canales`
14. `programacion-gpu-nvidia-cfd`
15. `curso-practico-de-costos-y-presupuestos-con-s10`
16. `curso-practico-de-sap2000-para-analisis-estructural`
17. `curso-practico-de-modelado-y-analisis-estructural-con-etabs`
18. `curso-practico-de-autodesk-inventor-para-diseno-mecanico`
19. `curso-practico-de-revit-para-modelado-bim`
20. `curso-practico-de-excel-nivel-i`
21. `curso-practico-de-excel-nivel-ii`
22. `curso-practico-de-excel-nivel-iii`
23. `curso-practico-de-autocad-nivel-i`
24. `curso-practico-de-autocad-nivel-ii`
25. `curso-practico-de-autocad-nivel-iii`
26. `curso-practico-de-solidworks-para-diseno-3d`
27. `curso-practico-de-freecad-para-diseno-3d`
28. `curso-practico-de-matlab-y-octave-para-ingenieria`
29. `curso-practico-de-python-basico`
30. `curso-practico-de-python-poo`
31. `curso-practico-de-python-web`
32. `curso-practico-de-frontend-web`
33. `curso-practico-de-informatica-basica`
34. `curso-practico-de-gnu-linux`
35. `preparacion-para-admision-unmsm`
36. `preparacion-para-admision-uni`
37. `preparacion-para-admision-unac`

La lista coincide exactamente con los cursos publicados y visibles de `data/cursos_tw_educa.json` y con su presencia en `data/catalogo_global.json`.

## 5. Convocatorias finales

El resultado final contiene 444 convocatorias: 37 cursos por 12 meses, desde agosto de 2026 hasta julio de 2027. Cada curso tiene exactamente 12 fechas y cada JSON mensual contiene exactamente 37 registros.

## 6. Redundancias eliminadas

Las tarjetas muestran únicamente la próxima fecha y un control compacto para desplegar las 12. Las páginas de detalle muestran cuatro filas inicialmente y las ocho restantes bajo `Mostrar las 12 fechas`. Se eliminaron tarjetas gigantes, precios únicos dentro del cronograma y repeticiones de fecha, hora y zona horaria.

## 7. Zona horaria

`America/Lima` se presenta una sola vez en el contexto del cronograma. La conversión a hora local solo aparece cuando la zona detectada por el navegador es distinta de Lima.

## 8. Precios PEN

Se preservaron sin alterar las tablas PEN existentes por perfil y etapa comercial. Los 37 cursos conservan Preventa, Lanzamiento y Regular; 28 cursos tienen dos perfiles y nueve cursos tienen tres.

## 9. Precios USD

Se añadió una tabla USD paralela para cada curso, con los mismos perfiles y etapas que la tabla PEN. La conversión está centralizada en `data/precios_internacionales_tw_educa.json`, usa redondeo entero hacia arriba y el tipo de venta referencial revisado de `3.411 PEN/USD`, con fecha de referencia 2026-07-24 y revisión 2026-07-29. La tarifa internacional queda sujeta a confirmación comercial y a eventuales comisiones del medio de pago.

## 10. Perfiles y etapas

El validador exige igualdad exacta entre los perfiles PEN originales y los perfiles USD generados. Para cada perfil comprueba las tres etapas: Preventa, Lanzamiento y Regular. También protege los cursos con perfil Premium para evitar su pérdida.

## 11. Opciones de pago

Se mantuvieron las opciones vigentes de pago y se añadió un bloque explícito para pagos internacionales. PayPal continúa disponible mediante enlace coordinado; la página aclara que tipo de cambio, comisión y total deben confirmarse antes del pago.

## 12. Diseño y comportamiento adaptable

El contenido central respeta el máximo aprobado de 1440 px. La vista anual utiliza cuatro columnas en escritorio, dos en tableta y una en móvil. Se corrigieron anchos mínimos y quiebres de texto para evitar desbordamiento horizontal, sin `scale`, `zoom` ni duplicación de paneles.

## 13. Validadores ejecutados

Pasaron:

- `python tools/validar_cronograma_tw_educa.py`
- `python tools/validar_layout_columna_central.py`
- `python tools/validar_no_paneles_duplicados.py`
- `python tools/validar_version_assets.py`
- comprobación sintáctica de JavaScript con Node
- compilación sintáctica de los scripts Python modificados
- comprobación de idempotencia del generador
- revisión de diferencias y búsqueda de credenciales

El validador específico confirmó 37 cursos, 444 convocatorias, 37 páginas protegidas y 45 JSON válidos.

La política del repositorio menciona `tools/validar_layout_tres_paneles.py`, pero ese archivo no existe en el árbol actual. Se ejecutó en su lugar el validador de diseño disponible, `tools/validar_layout_columna_central.py`, además del control independiente de paneles duplicados.

## 14. Validación HTTP

Se probaron 118 URL únicas tanto localmente como en GitHub Pages: sitemap, 37 rutas de curso, páginas de TW Educa, cronograma anual, pagos y archivos JSON canónicos. Resultado de la primera publicación: 118 respuestas HTTP 200, cero HTTP 404 y cero respuestas inesperadas.

## 15. Consola y navegador

La consola quedó sin errores. Se verificaron los 37 detalles, tablas PEN/USD, temarios, PayPal, mensajes de WhatsApp, filtros y las 444 tarjetas de la vista de todos los meses. Las resoluciones verificadas incluyen 1920, 1366, 1024, 768, 430, 390 y 360 px, sin desbordamiento horizontal.

## 16. Commit técnico

Primer commit:

`981411c0f7bf15c389c5f324699b00e07582fe7a` — `fix: restrict TW Educa schedule to 37 published courses`

El segundo commit contiene exclusivamente este reporte de cierre y usa el mensaje autorizado para documentar la preservación de precios escalonados PEN y USD.

## 17. Push

El primer commit fue enviado correctamente a `origin/main`. El segundo push se verifica después de crear el commit de este reporte.

## 18. GitHub Pages y riesgos pendientes

La ejecución de Pages `30432243794` para el primer commit terminó correctamente y las 118 URL públicas pasaron la comprobación. El despliegue del segundo commit se supervisa hasta estado exitoso.

Riesgos residuales:

- Las fechas continúan sujetas a confirmación de grupo mínimo y calendario comercial.
- Las tarifas internacionales deben confirmarse antes del pago por variaciones del tipo de cambio y comisiones.
- El tipo referencial USD debe revisarse periódicamente; no es una cotización irrevocable.
