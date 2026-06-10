# Arquitectura del proyecto Tecprog World

Esta guia explica donde esta cada cosa y como mantener el sitio sin depender de IA. Antes de hacer cambios grandes, lee tambien `docs/CHECKLIST_PUBLICACION.md`, `docs/LINEAMIENTOS_UTF8.md` y `docs/POLITICA_PUBLICACION_PDF.md`.

## 1. Estructura general

```text
index.html
assets/
data/
lineas/
catalogo/
detalle/
empresa/
pagos/
legal/
docs/
scripts/
_auditoria_codex/
```

- `index.html`: pagina principal del sitio. Contiene hero, lineas de negocio, cursos destacados, servicios, productos, pagos y contacto.
- `assets/`: recursos publicos del sitio: CSS, JavaScript, imagenes, iconos, PDF y QR.
- `data/`: archivos JSON y fuentes TXT que alimentan catalogos, detalles, cursos, servicios, productos, precios y pagos.
- `lineas/`: paginas de cada linea de negocio: TW Educa, TW Innova, TW Interactive, TW Construye, TW Inox, TW Salud, etc.
- `catalogo/`: paginas de catalogos comerciales o academicos. Algunas son HTML estatico y otras cargan JSON con JavaScript.
- `detalle/`: paginas dinamicas de detalle. Reciben parametros por URL, por ejemplo `detalle/curso.html?id=openfoam-cfd&catalogo=general`.
- `empresa/`: paginas institucionales: nosotros, contacto y mapa del sitio.
- `pagos/`: informacion de pagos en Peru e internacionales.
- `legal/`: terminos, privacidad, libro de reclamaciones y politicas de pago.
- `docs/`: documentacion de mantenimiento del proyecto.
- `scripts/`: utilidades para generar catalogos, revisar UTF-8, optimizar imagenes y revisar peso del repositorio.
- `_auditoria_codex/`: reportes incrementales de auditoria y planes. No es contenido comercial para clientes.

## 2. Donde colocar imagenes

Usa rutas relativas compatibles con GitHub Pages. Evita espacios y tildes en nombres de archivo nuevos.

```text
assets/img/logos/
assets/img/banners/
assets/img/lineas/
assets/img/cursos/
assets/img/servicios/
assets/img/productos/
assets/img/software/
assets/img/guias/
assets/img/qr/
```

- `assets/img/logos/`: logos oficiales, isotipos y marcas institucionales.
- `assets/img/banners/`: fondos, banners institucionales y recursos visuales generales.
- `assets/img/lineas/`: imagenes por linea de negocio.
- `assets/img/cursos/`: miniaturas de cursos y capacitaciones.
- `assets/img/servicios/`: imagenes de servicios tecnicos, salud, construccion, inox, etc.
- `assets/img/productos/`: productos fisicos o digitales.
- `assets/img/software/`: software, dashboards, plugins, apps y sistemas.
- `assets/img/guias/`: portadas o miniaturas de guias PDF.
- `assets/img/qr/`: QR de pago. No optimizar agresivamente; debe conservar legibilidad.

## 3. Donde colocar PDFs

```text
assets/pdf/guias/
assets/pdf/compendios/
assets/pdf/catalogos/
assets/pdf/brochures/
```

- `assets/pdf/guias/`: guias tecnicas, manuales y documentos descargables de apoyo.
- `assets/pdf/compendios/`: compendios de cursos o materiales educativos.
- `assets/pdf/catalogos/`: catalogos mensuales o catalogos por linea de negocio.
- `assets/pdf/brochures/`: fichas comerciales, brochures y presentaciones exportadas a PDF.

Publica solo PDF finales. No copies fuentes LaTeX ni auxiliares al repositorio web.

## 4. Donde colocar fuentes TXT

```text
data/fuentes/
```

Aqui van los archivos base editables por humanos, por ejemplo:

- `catalogo_base_cursos_tw_educa.txt`
- `catalogo_base_tw_salud.txt`
- `catalogo_base_tw_interactive.txt`
- `catalogo_base_tw_innova.txt`
- `catalogo_base_tw_inox.txt`
- `catalogo_base_tw_construye.txt`

Usa UTF-8 y estructura delimitada por pipes cuando el script lo requiera.

## 5. Donde editar catalogos

Archivos principales:

```text
data/catalogo-general-cursos.json
data/tw-salud.json
data/tw-interactive.json
data/tw-innova.json
data/tw-inox.json
data/tw-construye.json
data/ofertas.json
```

Tambien existen catalogos usados por paginas dinamicas:

```text
data/catalogo-tw-salud.json
data/catalogo-tw-interactive.json
data/catalogo-tw-innova.json
data/catalogo-tw-inox.json
data/catalogo-tw-construye.json
```

Regla practica: si editas a mano un JSON grande, valida inmediatamente con:

```powershell
node -e "JSON.parse(require('fs').readFileSync('data/catalogo-general-cursos.json','utf8')); console.log('JSON OK')"
```

## 6. Como agregar un curso

1. Decide si sera curso general, curso de periodo o curso destacado.
2. Para el catalogo general, edita la fuente en `data/fuentes/catalogo_base_cursos_tw_educa.txt` o directamente `data/catalogo-general-cursos.json`.
3. Agrega campos clave:
   - `id`
   - `linea`
   - `categoria`
   - `curso`
   - `modalidad`
   - `horas_certificables`
   - `precio_peru_igv_soles`
   - `precio_internacional_usd`
   - `descripcion_corta`
   - `temario_base`
   - `imagen`
   - `whatsapp_message`
