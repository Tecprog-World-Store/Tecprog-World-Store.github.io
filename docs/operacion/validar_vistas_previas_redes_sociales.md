# Validar vistas previas en redes sociales

Fecha: 2026-07-04

## Despues del push

1. Publicar los cambios en GitHub Pages.
2. Esperar a que GitHub Pages despliegue la nueva version.
3. Abrir Facebook Sharing Debugger.
4. Pegar una URL estatica, por ejemplo:
   `https://tecprog-world-store.github.io/cursos/realidad-virtual-unity-meta-quest/`
5. Pulsar `Debug`.
6. Pulsar `Scrape Again`.
7. Verificar que aparezcan:
   - titulo especifico del curso;
   - descripcion especifica;
   - flyer WebP del curso;
   - URL canonica estatica.
8. Repetir con WhatsApp, LinkedIn y X.

## URLs recomendadas para prueba

- `https://tecprog-world-store.github.io/cursos/realidad-virtual-unity-meta-quest/`
- `https://tecprog-world-store.github.io/cursos/programacion-autocad-csharp/`
- `https://tecprog-world-store.github.io/cursos/qgis-python-plugins/`
- `https://tecprog-world-store.github.io/cursos/ia-offline-python-ollama-pyside/`
- `https://tecprog-world-store.github.io/cursos/cfd-openfoam-wsl/`
- `https://tecprog-world-store.github.io/cursos/machine-learning-mecanica-fluidos/`
- `https://tecprog-world-store.github.io/cursos/programacion-gpu-nvidia-cfd/`

## Notas de cache social

- Las redes pueden conservar vistas previas antiguas.
- No agregar parametros aleatorios a la URL canonica final.
- Usar `Scrape Again` en Facebook si conserva la imagen anterior.
- Versionar la imagen solo si se reemplaza el flyer por otro archivo.
- No automatizar acciones dentro de Facebook.

