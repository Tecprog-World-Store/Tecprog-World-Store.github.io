# 17. Documentacion de mantenimiento

Fecha: 2026-06-10

## Objetivo aplicado

Se agrego documentacion para mantener la arquitectura del sitio Tecprog World sin depender de IA y sin mover archivos.

## Archivos creados

- `docs/ARQUITECTURA_DEL_PROYECTO.md`
- `docs/CHECKLIST_PUBLICACION.md`
- `_auditoria_codex/17_documentacion_mantenimiento.md`

## Alcance documentado

`docs/ARQUITECTURA_DEL_PROYECTO.md` explica:

- Estructura general del repositorio.
- Donde colocar imagenes.
- Donde colocar PDF.
- Donde colocar fuentes TXT.
- Donde editar catalogos.
- Como agregar un curso.
- Como agregar un servicio.
- Como agregar un producto.
- Como agregar un PDF.
- Como agregar una imagen.
- Como cambiar precios.
- Como revisar UTF-8.
- Como publicar en GitHub Pages.
- Que archivos no subir.
- Como hacer backup antes de cambios grandes.

`docs/CHECKLIST_PUBLICACION.md` incluye lista de revision para:

- Enlaces.
- Precios.
- WhatsApp.
- Footer.
- PDF.
- Imagenes.
- UTF-8.
- Responsive.
- Consola.
- Commit.
- Push.

## Decisiones

- No se movieron archivos.
- No se eliminaron archivos.
- Se respeto la estructura actual.
- Se documento la arquitectura existente, incluyendo `_auditoria_codex/` como carpeta de reportes.
- Se referenciaron scripts existentes como `scripts/revisar_utf8.bat`, `scripts/revisar_utf8.py`, generadores de catalogo y optimizacion de imagenes.

## Recomendaciones siguientes

- Mantener `docs/ARQUITECTURA_DEL_PROYECTO.md` actualizado cuando se creen nuevas carpetas.
- Agregar ejemplos concretos por tipo de JSON si se estabiliza el esquema final.
- Convertir los reportes de auditoria mas importantes en tareas de mantenimiento incremental.
- Antes de reorganizar carpetas, crear un reporte de propuesta y revisar impacto en rutas de GitHub Pages.
