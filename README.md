# Tecprog World E.I.R.L. - Sitio web para GitHub Pages

Primera versión profesional del sitio corporativo y comercial estático de Tecprog World E.I.R.L. El sitio usa HTML, CSS y JavaScript puro, no requiere backend, no usa claves API y funciona directamente en GitHub Pages.

## Estructura

```text
/
├── index.html
├── README.md
├── assets/
│   ├── img/
│   │   ├── logos/
│   │   ├── banners/
│   │   ├── cursos/
│   │   ├── servicios/
│   │   │   ├── protesis_y_ortesis/
│   │   │   └── cursos_ingenieros_y_cientificos/
│   │   ├── productos/
│   │   └── qr/
│   ├── icons/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── main.js
│       └── materiales.js
├── catalogo/
│   ├── materiales-educativos.html
│   └── hp-50g.html
├── detalle/
│   └── material.html
├── servicios/
│   └── protesis-y-ortesis.html
├── legal/
│   ├── libro-reclamaciones.html
│   ├── terminos-condiciones.html
│   └── politicas-privacidad.html
├── temario_cursos/
│   └── hp_50g/
└── data/
    ├── servicios.json
    ├── productos.json
    ├── cursos.json
    └── materiales.json
```

## Editar cursos, servicios y productos

Los catálogos principales se cargan desde:

- `data/cursos.json`
- `data/servicios.json`
- `data/productos.json`

Cada elemento puede usar esta estructura:

```json
{
  "nombre": "Nombre visible",
  "linea": "TW Educa",
  "categoria": "Categoría",
  "descripcion": "Texto comercial breve",
  "precio": "Desde S/ 149",
  "modalidad": "Virtual",
  "imagen": "assets/img/cursos/archivo.svg",
  "etiqueta": "Etiqueta",
  "paypal": "https://www.paypal.com/paypalme/editar-enlace"
}
```

Después de editar un JSON, valida que no falten comas, comillas o corchetes. Un JSON inválido impedirá que se renderice esa sección.

## Materiales y páginas individuales

El catálogo ampliado vive en:

```text
data/materiales.json
```

Este archivo alimenta:

- `detalle/material.html?id=material-id`
- `servicios/protesis-y-ortesis.html`
- `catalogo/materiales-educativos.html`
- `catalogo/hp-50g.html`

Para agregar nuevos materiales, coloca imágenes o archivos en una de estas carpetas y luego agrega o actualiza el registro correspondiente en `data/materiales.json`:

- `assets/img/servicios/protesis_y_ortesis/`
- `assets/img/servicios/cursos_ingenieros_y_cientificos/`
- `temario_cursos/hp_50g/`

Cada registro de `data/materiales.json` usa campos como `id`, `titulo`, `tipo`, `linea`, `categoria`, `descripcion_corta`, `descripcion_larga`, `imagen`, `beneficios`, `incluye`, `entregables`, `precio_desde_soles_igv`, `precio_exterior_usd`, `seo_title`, `seo_description`, `keywords` y `whatsapp_message`.

Para abrir una página individual:

```text
detalle/material.html?id=temario-programacion-hp-50g
```

Si una imagen no carga, el sitio muestra un placeholder visual elegante. Si el archivo tiene espacios, mayúsculas o caracteres especiales, JavaScript aplica codificación de ruta al mostrarlo; aun así se recomienda normalizar nombres.

## Nombres de archivo recomendados

Usa nombres:

- en minúsculas
- sin espacios
- sin tildes
- con guiones medios

Ejemplos:

```text
protesis-mano-prototipo-01.png
curso-qgis-basico.png
hp50g-programacion-matrices.png
```

## WhatsApp, PayPal y Yape

El número oficial está configurado en:

- `assets/js/main.js`
- `assets/js/materiales.js`

```js
const WHATSAPP_NUMBER = "51952354282";
```

Los botones de detalle generan este mensaje:

