#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TXT_DIR = ROOT / "Cursos a dictar" / "cursos_txt_tecprog_world"
COURSES_JSON = ROOT / "data" / "cursos_tw_educa.json"
CATALOG_JSON = ROOT / "data" / "catalogo_global.json"
DOCS_DIR = ROOT / "docs" / "operacion"
BASELINE_BACKUP = ROOT / "backups" / "fase_precios_whatsapp_temarios_20260707_224803" / "data" / "cursos_tw_educa.json"

TXT_BY_ID = {}
for path in sorted(TXT_DIR.glob("[0-9][0-9]_*.txt")):
    match = re.match(r"^(\d{2})_", path.name)
    if not match or match.group(1) == "00":
        continue
    TXT_BY_ID[f"tw-educa-curso-{int(match.group(1)):02d}"] = path

COMMERCIAL_SOURCES = {
    "tw-educa-curso-01": "TXT local 01 y flyer Curso_practico_de_realidad_virtual.png",
    "tw-educa-curso-02": "TXT local 02 y flyer Curso_practico_de_programacion_para_autocad.png",
    "tw-educa-curso-03": "TXT local 03 y flyer Curso_practico_de_programacion_en_Qgis.png",
    "tw-educa-curso-04": "TXT local 04 y flyer Curso_practico_de_software_de_IA_Offline_con_Python_Ollama_y_pyside.png",
    "tw-educa-curso-05": "TXT local 05 y flyer Curso_practico_De_geoportales_web_gis.png",
    "tw-educa-curso-06": "TXT local 06 y flyer Curso_practico_latex_y_texmaker_para_investigacion_cientifica.png",
    "tw-educa-curso-07": "TXT local 07 y flyer Curso_practico_machine_learning_aplicado_a_mecanica_de_fluidos.png",
    "tw-educa-curso-08": "TXT local 08 y flyer Curso_practico_CFD_con_OpenFOAM_WSL.png",
    "tw-educa-curso-09": "TXT local 09 y flyer Curso_practico_Cloud_Computing_para_OpenFOAM.png",
    "tw-educa-curso-10": "TXT local 10 y flyer Curso_practico_de_datos_climaticos_y_oceanograficos_con_Python.png",
    "tw-educa-curso-11": "TXT local 11 y flyer Curso_practico_C++_aplicado_a_mecanica_de_fluidos.png",
    "tw-educa-curso-12": "TXT local 12 y flyer Curso_practico_apps_moviles_para_mecanica_de_fluidos.png",
    "tw-educa-curso-13": "TXT local 13 y flyer Curso_practico_vision_artificial_aplicada_a_rios_y_canales.png",
    "tw-educa-curso-14": "TXT local 14 y flyer Curso_practico_programacion_GPU_nvidia_aplicada_a_CFD.png",
}

OFFICIAL_SOURCES = [
    "Python documentation: https://docs.python.org/3/tutorial/index.html",
    "PyQGIS Developer Cookbook: https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/index.html",
    "OpenFOAM User Guide: https://www.openfoam.com/documentation/user-guide",
    "OpenFOAM User Guide (CFD Direct): https://doc.cfd.direct/openfoam/user-guide/",
    "Meta Horizon OS Unity setup: https://developers.meta.com/horizon/documentation/unity/unity-project-setup/",
    "Unity Meta Quest development manual: https://docs.unity3d.com/6000.0/Documentation/Manual/xr-meta-quest-develop.html",
    "scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html",
    "NVIDIA CUDA C Programming Guide: https://docs.nvidia.com/cuda/cuda-programming-guide/index.html",
    "Flutter documentation: https://docs.flutter.dev/",
    "Dart documentation: https://dart.dev/docs",
    "GeoServer User Manual: https://docs.geoserver.org/main/en/user/index.html",
    "PostGIS documentation: https://postgis.net/",
]


