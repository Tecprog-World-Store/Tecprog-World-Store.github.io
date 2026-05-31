# Tecprog World E.I.R.L. - Sitio GitHub Pages

Primera versión profesional del sitio corporativo y comercial de Tecprog World E.I.R.L. para publicar en GitHub Pages.

## Estructura

```text
/
├── index.html
├── assets/
│   ├── img/
│   │   ├── logos/
│   │   ├── banners/
│   │   ├── cursos/
│   │   ├── servicios/
│   │   ├── productos/
│   │   └── qr/
│   ├── icons/
│   ├── css/styles.css
│   └── js/main.js
├── legal/
│   ├── libro-reclamaciones.html
│   ├── terminos-condiciones.html
│   └── politicas-privacidad.html
└── data/
    ├── servicios.json
    ├── productos.json
    └── cursos.json
```

## Editar productos, cursos y servicios

Los contenidos comerciales se administran en archivos JSON:

- `data/productos.json`
- `data/cursos.json`
- `data/servicios.json`

Cada elemento acepta estos campos:

```json
{
  "nombre": "Nombre visible",
  "categoria": "Categoria",
  "descripcion": "Descripcion comercial breve",
  "precio": "Desde S/ 00.00",
  "imagen": "assets/img/productos/archivo.jpg",
  "paypal": "https://www.paypal.com/paypalme/tu-enlace"
}
```

Si no tienes una imagen todavia, deja el campo `imagen` vacio o apunta a una ruta futura. El sitio mostrara un bloque visual de respaldo.

## Cambiar datos de contacto

Edita las constantes al inicio de `assets/js/main.js`:

```js
const WHATSAPP_NUMBER = "51999999999";
const CONTACT_EMAIL = "contacto@tecprogworld.com";
```

Usa el numero de WhatsApp en formato internacional, sin espacios ni simbolos.

## Agregar imagenes

Coloca archivos livianos en estas carpetas:

- Logos: `assets/img/logos/`
- Banners: `assets/img/banners/`
- Cursos: `assets/img/cursos/`
- Servicios: `assets/img/servicios/`
- Productos: `assets/img/productos/`
- QR Yape: `assets/img/qr/yape.png`

El sitio ya reserva una zona para `assets/img/qr/yape.png`. Cuando tengas el QR real, guarda la imagen con ese nombre.

## PayPal y Yape

Los botones de PayPal quedan como enlaces editables en cada archivo JSON. Cambia el valor `paypal` por el enlace real de pago o checkout.

La zona Yape es informativa y debe actualizarse con el QR real antes de usarla comercialmente.

## Libro de reclamaciones

`legal/libro-reclamaciones.html` contiene una maqueta visual estatica. Para uso operativo debe conectarse luego a correo, Google Forms, Formspree o un backend propio.

## Publicar en GitHub Pages

1. Sube los archivos al repositorio.
2. En GitHub, entra a `Settings > Pages`.
3. En `Build and deployment`, selecciona `Deploy from a branch`.
4. Elige la rama `main` y la carpeta `/root`.
5. Guarda los cambios.

GitHub Pages publicara el sitio como una web estatica sin backend.

## Probar localmente

Como el sitio carga datos JSON con `fetch`, es mejor probarlo con un servidor local:

```powershell
python -m http.server 8080
```

Luego abre `http://localhost:8080`.
