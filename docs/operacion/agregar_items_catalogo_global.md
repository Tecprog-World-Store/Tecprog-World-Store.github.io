# Cómo agregar items al catálogo global

Archivo principal: `data/catalogo_global.json`

## 1. Crear un nuevo objeto

Agrega un objeto dentro del arreglo JSON. El `id` debe ser único, estable y en minúsculas, por ejemplo:

```json
{
  "id": "tw-educa-009",
  "linea_negocio": "tw-educa",
  "categoria": "Programación",
  "nombre": "Curso JavaScript aplicado",
  "descripcion_corta": "Curso práctico para crear interfaces web interactivas.",
  "descripcion_larga": "Curso sujeto a modalidad, fechas, vacantes y alcance del temario.",
  "precio_soles": null,
  "precio_dolares": null,
  "moneda_principal": "PEN",
  "tipo_item": "curso",
  "estado": "cotizar",
  "tags": ["javascript", "web", "programación"],
  "imagen": "assets/img/cursos/curso-tecnologia-negocios.svg",
  "banner": "assets/img/banners/tw-educa/banner-tw-educa-01.png",
  "url_detalle": "detalle/item.html?id=tw-educa-009",
  "whatsapp_mensaje": "Hola Tecprog World, deseo información sobre el Curso JavaScript aplicado.",
  "destacado": false,
  "oferta": false,
  "fecha_actualizacion": "2026-06-12",
  "visible_cliente": true
}
```

## 2. Campos obligatorios

- `id`
- `linea_negocio`
- `categoria`
- `nombre`
- `descripcion_corta`
- `descripcion_larga`
- `precio_soles`
- `precio_dolares`
- `moneda_principal`
- `tipo_item`
- `estado`
- `tags`
- `imagen`
- `banner`
- `url_detalle`
- `whatsapp_mensaje`
- `destacado`
- `oferta`
- `fecha_actualizacion`
- `visible_cliente`

## 3. Líneas de negocio válidas

- `tw-store`
- `tw-disfruta`
- `tw-educa`
- `tw-innova`
- `tw-salud`
- `tw-interactive`
- `tw-construye`
- `tw-inox`
- `tw-investiga`

## 4. Precio y estado

Si hay precio público:

```json
"precio_soles": 120,
"precio_dolares": null,
"estado": "bajo_pedido"
```

Si todavía no hay precio definido:

```json
"precio_soles": null,
"precio_dolares": null,
"estado": "cotizar"
```

Estados recomendados:

- `disponible`
- `bajo_pedido`
- `cotizar`
- `proximamente`

No prometas stock inmediato ni garantía sin confirmación.

## 5. Imágenes placeholder

Usa assets locales existentes mientras no haya imagen final:

- Producto genérico: `assets/img/store/placeholders/producto-generico.svg`
- Celular: `assets/img/store/placeholders/celular.svg`
- Laptop: `assets/img/store/placeholders/laptop.svg`
- Monitor: `assets/img/store/placeholders/monitor.svg`
- Audio: `assets/img/store/placeholders/audifonos.svg`
- Realidad virtual: `assets/img/store/placeholders/realidad-virtual.svg`

## 6. URL de detalle

Cada item debe tener:

```json
"url_detalle": "detalle/item.html?id=ID_DEL_ITEM"
```

Ejemplo:

```json
"url_detalle": "detalle/item.html?id=tw-store-001"
```

## 7. Mensaje de WhatsApp

Debe ser claro y específico:

```json
"whatsapp_mensaje": "Hola Tecprog World, deseo cotizar el producto iPhone 16e 5G 128GB de TW Store. ¿Está disponible para envío?"
```

No uses mensajes que afirmen stock o garantía confirmada.

## 8. Campos que no deben ser públicos

No agregar al catálogo global público:

- `precio_fuente`
- `precio_proveedor`
- `precio_compra`
- `margen_sugerido`
- `margen_interno`
- `proveedor`
- `fuente`
- `url_fuente`
- `url_fuente_interna`
- datos de scraping

Si se necesitan para operación interna, deben vivir en un archivo privado o de backoffice, no en el render público.

## 9. Cómo probar

1. Validar JSON:

```bash
node -e "JSON.parse(require('fs').readFileSync('data/catalogo_global.json','utf8')); console.log('OK')"
```

2. Abrir:

```text
http://localhost:8000/store/index.html
```

3. Buscar el nombre del item.

4. Probar filtros por línea, categoría y estado.

5. Abrir detalle:

```text
http://localhost:8000/detalle/item.html?id=ID_DEL_ITEM
```

6. Confirmar que no aparecen datos internos.

## 10. Preparar imagen futura

Agregar entrada en `data/imagenes_pendientes.json`:

```json
{
  "id": "tw-educa-009",
  "linea_negocio": "tw-educa",
  "archivo_esperado": "assets/img/catalogo/tw-educa/tw-educa-009.webp",
  "estado": "pendiente",
  "prompt_sugerido": "Imagen comercial para Curso JavaScript aplicado..."
}
```