ENRICHED = {
    "tw-educa-curso-01": [
        ("Fundamentos de Unity, XR y Meta Quest", [
            "Objetivo: preparar un proyecto VR ejecutable en Meta Quest 2/3.",
            "Instalacion de Unity Hub, version LTS recomendada y modulos Android.",
            "Estructura de una escena Unity: GameObjects, componentes, materiales y prefabs.",
            "Configuracion de XR Plug-in Management, OpenXR y perfil Meta Quest.",
            "Preparacion del visor: modo desarrollador, cable USB, permisos y pruebas de conexion.",
            "Practica: escena base con suelo, iluminacion, camara XR y objeto interactuable.",
            "Resultado: proyecto Unity validado para compilar hacia Android/Quest.",
        ]),
        ("Interaccion VR y controladores", [
            "Objetivo: implementar interacciones basicas con manos o controladores.",
            "XR Origin, tracking, locomocion simple y zonas seguras de trabajo.",
            "Ray interactor, direct interactor, agarre, soltar y activacion de objetos.",
            "Colliders, rigidbodies y eventos para respuestas visuales o sonoras.",
            "Organizacion de prefabs reutilizables para escenarios tecnicos.",
            "Practica: panel interactivo y objetos manipulables dentro de la escena.",
            "Resultado: escena navegable con interaccion VR verificable.",
        ]),
        ("Diseño de experiencia y optimizacion", [
            "Objetivo: mejorar confort, rendimiento y claridad de una experiencia VR.",
            "Escala real, ergonomia, distancia de lectura y ubicacion de elementos UI.",
            "Materiales, luces, baked lighting y criterios de rendimiento para Quest.",
            "Uso prudente de particulas, sombras, texturas y mallas optimizadas.",
            "Pruebas en visor: FPS, mareo, colisiones y limites del area de juego.",
            "Practica: optimizacion de la escena y checklist de experiencia.",
            "Resultado: prototipo VR mas estable y presentable.",
        ]),
        ("Compilacion y proyecto final", [
            "Objetivo: generar una APK funcional y presentar el prototipo.",
            "Build settings, player settings, identificador de paquete y versionado.",
            "Depuracion de errores frecuentes de SDK, permisos y despliegue.",
            "Instalacion en visor y verificacion de controles, escala e interaccion.",
            "Documentacion breve del flujo de usuario y decisiones tecnicas.",
            "Practica: cierre del proyecto final con evidencia en visor.",
            "Resultado: prototipo VR instalado o listo para instalacion en Meta Quest.",
        ]),
    ],
    "tw-educa-curso-02": [
        ("Entorno AutoCAD .NET y primer comando C#", [
            "Objetivo: preparar Visual Studio para programar comandos de AutoCAD.",
            "Conceptos de API .NET, ensamblados, referencias y version compatible de AutoCAD.",
            "Creacion de Class Library, configuracion de plataforma y carga con NETLOAD.",
            "Estructura de un comando C#: atributos, Document, Editor y Database.",
            "Mensajes en consola, seleccion de entidades y lectura de propiedades.",
            "Practica: comando de diagnostico que selecciona objetos y muestra informacion.",
            "Resultado: primer plugin cargable en AutoCAD con comando propio.",
        ]),
        ("Dibujo y modificacion de entidades", [
            "Objetivo: crear geometria 2D desde codigo con transacciones seguras.",
            "Lineas, polilineas, circulos, textos, capas y estilos basicos.",
            "Uso de Transaction, BlockTableRecord y manejo de errores.",
            "Lectura de puntos del usuario y parametros por consola.",
            "Automatizacion de rutinas repetitivas de dibujo tecnico.",
            "Practica: generar una plantilla de dibujo parametrica.",
            "Resultado: comando que crea entidades organizadas por capa.",
        ]),
        ("Datos, bloques y automatizacion CAD", [
            "Objetivo: trabajar con bloques, atributos y datos de dibujo.",
            "Insercion de bloques, atributos, escalas y unidades.",
            "Extraccion de informacion para reportes simples.",
            "Validacion de nombres de capas, colores y convenciones CAD.",
            "Conexion con archivos CSV o tablas basicas cuando aplique.",
            "Practica: rutina para insertar y listar elementos tecnicos.",
            "Resultado: automatizacion CAD con datos reutilizables.",
        ]),
        ("Empaquetado y proyecto final", [
            "Objetivo: entregar una herramienta CAD pequena pero usable.",
            "Organizacion del codigo, nombres de comandos y mensajes claros.",
            "Pruebas en dibujos de ejemplo y depuracion de excepciones comunes.",
            "Documentacion de instalacion, carga y uso del plugin.",
            "Criterios de compatibilidad con versiones de AutoCAD.",
            "Practica: cierre del plugin final y demostracion guiada.",
            "Resultado: plugin C# documentado para automatizar una tarea CAD.",
        ]),
    ],
    "tw-educa-curso-03": [
        ("PyQGIS, consola y estructura de plugin", [
            "Objetivo: comprender el entorno Python de QGIS y el esqueleto de un plugin.",
            "Diferencia entre consola, scripts, procesamiento y plugin instalable.",
            "Estructura de archivos, metadata.txt, recursos, iconos y acciones.",
            "Uso de QgsProject, capas vectoriales, CRS y acceso a atributos.",
            "Preparacion de entorno con Plugin Builder o plantilla equivalente.",
            "Practica: plugin minimo con boton y mensaje en QGIS.",
            "Resultado: plugin cargable con estructura correcta.",
        ]),
        ("Capas, geometria y procesamiento", [
            "Objetivo: leer, validar y procesar datos espaciales desde PyQGIS.",
            "Iteracion sobre features, campos, geometria y filtros.",
            "Creacion de capas temporales y escritura de resultados.",
            "Uso basico de Processing Framework y algoritmos nativos.",
            "Manejo de errores de datos, CRS y geometria invalida.",
            "Practica: herramienta para calcular y exportar atributos espaciales.",
            "Resultado: plugin que ejecuta un flujo GIS reproducible.",
        ]),
        ("Interfaz con PyQt y experiencia de usuario", [
            "Objetivo: construir un dialogo util para seleccionar entradas y opciones.",
            "Widgets, formularios, validaciones y mensajes de estado.",
            "Seleccion de capas activas, campos y rutas de salida.",
            "Integracion de señales, slots y barra de progreso.",
            "Buenas practicas para no bloquear la interfaz de QGIS.",
            "Practica: dialogo de parametros para el flujo de procesamiento.",
            "Resultado: plugin con interfaz funcional y validacion basica.",
        ]),
        ("Empaquetado, pruebas y proyecto final", [
            "Objetivo: dejar el plugin listo para distribucion interna.",
            "Versionado, metadatos, dependencias y compatibilidad QGIS 3.x.",
            "Pruebas con datos pequenos, casos vacios y errores controlados.",
            "Documentacion de instalacion y manual breve de uso.",
            "Revision de codigo, nombres y limpieza de archivos temporales.",
            "Practica: entrega del plugin final con datos de ejemplo.",
            "Resultado: plugin PyQGIS instalable y demostrable.",
        ]),
    ],
}

