# Checklist Publicacion Layout Estable

Fecha: 2026-07-08.

Antes de publicar:

- Confirmar que no existe `service-worker.js` ni `sw.js`.
- Ejecutar `python tools/actualizar_version_assets.py --version NUEVA_VERSION` si se cambia CSS o JS.
- Ejecutar `python tools/validar_version_assets.py`.
- Ejecutar `python tools/validar_no_paneles_duplicados.py`.
- Ejecutar `python tools/validar_layout_tres_paneles.py`.
- Probar primera carga sin F5 en `/`, `/store/`, `/educa/`, `/disfruta/`, `/innova/`, `/salud/`, `/interactive/`, `/construye/`, `/inox/`, `/investiga/`, `/pagos/peru.html`.
- Probar resoluciones 390x844, 768x1024, 1366x768 y 1920x1080.
- Verificar que no hay overflow horizontal.
- Verificar navegacion, filtros, cards y enlaces WhatsApp.
- Confirmar que no hay errores de consola.
- Confirmar que no se hizo commit ni push si la tarea no lo pidio.
