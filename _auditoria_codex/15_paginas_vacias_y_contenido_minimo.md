# 15. Paginas vacias, debiles y contenido minimo

Fecha de auditoria: 2026-06-10

## Criterio usado

Una pagina se considera completa cuando tiene titulo claro, meta descripcion, contenido principal, CTA de WhatsApp, precio o condicion comercial si corresponde, enlace de retorno o navegacion, footer o scripts institucionales, ausencia de mojibake, ausencia de placeholders visibles y sin botones vacios.

Nota: varias paginas son shells dinamicos que se completan con JavaScript. Se marcan como debiles cuando el HTML base queda casi vacio o sin fallback suficiente, aunque el render dinamico pueda funcionar.

## Resumen

- Paginas analizadas: 44
- Completas: 12
- Debiles: 28
- Vacias o casi vacias: 2
- Errores criticos detectados: 0 enlaces locales rotos en la muestra auditada
- Riesgo mas frecuente: paginas dinamicas sin contenido minimo fallback y paginas comerciales sin precio/condicion visible en HTML base

## Detalle por pagina

| Ruta | Titulo detectado | Estado | Problema | Contenido minimo requerido | Enlaces faltantes | Precios faltantes | Imagenes faltantes | CTA faltante | Prioridad |
|---|---|---|---|---|---|---|---|---|---|
| `index.html` | Tecprog World E.I.R.L. | completa | Sin problema mayor. | Mantener hero, lineas, carruseles, pagos y contacto. | No detectados. | No. | No. | No. | Baja |
| `empresa/contacto.html` | Contacto | completa | Sin problema mayor. | Mantener QR, WhatsApp, correo, ubicacion y redes. | No detectados. | No aplica. | No. | No. | Baja |
| `empresa/mapa-del-sitio.html` | Mapa de navegacion | debil | Falta meta descripcion y CTA; es utilitario pero puede mejorar SEO. | Agregar meta description, bloque de contacto y CTA WhatsApp/volver al inicio. | No detectados. | No aplica. | No aplica. | Si. | Media |
| `empresa/nosotros.html` | Empresa | completa | Sin problema mayor. | Mantener historia, datos empresariales, lineas y CTA. | No detectados. | No aplica. | No. | No. | Baja |
| `lineas/tw-construye.html` | TW Construye | debil | Contenido aceptable, pero faltan precios o condiciones comerciales visibles. | Agregar paquetes desde, nota de coordinacion con profesionales habilitados y enlace a catalogo TW Construye. | No detectados. | Si. | No. | No. | Alta |
| `lineas/tw-educa.html` | TW Educa | completa | Completa tras estrategia MOOC; revisar acentos ASCII/UTF-8 en textos. | Mantener explicacion MOOC gratis + certificacion pagada. | No detectados. | No. | No. | No. | Baja |
| `lineas/tw-innova.html` | TW Innova | debil | Sin precios o condiciones comerciales en pagina de linea. | Agregar rangos desde para software, soporte, hardware, diagnostico y capacitacion; enlazar catalogo. | No detectados. | Si. | No. | No. | Alta |
| `lineas/tw-inox.html` | TW Inox | debil | Sin precios o condiciones comerciales visibles. | Agregar servicios desde, nota de coordinacion con tecnicos/talleres y CTA de cotizacion. | No detectados. | Si. | No. | No. | Alta |
| `lineas/tw-interactive.html` | TW Interactive - Ingenieros Consultores | completa | Sin problema mayor. | Mantener ramas tecnicas, nota de alcance y catalogo. | No detectados. | No. | No. | No. | Baja |
| `lineas/tw-investiga.html` | TW Investiga | debil | Buen contenido tecnico, pero sin precio o condicion comercial. | Agregar asesorias desde, informe breve desde, proyecto I+D desde y enlace a contacto/cotizacion. | No detectados. | Si. | No. | No. | Media |
| `lineas/tw-protesis-ortesis.html` | Protesis y ortesis ahora es TW Salud | debil | Ruta alias preservada; falta condicion comercial o precio referencial. | Mantener aviso de alias, agregar enlace claro a catalogo TW Salud y nota de precios referenciales. | No detectados. | Si. | No. | No. | Media |
| `lineas/tw-salud-vida.html` | TW Salud y Vida ahora es TW Salud | debil | Ruta alias preservada; contenido corto y sin precio/condicion. | Agregar bloque minimo de alias, categorias TW Salud, enlace catalogo y nota responsable. | No detectados. | Si. | No. | No. | Media |
| `lineas/tw-salud.html` | TW Salud | completa | Sin problema mayor; contiene nota responsable y catalogo. | Mantener nota obligatoria, subcategorias y CTA. | No detectados. | No. | No. | No. | Baja |
| `lineas/tw-store.html` | Tecprog World Store | debil | Contenido breve; sin precios ni catalogo comercial propio. | Agregar productos destacados, precios desde, medios de pago, enlace a descargas/materiales y CTA. | No detectados. | Si. | No. | No. | Alta |
| `lineas/tw-taller.html` | TW Taller | debil | Falta meta descripcion, contenido breve y sin precios. | Agregar diagnostico desde, mantenimiento desde, soporte por alcance, condiciones y CTA. | No detectados. | Si. | No. | No. | Media |
| `catalogo/catalogo-general-tw-educa-pdf.html` | Catalogo general TW Educa PDF | debil | Pagina PDF sin precio/condicion comercial visible. | Agregar nota MOOC/certificacion, enlace al catalogo HTML y CTA WhatsApp. | No detectados. | Si. | No. | No. | Media |
| `catalogo/catalogo-general-tw-educa.html` | Catalogo general de cursos TW Educa | completa | Sin problema mayor. | Mantener filtros MOOC, certificado, en vivo, grabado y especializacion. | No detectados. | No. | No. | No. | Baja |
| `catalogo/catalogo-mensual.html` | Catalogo mensual Tecprog World | debil | Contenido general sin precios resumidos. | Agregar resumen por lineas: cursos, servicios, catalogos PDF, pagos y precios desde. | No detectados. | Si. | No. | No. | Alta |
| `catalogo/compendios.html` | Libros, compendios y guias tecnicas | debil | Falta CTA WhatsApp visible y precios en HTML base. | Agregar CTA, nota de precios/material incluido y fallback con 3 compendios destacados. | No detectados. | Si. | No. | Si. | Alta |
| `catalogo/cursos-junio-2026.html` | Cursos junio 2026 | vacia | Pagina casi vacia, sin meta descripcion ni listado real. | Agregar cursos del periodo, precios MOOC/certificado, fechas, CTA y enlace al catalogo general. | No detectados. | Si. | No. | No. | Alta |
| `catalogo/cursos.html` | Cursos | vacia | Pagina casi vacia, sin meta descripcion ni catalogo visible. | Agregar listado inicial, filtros basicos, modelo MOOC, precios desde y CTA. | No detectados. | Si. | No. | No. | Alta |
| `catalogo/descargas.html` | Zona de Descargas | debil | Sin precio/condicion comercial; recursos gratuitos no diferenciados. | Agregar secciones gratis/pagado, licencias, guias, scripts y CTA de soporte. | No detectados. | Si, si hay recursos pagados. | No. | No. | Media |
| `catalogo/guias.html` | Guias tecnicas Tecprog World | debil | Sin precio/condicion comercial visible en HTML base. | Agregar nota de guias gratuitas/pagadas, CTA y fallback de 3 guias destacadas. | No detectados. | Si, si hay guias pagadas. | No. | No. | Media |
| `catalogo/hp-50g.html` | Programacion HP 50G para ingenieria | completa | Contenido suficiente; el aviso independiente no es placeholder. | Mantener precio, aviso independiente, recursos y CTA. | No detectados. | No. | No. | No. | Baja |
| `catalogo/materiales-educativos.html` | Cursos para ingenieros y cientificos | completa | Contenido suficiente; los avisos independientes son correctos. | Mantener filtros, precios referenciales y CTA. | No detectados. | No. | No. | No. | Baja |
| `catalogo/tw-construye.html` | Catalogo TW Construye | debil | Shell dinamico sin fallback suficiente; CTA solo por JS. | Agregar noscript/fallback con hero, 3 ofertas, precios desde y CTA WhatsApp. | No detectados. | Via JSON, pero no fallback. | No, dinamica. | En HTML base. | Alta |
| `catalogo/tw-innova.html` | Catalogo TW Innova | debil | Shell dinamico sin fallback suficiente; CTA solo por JS. | Agregar fallback con categorias, precios desde y CTA. | No detectados. | Via JSON, pero no fallback. | No, dinamica. | En HTML base. | Alta |
| `catalogo/tw-inox.html` | Catalogo TW Inox | debil | Shell dinamico sin fallback suficiente; CTA solo por JS. | Agregar fallback con servicios, nota tecnica y CTA. | No detectados. | Via JSON, pero no fallback. | No, dinamica. | En HTML base. | Alta |
| `catalogo/tw-interactive.html` | Catalogo TW Interactive | debil | Tiene noscript, pero HTML base depende de JS para contenido comercial. | Agregar fallback con 5 ramas, precios desde y enlace WhatsApp. | No detectados. | Via JSON, pero no fallback completo. | No, dinamica. | En HTML base. | Media |
| `catalogo/tw-salud.html` | Catalogo TW Salud | debil | Tiene noscript, pero HTML base depende de JS para contenido comercial. | Agregar fallback con nota responsable, 5 categorias, precios desde y CTA. | No detectados. | Via JSON, pero no fallback completo. | No, dinamica. | En HTML base. | Media |
| `detalle/compendio.html` | Compendio | debil | Shell dinamico; sin fallback de contenido/CTA en HTML base. | Agregar fallback "selecciona compendio", CTA, retorno a compendios y nota de precios. | No detectados. | Via JSON, no fallback. | Dinamica. | En HTML base. | Media |
| `detalle/curso.html` | Curso | debil | Shell dinamico; sin CTA visible antes de JS. | Agregar fallback con explicacion MOOC, certificado desde y retorno al catalogo. | No detectados. | Via JS, no fallback. | Dinamica. | En HTML base. | Alta |
| `detalle/guia.html` | Guia tecnica | debil | Shell dinamico; sin fallback ni CTA. | Agregar fallback con volver a guias, descarga/consulta y contacto. | No detectados. | Depende de guia. | Dinamica. | En HTML base. | Media |
| `detalle/material.html` | Material | debil | Shell dinamico; sin fallback ni CTA en HTML base. | Agregar fallback con volver a materiales, WhatsApp y nota de pago. | No detectados. | Via JSON, no fallback. | Dinamica. | En HTML base. | Media |
| `detalle/oferta.html` | Oferta | debil | Shell dinamico; sin fallback para ofertas por linea. | Agregar fallback con volver a catalogos, WhatsApp y selector de linea. | No detectados. | Via JSON, no fallback. | Dinamica. | En HTML base. | Alta |
| `detalle/producto.html` | Producto | debil | Shell dinamico; sin fallback ni CTA en HTML base. | Agregar fallback con productos, WhatsApp, pagos y retorno. | No detectados. | Via JSON, no fallback. | Dinamica. | En HTML base. | Media |
| `detalle/servicio.html` | Servicio | debil | Shell dinamico; sin fallback ni CTA en HTML base. | Agregar fallback con servicios, precios desde y WhatsApp. | No detectados. | Via JS, no fallback. | Dinamica. | En HTML base. | Media |
| `detalle/software.html` | Software | debil | Shell dinamico; sin fallback ni CTA en HTML base. | Agregar fallback con soluciones software, precios desde y WhatsApp. | No detectados. | Via JS, no fallback. | Dinamica. | En HTML base. | Media |
| `pagos/internacionales.html` | Pagos internacionales | completa | Sin problema mayor. | Mantener PayPal, condiciones y CTA. | No detectados. | No. | No aplica. | No. | Baja |
| `pagos/peru.html` | Pagos en Peru | completa | Sin problema mayor. | Mantener QR, transferencia, advertencias y CTA. | No detectados. | No. | No aplica. | No. | Baja |
| `legal/libro-reclamaciones.html` | Libro de Reclamaciones | completa | Sin problema mayor. | Mantener formulario/enlace y datos legales. | No detectados. | No aplica. | No aplica. | No. | Baja |
| `legal/politicas-pagos-reembolsos.html` | Politicas de Pagos y Reembolsos | debil | Falta meta descripcion y contenido algo corto. | Agregar meta, secciones de reembolsos, plazos, medios de pago y contacto. | No detectados. | No aplica. | No aplica. | No. | Media |
| `legal/politicas-privacidad.html` | Politicas de Privacidad | debil | Falta meta descripcion. | Agregar meta y reforzar tratamiento de datos, WhatsApp, correo y derechos ARCO si aplica. | No detectados. | No aplica. | No aplica. | No. | Media |
| `legal/terminos-condiciones.html` | Terminos y Condiciones | debil | Falta meta descripcion. | Agregar meta y reforzar condiciones de cursos, servicios, pagos, propiedad intelectual y limitaciones. | No detectados. | No aplica. | No aplica. | No. | Media |

## Observaciones generales

- No se detectaron enlaces locales rotos en las paginas auditadas.
- No se confirmo mojibake critico en HTML fuente, aunque conviene ejecutar `scripts/revisar_utf8.bat` antes de publicar.
- Las paginas de detalle y catalogos por linea dependen de JavaScript. Funcionan mejor si reciben un fallback minimo para usuarios sin JS, indexacion SEO y cargas fallidas.
- Las paginas comerciales antiguas `tw-store.html`, `tw-taller.html`, `catalogo/cursos.html` y `catalogo/cursos-junio-2026.html` son las mas visibles como incompletas.