ENRICHED.update({
    "tw-educa-curso-04": [
        ("Entorno local de IA y arquitectura", ["Objetivo: instalar una base local de IA sin depender de servicios externos.", "Instalacion de Python, entorno virtual, Ollama y modelos ligeros.", "Conceptos de LLM local, prompts, contexto, latencia y memoria.", "Estructura de una aplicacion desktop con PySide.", "Conexion inicial entre Python y Ollama por API local.", "Practica: ventana simple que envia prompts y muestra respuestas.", "Resultado: prototipo desktop conectado a un modelo local."]),
        ("Interfaz PySide y flujo de conversacion", ["Objetivo: construir una interfaz limpia para consultas locales.", "Widgets principales, layouts, señales y slots.", "Entrada de usuario, historial, estados de carga y manejo de errores.", "Persistencia simple de conversaciones y configuracion.", "Plantillas de prompt para tareas tecnicas concretas.", "Practica: chat local con historial y parametros basicos.", "Resultado: interfaz usable para conversar con el modelo."]),
        ("Archivos, contexto y funciones utiles", ["Objetivo: sumar contexto local sin prometer capacidades irreales.", "Lectura controlada de texto, fragmentacion y limites de contexto.", "Resumen, clasificacion y extraccion de datos simples.", "Validacion de respuestas y advertencias sobre alucinaciones.", "Organizacion de modulos para mantener el codigo mantenible.", "Practica: asistente que procesa un archivo de ejemplo.", "Resultado: aplicacion que usa contexto local verificable."]),
        ("Empaquetado y proyecto final", ["Objetivo: entregar una app offline funcional y documentada.", "Configuracion de icono, rutas, dependencias y variables.", "Pruebas sin internet, manejo de modelo no disponible y mensajes de ayuda.", "Empaquetado con herramienta adecuada segun el entorno.", "Documentacion de instalacion y requisitos de hardware.", "Practica: cierre de la app final con demostracion.", "Resultado: software desktop de IA offline listo para prueba interna."]),
    ],
    "tw-educa-curso-05": [
        ("Arquitectura Web GIS", ["Objetivo: comprender los componentes de un geoportal moderno.", "Roles de PostGIS, GeoServer, backend Python y cliente web.", "Formatos y servicios geoespaciales: WMS, WFS, GeoJSON y tiles.", "Preparacion de datos, CRS, estilos y metadatos minimos.", "Instalacion local de servicios y verificacion de puertos.", "Practica: publicar una capa de prueba en GeoServer.", "Resultado: stack base listo para un geoportal sencillo."]),
        ("Datos espaciales y servicios GeoServer", ["Objetivo: publicar datos con estilos y servicios interoperables.", "Conexion a PostGIS o almacenamiento de prueba.", "Workspaces, stores, layers y estilos SLD/alternativas.", "Filtros, bounding boxes, permisos basicos y rendimiento inicial.", "Pruebas de WMS/WFS desde navegador y herramientas GIS.", "Practica: capa estilizada y consultable.", "Resultado: servicio geoespacial verificable."]),
        ("Backend Python y cliente web", ["Objetivo: integrar datos espaciales con una interfaz web.", "API ligera con Python para catalogo, consultas y configuracion.", "Cliente con mapa, capas, controles, leyenda y popups.", "Consumo de GeoJSON/WMS y manejo de proyecciones.", "Validacion de errores frecuentes de CORS, rutas y puertos.", "Practica: visor web con capas y consulta de atributos.", "Resultado: geoportal minimo funcional."]),
        ("Despliegue y proyecto final", ["Objetivo: preparar una entrega reproducible.", "Organizacion de carpetas, variables, respaldos y datos de ejemplo.", "Opciones de despliegue local, VPS o intranet.", "Checklist de seguridad basica y rendimiento.", "Documentacion de uso y mantenimiento.", "Practica: presentacion del geoportal final.", "Resultado: geoportal Web GIS demostrable con servicios publicados."]),
    ],
    "tw-educa-curso-06": [
        ("Fundamentos LaTeX y entorno", ["Objetivo: escribir el primer documento cientifico correctamente estructurado.", "Instalacion de TeX Live o MiKTeX y configuracion de Texmaker.", "Preambulo, clases de documento, paquetes y codificacion.", "Secciones, parrafos, listas, tablas simples y compilacion PDF.", "Errores frecuentes de compilacion y lectura del log.", "Practica: articulo corto con estructura academica.", "Resultado: documento LaTeX compilado y ordenado."]),
        ("Matematica, figuras y tablas", ["Objetivo: producir contenido tecnico legible y reproducible.", "Ecuaciones en linea y en bloque, alineaciones y numeracion.", "Figuras, rutas de imagen, captions y referencias cruzadas.", "Tablas, unidades, simbolos y formatos recomendados.", "Organizacion de archivos para proyectos medianos.", "Practica: seccion tecnica con ecuaciones, figura y tabla.", "Resultado: documento con elementos cientificos integrados."]),
        ("Bibliografia y formato academico", ["Objetivo: gestionar referencias y citas sin desorden manual.", "BibTeX/BibLaTeX, archivo .bib, estilos y compilacion.", "Citas, bibliografia, enlaces, indice y numeracion.", "Plantillas para articulos, informes, tesis y separatas.", "Buenas practicas para nombres, rutas y control de versiones.", "Practica: informe con bibliografia y referencias cruzadas.", "Resultado: manuscrito academico coherente y citables."]),
        ("Proyecto final y entrega", ["Objetivo: cerrar un documento listo para revision.", "Revision de formato, consistencia visual y advertencias.", "Exportacion de PDF final y carpeta reproducible.", "Adaptacion a plantilla institucional o revista cuando aplique.", "Checklist de entrega: portada, resumen, figuras, tablas y bibliografia.", "Practica: entrega final del informe cientifico.", "Resultado: documento LaTeX completo con estructura profesional."]),
    ],
    "tw-educa-curso-07": [
        ("Datos de fluidos y Python cientifico", ["Objetivo: preparar datasets tecnicos para modelado predictivo.", "Tipos de datos en fluidos: CFD, laboratorio, sensores e hidrologia.", "Limpieza con Pandas, unidades, valores faltantes y outliers.", "Variables fisicas, escalamiento y separacion train/test.", "Visualizacion con Matplotlib para detectar patrones.", "Practica: dataset de variables hidraulicas o CFD simplificado.", "Resultado: datos listos para entrenar modelos supervisados."]),
        ("Modelos supervisados para prediccion", ["Objetivo: entrenar modelos de regresion aplicables a variables fisicas.", "Regresion lineal, arboles, random forest y criterios de seleccion.", "Entrenamiento con scikit-learn, pipelines y validacion cruzada basica.", "Metricas RMSE, MAE, R2 e interpretacion tecnica.", "Riesgos de sobreajuste y fuga de datos.", "Practica: prediccion de una variable de flujo.", "Resultado: modelo evaluado con metricas y graficos."]),
        ("Modelos sustitutos y reduccion de orden", ["Objetivo: aproximar resultados costosos sin reemplazar la fisica.", "Concepto de surrogate model para simulaciones o experimentos.", "Seleccion de features, importancia de variables y sensibilidad simple.", "Comparacion entre modelos y analisis de residuos.", "Visualizacion de superficies o curvas de respuesta.", "Practica: modelo sustituto para un caso parametrico.", "Resultado: aproximador documentado con limites de uso."]),
        ("Proyecto final aplicado", ["Objetivo: presentar un flujo ML completo para mecanica de fluidos.", "Definicion del problema, variables, supuestos y datos.", "Entrenamiento, ajuste razonable y comparacion de modelos.", "Interpretacion fisica de resultados y advertencias.", "Preparacion de notebook y reporte breve.", "Practica: exposicion del proyecto final.", "Resultado: notebook con modelo predictivo, metricas e interpretacion."]),
    ],
    "tw-educa-curso-08": [
        ("WSL, Linux y caso OpenFOAM", ["Objetivo: preparar OpenFOAM en Windows 10/11 usando WSL.", "Instalacion de WSL, distribucion Linux y dependencias basicas.", "Estructura de casos OpenFOAM: 0, constant y system.", "Comandos esenciales de terminal, rutas y permisos.", "Ejecucion de tutorial de prueba y revision de logs.", "Practica: correr un caso base y ubicar resultados.", "Resultado: entorno OpenFOAM funcional en WSL."]),
        ("Malla, condiciones y solver", ["Objetivo: modificar un caso CFD sencillo con criterio.", "blockMesh, geometria simple, parches y calidad de malla.", "Condiciones iniciales y de borde para variables principales.", "Seleccion de solver segun tipo de problema introductorio.", "ControlDict, fvSchemes, fvSolution y estabilidad numerica.", "Practica: ajustar dominio y condiciones de un caso guiado.", "Resultado: simulacion estable con parametros conocidos."]),
        ("Postproceso y validacion", ["Objetivo: interpretar resultados sin quedarse solo en imagenes.", "ParaView, campos, cortes, lineas, vectores y contornos.", "Extraccion de valores, convergencia, residuos y balances simples.", "Comparacion cualitativa con expectativas fisicas.", "Errores frecuentes: unidades, parches, malla y pasos de tiempo.", "Practica: reporte de resultados de un caso OpenFOAM.", "Resultado: postproceso con graficos e interpretacion tecnica."]),
        ("Proyecto final CFD", ["Objetivo: integrar configuracion, corrida y reporte de un caso.", "Organizacion de carpetas y reproduccion de una simulacion.", "Ajuste de parametros dentro de un alcance de 16 horas.", "Revision de logs, resultados y limitaciones.", "Preparacion de capturas, tablas y conclusiones.", "Practica: presentacion del caso final.", "Resultado: caso OpenFOAM ejecutado en WSL y documentado."]),
    ],
    "tw-educa-curso-09": [
        ("Fundamentos cloud para CFD", ["Objetivo: comprender cuando conviene llevar OpenFOAM a la nube.", "Conceptos de instancia, CPU, RAM, almacenamiento, red y costos.", "Comparacion de ejecucion local, WSL y servidor cloud.", "Preparacion de llaves SSH y buenas practicas de acceso.", "Instalacion base de OpenFOAM en una instancia de prueba.", "Practica: conexion remota y verificacion del entorno.", "Resultado: servidor cloud listo para pruebas CFD pequenas."]),
        ("Transferencia, ejecucion y monitoreo", ["Objetivo: ejecutar un caso OpenFOAM remoto de forma ordenada.", "Subida de casos, compresion, rutas y permisos.", "Ejecucion en background, logs, residuos y monitoreo de recursos.", "Control de costos, apagado de instancias y limpieza.", "Paralelizacion introductoria cuando el caso lo justifique.", "Practica: correr un caso remoto y descargar resultados.", "Resultado: flujo remoto reproducible y controlado."]),
        ("Postproceso y automatizacion", ["Objetivo: integrar resultados cloud con el trabajo local.", "Descarga selectiva de campos y reduccion de archivos pesados.", "Postproceso remoto o local con ParaView/paraFoam segun recursos.", "Scripts basicos para preparar, ejecutar y respaldar casos.", "Checklist de seguridad minima: llaves, usuarios y puertos.", "Practica: script simple de lanzamiento y recuperacion.", "Resultado: proceso de corrida cloud mas repetible."]),
        ("Proyecto final y costos", ["Objetivo: presentar una simulacion cloud con control tecnico y economico.", "Seleccion de instancia acorde al caso y presupuesto.", "Ejecucion, monitoreo, resultados y evidencia de apagado.", "Reporte de tiempos, recursos usados y limitaciones.", "Buenas practicas para futuras convocatorias o proyectos.", "Practica: exposicion de caso final en nube.", "Resultado: caso OpenFOAM ejecutado en cloud con reporte de costos."]),
    ],
    "tw-educa-curso-10": [
        ("Datos climaticos y oceanograficos", ["Objetivo: preparar datos ambientales en Python.", "Fuentes habituales: estaciones, grillas, NetCDF, CSV y APIs.", "Entornos con Python, Jupyter, NumPy, Pandas, xarray y Matplotlib.", "Fechas, husos horarios, unidades y metadatos.", "Lectura, limpieza y control de calidad inicial.", "Practica: cargar una serie temporal y diagnosticar problemas.", "Resultado: dataset ambiental limpio y documentado."]),
        ("Series temporales y estadistica", ["Objetivo: analizar variabilidad temporal y eventos.", "Resampleo, acumulados, promedios moviles y anomalías.", "Deteccion de faltantes, extremos y consistencia basica.", "Graficos de series, climatologias y distribuciones.", "Interpretacion tecnica sin sobreprometer conclusiones.", "Practica: analisis de precipitacion, viento, nivel o temperatura.", "Resultado: notebook con graficos y metricas temporales."]),
        ("Datos espaciales y grillas", ["Objetivo: trabajar con campos climatico-oceanograficos georreferenciados.", "NetCDF, coordenadas, dimensiones y seleccion por region.", "Mapas, cortes, perfiles y comparacion entre periodos.", "Uso de cartografia basica y exportacion de resultados.", "Buenas practicas de memoria para archivos grandes.", "Practica: mapa de variable ambiental en una region.", "Resultado: visualizacion espacial reproducible."]),
        ("Proyecto final aplicado", ["Objetivo: integrar lectura, analisis y visualizacion.", "Definicion de pregunta tecnica y fuente de datos.", "Procesamiento temporal y espacial dentro de un alcance realista.", "Graficos finales, interpretacion y limitaciones.", "Organizacion del notebook y archivos de salida.", "Practica: exposicion de resultados.", "Resultado: reporte tecnico breve con datos climaticos u oceanograficos."]),
    ],
    "tw-educa-curso-11": [
        ("C++ moderno para calculo tecnico", ["Objetivo: preparar bases de C++ aplicadas a problemas de fluidos.", "Compilador, proyecto, archivos fuente y flujo de compilacion.", "Tipos, funciones, referencias, vectores y manejo basico de errores.", "Entrada/salida de datos y organizacion de resultados.", "Buenas practicas para codigo numerico legible.", "Practica: calculadora de parametros hidraulicos simples.", "Resultado: programa C++ compilable y documentado."]),
        ("Estructuras numericas y discretizacion", ["Objetivo: representar mallas y variables fisicas sencillas.", "Arreglos, std::vector, estructuras y clases pequenas.", "Discretizacion 1D, condiciones de borde e iteraciones.", "Lectura/escritura CSV para postproceso.", "Validacion con casos conocidos y unidades.", "Practica: solucion numerica introductoria de transporte o difusion 1D.", "Resultado: solver didactico con salida verificable."]),
        ("Rendimiento y organizacion", ["Objetivo: mejorar claridad y eficiencia sin complejidad excesiva.", "Separacion en funciones, headers y modulos simples.", "Perfilado basico, reservas de memoria y bucles eficientes.", "Uso responsable de plantillas o clases cuando aporten claridad.", "Pruebas con parametros y comparacion de resultados.", "Practica: refactor del solver y medicion simple.", "Resultado: codigo tecnico mas mantenible."]),
        ("Proyecto final de software tecnico", ["Objetivo: cerrar una herramienta numerica pequena.", "Definicion del problema, ecuaciones simplificadas y supuestos.", "Implementacion, pruebas y graficos via CSV externo.", "Documentacion de uso, parametros y limitaciones.", "Revision de errores frecuentes de compilacion y ejecucion.", "Practica: presentacion del programa final.", "Resultado: miniaplicacion C++ aplicada a mecanica de fluidos."]),
    ],
    "tw-educa-curso-12": [
        ("Dart, Flutter y app tecnica base", ["Objetivo: iniciar una app movil para calculos de fluidos.", "Instalacion de Flutter SDK, Android Studio y emulador/dispositivo.", "Conceptos de Dart: variables, funciones, clases y null safety.", "Widgets, estructura de proyecto y hot reload.", "Diseno de pantalla para entrada de parametros tecnicos.", "Practica: calculadora movil simple.", "Resultado: app Flutter ejecutable con formulario tecnico."]),
        ("Estado, validacion y unidades", ["Objetivo: construir formularios confiables para datos de ingenieria.", "Text fields, validadores, conversion de tipos y mensajes de error.", "Manejo de estado simple y separacion de logica de calculo.", "Unidades, rangos validos y resultados con formato.", "Componentes reutilizables para tarjetas y resultados.", "Practica: modulo de calculo con validacion.", "Resultado: app que evita entradas incoherentes."]),
        ("Visualizacion y persistencia ligera", ["Objetivo: mejorar la utilidad de la app tecnica.", "Graficos simples o tablas para resultados.", "Persistencia local basica de casos o parametros.", "Navegacion entre pantallas y organizacion de componentes.", "Pruebas manuales en distintos tamanos de pantalla.", "Practica: historial de calculos o escenarios.", "Resultado: app movil mas completa y usable."]),
        ("Proyecto final y compilacion", ["Objetivo: entregar una APK o build de prueba.", "Icono, nombre de app, permisos y configuracion Android.", "Pruebas en dispositivo, errores frecuentes y rendimiento.", "Documentacion de formulas, supuestos y uso.", "Preparacion de capturas y demostracion.", "Practica: cierre del proyecto final.", "Resultado: app movil tecnica para mecanica de fluidos lista para prueba."]),
    ],
    "tw-educa-curso-13": [
        ("Imagen, video y medicion de flujo", ["Objetivo: entender el flujo de trabajo de vision artificial en rios y canales.", "Conceptos de imagen digital, video, FPS, resolucion y escala.", "Preparacion de Python, OpenCV, NumPy y notebooks.", "Carga de video, frames, recortes y calibracion basica.", "Limitaciones de iluminacion, perspectiva, reflejos y turbidez.", "Practica: extraccion de frames y region de interes.", "Resultado: video preparado para analisis reproducible."]),
        ("Preprocesamiento y deteccion", ["Objetivo: resaltar patrones visibles en superficie o estructuras.", "Filtros, color, escala de grises, umbrales y morfologia.", "Deteccion de bordes, contornos y puntos de referencia.", "Seguimiento simple de objetos o texturas cuando el video lo permita.", "Control de falsos positivos y revision visual.", "Practica: deteccion de elementos en canal o rio.", "Resultado: pipeline de preprocesamiento documentado."]),
        ("Velocidad, trayectorias e interpretacion", ["Objetivo: estimar variables observables sin prometer precision absoluta.", "Relacion pixel-metro, tiempo y desplazamiento.", "Seguimiento de trazadores o patrones con criterios basicos.", "Calculo de velocidades aproximadas y visualizacion de trayectorias.", "Validacion con datos de referencia cuando existan.", "Practica: estimacion de velocidad superficial en video de ejemplo.", "Resultado: analisis con supuestos y limites claros."]),
        ("Proyecto final aplicado", ["Objetivo: presentar un flujo de vision artificial para caso hidraulico.", "Seleccion de video, calibracion y objetivo de medicion.", "Procesamiento, visualizacion y exportacion de resultados.", "Interpretacion tecnica y advertencias de calidad de datos.", "Organizacion de notebook, codigo y evidencias.", "Practica: exposicion del proyecto final.", "Resultado: notebook de vision artificial aplicado a rios o canales."]),
    ],
    "tw-educa-curso-14": [
        ("CUDA y modelo de ejecucion GPU", ["Objetivo: comprender como programar kernels CUDA introductorios.", "Arquitectura CPU/GPU, host, device, threads, blocks y grids.", "Instalacion de CUDA Toolkit y verificacion con ejemplos.", "Primer kernel, compilacion y ejecucion.", "Transferencia de memoria entre host y device.", "Practica: suma vectorial y medicion simple.", "Resultado: programa CUDA funcional y explicado."]),
        ("Memoria, paralelismo y patrones basicos", ["Objetivo: escribir kernels mas utiles para calculo numerico.", "Memoria global, compartida y acceso coalescente a nivel introductorio.", "Mapeo de indices 1D/2D y control de limites.", "Sincronizacion dentro de bloques y errores frecuentes.", "Comparacion CPU vs GPU en tamanos pequenos y medianos.", "Practica: operacion sobre matriz o campo escalar.", "Resultado: kernel parametrico para datos tipo CFD."]),
        ("Aplicacion a mallas y operadores CFD", ["Objetivo: relacionar CUDA con operaciones comunes de simulacion.", "Campos escalares/vectoriales, stencil simple y diferencias finitas.", "Condiciones de borde simplificadas y arreglos linealizados.", "Medicion de tiempo, ancho de banda y cuellos de botella.", "Validacion numerica contra version CPU.", "Practica: operador de difusion o suavizado en grilla 2D.", "Resultado: kernel aplicado a campo CFD simplificado."]),
        ("Proyecto final y buenas practicas", ["Objetivo: entregar un ejemplo GPU reproducible y honesto en alcance.", "Organizacion de codigo CUDA/C++ y parametros de ejecucion.", "Manejo de errores CUDA y limpieza de memoria.", "Reporte de rendimiento y limitaciones del hardware usado.", "Recomendaciones para continuar hacia solvers mas complejos.", "Practica: presentacion del proyecto final.", "Resultado: miniaplicacion CUDA aplicada a un operador numerico."]),
    ],
})


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def section(text: str, title: str) -> str:
    pattern = rf"^{re.escape(title)}\s*\n(?P<body>.*?)(?=^[A-ZÁÉÍÓÚÑ¿][A-ZÁÉÍÓÚÑ0-9 /().,;:-]+$|\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group("body").strip() if match else ""


