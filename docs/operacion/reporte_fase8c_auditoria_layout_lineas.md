# Reporte Fase 8C - Auditoría de layout de líneas

## Tabla por página

| Página | Estado inicial | Panel izquierdo | Panel central | Panel derecho | Buscador arriba | Problema principal | Cambio recomendado | Estado final |
|---|---|---|---|---|---|---|---|---|
| /store/index.html | Parcial | Sí | Sí | Sí | No, hero arriba | No, catálogo debajo | Reordenar catálogo primero, buscador central y cards 1:1 | Corregida |
| /educa/index.html | Parcial | Sí | Sí | Sí | No, hero/video arriba | No, catálogo debajo | Reordenar catálogo primero, preservar video abajo | Corregida |
| /innova/index.html | Parcial | Sí | Sí | Sí | No, hero arriba | No, catálogo debajo | Reordenar catálogo primero | Corregida |
| /salud/index.html | Parcial | Sí | Sí | Sí | No, hero arriba | No, catálogo debajo | Reordenar catálogo primero | Corregida |
| /interactive/index.html | Parcial | Sí | Sí | Sí | No, hero arriba | No, catálogo debajo | Reordenar catálogo primero | Corregida |
| /construye/index.html | Parcial | Sí | Sí | Sí | No, hero arriba | No, catálogo debajo | Reordenar catálogo primero | Corregida |
| /inox/index.html | Parcial | Sí | Sí | Sí | No, hero arriba | No, catálogo debajo | Reordenar catálogo primero | Corregida |
| /investiga/index.html | Parcial | Sí | Sí | Sí | No, hero arriba | No, catálogo debajo | Reordenar catálogo primero | Corregida |
| /disfruta/index.html | Parcial | Sí | Sí | Sí | No, hero arriba | No, catálogo debajo | Reordenar catálogo primero | Corregida |

## Problemas encontrados

- El motor de catálogo ya generaba estructura de tres paneles, pero en las páginas de línea aparecía debajo de un hero grande.
- TW Educa tenía video antes del catálogo, lo que desplazaba cursos y búsqueda.
- Las cards usaban imagen contenida con espacio interno, no un formato comercial cuadrado.
- Había textos visibles con mojibake en paneles y páginas, especialmente `Catálogo`, `Tecnología`, `técnico`, `Guías` y variantes.

## Páginas que ya cumplían parcialmente

Todas las páginas objetivo ya usaban `assets/js/catalogo-global.js` y `commerce-shell`, por lo que se reutilizó el motor existente sin duplicar HTML comercial.

## Páginas corregidas

Se corrigieron las nueve páginas objetivo: Store, Educa, Innova, Salud, Interactive, Construye, Inox, Investiga y Disfruta.
