# REPORTE DE DEPURACIÓN FINAL DEL REPOSITORIO

Fecha de cierre: 2026-07-29
Repositorio: `C:\Users\ACER\Documents\GitHub\Tecprog-World-Store.github.io`
Archivo externo: `C:\Users\ACER\Documents\GitHub\Tecprog-World-Store-archivo`

## 1. Resumen ejecutivo

La depuración final quedó completada sobre `main` sin cambiar la arquitectura pública protegida, las rutas SEO, los canonicals, los precios ni las políticas comerciales. Se retiraron del repositorio público fuentes editoriales, documentación histórica, recursos sin consumidor, duplicados y originales pesados ya sustituidos por WebP.

El lote técnico quedó publicado en GitHub Pages mediante el commit `54e34e053899aba79b4705b9b77c14bf86290c7d`. El workflow `pages build and deployment` terminó correctamente y la validación pública confirmó 100 URL HTTP 200, 0 URL HTTP 404 y consola limpia en 14 páginas críticas.

## 2. Estado inicial

| Métrica | Valor inicial |
|---|---:|
| Archivos | 813 |
| Carpetas | 140 |
| Tamaño | 424.893.545 bytes |
| Rama inicial | `fase-02-correcciones-seo-limpieza-segura` |
| `main` remota integrada | Sí, merge `0c1ce8e` |
| Cambios locales ajenos | 0 |

Se crearon antes de modificar:

- Etiqueta local `pre-depuracion-final-20260728`.
- Rama local `respaldo-pre-depuracion-final-20260728`.

Ambas apuntan al estado integrado `0c1ce8e8f512889f5881379e3bce23aa502f313f`.

## 3. Estado final

| Métrica | Valor final |
|---|---:|
| Archivos | 445, incluido este reporte |
| Carpetas | 108 |
| Tamaño | 58.436.713 bytes |
| Archivos archivados | 380 |
| Bytes archivados | 370.357.189 |
| Archivos eliminados reproducibles | 19 `.gitkeep` |
| Carpetas vacías retiradas | 32 |
| Grupos SHA-256 duplicados restantes | 0 |
| Recursos multimedia sin consumidor restantes | 0 |

## 4. Archivos conservados

Se conservaron:

- Las 100 páginas públicas declaradas en `sitemap.xml`.
- Los HTML operativos de portada, líneas, catálogos, cursos, detalles, empresa, legal, pagos, servicios y herramientas.
- `assets/css/styles.css` y los 14 JavaScript operativos.
- Los JSON canónicos y los datos consumidos por frontend, generadores o validadores.
- Los PNG de Open Graph realmente utilizados.
- Los tres MP3 activos declarados en `assets/audio/playlist.json`.
- Los PDF públicos y sus iframes.
- `README.md`, `AGENTS.md`, los cinco documentos generales imprescindibles y `docs/restricciones_codex/**`.
- Los scripts de generación y validación necesarios para mantenimiento.

De los 16 JSON del grupo histórico “sin consumo confirmado”, se conservaron 9 por dependencia o valor comercial vigente:

- `data/imagenes_pendientes.json`
- `data/lineas.json`
- `data/ofertas.json`
- `data/politica_precios_tw_educa.json`
- `data/precios.json`
- `data/productos_store.json`
- `data/tw-interactive.json`
- `data/tw-salud.json`
- `data/visual/visual_briefs_store.json`

## 5. Archivos archivados

El manifiesto final contiene 380 filas verificadas:

| Categoría | Archivos | Bytes |
|---|---:|---:|
| Documentación histórica | 68 | 2.951.336 |
| Fuentes editoriales | 94 | 68.319.228 |
| Fuentes maestras de imágenes optimizadas | 40 | 62.869.950 |
| JSON editoriales no consumidos | 7 | 23.639 |
| Recursos no operativos | 168 | 236.133.516 |
| Reportes históricos | 3 | 59.520 |
| **Total** | **380** | **370.357.189** |

Cada fila registra origen, destino, categoría, motivo, tamaño, SHA-256, estado de copia, verificación, acción final, timestamp y procedimiento de restauración.

## 6. Archivos eliminados

Se eliminaron sin archivar 19 archivos `.gitkeep` de un byte. Eran marcadores reproducibles y su retirada permitió eliminar carpetas vacías. No se eliminó ningún recurso operativo sin copia externa verificada.

## 7. Duplicados resueltos

