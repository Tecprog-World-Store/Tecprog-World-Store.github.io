# 11. Normalizacion de lineas de negocio

Fecha de ejecucion: 2026-06-10

## Objetivo aplicado

Se normalizo la arquitectura visible de lineas de negocio para que Tecprog World E.I.R.L. use siete lineas canonicas:

1. TW Investiga
2. TW Innova
3. TW Educa
4. TW Interactive
5. TW Construye
6. TW Inox
7. TW Salud

La linea de salud queda consolidada como:

- Nombre completo: TW Salud y Vida - Protesis y Tecnologia Medica
- Nombre corto: TW Salud

## Archivos modificados

- `data/lineas.json`
- `assets/js/navigation.js`
- `assets/js/main.js`
- `assets/js/materiales.js`
- `data/materiales.json`
- `index.html`
- `lineas/tw-salud.html`
- `lineas/tw-protesis-ortesis.html`
- `lineas/tw-salud-vida.html`
- `empresa/contacto.html`
- `empresa/mapa-del-sitio.html`
- `servicios/protesis-y-ortesis.html`
- `README.md`

## Nombres reemplazados

- `TW Protesis y Ortesis` como linea independiente se reemplazo por `TW Salud`.
- `TW Protesis y Ortesis` en redes sociales se reemplazo por `TW Salud`.
- `TW Salud y Vida / TW Bionic` como linea visible se reemplazo por `TW Salud`.
- La ruta de inicio `lineas/tw-protesis-ortesis.html` fue reemplazada por `lineas/tw-salud.html` en navegacion y tarjetas visibles.
- El conteo del hero de inicio paso de 6 a 7 lineas de negocio.

## Alias detectados y consolidados

Los siguientes nombres se conservan como alias historicos o categorias internas de TW Salud, no como lineas separadas:

- TW Protesis y Ortesis
- TW Bionic
- TW Salud y Vida
- Protesis y Tecnologia Medica
- Protesis y Ortesis

## Rutas preservadas

No se eliminaron rutas antiguas. Se mantuvieron como paginas alias con aviso interno:

- `lineas/tw-protesis-ortesis.html`
- `lineas/tw-salud-vida.html`

Ambas paginas informan que la linea canonica es `TW Salud` y enlazan a `lineas/tw-salud.html`.

## Rutas nuevas o canonicas

- `lineas/tw-salud.html` queda como pagina canonica de TW Salud.
- `lineas/tw-interactive.html` se incorpora a navegacion, mapa del sitio y datos canonicos como linea oficial ya existente en el repositorio.

## Cambios por superficie

- `data/lineas.json`: se dejo una lista canonica de 7 lineas, se agrego `tw-interactive` y se reemplazo `tw-protesis-ortesis` por `tw-salud`.
- `assets/js/main.js`: las tarjetas de inicio ahora renderizan `TW Salud` y `TW Interactive`; no hay tarjeta independiente para protesis y ortesis.
- `assets/js/navigation.js`: el menu superior y footer institucional enlazan a `TW Salud` y agregan `TW Interactive`.
- `index.html`: se actualizo la navegacion estatica, textos principales, conteo de lineas y enlaces de footer/redes.
- `data/materiales.json` y `assets/js/materiales.js`: las ofertas de protesis y tecnologia medica se etiquetan con `TW Salud`; la categoria `Protesis, ortesis y tecnologia medica` se conserva como categoria de servicio.
- `servicios/protesis-y-ortesis.html`: la pagina conserva la categoria de servicios, pero la etiqueta de linea pasa a `TW Salud`.
- `empresa/contacto.html`: el canal de Facebook historico `twbionic` se muestra como `TW Salud`.
- `empresa/mapa-del-sitio.html`: el mapa lista las siete lineas canonicas y apunta Salud a `lineas/tw-salud.html`.
- `README.md`: documenta siete lineas canonicas y el tratamiento de alias de TW Salud.

## Enlaces que deben revisarse manualmente

- Enlaces externos de redes sociales, especialmente `https://www.facebook.com/twbionic/`, porque se mantiene como canal historico asociado a TW Salud.
- Enlaces entrantes externos hacia `lineas/tw-protesis-ortesis.html` y `lineas/tw-salud-vida.html`; las rutas funcionan como alias, pero conviene actualizar publicaciones externas futuras a `lineas/tw-salud.html`.
- Contenido comercial de la categoria `Protesis, ortesis y tecnologia medica` en catalogos y materiales, para confirmar que mantiene lenguaje de diseno, prototipado, soporte tecnico y validacion profesional cuando corresponda.

## Validaciones ejecutadas

- JSON valido para `data/lineas.json` y `data/materiales.json`.
- Sintaxis JavaScript valida para `assets/js/main.js`, `assets/js/navigation.js` y `assets/js/materiales.js`.
- Enlaces locales existentes en paginas tocadas: `index.html`, paginas alias de Salud, contacto, mapa y servicio de protesis y ortesis.
- `data/lineas.json` contiene 7 lineas canonicas, una sola entrada `tw-salud` y ninguna entrada independiente `tw-protesis-ortesis` o `tw-salud-vida`.
- Paginas `lineas/tw-salud.html`, `lineas/tw-protesis-ortesis.html` y `lineas/tw-salud-vida.html` tienen contenido visible suficiente y no quedaron vacias.

## Advertencias

- Las menciones a alias se mantienen de forma intencional dentro de `data/lineas.json`, `README.md` y paginas alias para preservar trazabilidad.
- La categoria `Protesis y ortesis` sigue siendo valida como categoria de servicios dentro de TW Salud.
- No se eliminaron archivos ni se movieron rutas antiguas.
