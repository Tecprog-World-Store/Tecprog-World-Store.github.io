# Instrucciones Para Codex

1. Leer primero todos los archivos en `docs/restricciones_codex/`.
2. No modificar la arquitectura aprobada salvo orden explicita del usuario.
3. No duplicar paneles laterales, panel central, navegacion ni panel derecho.
4. Ejecutar pruebas de no regresion antes de entregar cambios estructurales:
   - `python tools/validar_layout_tres_paneles.py`
   - `python tools/validar_no_paneles_duplicados.py`
   - `python tools/validar_version_assets.py`
5. Crear backup antes de cambios estructurales.
6. No hacer commit ni push salvo instruccion explicita del usuario.
7. Mantener compatibilidad con GitHub Pages.
8. Mantener rutas SEO, canonicals, sitemap y Open Graph salvo instruccion explicita.
9. Mantener mensajes comerciales aprobados, precios correctos y politicas de pago vigentes.
10. Reportar cualquier conflicto entre una instruccion nueva y una restriccion anterior antes de modificar.
11. Las paginas comerciales con `data-commerce-panel-strategy="local"` no deben cargar `right-panel.js`.
12. Todas las referencias locales a CSS y JS deben usar una version uniforme con `?v=`.
