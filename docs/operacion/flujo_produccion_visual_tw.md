# Flujo de producción visual Tecprog World

## 1. Elegir objetivo visual

Selecciona una línea, producto bandera, curso, servicio o proyecto desde:

- `data/catalogo_global.json`
- `data/imagenes_pendientes.json`

## 2. Elegir prompt base

Para banners:

```text
data/visual/prompts_banners_lineas_tw.md
```

Para flyers:

```text
data/visual/prompts_flyers_productos_tw.md
```

## 3. Generar imagen externamente

Usa ChatGPT, Canva u otra herramienta aprobada. No usar imágenes de terceros sin permiso.

## 4. Exportar archivo inicial

Puedes exportar en PNG/JPG si la herramienta no entrega WebP. Mantén alta calidad inicial.

## 5. Convertir u optimizar a WebP

Ejecuta:

```bash
python tools/optimizar_imagenes_webp_tw.py
```

Si falta Pillow:

```bash
pip install pillow
```

## 6. Guardar en ruta correcta

Ejemplos:

- Banner: `assets/img/banners/tw-store.webp`
- Flyer: `assets/img/store/flyers/tw-store-portada.webp`
- Producto: `assets/img/store/productos/tw-store-001.webp`
- OG: `assets/img/store/og/tw-store-og.webp`

## 7. Validar imágenes

Ejecuta:

```bash
python tools/validar_imagenes_tw.py
```

Revisa:

```text
docs/operacion/reporte_imagenes_tw.md
```

## 8. Asociar imágenes de producto

Si colocaste imágenes como `assets/img/store/productos/ID.webp`, ejecuta:

```bash
python tools/asociar_imagenes_catalogo.py
```

El script crea respaldo antes de modificar el catálogo.

## 9. Actualizar manifiesto

Revisa `data/imagenes_pendientes.json` y ajusta `estado` si corresponde:

- `pendiente`
- `generado`
- `optimizado`
- `integrado`
- `revisar`

## 10. Probar sitio localmente

Ejecuta:

```bash
python -m http.server 8000
```

Probar:

- `http://localhost:8000/index.html`
- `http://localhost:8000/store/index.html`
- `http://localhost:8000/detalle/item.html?id=tw-store-001`
- `http://localhost:8000/empresa/mapa-del-sitio.html`

## 11. Revisar peso del repositorio

Evita subir imágenes pesadas innecesarias. Si una imagen pesa más de lo recomendado, optimízala o reemplázala.

## 12. Commit

Antes de hacer commit:

- Validar JSON.
- Validar imágenes.
- Revisar que no aparezcan datos internos.
- Confirmar que no hay rutas rotas visibles.

