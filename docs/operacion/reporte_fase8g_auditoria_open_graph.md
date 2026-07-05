# Reporte Fase 8G - Auditoria Open Graph

Fecha: 2026-07-04

## Causa confirmada

Las URLs dinamicas de curso, por ejemplo:

`https://tecprog-world-store.github.io/detalle/curso.html?id=tw-educa-curso-01&catalogo=tw-educa-vivo`

cargaban la ficha correcta con JavaScript, pero el HTML inicial de `detalle/curso.html` mantenia metadatos genericos:

- `og:title`: `Curso | Tecprog World E.I.R.L.`
- `og:description`: descripcion generica de cursos TW Educa
- `og:type`: `product`
- `og:image`: `../assets/img/store/og/tw-store-og.webp`
- `og:url`: `https://tecprog-world-store.github.io/detalle/curso.html`
- `canonical`: `https://tecprog-world-store.github.io/detalle/curso.html`
- `twitter:image`: `../assets/img/store/og/tw-store-og.webp`

`assets/js/detalle.js` cambiaba esos metadatos despues de cargar el curso, pero Facebook, WhatsApp, LinkedIn y X leen principalmente el HTML inicial. Por eso Facebook podia mostrar la imagen generica de TW Store en lugar del flyer especifico del curso.

## Archivos auditados

| Archivo | Hallazgo |
|---|---|
| `detalle/curso.html` | Contiene metadatos iniciales genericos y `tw-store-og.webp`. |
| `detalle/item.html` | Tambien actualiza metadatos por JS para items genericos; queda como alcance futuro para productos/servicios. |
| `assets/js/detalle.js` | Renderiza curso correcto y actualiza meta tags en cliente. Ahora tambien soporta `data-course-id` y rutas root-relative. |
| `data/cursos_tw_educa.json` | Fuente principal de los 14 cursos vivos TW Educa, con imagen especifica por curso. |
| `data/catalogo_global.json` | Contenia enlaces dinamicos `detalle/curso.html?id=...`; ahora apunta a URLs estaticas. |
| `assets/img/educa/cursos/` | Contiene los 14 flyers WebP especificos de curso. |

## Paginas afectadas

Los 14 cursos `tw-educa-curso-01` a `tw-educa-curso-14` estaban afectados cuando se compartian mediante URL dinamica.

## Decision tecnica

Se crean paginas estaticas por curso en:

`/cursos/<slug>/index.html`

Cada pagina incluye en el HTML inicial:

- `title`
- `description`
- `canonical`
- `og:title`
- `og:description`
- `og:url`
- `og:image`
- `og:image:secure_url`
- `og:image:alt`
- `og:image:type`
- `og:image:width`
- `og:image:height`
- `twitter:card`
- `twitter:title`
- `twitter:description`
- `twitter:image`

La pagina dinamica antigua no se elimina y sigue funcionando para compatibilidad.

