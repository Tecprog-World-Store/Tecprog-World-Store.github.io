# Estrategia de publicación de CORVUS AI v4

Estado al 2026-08-11: la ficha y el manual están preparados localmente. El instalador no se ha copiado al repositorio, no está publicado y no existe una URL de descarga autorizada.

## Arquitectura recomendada

- Mantener la página oficial y el manual en GitHub Pages, dentro de TW Innova.
- Hospedar el instalador fuera de GitHub Pages.
- Recomendar inicialmente **GitHub Releases** si se autoriza un repositorio público o privado adecuado para el producto: permite asociar binarios y notas a una versión/tag, ofrece URL única por release y estadísticas de descarga mediante API.
- Usar **SourceForge** como alternativa si se prioriza una red de mirrors, gestión específica de archivos y un canal de distribución separado del repositorio del sitio.

## Comparación breve

| Canal | Ventaja principal | Consideración |
|---|---|---|
| GitHub Releases | Versiones, notas, tags y activos quedan juntos; facilita enlazar una versión exacta desde la ficha oficial. | Requiere decidir en qué repositorio vivirá el release y quién tendrá permisos de publicación. |
| SourceForge | Sistema de archivos de releases y mirrors distribuidos; útil para una zona de descargas independiente. | Requiere crear y mantener un proyecto/canal adicional y su identidad pública. |

Fuentes oficiales consultadas:

- GitHub Docs, “About releases”: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- GitHub Docs, “Linking to releases”: https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases
- SourceForge, “Release Files for Download”: https://sourceforge.net/p/forge/documentation/Release%20Files%20for%20Download/

## Secuencia antes de habilitar la descarga

1. Decidir el host externo y la cuenta/repositorio autorizados.
2. Resolver si se publicará el alfa sin firma o si se esperará a una firma Authenticode válida.
3. Analizar el instalador final con herramientas de seguridad apropiadas.
4. Publicar el archivo sin modificarlo después de calcular su SHA-256.
5. Comprobar desde una sesión externa que la URL descarga exactamente el archivo esperado.
6. Actualizar la ficha con URL, tamaño, fecha, nombre exacto, versión y SHA-256.
7. Sustituir la CTA deshabilitada solo después de verificar el enlace.

## Decisión pendiente

Se necesita autorización explícita para elegir **GitHub Releases** o **SourceForge** como host del instalador y para publicar el binario. También debe decidirse si la publicación alfa puede avanzar sin firma digital o si debe esperar la firma.
