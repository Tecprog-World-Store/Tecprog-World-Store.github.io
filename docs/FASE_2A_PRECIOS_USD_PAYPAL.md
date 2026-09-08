# Fase 2A: inventario para revisión

Moneda objetivo: USD. Esta fase no cambia la moneda ni los precios publicados; no convierte PEN, consulta Internet ni modifica HTML, CSS, JS o datos operativos.

## Fuentes

- `data/catalogo_global.json`: catálogo público principal.
- `data/productos_store.json`: origen de productos y márgenes históricos; no sustituye automáticamente al catálogo principal.
- `data/cursos_tw_educa.json` y `data/precios_internacionales_tw_educa.json`: cursos vigentes, perfiles y etapas PEN/USD.
- `data/catalogo-general-cursos.json`, `data/cursos.json`, `data/cursos/2026-06.json`: catálogos de cursos que siguen teniendo lectores públicos.
- `data/catalogo-tw-{construye,innova,inox,interactive,salud}.json`: catálogos por línea. `data/tw-salud.json` y `data/tw-interactive.json` son fuentes de los catálogos correspondientes, no filas adicionales.
- `data/materiales.json`, `data/guias.json`, `data/compendios.json`, `data/ofertas.json`: materiales, recursos y ofertas.
- `data/precios.json`, `data/pagos.json`: bases explícitas y referencias de cobro.
- `data/politica_precios_tw_educa.json`: política histórica PEN; no representa productos adicionales. Cronogramas, banners, briefs, TXT y páginas generadas no añaden productos al inventario.

## Lectura del CSV

720 registros de inventario por fuente/tarifa, **no 720 productos únicos**. La clave es `(archivo_fuente, id)`. Se conservan las apariciones en distintos catálogos para no ocultar discrepancias. Los 37 cursos vigentes se desglosan en 249 tarifas por perfil y etapa; los sufijos del ID identifican esas variantes.

`precio_actual` conserva los campos monetarios originales como JSON dentro de una celda CSV, incluidos precios PEN, modalidades y valores nulos. `moneda_actual` puede contener PEN/USD. El archivo fuente permite consultar el contexto completo. No se consolidan IDs entre fuentes: por ejemplo, `tw-store-014` identifica Meta Quest 3 en el catálogo global y una laptop ASUS en productos_store. Ningún precio se transfiere entre ellos.

## Criterios

- PRECIO_BASE_USD_DEFINIDO: existe importe USD numérico o un importe USD inequívoco en texto. Se conserva como base para esta simulación, según la instrucción del usuario, incluso cuando el original indica «desde». Esto no convierte una tarifa mínima en presupuesto cerrado ni acredita que el importe histórico fuera neto.
- PRECIO_EN_PEN_REQUIERE_CONVERSION: importe PEN sin base USD utilizable; equivale a REQUIERE_CONVERSION_USD. Base y cálculos USD vacíos.
- SIN_PRECIO: sin importe ni evidencia suficiente para otra categoría.
- PRECIO_REQUIERE_INVESTIGACION: producto sin importe con precio pendiente de consulta. Incluye Meta Quest 3; no se toma el precio de la laptop con el mismo ID.
- NO_APLICA_PRECIO_FIJO: servicios/proyectos variables sin importe definido y recursos expresamente gratuitos. Los ceros existentes se preservan; no se aplica una comisión a una descarga gratuita.

Las tarifas internacionales de cursos ya existentes se conservan por perfil/etapa. No se ejecuta ni actualiza su conversión histórica. Un registro con importes USD y PEN se clasifica por USD; PEN permanece en `precio_actual`. Por ello el total de la categoría PEN no equivale a todas las apariciones de importes PEN.

## Cálculo propuesto, todavía no publicado

`precio_paypal_calculado_usd = (precio_base_usd + 0.30) / 0.946`.

Referencia comercial proporcionada por el usuario: 5.40% + USD 0.30 por transacción. Sin margen de conversión ni otros cargos. El bruto se conserva con seis decimales redondeados hacia arriba; el redondeo comercial usa el cálculo completo: por debajo de 20, techo al entero; desde 20, menor entero terminado en 9 que sea mayor o igual al bruto. No añade decenas innecesarias: 528.86 → 529; 1057.40 → 1059. No se añade JS porque todavía no se publica esta política.

## Validación

545 registros con USD definido, 92 PEN pendientes, 8 sin precio, 2 requieren investigación y 73 sin precio fijo. Se verifica cobertura de las 17 fuentes de registros y de todas las tarifas internacionales, clave compuesta única, 14 columnas, lectura CSV UTF-8, cálculo y cobertura neta con aritmética decimal. Los archivos previamente versionados deben permanecer idénticos byte a byte. Sin commit ni push.