```text
Hola, deseo información sobre [TÍTULO]. Vengo desde la web de Tecprog World E.I.R.L.
```

Para PayPal, reemplaza `https://www.paypal.com/paypalme/editar-enlace` por el enlace real de pago.

Para Yape o Plin, coloca el QR real en:

```text
assets/img/qr/
```

Si hay varias imágenes de QR, se recomienda usar una sola principal o actualizar `qrPath` en `assets/js/materiales.js`. Actualmente se usa:

```text
assets/img/qr/QR_Yape.png
```

No publiques datos bancarios sensibles si no corresponde mostrarlos en la web.

## Editar imágenes

Usa imágenes optimizadas, livianas y con nombres sin espacios. Ejemplos:

- `assets/img/logos/logo-tecprog-world.png`
- `assets/img/banners/hero-tech.svg`
- `assets/img/cursos/qgis-cuencas.png`
- `assets/img/servicios/desarrollo-web.png`
- `assets/img/productos/plantilla-web.png`

## Páginas legales

Las páginas legales iniciales están en `legal/`:

- `legal/libro-reclamaciones.html`
- `legal/terminos-condiciones.html`
- `legal/politicas-privacidad.html`

El Libro de Reclamaciones es una maqueta visual estática. Para operación formal debe conectarse luego a correo, Google Forms, Formspree o un backend validado.

## Probar localmente

Como el sitio carga JSON con `fetch`, pruébalo con un servidor local:

```powershell
python -m http.server 8080
```

Luego abre:

```text
http://localhost:8080
```

## Publicar en GitHub Pages

1. Sube los archivos al repositorio.
2. En GitHub, entra a `Settings > Pages`.
3. Selecciona `Deploy from a branch`.
4. Elige la rama `main` y la carpeta `/root`.
5. Guarda los cambios.

## Pendientes recomendados

- Reemplazar los enlaces temporales de Facebook y PayPal por enlaces oficiales.
- Revisar textos legales con asesoría antes de operación formal.
- Normalizar nombres de archivos nuevos cuando sea posible.
- Agregar más fotos, banners o mockups propios cuando estén disponibles.
- Conectar el Libro de Reclamaciones a un mecanismo real cuando se inicie operación formal.

## Produccion de compendios LaTeX

Los fuentes LaTeX, capitulos, referencias, figuras de trabajo, logs y archivos auxiliares de compendios deben mantenerse fuera del repositorio web en:

```text
D:\DiskE01\Organizacionies\E-TW\Produccion_LaTeX_TW
```

El repositorio GitHub Pages debe mantenerse liviano. No subir fuentes LaTeX pesadas, bibliotecas completas, libros, papers protegidos, imagenes originales muy pesadas ni archivos auxiliares de compilacion. Solo subir PDF finales optimizados, imagenes web comprimidas, archivos JSON, HTML, CSS y JS.

Compendios publicados:

- `assets/pdf/compendios/hp-50g-programacion-ingenieria.pdf`
- `assets/pdf/compendios/qgis-basico-ingenieria-gestion-territorial.pdf`

Paginas relacionadas:

- `catalogo/compendios.html`
- `detalle/compendio.html?id=hp-50g-programacion-ingenieria`
- `detalle/compendio.html?id=qgis-basico-ingenieria-gestion-territorial`
- `data/compendios.json`

Para revisar el peso de carpetas publicas:

```bat
scripts\revisar_peso_repo.bat
```

## Optimizacion de imagenes web

Formatos recomendados:

- PNG: logos, QR o graficos con transparencia.
- JPG: fotos.
- WEBP: banners, tarjetas, miniaturas y web.
- SVG: iconos simples.

El flujo externo de conversion WebP esta en:

```text
D:\DiskE01\Organizacionies\E-TW\Produccion_LaTeX_TW\scripts\optimizar_imagenes_web.bat
```

Si Pillow no esta instalado:

```bat
pip install pillow
```
