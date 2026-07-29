# REPORTE FASE 03A — ARCHIVADO EXTERNO REVERSIBLE

## 1. Resumen ejecutivo

Se archivaron externamente y se retiraron del repositorio operativo exactamente 372 archivos autorizados. La copia externa conserva la estructura relativa y fue verificada archivo por archivo mediante tamaño y SHA-256. No hubo faltantes, diferencias ni extras inesperados. La prueba de restauración de 11 archivos fue correcta y la carpeta temporal quedó vacía.

La operación de archivado quedó completada y es reversible sin depender de Git. La validación funcional confirmó 100 URL HTTP 200, 0 rutas 404, recursos e imágenes correctos y los tres validadores protegidos con código 0. Queda documentada una observación de navegador: la instrumentación del navegador integrado emitió una excepción `MutationObserver` al cargar el iframe PDF de `catalogo/catalogo-mensual.html`. No se detectó relación con los archivos archivados y no se modificó código operativo fuera del alcance.

## 2. Estado inicial de Git

El estado inicial correspondía exclusivamente a la FASE 02 y sus dos informes:

- Modificados: `.gitignore`, `assets/js/detalle.js`, `data/sitemap_comercial.json` y `sitemap.xml`.
- Eliminados por FASE 02: seis archivos versionados de `.idea/` y tres archivos `.pyc` de `tools/__pycache__/`.
- Eliminado e ignorado por FASE 02: `.idea/workspace.xml`.
- Sin seguimiento: `AUDITORIA_REPOSITORIO_FASE_01.md` y `REPORTE_FASE_02_CORRECCIONES_Y_LIMPIEZA.md`.
- No se descartó ni revirtió ningún cambio previo.

## 3. Rama utilizada

`fase-02-correcciones-seo-limpieza-segura`

No se creó otra rama y no se ejecutó `git add`, `git commit` ni `git push`.

## 4. Conjuntos archivados

| Conjunto | Archivos | Bytes | Destino |
|---|---:|---:|---|
| `_auditoria_codex/**` | 23 | 178.428 | `auditorias-historicas/_auditoria_codex/**` |
| `backups/**` | 302 | 5.725.249 | `backups/**` |
| `build/**` | 43 | 955.876 | `builds-generados/build/**` |
| Cuatro JSON autorizados de `data/` | 4 | 339.162 | `snapshots-data/**` |
| **Total** | **372** | **7.198.715** | |

Los cuatro JSON fueron:

- `data/catalogo_global.backup_fase7.json`
- `data/catalogo_global.backup_fase8f.json`
- `data/cursos_tw_educa.backup_fase8f.json`
- `data/imagenes_pendientes.backup-fase8-cierre-20260612-204801.json`

## 5. Cantidad esperada y cantidad real

- Cantidad esperada: 372 archivos.
- Cantidad inventariada: 372 archivos.
- Cantidad copiada: 372 archivos.
- Cantidad verificada: 372 archivos.
- Cantidad retirada: 372 archivos.
- Diferencia: 0 archivos.

## 6. Tamaño esperado y tamaño real

- Referencia esperada: cerca de 6,9 MB.
- Medición real: 7.198.715 bytes, equivalentes a 7,199 MB decimales o 6,87 MiB.
- Diferencias de tamaño entre origen y destino: 0.

## 7. Estructura externa creada

La estructura se creó fuera del repositorio, en:

`C:\Users\ACER\Documents\GitHub\Tecprog-World-Store-archivo`

Contiene:

- `auditorias-historicas`
- `backups`
- `builds-generados`
- `snapshots-data`
- `manifiestos`
- `pruebas-restauracion`

El destino externo no contiene `.git` y no fue inicializado como repositorio.

## 8. Resultado de la copia

- Copias nuevas realizadas: 372.
- Archivos previamente existentes idénticos: 0.
- Sobrescrituras: 0.
- Faltantes: 0.
- Extras inesperados dentro del lote: 0.
- Timestamps: se conservó `LastWriteTimeUtc` cuando fue técnicamente posible.

## 9. Resultado de verificación SHA-256

Los 372 archivos se compararon por tamaño y SHA-256 entre origen y destino antes de retirar los originales:

- Tamaños coincidentes: 372/372.
- SHA-256 coincidentes: 372/372.
- Diferencias de tamaño: 0.
- Diferencias de hash: 0.
- Muestra recalculada después de retirar originales: 11/11 hashes coincidentes.

