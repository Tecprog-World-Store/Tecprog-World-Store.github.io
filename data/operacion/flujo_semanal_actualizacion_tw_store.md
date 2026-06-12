# Flujo semanal de actualizacion TW Store

Este flujo ayuda a mantener TW Store ordenado, liviano y transparente.

## 1. Revisar precios fuente

Consultar las URLs registradas en `data/productos_store.json`. Verificar si el precio fuente se mantiene, subio, bajo o requiere revision manual.

## 2. Revisar stock

Confirmar si el producto sigue disponible o si debe marcarse como stock por confirmar, bajo pedido o no disponible temporalmente.

## 3. Elegir 5 productos para campana

Seleccionar cinco productos con mejor potencial comercial de la semana. Priorizar productos visuales, utiles, con margen razonable y orientados a estudiantes, profesionales, gamers o creadores de contenido.

## 4. Actualizar data/productos_store.json

Actualizar precio fuente, precio TW Store, estado, etiquetas, gancho comercial y fecha de revision cuando corresponda.

## 5. Actualizar data/campanias/top_productos_semana.json

Registrar los cinco productos priorizados con motivo de seleccion, idea de flyer, textos para redes y mensaje de WhatsApp.

## 6. Generar briefs visuales

Actualizar o generar los briefs de `data/visual/visual_briefs_store.json` para mantener consistencia en flyers y piezas de Canva.

## 7. Preparar flyers

Usar la plantilla de Canva o los HTML de previsualizacion. Mantener producto centrado, precio visible, CTA de WhatsApp y aviso de disponibilidad.

## 8. Revisar textos

Antes de publicar, revisar que no se prometa stock inmediato, garantia no validada ni representacion oficial de marcas externas.

## 9. Publicar manualmente

Publicar de forma manual en las redes o canales elegidos. No automatizar publicaciones sin revision humana.

## 10. Medir consultas por WhatsApp

Registrar que productos generaron consultas, que objeciones aparecieron y que productos no tuvieron traccion.

## 11. Retirar productos sin traccion

Retirar o pausar productos sin consultas en 30 dias, con precio inestable, baja disponibilidad o margen insuficiente.

## 12. Documentar cambios

Anotar fecha de revision, productos actualizados, productos retirados, cambios de precio y observaciones operativas.

## Comandos utiles

```powershell
python tools\revisar_catalogo_fuentes.py
python tools\generar_flyers_html_tw_store.py
```
