# README TW Store

TW Store es la linea comercial de e-commerce tecnologico de Tecprog World. Funciona como catalogo bajo pedido o dropshipping manual: el cliente consulta por WhatsApp y luego se confirma precio, stock, garantia y envio antes de avanzar.

No es una tienda transaccional con pagos en linea. GitHub Pages se usa como vitrina ligera, no como sistema de checkout.

## Como funciona TW Store

1. El cliente revisa productos en el catalogo.
2. El cliente presiona el boton de WhatsApp.
3. Se valida precio actualizado, disponibilidad, garantia y envio.
4. Se envia cotizacion manual.
5. Si el cliente acepta, se coordina el siguiente paso de forma manual.

Frase base:

Producto sujeto a disponibilidad, confirmacion de precio, garantia y condiciones de entrega.

## Como actualizar catalogo

Archivo principal:

```text
data/productos_store.json
```

Cada producto debe mantener:

- `id`
- `nombre`
- `categoria`
- `precio_fuente`
- `precio_publico`
- `fuente`
- `url_fuente`
- `estado`
- `etiquetas`
- `imagen`
- `gancho`
- `ultima_revision`

Antes de publicar cambios, validar que el JSON sea correcto:

```powershell
python -m json.tool data\productos_store.json > $null
```

## Como revisar precios

Usar el script operativo:

```powershell
python tools\revisar_catalogo_fuentes.py
```

El reporte se genera en:

```text
data/operacion/reporte_revision_catalogo.md
```

Si no quieres consultar URLs y solo deseas crear una plantilla de revision manual:

```powershell
python tools\revisar_catalogo_fuentes.py --sin-red
```

Importante: el script no reemplaza la revision humana. Si una fuente no puede leerse o el precio no se detecta de forma confiable, el producto debe revisarse manualmente.

## Como elegir productos de campana

Archivo semanal:

```text
data/campanias/top_productos_semana.json
```

Criterios recomendados:

- Producto visualmente atractivo.
- Util para estudiantes, profesionales, gamers o creadores.
- Precio competitivo.
- Margen aceptable.
- Stock o reposicion probable.
- Baja complejidad de gestion.

Usar tambien:

```text
data/marketing/criterios_rotacion_productos.md
data/marketing/calendario_contenido_tw_store.md
```

## Como cuidar el peso de imagenes

- Guardar imagenes de tienda en `assets/img/store/productos/`.
- Preferir WEBP o SVG livianos.
- Evitar subir imagenes grandes, duplicadas o sin comprimir.
- No descargar imagenes protegidas sin permiso.
- Usar placeholders propios si no hay imagen autorizada.
- Mantener nombres de archivo cortos, en minusculas y sin espacios.

## Como publicar manualmente

1. Revisar precio y stock.
2. Revisar texto del flyer o publicacion.
3. Confirmar que no promete stock inmediato, garantia no validada ni distribucion oficial.
4. Crear o editar pieza visual en Canva.
5. Publicar manualmente en la red elegida.
6. Responder consultas por WhatsApp con validacion previa.

No automatizar publicaciones sin revision humana.

## Como usar mensajes de WhatsApp

Plantillas:

```text
data/whatsapp/mensajes_modelo_tw_store.md
```

Antes de enviar:

- Personalizar el nombre del producto.
- Confirmar si el cliente esta en Lima o provincia.
- Validar precio, disponibilidad, garantia y envio.
- Evitar insistencia agresiva.
- No enviar mensajes masivos.

## Como evitar promesas comerciales no verificadas

No usar frases como:

- Stock garantizado.
- Entrega inmediata.
- Garantia oficial asegurada.
- Somos distribuidores oficiales.
- Precio final fijo.

Usar frases como:

- Precio sujeto a confirmacion.
- Stock por validar antes de la compra.
- Producto bajo pedido.
- Envio a coordinar.
- Garantia y entrega se confirman antes de la compra.

## Archivos operativos relacionados

```text
data/legal/politica_comercial_tw_store.md
data/legal/aviso_disponibilidad_tw_store.md
data/operacion/no_automatizar_tw_store.md
data/operacion/flujo_semanal_actualizacion_tw_store.md
data/operacion/reporte_revision_catalogo.md
```

## Comandos utiles

```powershell
python tools\revisar_catalogo_fuentes.py
python tools\generar_flyers_html_tw_store.py
python -m json.tool data\productos_store.json > $null
python -m json.tool data\campanias\top_productos_semana.json > $null
```
