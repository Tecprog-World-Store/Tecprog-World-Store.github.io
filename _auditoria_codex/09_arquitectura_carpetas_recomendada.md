# Arquitectura de carpetas recomendada

## Mantener

- ssets/css/: estilos globales.
- ssets/js/: componentes reutilizables y renderizadores de catalogos.
- ssets/img/: imagenes optimizadas por dominio.
- ssets/pdf/: solo PDF finales publicos.
- data/: JSON consumidos por GitHub Pages.
- data/fuentes/: TXT base usados para generar JSON.
- docs/: politicas y documentacion tecnica.
- scripts/: generadores y validadores.

## Documentar mejor

- data/fuente/: parece carpeta legacy; consolidar gradualmente en data/fuentes/.
- lineas/: distinguir paginas canonicas de alias.
- servicios/: separar paginas historicas de servicios actuales por catalogo.
- catalogo/: documentar que contiene catalogos por linea, cursos, compendios, descargas y PDFs.

## Recomendacion de canon

- Canon salud: TW Salud y Vida - Prótesis y Tecnología Médica.
- Nombre corto publico: TW Salud.
- Catalogos comerciales por linea: catalogo/tw-salud.html, catalogo/tw-innova.html, catalogo/tw-inox.html, catalogo/tw-construye.html.
- Detalle comercial unificado: detalle/oferta.html?id=...&linea=....