Se resolvieron los diez duplicados operativos:

- Nueve pares PNG de flyers dejaron de existir en las rutas duplicadas `assets/img/flyers/` y `assets/img/store/flyers/`. La ruta operativa canónica es ahora el WebP correspondiente bajo `assets/img/store/flyers/`; los PNG fuente están en el archivo externo.
- `data/fuentes/catalogo_base_cursos_tw_educa.txt` quedó como fuente canónica.
- `data/fuente/catalogo_base_cursos_tw_educa.txt` fue archivado y retirado.

La revisión SHA-256 final no encontró grupos duplicados.

## 8. Recursos optimizados

Se migraron 40 imágenes activas mayores de 500 KB desde PNG/JPG hacia WebP, sin redimensionar ni cambiar proporciones.

- Peso original: 62.869.950 bytes.
- Peso WebP resultante: 4.960.574 bytes.
- Reducción del lote: 57.909.376 bytes, equivalente a 92,1 %.
- Archivos WebP nuevos: 30.
- WebP existentes reutilizados: 10.
- Consumidores actualizados: 26 archivos HTML, JavaScript y JSON.
- PNG de Open Graph modificados: 0.

La comparación visual de muestras de producto y banner no mostró degradación apreciable.

## 9. Tratamiento de `Cursos a dictar`

Los 76 archivos, 68.197.358 bytes, fueron clasificados como fuentes editoriales:

- 37 PNG de piezas maestras.
- 39 TXT de temarios, índice y manifiesto.

No tenían coincidencias SHA-256 con los recursos operativos ni consumidores públicos. Fueron copiados a:

