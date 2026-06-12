# Estrategia para OpenGraph y carruseles

Fecha: 2026-06-12

## Decision

No generar imagenes OpenGraph ni carruseles en esta fase.

## OpenGraph

Los banners horizontales existentes ya funcionan como `og:image` en las paginas de linea. Aunque el formato ideal de OpenGraph suele ser `1200x630`, los banners `1920x640` ya ofrecen una imagen horizontal liviana, coherente y validada.

Recomendacion:

1. Mantener los banners actuales como `og:image` mientras no haya una campana fuerte de redes.
2. Generar OG dedicados solo si se detecta uso frecuente en Facebook, LinkedIn, WhatsApp o Twitter/X.
3. Si se generan OG luego, derivarlos de los banners existentes para ahorrar tiempo y mantener identidad.

## Carruseles

Los carruseles solo se justifican cuando haya campanas activas, por ejemplo:

- Lanzamiento de una linea.
- Campana de productos bandera.
- Promocion por temporada.
- Caso de exito o servicio priorizado.

No conviene generar carruseles genericos todavia porque aumentan peso del repositorio y pueden quedar obsoletos.

## Prioridad recomendada

1. Flyers de linea.
2. Imagenes de productos bandera.
3. OpenGraph si se comparte mucho en redes.
4. Carruseles solo por campanas especificas.