4. Aplica la politica MOOC:
   - `acceso_mooc_gratuito: true`
   - `mooc_texto: "Acceso MOOC: Gratis"`
   - `certificado_desde_soles`
   - `certificado_texto`
   - `nota_precio_mooc`
5. Valida el JSON.
6. Prueba la URL:

```text
detalle/curso.html?id=ID_DEL_CURSO&catalogo=general
```

## 7. Como agregar un servicio

1. Identifica la linea: TW Salud, TW Interactive, TW Innova, TW Inox, TW Construye u otra.
2. Edita el JSON correspondiente o su TXT base en `data/fuentes/`.
3. Campos recomendados:
   - `id`
   - `linea_slug`
   - `linea`
   - `categoria`
   - `oferta` o `servicio`
   - `tipo`
   - `descripcion_corta`
   - `descripcion_larga`
   - `publico_objetivo`
   - `entregables`
   - `precio_soles_texto`
   - `precio_usd_texto`
   - `imagen`
   - `whatsapp_message`
4. Si es oferta por linea, valida:

```text
detalle/oferta.html?id=ID&linea=tw-salud
```

## 8. Como agregar un producto

1. Coloca la imagen en `assets/img/productos/`.
2. Edita `data/productos.json` o `data/ofertas.json` segun donde deba aparecer.
3. Incluye:
   - nombre
   - categoria
   - descripcion
   - precio desde
   - imagen
   - enlace de detalle
   - mensaje de WhatsApp
4. Si es recurso digital, indica condiciones de entrega, descarga y pagos.

## 9. Como agregar un PDF

1. Genera el PDF fuera del repositorio si viene de LaTeX, Word u otra fuente pesada.
2. Copia solo el PDF final a:
   - `assets/pdf/guias/`
   - `assets/pdf/compendios/`
   - `assets/pdf/catalogos/`
   - `assets/pdf/brochures/`
3. Usa nombre en minusculas, sin espacios ni tildes.
4. Registra el PDF en el JSON correspondiente:
   - `data/guias.json`
   - `data/compendios.json`
   - catalogo mensual o pagina HTML de contexto
5. Abre la pagina que lo muestra y prueba descarga/visor.

## 10. Como agregar una imagen

1. Elige la carpeta correcta dentro de `assets/img/`.
2. Usa nombres descriptivos sin espacios, por ejemplo:

```text
assets/img/cursos/openfoam-cfd-basico.webp
```

3. Optimiza tamaño cuando sea posible.
4. No optimices agresivamente logos ni QR.
5. Actualiza el JSON o HTML que referencia la imagen.
6. Prueba que la ruta funcione desde una pagina en subcarpeta.

## 11. Como cambiar precios

Archivos comunes:

```text
data/precios.json
data/pagos.json
data/ofertas.json
data/catalogo-general-cursos.json
data/politica_precios_tw_educa.json
data/catalogo-tw-*.json
```

Reglas:

- Usa siempre "Desde S/ ..." y "Desde USD ..." cuando el alcance pueda variar.
- Para TW Educa, distingue MOOC gratuito de certificado/curso pagado.
- Para servicios a medida, evita precio fijo cerrado salvo que sea paquete definido.
- Actualiza mensajes de WhatsApp si el precio o modalidad cambia.
- Valida JSON despues del cambio.

## 12. Como revisar UTF-8

Ejecuta:

```bat
scripts\revisar_utf8.bat
```

O directamente:

```powershell
python scripts\revisar_utf8.py
```

Para correcciones conocidas:

```powershell
python scripts\revisar_utf8.py --fix
```

Revisa manualmente si ves textos como `Ã¡`, `Â`, `�` o signos raros.

## 13. Como publicar en GitHub Pages

1. Validar JSON.
2. Revisar enlaces locales.
3. Revisar que imagenes, PDF y scripts carguen con rutas relativas.
4. Revisar responsive en movil y escritorio.
5. Ejecutar revision UTF-8.
6. Revisar consola del navegador.
7. Hacer commit.
8. Hacer push a la rama publicada.
9. Esperar despliegue de GitHub Pages.
10. Abrir la URL publica y probar paginas clave.

## 14. Que archivos no subir

No subir:

- Fuentes LaTeX de produccion si pertenecen a carpeta externa.
- Auxiliares LaTeX: `.aux`, `.log`, `.out`, `.toc`, `.fls`, `.fdb_latexmk`, `.synctex.gz`, `.bbl`, `.bcf`, `.blg`, `.run.xml`, `.xdv`.
- Archivos temporales de Office: `~$archivo.docx`.
- Backups pesados como `.zip`, `.rar`, `.7z` dentro del repo web.
- Bases de datos privadas, claves, tokens, credenciales o informacion bancaria sensible.
- Imagenes enormes sin optimizar.

## 15. Como hacer backup antes de cambios grandes

Opcion recomendada con Git:

```powershell
git status
git add .
git commit -m "backup antes de cambios grandes"
```

Opcion de rama:

```powershell
git checkout -b backup/fecha-descripcion
git add .
git commit -m "backup de trabajo"
```

Opcion manual:

1. Cierra editores.
2. Copia la carpeta del repositorio a un disco externo.
3. Usa un nombre con fecha:

```text
Tecprog-World-Store.github.io_backup_2026-06-10
```

Antes de cualquier generacion masiva, revisa:

```powershell
git status --short
```

Si hay cambios que no entiendes, no los borres ni los reviertas sin revisar.