## 10. Resultado de la prueba de restauración

Se restauró temporalmente desde el archivo externo una muestra de 11 archivos:

- 2 de `_auditoria_codex/**`.
- 3 de `backups/**`.
- 2 de `build/**`.
- Los 4 JSON autorizados.

La muestra obtuvo 11/11 coincidencias de cantidad, tamaño y SHA-256. Los JSON se analizaron correctamente; los textos fueron legibles y los demás archivos pudieron abrirse. Después de la prueba se retiraron exclusivamente las copias temporales. `pruebas-restauracion` quedó disponible y vacía.

## 11. Archivos retirados del repositorio

Se retiraron exactamente las 372 rutas incluidas en `MANIFIESTO_ARCHIVADO_FASE_03A.csv`. La comparación con Git confirmó 372 eliminaciones versionadas pertenecientes al lote y nueve eliminaciones versionadas previas de FASE 02, sin eliminaciones nuevas fuera del manifiesto.

## 12. Carpetas retiradas

Al quedar vacías se retiraron:

- `_auditoria_codex/`
- `backups/`
- `build/`

También se retiraron únicamente sus subcarpetas vacías. No se eliminó ninguna carpeta con archivos fuera del manifiesto.

## 13. Reducción de tamaño lograda

Medición excluyendo `.git` y realizada antes de crear este reporte:

| Métrica | Antes | Después de la retirada | Reducción |
|---|---:|---:|---:|
| Archivos | 1.184 | 812 | 372 |
| Carpetas | 335 | 140 | 195 |
| Bytes | 432.078.463 | 424.879.748 | 7.198.715 |

La reducción de bytes fue 1,6661 %. El archivo de reporte creado después de esta medición es documentación de la fase y no forma parte del lote archivado.

## 14. Estado de las referencias activas

No se encontraron dependencias públicas o de lectura hacia `_auditoria_codex/`, `backups/`, `build/` ni los cuatro JSON retirados.

La única mención operativa es `tools/generar_flyers_html_tw_store.py`, que define `build/flyers_html` como directorio de salida. El script crea ese directorio y sus artefactos; no lee ni depende de los 43 archivos archivados. Por ello no fue necesario restaurar ni excluir ningún elemento.

## 15. Resultado de validación del sitemap

- XML válido: sí.
- URL declaradas: 100.
- URL únicas: 100.
- Duplicadas: 0.
- Rutas locales: 0.

## 16. Resultado HTTP de las 100 URL

- URL probadas: 100.
- HTTP 200: 100.
- HTTP 404: 0.
- Otros errores HTTP: 0.

Además, en la muestra de navegador se verificaron 128 recursos locales y 357 enlaces internos: todos respondieron HTTP 200, incluidos los reintentos controlados tras saturación inicial de conexiones concurrentes.

## 17. Resultado de los tres validadores

Los tres comandos finalizaron con código 0:

```text
OK: paginas clave respetan maximo tres paneles y separan paneles locales/globales.
OK: no hay paneles estructurales duplicados ni referencias legacy en HTML publico.
OK: assets CSS/JS locales usan v=20260708-01 sin duplicados por pagina.
```

## 18. Resultado de prueba en navegador

Se probaron 25 páginas representativas: portada, Store, líneas comerciales, catálogos, cursos, detalles, empresa, pagos y páginas legales.

- Páginas con título: 25/25.
- Páginas con canonical: 25/25.
- Páginas con `og:title`: 25/25.
- Páginas con `og:url`: 25/25.
- Páginas con CSS local: 25/25.
- Páginas con JavaScript local: 25/25.
- Imágenes rotas: 0.
- Recursos locales revisados: 128/128 HTTP 200.
- Enlaces internos recopilados: 357/357 HTTP 200.
- JSON del repositorio analizados: 35/35 válidos.

El servidor local quedó detenido y no quedaron pestañas de prueba abiertas.

## 19. Errores o advertencias

- Advertencias de consola: 0.
- Excepciones observadas: 1.
- Página: `catalogo/catalogo-mensual.html`.
- Mensaje: `Failed to execute 'observe' on 'MutationObserver': parameter 1 is not of type 'Node'.`

