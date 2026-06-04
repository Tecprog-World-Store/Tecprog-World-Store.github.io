# Tecprog World E.I.R.L.

Sitio web oficial estático de Tecprog World E.I.R.L., empresa peruana de tecnología aplicada. Publicación objetivo: GitHub Pages en `https://tecprog-world-store.github.io`.

## Datos Oficiales

- Empresa: Tecprog World E.I.R.L.
- País: Perú
- WhatsApp: `+51 952 354 282` (`51952354282` para enlaces `wa.me`)
- Correo: `grupotecprog@gmail.com`
- Logo: `assets/img/logos/logo-tecprog-world.png`
- QR de pago: `assets/img/qr/`

## Líneas De Negocio

Las seis líneas principales se editan en `data/lineas.json`:

- TW Investiga
- TW Innova para el desarrollo del software y el hardware
- TW Educa para ingenieros y científicos
- TW Construye
- TW Inox
- TW Prótesis y Órtesis

Cada entrada debe conservar los campos `id`, `nombre`, `nombre_corto`, `descripcion_corta`, `descripcion_larga`, `servicios_principales`, `categorias`, `pagina`, `facebook`, `imagen`, `icono` y `whatsapp_message`.

## Redes Sociales

Enlaces oficiales:

- Web: `https://tecprog-world-store.github.io`
- Facebook principal: `https://www.facebook.com/tecprogworld`
- Facebook TW Educa: `https://www.facebook.com/tecprogworld.educa`
- Facebook TW Innova: `https://www.facebook.com/tecprogworld.innova`
- Facebook TW Construye: `https://www.facebook.com/tecprogworld.construye`
- Facebook TW Prótesis y Órtesis / TW Bionic: `https://www.facebook.com/twbionic/`
- TikTok: `https://www.tiktok.com/@tecprogworld`
- YouTube: `https://www.youtube.com/@tecprogworld`
- LinkedIn: `https://www.linkedin.com/company/tecprog-world`

Los enlaces externos deben abrir con `target="_blank"` y `rel="noopener noreferrer"`.

## Navegación

La plataforma usa tres niveles:

- Menú superior: navegación global entre áreas principales.
- Índice izquierdo: navegación dentro de la página actual.
- Panel derecho: acciones rápidas, recursos, redes, video destacado y compartición.

Los componentes reutilizables están en:

- `assets/js/navigation.js`: menú global, footer institucional, botón flotante de WhatsApp e índice móvil.
- `assets/js/right-panel.js`: panel derecho, copiar enlace, compartir página y recursos destacados.

Las páginas internas que requieran índice deben usar `main.with-side-nav` y un `aside.side-nav`.

## Cursos

Los cursos se administran en:

- `data/cursos.json`
- `data/cursos/2026-06.json`
- Páginas de catálogo: `catalogo/cursos.html` y `catalogo/cursos-junio-2026.html`

Para asociar un compendio, agregar un enlace a `detalle/compendio.html?id=ID_DEL_COMPENDIO` o al PDF final en `assets/pdf/compendios/`.

## Compendios PDF

El catálogo se alimenta desde `data/compendios.json`. Cada registro debe incluir título, curso asociado, descripción, páginas estimadas, PDF, imagen, versión, precio referencial y mensaje WhatsApp.

Los PDF finales van en:

```text
assets/pdf/compendios/
```

Los fuentes LaTeX deben mantenerse fuera del repositorio web:

```text
D:\DiskE01\Organizacionies\E-TW\Produccion_LaTeX_TW
```

Compilar cada proyecto LaTeX fuera del repositorio y copiar solo el PDF final optimizado a `assets/pdf/compendios/`.

## Imágenes

- PNG: logos y QR.
- SVG: iconos y gráficos livianos.
- WebP: tarjetas, banners y miniaturas.
- JPG: fotos cuando no exista WebP.

El banner institucional principal está en:

```text
assets/img/banner_horizontal_tw/figuraHorizontal01.png
assets/img/banner_horizontal_tw/figuraHorizontal01.webp
```

Para convertir imágenes sin borrar originales:

```bat
scripts\optimizar_imagenes_web.bat
```

El script omite `assets/img/qr/` y `assets/img/logos/` para proteger legibilidad y transparencias.

Si Pillow no está instalado:

```bat
python -m pip install pillow
```

## QR De Pago

Usar las clases:

- `payment-qr-card`
- `payment-qr-frame`
- `payment-qr-image`

El QR debe mantenerse cuadrado, centrado, grande y con `object-fit: contain`. Debajo debe mostrarse “Pago nacional por QR” y la nota de confirmación antes de operar.

## Footer Institucional

El footer se renderiza desde `assets/js/navigation.js` e incluye identidad, RUC, estado, contacto, dirección fiscal, redes, legales y mapa/enlace de Google Maps.

## UTF-8

Todos los HTML deben incluir:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Guardar archivos como UTF-8. Si aparecen textos como `razón`, `país` o `teléfono`, corregirlos antes de publicar.

Validación rápida:

```powershell
rg -n "patrones_de_codificacion_rota" -g "*.html" -g "*.css" -g "*.js" -g "*.json" -g "*.md"
```

## Publicación En GitHub Pages

1. Confirmar que los JSON sean válidos.
2. Revisar rutas relativas en páginas dentro de subcarpetas.
3. Verificar que `index.html` y las páginas internas carguen CSS, JS, imágenes y PDF.
4. Confirmar que no existan textos de prueba visibles.
5. Subir cambios al repositorio publicado con GitHub Pages.

## Estrategia PayPal y precios

Etapa inicial recomendada:

- Usar enlaces de pago y codigos QR de PayPal por oferta frecuente: curso especifico, material digital, compendio PDF, servicio empaquetado o reserva de proyecto.
- En paginas publicas, los botones pueden abrir el enlace PayPal externo cuando `paypal_link` exista en `data/pagos.json`.
- Si `paypal_link` esta vacio, el boton debe abrir WhatsApp con el mensaje: `Hola, deseo solicitar enlace PayPal para [NOMBRE]. Soy cliente internacional.`
- Para servicios a medida no usar enlace fijo; usar solicitud de cotizacion o solicitud de enlace PayPal.
- Para proyectos grandes usar pagos por hitos: inicio, avance, entrega y soporte.
- Para pagos recurrentes dejar como futuro: suscripciones o membresias.

Archivos de referencia:

- `data/pagos.json`
- `data/precios.json`
- `data/ofertas.json`
- `herramientas/calculadora-precios.html`

Notas de calculo:

- Peru: calcular precio final con IGV 18% cuando corresponda.
- Internacional: no asumir IGV 18%.
- PayPal 5.40% + USD 0.30 es referencial y debe verificarse porque las tarifas pueden cambiar.
- No inventar comisiones bancarias; dejar campos configurables y verificar tarifario BCP vigente si aplica.