`C:\Users\ACER\Documents\GitHub\Tecprog-World-Store-archivo\fuentes-editoriales\Cursos a dictar\`

La copia se verificó antes de retirar los originales. La carpeta pública quedó eliminada.

## 10. Tratamiento de los 183 no referenciados

El grupo histórico de 183 quedó completamente resuelto:

- 167 recursos multimedia del grupo original: archivados.
- 7 JSON editoriales: archivados.
- 9 JSON con dependencia de frontend, herramientas o política comercial: conservados y justificados.

Además se detectó y archivó un recurso multimedia adicional que quedó huérfano después de integrar las fases anteriores. El recálculo final registra 0 recursos multimedia sin consumidor.

## 11. Tratamiento de los diez duplicados

Los nueve pares de flyers se canonicalizaron hacia WebP bajo `assets/img/store/flyers/`. El TXT duplicado se canonicalizó hacia `data/fuentes/`. No quedan consumidores de las copias secundarias ni carpetas `data/fuente` y `data/fuentes` paralelas.

## 12. Nueva arquitectura

La arquitectura pública conserva las URL existentes y GitHub Pages desde la raíz:

```text
/
├── index.html
├── assets/
├── data/
├── catalogo/
├── cursos/
├── detalle/
├── lineas/
├── store/, educa/, disfruta/, innova/, salud/
├── interactive/, construye/, inox/, investiga/
├── empresa/, legal/, pagos/, servicios/, herramientas/
├── scripts/
├── tools/
├── docs/
│   └── restricciones_codex/
├── sitemap.xml
├── robots.txt
├── site.webmanifest
├── README.md
├── AGENTS.md
├── LICENSE
└── REPORTE_DEPURACION_FINAL_REPOSITORIO.md
```

No se movieron URL públicas por estética y no se alteró el esquema de tres paneles.

## 13. Tamaño antes y después

- Antes: 424.893.545 bytes.
- Después: 58.436.713 bytes.
- Reducción final: 366.456.832 bytes.
- Porcentaje de reducción final: 86,25 %.
- Bytes archivados: 370.357.189.
- Bytes eliminados reproducibles: 19.

## 14. Resultados HTTP

Validación local:

- XML válido: sí.
- URL únicas del sitemap: 100.
- HTTP 200: 100.
- HTTP 404: 0.
- Recursos y enlaces locales extraídos de las páginas: 134/134 HTTP 200.
- Rutas de activos en 22 JSON críticos: 169/169 presentes.

Validación pública:

- Workflow GitHub Pages: `success`.
- URL probadas: 100.
- HTTP 200: 100.
- HTTP 404: 0.
- WebP nuevo de control: HTTP 200.
- PNG retirado de control: HTTP 404 y sin consumidores.

## 15. Resultados de consola

Se probaron 30 páginas representativas en navegador local y 14 páginas críticas en el sitio publicado.

- Errores propios de JavaScript en producción: 0.
- Advertencias de consola en la muestra pública: 0.
- Título, canonical, Open Graph, CSS y JavaScript: presentes en 14/14 páginas públicas críticas.
- Páginas con enlaces WhatsApp en la muestra local: 29/30.
- Páginas con enlaces PayPal en la muestra local: 6/30.
- Formularios locales detectados: calculadora de precios; no se enviaron datos.

## 16. Resultado de validadores

Los tres validadores terminaron con código 0 antes de modificar, después de cada lote y antes del commit:

```text
OK: paginas clave respetan maximo tres paneles y separan paneles locales/globales.
OK: no hay paneles estructurales duplicados ni referencias legacy en HTML publico.
OK: assets CSS/JS locales usan v=20260708-01 sin duplicados por pagina.
```

Los JSON restantes se analizaron correctamente y `git diff --check` no detectó errores.

## 17. Diagnóstico del iframe PDF

`catalogo/catalogo-mensual.html` conserva el iframe y el PDF operativo. El repositorio no contiene `MutationObserver`; la búsqueda estructural y textual solo encontró `IntersectionObserver`.

La excepción:

`Failed to execute 'observe' on 'MutationObserver': parameter 1 is not of type 'Node'`

apareció durante la instrumentación local del iframe, sin URL de código propio. En la muestra publicada final, incluida la página mensual, la consola quedó limpia. Chrome local no pudo aportar una segunda lectura aislada porque otra interfaz de extensión bloqueó el control automatizado. La evidencia disponible atribuye la excepción a instrumentación/extensión, no al sitio. No se modificó código ni se retiró el iframe.

## 18. Commits creados

1. `54e34e0 chore: archive optimize and canonicalize static resources`
2. Commit posterior: incorporación de este reporte final.

## 19. Hash del último commit

Commit técnico publicado y validado:

`54e34e053899aba79b4705b9b77c14bf86290c7d`

El commit que incorpora este mismo reporte es necesariamente posterior; su hash no puede autoescribirse dentro de su propio contenido porque modificaría el hash. Se informa en la respuesta final de cierre.

## 20. Resultado del push

`git push origin main` terminó correctamente:

`0c1ce8e..54e34e0 main -> main`

No se utilizó `--force`.

## 21. Resultado del sitio publicado

GitHub Pages desplegó correctamente `54e34e0`. Se verificaron portada, Store, Educa, cinco cursos, catálogos, detalle, empresa, pagos Perú, pagos internacionales, sitemap y robots. Las 100 URL públicas respondieron 200 y la muestra de navegador no registró errores de consola.

## 22. Riesgos pendientes

- `data/imagenes_pendientes.json` conserva 8 imágenes futuras no publicadas; no son referencias operativas rotas.
- Cinco WebP activos pesan entre 259 y 350 KB. Están por debajo del umbral prioritario de 500 KB y no se recomprimieron para evitar pérdida acumulativa.
- La excepción local del iframe solo puede aislarse completamente en Chrome cuando no haya una interfaz de extensión bloqueando el control; producción quedó limpia.
- Los catálogos mensuales todavía requieren un flujo canónico para evitar snapshots duplicados.

## 23. Procedimiento de restauración

1. Buscar el archivo en `MANIFIESTO_DEPURACION_FINAL.csv`.
2. Verificar el SHA-256 del destino externo.
3. Crear únicamente la carpeta padre del origen.
4. Copiar sin sobrescribir silenciosamente un archivo diferente.
5. Restaurar el timestamp registrado.
6. Verificar tamaño y SHA-256.
7. Ejecutar los tres validadores, validar los JSON y probar las 100 URL.

La prueba de restauración aislada verificó 10/10 archivos de categorías distintas y retiró la carpeta temporal sin residuos.

## 24. Recomendaciones para cronogramas mensuales

Implementar un único archivo canónico por periodo, por ejemplo `data/cursos/2026-08.json`, con esquema validado y campos de vigencia. `catalogo/catalogo-mensual.html` debe consumir el periodo activo mediante un manifiesto mínimo como `data/cursos/actual.json`, mientras un script idempotente genera páginas sociales, actualiza sitemap y valida precios, fechas, imágenes y WhatsApp. Los periodos cerrados deben archivarse externamente, no duplicarse en varios JSON públicos.
