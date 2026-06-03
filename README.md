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
│   │   ├── productos/
│   │   └── qr/
│   ├── icons/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
├── legal/
│   ├── libro-reclamaciones.html
│   ├── terminos-condiciones.html
│   └── politicas-privacidad.html
└── data/
    ├── servicios.json
    ├── productos.json
    └── cursos.json
```

## Editar cursos, servicios y productos

Los catálogos se cargan desde archivos JSON:

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

## WhatsApp, PayPal y Yape

El número oficial está configurado en `assets/js/main.js`:

```js
const WHATSAPP_NUMBER = "51952354282";
```

Los botones de compra generan este mensaje:

```text
Hola, deseo información para comprar: [nombre del producto/servicio]
```

Para PayPal, reemplaza `https://www.paypal.com/paypalme/editar-enlace` en cada elemento JSON por el enlace real de pago.

Para Yape o Plin, coloca el QR real en:

```text
assets/img/qr/yape.png
```

La web ya tiene una zona visual preparada para ese archivo.

## Editar imágenes

Usa imágenes optimizadas, livianas y con nombres sin espacios. Ejemplos:

- `assets/img/logos/logo-tecprog-world.png`
- `assets/img/banners/hero-tech.svg`
- `assets/img/cursos/qgis-cuencas.png`
- `assets/img/servicios/desarrollo-web.png`
- `assets/img/productos/plantilla-web.png`

Si una imagen de catálogo no existe, el sitio mantiene una tarjeta visual con placeholder local.

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
- Colocar el QR real de Yape o Plin.
- Revisar textos legales con asesoría antes de operación formal.
- Agregar fotos, banners o mockups propios cuando estén disponibles.
- Ampliar catálogos y crear páginas internas de detalle en una siguiente versión.
