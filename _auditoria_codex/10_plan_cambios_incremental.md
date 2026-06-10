# Plan de cambios incremental

## Fase 1 - Consolidacion documental

1. Definir oficialmente la linea canonica TW Salud y Vida - Prótesis y Tecnología Médica.
2. Documentar alias permitidos y redirecciones internas.
3. Marcar paginas historicas o alias en README y mapa del sitio.

## Fase 2 - Navegacion y contenido

1. Unificar menu superior y footer con nombres canonicos.
2. Revisar paginas con menos de 120 palabras y ampliar contenido util.
3. Reemplazar enlaces href="#" por acciones reales o botones con JS documentado.
4. Validar rutas relativas por carpeta.

## Fase 3 - Catalogos y precios

1. Definir matriz de precios por tipo: MOOC, taller, curso, programa, servicio.
2. Revisar JSON con precios cero o solo cotizacion.
3. Separar material digital, curso y asesoria.

## Fase 4 - Activos y peso

1. Documentar PDFs finales y fuentes externas.
2. Optimizar imagenes grandes y mantener WebP cuando aplique.
3. Revisar peso total antes de publicar.

## Fase 5 - Validacion antes de cambios mayores

1. Ejecutar scripts/revisar_utf8.bat.
2. Validar JSON con python -m json.tool.
3. Validar HTML clave en navegador local.
4. Revisar consola y enlaces internos.
