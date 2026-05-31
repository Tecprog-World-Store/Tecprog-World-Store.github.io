# Tecprog World E.I.R.L. - Sitio GitHub Pages

Sitio corporativo y comercial estático de Tecprog World E.I.R.L. para publicar en GitHub Pages. Usa HTML, CSS y JavaScript puro, sin backend, claves API ni dependencias pesadas.

## Estructura principal

```text
/
├── index.html
├── assets/
│   ├── img/
│   │   ├── logos/
│   │   ├── banners/
│   │   ├── lineas/
│   │   ├── cursos/
│   │   ├── servicios/
│   │   ├── productos/
│   │   ├── software/
│   │   ├── descargas/
│   │   └── qr/
│   ├── icons/
│   ├── css/styles.css
│   └── js/main.js
├── data/
│   ├── cursos.json
│   ├── servicios.json
│   ├── productos.json
│   ├── software.json
│   └── descargas.json
└── legal/
    ├── libro-reclamaciones.html
    ├── terminos-condiciones.html
    └── politicas-privacidad.html
```

## Editar contenido comercial

Los catálogos se editan desde la carpeta `data/`:

- `data/cursos.json`
- `data/servicios.json`
- `data/productos.json`
- `data/software.json`
- `data/descargas.json`

Para cursos, servicios y productos usa esta base:

```json
{
  "nombre": "Nombre visible",
  "categoria": "Categoría",
  "descripcion": "Descripción comercial breve",
  "precio": "Desde S/ 00.00",
  "imagen": "assets/img/productos/archivo.svg",
  "paypal": "https://www.paypal.com/paypalme/editar-enlace"
}
```

Para descargas:

```json
{
  "nombre": "Nombre de la descarga",
  "tipo": "Software open-source",
  "linea_negocio": "TW Innova",
  "descripcion": "Descripción breve",
  "version": "0.1.0",
  "sistema_operativo": "Web / multiplataforma",
  "licencia": "MIT",
  "url_descarga": "https://github.com/",
  "url_documentacion": "https://github.com/",
  "imagen": "assets/img/descargas/archivo.svg",
  "etiqueta": "open-source"
}
```

## WhatsApp, PayPal y Yape

Edita al inicio de `assets/js/main.js`:

```js
const WHATSAPP_NUMBER = "51999999999";
const CONTACT_EMAIL = "contacto@tecprogworld.com";
const DEFAULT_PAYPAL_URL = "https://www.paypal.com/paypalme/editar-enlace";
```

El mensaje de WhatsApp se genera así:

```text
Hola, deseo información sobre: [nombre]. Vengo desde la web de Tecprog World.
```

Para Yape, coloca el QR real en:

```text
assets/img/qr/yape.png
```

## Imágenes

El sitio incluye placeholders SVG propios, livianos y editables. Puedes reemplazarlos por imágenes optimizadas en:

- `assets/img/banners/`
- `assets/img/lineas/`
- `assets/img/software/`
- `assets/img/descargas/`
- `assets/img/cursos/`
- `assets/img/servicios/`
- `assets/img/productos/`

Usa nombres en minúsculas y sin espacios, por ejemplo `software-comercial-dashboard.png`.

## Publicar en GitHub Pages

1. Sube los archivos al repositorio.
2. En GitHub entra a `Settings > Pages`.
3. Selecciona `Deploy from a branch`.
4. Elige la rama `main` y la carpeta `/root`.
5. Guarda los cambios.

## Probar localmente

Como el sitio carga JSON con `fetch`, pruébalo con un servidor local:

```powershell
python -m http.server 8080
```

Luego abre `http://localhost:8080`.

## Pendientes recomendados

- Reemplazar enlaces temporales de Facebook, PayPal, GitHub y documentación.
- Confirmar correo empresarial y número real de WhatsApp.
- Colocar el QR Yape real.
- Revisar textos legales antes de iniciar ventas formales.