def bullets(section_text: str) -> list[str]:
    items = []
    for line in section_text.splitlines():
        clean = line.strip()
        if clean.startswith("- "):
            items.append(clean[2:].strip())
        elif re.match(r"^\d+\.\s+", clean):
            items.append(re.sub(r"^\d+\.\s+", "", clean).strip())
    return items


def parse_prices(text: str):
    body = section(text, "INVERSIÓN REFERENCIAL (IGV INCLUIDO)")
    prices = []
    values_all = []
    for line in body.splitlines():
        clean = line.strip()
        match = re.match(r"^- ([^:]+):\s*S/\s*([\d,]+)\s*\|\s*S/\s*([\d,]+)\s*\|\s*S/\s*([\d,]+)", clean)
        if not match:
            continue
        values = [int(match.group(i).replace(",", "")) for i in (2, 3, 4)]
        values_all.extend(values)
        prices.append({
            "publico": match.group(1).strip(),
            "preventa_soles": values[0],
            "lanzamiento_soles": values[1],
            "regular_soles": values[2],
            "moneda": "PEN",
            "incluye_igv": True,
        })
    minimum = min(values_all) if values_all else None
    return minimum, prices


def parse_detailed_sessions(text: str):
    body = section(text, "TEMARIO / CRONOGRAMA ACADÉMICO DETALLADO")
    if not body:
        return None
    matches = list(re.finditer(r"^(Sesi[óo]n|Semana)\s+(\d+)\s+[—-]\s+(.+)$", body, flags=re.M))
    modules = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        contents = bullets(body[start:end])
        if len(contents) >= 4:
            modules.append({
                "modulo": int(match.group(2)),
                "titulo": match.group(3).strip(),
                "proposito": contents[0],
                "contenidos": contents,
                "practica": next((x for x in contents if x.lower().startswith("práctica") or x.lower().startswith("practica")), "Práctica guiada de la sesión."),
                "resultado": next((x for x in contents if x.lower().startswith("resultado") or x.lower().startswith("producto")), "Resultado verificable de la sesión."),
                "tarea": "Avance del proyecto final o evidencia práctica de la sesión.",
            })
    return modules or None


