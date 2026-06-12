# Estrategia de imagenes para productos e items

Fecha: 2026-06-12

## Resumen del catalogo

`data/catalogo_global.json` contiene 67 items.

| Linea | Items |
|---|---:|
| TW Store | 15 |
| TW Disfruta | 6 |
| TW Educa | 8 |
| TW Innova | 8 |
| TW Salud | 6 |
| TW Interactive | 6 |
| TW Construye | 6 |
| TW Inox | 6 |
| TW Investiga | 6 |

Por tipo de item:

| Tipo | Cantidad |
|---|---:|
| producto | 17 |
| servicio | 24 |
| curso | 8 |
| consultoria | 8 |
| proyecto | 5 |
| videojuego | 1 |
| contenido digital | 2 |
| merchandising | 2 |

## Criterio principal

No conviene generar 67 imagenes individuales de inmediato. La mayoria de servicios, cursos, consultorias y proyectos pueden funcionar con placeholders por linea o categoria mientras se valida demanda comercial.

## Clasificacion por grupo

### 1. Producto tecnologico especifico de TW Store

Items: `tw-store-001` a `tw-store-015`.

Estrategia recomendada: mezcla de A y C.

- A) Imagen individual necesaria para productos bandera: celulares destacados, laptop gamer, realidad virtual, audio de alto ticket y accesorio util para campanas.
- C) Imagen por categoria para productos secundarios: audio economico, monitores similares, celulares de menor prioridad.
- No usar imagenes de terceros sin permiso. Si se producen visuales, deben ser composiciones propias o placeholders comerciales genericos sin logos no autorizados.

### 2. Servicio profesional

Items principales: `tw-innova-001` a `tw-innova-008`, `tw-salud-005`, `tw-salud-006`, `tw-construye-001` a `tw-construye-006`, `tw-investiga-003`, `tw-investiga-004`, `tw-investiga-006`.

Estrategia recomendada: B o C.

- B) Placeholder por categoria suficiente para servicios tecnicos recurrentes.
- C) Imagen por linea o categoria cuando varios servicios comparten estetica.
- A) Imagen individual solo para servicios bandera con alta intencion de consulta, como sitio web corporativo, realidad mixta, remodelacion de oficina o mantenimiento medico.

### 3. Curso

Items: `tw-educa-001` a `tw-educa-008`.

Estrategia recomendada: B o C.

- Un placeholder por categoria funciona para Ofimatica, Diseno tecnico, Programacion, GIS y Simulacion.
- A) Imagen individual solo para cursos bandera usados en campanas, por ejemplo Python y GIS aplicado.

### 4. Consultoria

Items: `tw-interactive-001` a `tw-interactive-005`, `tw-investiga-001`, `tw-investiga-002`, `tw-investiga-005`.

Estrategia recomendada: C.

- Imagen por linea/categoria para hidrologia, hidraulica, CFD, mineria, metodologia e investigacion.
- A) Imagen individual solo para consultorias con alta capacidad de venta o demostracion tecnica, como modelamiento hidraulico.

### 5. Proyecto

Items: `tw-salud-003`, `tw-salud-004`, `tw-inox-001`, `tw-inox-003`, `tw-inox-005`.

Estrategia recomendada: C o D.

- C) Imagen por linea/categoria cuando se trata de una familia de proyectos.
- D) No generar por ahora si el proyecto aun no tiene alcance o prioridad comercial clara.
- A) Imagen individual solo para piezas con buen valor visual y alta confianza comercial, como baranda de acero inoxidable.

### 6. Videojuego / entretenimiento

Items: `tw-disfruta-001` a `tw-disfruta-006`.

Estrategia recomendada: A para el producto bandera y C para el resto.

- A) Imagen individual para `tw-disfruta-001` si sera pieza de marca o campana.
- C) Imagen por categoria para demos, assets, coleccionables, merchandising y widgets hasta tener una campana concreta.

### 7. Metalmecanica

Items: `tw-inox-001` a `tw-inox-006`.

Estrategia recomendada: A para 1 o 2 piezas, C para el resto.

- A) Baranda de acero inoxidable y mesa/mueble metalico si se buscan consultas locales.
- C) Placeholder por categoria para estructuras, soldadura y proyectos metalmecanicos.

### 8. Construccion

Items: `tw-construye-001` a `tw-construye-006`.

Estrategia recomendada: C.

- Una imagen por categoria puede cubrir remodelacion, diseno tecnico, supervision y mantenimiento.
- A) Imagen individual para remodelacion de oficina si se usara en redes o WhatsApp Business.

### 9. Salud / tecnologia medica

Items: `tw-salud-001` a `tw-salud-006`.

Estrategia recomendada: A para servicios bandera, C para proyectos.

- A) Ortesis personalizada y protesis funcional tienen alto valor visual y comercial.
- C) Hardware/software inclusivo y mantenimiento medico pueden compartir estetica de linea mientras se validan campanas.

### 10. Investigacion

Items: `tw-investiga-001` a `tw-investiga-006`.

Estrategia recomendada: C o D.

- C) Imagen por categoria para datos cientificos, software cientifico y modelamiento.
- D) No generar piezas individuales de todos los servicios hasta priorizar oferta.
- A) Imagen individual solo para procesamiento de datos cientificos o software cientifico si se promueve activamente.

## Matriz de decision

| Estrategia | Cuantos aplicar ahora | Uso recomendado |
|---|---:|---|
| A) Imagen individual necesaria | Maximo 15 | Productos bandera, servicios con alta conversion y piezas de redes |
| B) Placeholder por categoria suficiente | 20-30 | Cursos, servicios generales y categorias recurrentes |
| C) Imagen por linea o categoria | 20-30 | Consultorias, construccion, metalmecanica, investigacion |
| D) No generar por ahora | Variable | Items exploratorios o sin campana activa |

## Recomendacion operativa

1. Producir primero solo las 15 imagenes priorizadas en `data/visual/prioridad_imagenes_productos.json`.
2. Crear despues placeholders por categoria para cubrir el resto sin inflar el repositorio.
3. Revisar conversion comercial antes de producir nuevas imagenes individuales.
4. Evitar imagenes externas o de terceros sin permiso.
