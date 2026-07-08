# Reporte De Proteccion Cambios Aprobados

Fecha: 2026-07-08.

## Restricciones creadas

Carpeta: `docs/restricciones_codex/`.

Archivos:

- `ARQUITECTURA_APROBADA.md`
- `CAMBIOS_PROTEGIDOS.md`
- `REGLAS_NO_REGRESION.md`
- `CHECKLIST_ANTES_DE_MODIFICAR.md`
- `INVENTARIO_ARCHIVOS_CRITICOS.md`

## Archivo raiz

Se creo `AGENTS.md` con instrucciones explicitas para Codex:

- Leer restricciones primero.
- No alterar arquitectura aprobada sin orden explicita.
- No duplicar paneles.
- Ejecutar validadores.
- Crear backup antes de cambios estructurales.
- No hacer commit ni push.
- Mantener GitHub Pages, SEO, Open Graph y mensajes comerciales.
- Reportar conflictos entre instrucciones nuevas y restricciones previas.

## Validadores creados

- `tools/validar_layout_tres_paneles.py`
- `tools/validar_version_assets.py`
- `tools/validar_no_paneles_duplicados.py`
- `tools/actualizar_version_assets.py`

## Estado

Las restricciones y validadores quedan disponibles para futuras tareas y deben ejecutarse antes de cambios estructurales.
