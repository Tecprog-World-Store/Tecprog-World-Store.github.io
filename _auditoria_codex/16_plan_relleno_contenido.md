# 16. Plan de relleno de contenido minimo

Fecha de plan: 2026-06-10

## Prioridad 1. Paginas comerciales

1. `catalogo/cursos.html`
   - Crear pagina real de cursos con 6 a 12 cursos destacados.
   - Incluir modelo MOOC: acceso gratis, certificado desde, curso en vivo y capacitacion institucional.
   - Agregar CTA WhatsApp, retorno a TW Educa y precios desde.

2. `catalogo/cursos-junio-2026.html`
   - Rellenar con cursos vigentes del periodo `data/cursos/2026-06.json`.
   - Mostrar fechas, modalidad, precio MOOC/certificado, imagen y CTA.
   - Enlazar a `catalogo/catalogo-general-tw-educa.html`.

3. `catalogo/catalogo-mensual.html`
   - Agregar resumen por linea de negocio.
   - Mostrar PDF mensual, catalogos por linea, cursos, servicios y medios de pago.
   - Incluir precios desde y nota comercial.

4. `catalogo/compendios.html`
   - Agregar fallback HTML con 3 compendios destacados.
   - Mostrar precios/material incluido y CTA WhatsApp.

5. `lineas/tw-store.html`
   - Convertir en pagina comercial minima con productos digitales, materiales, licencias/demos y precios desde.
   - Agregar enlaces a descargas, materiales educativos, pagos y WhatsApp.

## Prioridad 2. Lineas de negocio

1. `lineas/tw-innova.html`
   - Agregar paquetes: diagnostico, software a medida, dashboards, plugins, soporte y capacitacion.
   - Mostrar precios desde y enlace a catalogo TW Innova.

2. `lineas/tw-construye.html`
   - Agregar precios desde, categorias de servicio, nota de profesionales habilitados y CTA.

3. `lineas/tw-inox.html`
   - Agregar servicios metalmecanicos, condiciones, coordinacion con tecnicos/talleres y precios desde.

4. `lineas/tw-investiga.html`
   - Agregar asesorias desde, informe tecnico breve, proyecto I+D y documentacion cientifica.

5. `lineas/tw-taller.html`
   - Agregar meta description, precios desde y relacion con soporte/mantenimiento.

6. Rutas alias de salud
   - `lineas/tw-protesis-ortesis.html`
   - `lineas/tw-salud-vida.html`
   - Mantener como alias, pero agregar bloque de precios referenciales y CTA hacia TW Salud.

## Prioridad 3. Catalogos

1. Catalogos dinamicos por linea:
   - `catalogo/tw-salud.html`
   - `catalogo/tw-innova.html`
   - `catalogo/tw-interactive.html`
   - `catalogo/tw-inox.html`
   - `catalogo/tw-construye.html`

   Accion: agregar fallback HTML o `noscript` robusto con hero, 3 a 5 ofertas, precios desde, nota legal/comercial y CTA WhatsApp.

2. `catalogo/guias.html`
   - Agregar fallback con guias destacadas, condicion gratis/pagado y CTA.

3. `catalogo/descargas.html`
   - Separar recursos gratuitos, recursos pagados, scripts, PDF y soporte.

4. `catalogo/catalogo-general-tw-educa-pdf.html`
   - Agregar bloque de precios MOOC/certificacion y enlace al catalogo HTML.

## Prioridad 4. Detalles

1. `detalle/curso.html`
   - Agregar fallback estatico con politica MOOC, certificado desde S/ 19, CTA y retorno al catalogo.

2. `detalle/oferta.html`
   - Agregar fallback para ofertas por linea con selector de catalogos.

3. `detalle/material.html`, `detalle/producto.html`, `detalle/servicio.html`, `detalle/software.html`, `detalle/compendio.html`, `detalle/guia.html`
   - Agregar fallback comun: "No se pudo cargar el detalle", enlaces de retorno, WhatsApp y nota comercial.

4. Validar que cada detalle tenga:
   - Titulo dinamico
   - Descripcion larga
   - Precio o condicion
   - Imagen
   - CTA WhatsApp
   - Enlace de retorno

## Prioridad 5. PDFs

1. Paginas PDF y catalogos mensuales
   - Verificar que cada PDF tenga pagina HTML de contexto.
   - Agregar fecha, version, alcance, enlace de descarga, precio si corresponde y WhatsApp.

2. `assets/pdf/`
   - Documentar PDF vigentes, obsoletos y faltantes en un inventario.
   - Evitar publicar fuentes LaTeX o auxiliares.

3. Compendios y guias
   - Diferenciar muestra gratuita, material incluido en curso y material pagado.

## Prioridad 6. SEO

1. Meta descriptions faltantes
   - `empresa/mapa-del-sitio.html`
   - `catalogo/cursos.html`
   - `catalogo/cursos-junio-2026.html`
   - `lineas/tw-taller.html`
   - `legal/politicas-pagos-reembolsos.html`
   - `legal/politicas-privacidad.html`
   - `legal/terminos-condiciones.html`

2. Titulos y H1
   - Asegurar que cada pagina tenga un H1 unico y especifico.
   - Evitar nombres genericos como `Curso`, `Producto`, `Oferta` sin fallback SEO.

3. Datos estructurados futuros
   - Agregar JSON-LD para Organization, Course, Product y Service cuando el contenido este estable.

4. Intern linking
   - Desde cada linea enlazar a su catalogo.
   - Desde cada catalogo enlazar a detalle, pagos y contacto.
   - Desde detalles enlazar a catalogo, linea y WhatsApp.

5. Mojibake y UTF-8
   - Ejecutar `scripts/revisar_utf8.bat`.
   - Corregir textos con acentos rotos antes de publicar.

## Orden sugerido de ejecucion

1. Rellenar `catalogo/cursos.html` y `catalogo/cursos-junio-2026.html`.
2. Agregar fallback a `detalle/curso.html` y catalogos dinamicos por linea.
3. Completar lineas con precios faltantes: TW Innova, TW Construye, TW Inox, TW Store y TW Taller.
4. Reforzar legales con meta descriptions.
5. Auditar PDF y paginas de descarga.
6. Ejecutar validacion SEO/UTF-8/enlaces.