def normalize_modules(course_id: str, text: str):
    if course_id in ENRICHED:
        source = ENRICHED[course_id]
        return [{
            "modulo": index + 1,
            "titulo": title,
            "proposito": contents[0],
            "contenidos": contents,
            "practica": next((x for x in contents if x.lower().startswith("practica")), "Práctica guiada de la sesión."),
            "resultado": next((x for x in contents if x.lower().startswith("resultado")), "Resultado verificable de la sesión."),
            "tarea": "Avance del proyecto final o evidencia práctica de la sesión.",
        } for index, (title, contents) in enumerate(source)]
    parsed = parse_detailed_sessions(text)
    return parsed


def price_lines(prices) -> list[str]:
    lines = []
    for item in prices:
        lines.append(
            f"- {item['publico']}: preventa S/ {item['preventa_soles']}, "
            f"lanzamiento S/ {item['lanzamiento_soles']}, regular S/ {item['regular_soles']}."
        )
    return lines


def whatsapp_message(course, prices) -> str:
    if prices:
        prices_text = "\n".join(price_lines(prices))
    else:
        prices_text = "- Inversión pendiente de confirmación. Deseo consultar la próxima convocatoria."
    return (
        f"Hola, deseo información para inscribirme en el curso \"{course['nombre']}\".\n\n"
        "He visto las modalidades y precios publicados:\n"
        f"{prices_text}\n\n"
        "Deseo conocer:\n"
        "1. Disponibilidad de vacantes.\n"
        "2. Próxima fecha de inicio.\n"
        "3. Modalidad y horario.\n"
        "4. Forma de pago.\n"
        "5. Requisitos para reservar mi vacante.\n\n"
        "Gracias."
    )