La excepción apareció de forma aislada al instrumentar la página que contiene un iframe PDF. El código del sitio no contiene `MutationObserver`; el PDF, el HTML y los demás recursos locales respondieron 200, y la página conserva título, canonical, Open Graph, CSS, JavaScript e imágenes válidas. No se cambió código operativo porque la incidencia no está vinculada con el archivado y su corrección excedería el alcance autorizado.

## 20. Estado final de Git

- Rama: `fase-02-correcciones-seo-limpieza-segura`.
- Cambios previos de FASE 02: conservados.
- Eliminaciones de FASE 03A: 372, todas presentes en el manifiesto.
- Eliminaciones versionadas previas de FASE 02: 9.
- Nuevo archivo de FASE 03A dentro del repositorio: este reporte.
- No se ejecutó `git add`, `git commit` ni `git push`.

## 21. Ruta exacta de los manifiestos externos

- CSV: `C:\Users\ACER\Documents\GitHub\Tecprog-World-Store-archivo\manifiestos\MANIFIESTO_ARCHIVADO_FASE_03A.csv`
- Markdown: `C:\Users\ACER\Documents\GitHub\Tecprog-World-Store-archivo\manifiestos\MANIFIESTO_ARCHIVADO_FASE_03A.md`

Los manifiestos no se copiaron al repositorio público.

## 22. Procedimiento completo de restauración

### Restaurar un archivo individual

1. Buscar su fila en el CSV mediante `RutaRelativaOrigen`.
2. Confirmar que existe `RutaAbsolutaDestino`.
3. Calcular SHA-256 del archivo externo y compararlo con `SHA256`.
4. Crear únicamente la carpeta padre de `RutaAbsolutaOrigen`.
5. Copiar el archivo sin sobrescribir silenciosamente un archivo distinto.
6. Restaurar `LastWriteTimeUtc` usando `FechaModificacionUTC`.
7. Comparar tamaño y SHA-256 del archivo restaurado con el CSV.

### Restaurar un conjunto completo

1. Filtrar el CSV por `Conjunto`: `_auditoria_codex`, `backups`, `build` o `snapshots-data`.
2. Verificar previamente todos los destinos del conjunto.
3. Copiar cada fila hacia su `RutaAbsolutaOrigen`, conservando la estructura relativa.
4. Restaurar los timestamps y verificar tamaño y SHA-256 de cada archivo.

### Restaurar los 372 archivos

1. Confirmar que el CSV contiene exactamente 372 filas.
2. Verificar antes de copiar que los 372 destinos existen y coinciden con sus hashes.
3. Recorrer todas las filas y recrear exclusivamente sus carpetas padre.
4. Detenerse ante cualquier conflicto de destino, tamaño o hash.
5. Copiar los 372 archivos y restablecer sus timestamps.
6. Exigir 372/372 coincidencias de tamaño y SHA-256.
7. Ejecutar los tres validadores protegidos, validar el XML y probar las 100 URL.
8. Repetir una muestra de navegador y revisar consola, CSS, JavaScript, JSON, imágenes, canonicals, Open Graph y enlaces.

No se ejecutó la restauración completa; solo la muestra obligatoria de 11 archivos.

## 23. Riesgos pendientes

- La observación de instrumentación del iframe PDF debe aislarse en una fase de diagnóstico separada antes de afirmar cero excepciones de consola para esa página.
- `build/flyers_html` seguirá recreándose si se ejecuta su generador; debe mantenerse como salida ignorada o archivarse nuevamente según la política que se apruebe.
- Los 183 recursos no referenciados requieren una matriz de consumo antes de decidir su destino.
- Los diez duplicados operativos requieren definir rutas canónicas y migrar referencias antes de retirar copias.
- `Cursos a dictar/**` conserva 76 archivos y 68.197.358 bytes; no debe moverse sin confirmar que existe otra fuente maestra.

## 24. Recomendación para FASE 03B

Realizar una fase exclusivamente de clasificación, sin eliminaciones automáticas: construir una matriz verificable para los 183 recursos no referenciados y los diez duplicados operativos, registrar por archivo referencias estáticas, dinámicas, editoriales, Open Graph y de herramientas, y decidir por grupos pequeños si se conservan, canonicalizan o archivan. Mantener `Cursos a dictar/**` fuera de la retirada hasta confirmar su fuente maestra. En paralelo, reproducir la excepción del iframe PDF en un navegador independiente para distinguir definitivamente instrumentación del entorno y código del sitio.