def sync_catalog_item(item, course):
    for key in [
        "precio", "precio_soles", "precios", "moneda", "numero_sesiones",
        "duracion_total_horas", "temario_general", "temario_por_sesion",
        "temario_base", "resultados_aprendizaje", "proyecto_final",
        "entregables", "herramientas", "materiales_incluidos",
        "certificacion", "faq", "whatsapp_mensaje", "estado_publicacion",
        "url_detalle", "url_publica", "url_canonica", "imagen", "imagen_og",
    ]:
        if key in course:
            item[key] = course[key]
    item["nombre"] = course["nombre"]
    item["linea"] = "tw-educa"
    item["linea_nombre"] = "TW Educa"
    item["tipo_item"] = "curso"
    item["visible_cliente"] = True


def main() -> None:
    courses = read_json(COURSES_JSON)
    baseline_courses = read_json(BASELINE_BACKUP) if BASELINE_BACKUP.exists() else courses
    baseline_by_id = {course["id"]: course for course in baseline_courses}
    report_rows = []
    whatsapp_changes = 0
    temario_changes = 0
    price_changes = 0
    s1_courses = []

    for course in courses:
        baseline = baseline_by_id.get(course["id"], course)
        txt = TXT_BY_ID.get(course["id"])
        text = txt.read_text(encoding="utf-8") if txt and txt.exists() else ""
        old_price = baseline.get("precio")
        old_min = baseline.get("precio_soles")
        old_whatsapp = baseline.get("whatsapp_mensaje", "")
        old_modules = baseline.get("temario_por_sesion") or []

        minimum, prices = parse_prices(text)
        if minimum:
            course["precio"] = f"Desde S/ {minimum} IGV incluido"
            course["precio_soles"] = minimum
            course["precios"] = prices
            course["moneda"] = "PEN"
        else:
            course["precio"] = "Consultar inversión"
            course["precio_soles"] = None
            course["precios"] = []

        modules = normalize_modules(course["id"], text)
        if modules:
            course["temario_por_sesion"] = modules
            course["temario_base"] = modules
            course["temario_general"] = [
                f"Sesión {m['modulo']}: {m['titulo']}." for m in modules
            ]
            course["temario_resumen"] = course["temario_general"]
            temario_changes += int(any(len((m.get("contenidos") or [])) < 4 for m in old_modules) or old_modules != modules)

        course["whatsapp_mensaje"] = whatsapp_message(course, course.get("precios") or [])
        course["etapas_comerciales"] = [
            {"etapa": "Preventa", "campo": "preventa_soles", "vigencia": "Consultar fecha límite y cupos por WhatsApp."},
            {"etapa": "Lanzamiento", "campo": "lanzamiento_soles", "vigencia": "Consultar disponibilidad de la etapa vigente."},
            {"etapa": "Regular", "campo": "regular_soles", "vigencia": "Tarifa referencial regular de la convocatoria."},
        ]
        course["fuente_interna"] = {
            "txt": str(txt.relative_to(ROOT)).replace("\\", "/") if txt else "",
            "precio": COMMERCIAL_SOURCES.get(course["id"], "TXT local del curso"),
            "actualizado": date.today().isoformat(),
            "confianza": "alta" if prices else "requiere_revision",
        }
        course["materiales_incluidos"] = course.get("materiales_incluidos") or course.get("incluye") or ["Archivos de práctica según convocatoria.", "Guía o material de apoyo del curso."]
        if not course.get("proyecto_final"):
            course["proyecto_final"] = "Proyecto aplicado integrador con evidencia verificable y presentación breve."
        if not course.get("resultados_aprendizaje"):
            course["resultados_aprendizaje"] = course.get("que_aprenderas") or ["Aplicar el flujo principal del curso en un caso guiado.", "Presentar un entregable final verificable."]

        if old_min == 1 or old_price == "Desde S/ 1 IGV incluido":
            s1_courses.append(course["nombre"])
        price_changes += int(old_price != course.get("precio") or old_min != course.get("precio_soles"))
        whatsapp_changes += int(old_whatsapp != course.get("whatsapp_mensaje"))

        report_rows.append({
            "id": course["id"],
            "slug": course["slug"],
            "nombre": course["nombre"],
            "imagen": course.get("imagen", ""),
            "txt": txt.name if txt else "",
            "precio_anterior": old_price,
            "precio_corregido": course.get("precio"),
            "mensaje_anterior": old_whatsapp,
            "mensaje_corregido": course.get("whatsapp_mensaje"),
            "sesiones": len(course.get("temario_por_sesion") or []),
            "temas_por_sesion": [len(m.get("contenidos") or []) for m in course.get("temario_por_sesion") or []],
            "estado": "PRECIO ERRÓNEO" if old_min == 1 else "CORRECTO",
            "confianza": "alta" if prices else "requiere revisión humana",
            "fuente": COMMERCIAL_SOURCES.get(course["id"], "TXT local"),
        })

    write_json(COURSES_JSON, courses)

    catalog = read_json(CATALOG_JSON)
    by_id = {course["id"]: course for course in courses}
    by_slug = {course["slug"]: course for course in courses}
    for item in catalog:
        course = by_id.get(item.get("id")) or by_slug.get(item.get("slug"))
        if course:
            sync_catalog_item(item, course)
    write_json(CATALOG_JSON, catalog)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    audit_lines = [
        "# Reporte auditoria precios cursos TW Educa",
        "",
        f"Fecha: {date.today().isoformat()}",
        "",
        f"- Cursos auditados: {len(courses)}",
        f"- Precios corregidos: {price_changes}",
        f"- Cursos con S/ 1.00 detectados: {len(s1_courses)}",
        "",
        "| ID | Slug | Curso | TXT | Precio anterior | Precio corregido | Sesiones | Temas por sesion | Estado | Confianza | Fuente |",
        "|---|---|---|---|---|---|---:|---|---|---|---|",
    ]
    for row in report_rows:
        audit_lines.append(
            f"| {row['id']} | {row['slug']} | {row['nombre']} | {row['txt']} | {row['precio_anterior']} | {row['precio_corregido']} | {row['sesiones']} | {row['temas_por_sesion']} | {row['estado']} | {row['confianza']} | {row['fuente']} |"
        )
    (DOCS_DIR / "reporte_auditoria_precios_cursos_tw.md").write_text("\n".join(audit_lines) + "\n", encoding="utf-8")

    whatsapp_lines = [
        "# Reporte correccion WhatsApp cursos TW",
        "",
        f"Fecha: {date.today().isoformat()}",
        f"- Mensajes corregidos: {whatsapp_changes}",
        "- Numero comercial usado: +51 952 354 282",
        "- CTA gratuitos eliminados del flujo comercial de cursos.",
        "",
        "| ID | Curso | Mensaje corregido |",
        "|---|---|---|",
    ]
    for row in report_rows:
        whatsapp_lines.append(f"| {row['id']} | {row['nombre']} | {row['mensaje_corregido'].replace(chr(10), '<br>')} |")
    (DOCS_DIR / "reporte_correccion_whatsapp_cursos_tw.md").write_text("\n".join(whatsapp_lines) + "\n", encoding="utf-8")

    temario_lines = [
        "# Reporte fortalecimiento temarios TW",
        "",
        f"Fecha: {date.today().isoformat()}",
        f"- Temarios fortalecidos o normalizados: {temario_changes}",
        "- Criterio: sesiones con titulo, proposito, practica, resultado y 4 o mas temas.",
        "",
        "## Fuentes oficiales consultadas",
        "",
        *[f"- {source}" for source in OFFICIAL_SOURCES],
        "",
        "| ID | Curso | Sesiones | Temas por sesion |",
        "|---|---|---:|---|",
    ]
    for row in report_rows:
        temario_lines.append(f"| {row['id']} | {row['nombre']} | {row['sesiones']} | {row['temas_por_sesion']} |")
    (DOCS_DIR / "reporte_fortalecimiento_temarios_tw.md").write_text("\n".join(temario_lines) + "\n", encoding="utf-8")

    validation_lines = [
        "# Reporte validacion comercial TW Educa",
        "",
        f"Fecha: {date.today().isoformat()}",
        f"- Cursos auditados: {len(courses)}",
        f"- Precios S/ 1.00 corregidos: {len(s1_courses)}",
        "- Pendiente real: validacion visual manual exhaustiva de todos los flyers en pantalla si se desea doble control humano.",
        "",
        "## Cursos que tenian S/ 1.00",
        "",
        *[f"- {name}" for name in s1_courses],
    ]
    (DOCS_DIR / "reporte_validacion_comercial_tw_educa.md").write_text("\n".join(validation_lines) + "\n", encoding="utf-8")

    checklist = [
        "# Checklist publicacion TW Educa",
        "",
        "- [x] Respaldar archivos modificados.",
        "- [x] Auditar 37 cursos visibles.",
        "- [x] Corregir precios residuales S/ 1.00.",
        "- [x] Reemplazar mensajes WhatsApp de material gratuito por mensajes de inscripcion.",
        "- [x] Fortalecer temarios por sesion.",
        "- [x] Crear validadores comerciales.",
        "- [ ] Revisar visualmente en navegador todas las resoluciones solicitadas antes de publicar.",
        "- [ ] Confirmar fechas vigentes de preventa/lanzamiento/regular para cada convocatoria.",
    ]
    (DOCS_DIR / "checklist_publicacion_tw_educa.md").write_text("\n".join(checklist) + "\n", encoding="utf-8")

    print(json.dumps({
        "cursos": len(courses),
        "precios_corregidos": price_changes,
        "s1": s1_courses,
        "whatsapp_corregidos": whatsapp_changes,
        "temarios": temario_changes,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
