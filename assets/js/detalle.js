const WHATSAPP_NUMBER_DETAIL = "51952354282";
const PAYPAL_URL_DETAIL = "https://www.paypal.com/paypalme/grupotecprog";

const detailItems = {
  "delft3d-wave-flow": detail("Delft3D Wave and Flow", "TW Educa", "Curso", "Modelamiento numérico", "Curso aplicado para modelamiento hidrodinámico, oleaje y análisis costero con enfoque técnico.", "Ayuda a profesionales y estudiantes a estructurar modelos costeros e hidráulicos con criterios prácticos.", "assets/img/servicios/cursos_ingenieros_y_cientificos/TW_EDUCA_MOOC_DELFT3D.jpg", "Desde S/ 249", "Desde USD 75 vía PayPal", "Virtual en vivo"),
  "admision-unac": detail("Preparación examen de admisión UNAC", "TW Educa", "Curso", "Preparación académica", "Programa para modalidades especiales con práctica guiada, materiales y orientación por objetivos.", "Ordena el estudio y refuerza los temas clave para rendir con mejor preparación.", "assets/img/cursos/capacitacion-empresarial.svg", "Desde S/ 149", "Desde USD 45 vía PayPal", "Virtual"),
  "matlab-programacion": detail("Programación de MATLAB", "TW Educa", "Curso", "Programación científica", "Fundamentos, scripts, funciones, gráficos y métodos de cálculo para ingeniería y ciencia.", "Permite automatizar cálculos y construir rutinas reproducibles para problemas técnicos.", "assets/img/cursos/curso-tecnologia-negocios.svg", "Desde S/ 199", "Desde USD 60 vía PayPal", "Virtual"),
  "openfoam-cfd": detail("CFD con OpenFOAM", "TW Educa", "Curso", "CFD e ingeniería", "Introducción práctica al flujo de trabajo CFD para casos educativos y simulación técnica.", "Reduce la curva de entrada a OpenFOAM mediante casos guiados y criterios de modelamiento.", "assets/img/cursos/capacitacion-empresarial.svg", "Desde S/ 249", "Desde USD 75 vía PayPal", "Virtual"),
  "python-poo": detail("Programación Orientada a Objetos con Python", "TW Educa", "Curso", "Software", "Clases, objetos, módulos, buenas prácticas y automatización con ejemplos aplicados.", "Fortalece la estructura del código para proyectos técnicos, científicos y empresariales.", "assets/img/servicios/cursos_ingenieros_y_cientificos/Curso_Python01.png", "Desde S/ 199", "Desde USD 60 vía PayPal", "Virtual"),
  "hp50g": detail("Programación HP 50G", "TW Educa", "Curso", "Calculadoras científicas", "Programación aplicada para automatizar cálculos y rutinas técnicas en HP 50G.", "Acelera cálculos repetitivos y rutinas de ingeniería en campo o aula.", "assets/img/servicios/cursos_ingenieros_y_cientificos/Curso_Programacion_HP50G.JPG", "Desde S/ 99", "Desde USD 30 vía PayPal", "Virtual"),
  "latex": detail("LaTeX", "TW Educa", "Curso", "Redacción técnica", "Documentos técnicos, tesis, informes, ecuaciones, tablas y plantillas profesionales.", "Mejora la presentación de documentos académicos y técnicos con formato consistente.", "assets/img/cursos/taller-innovacion-prototipado.svg", "Desde S/ 99", "Desde USD 30 vía PayPal", "Virtual"),
  "odoo-erp": detail("Odoo ERP", "TW Educa", "Curso", "Gestión empresarial", "Introducción a módulos, ventas, inventario, clientes y procesos para pequeños negocios.", "Facilita la comprensión de procesos ERP para organizar operaciones comerciales.", "assets/img/software/software-comercial-campus.svg", "Desde S/ 199", "Desde USD 60 vía PayPal", "Virtual"),
  "qgis-basico": detail("QGIS Básico", "TW Educa", "Curso", "GIS", "Mapas, capas, simbología, procesamiento espacial y entregables para proyectos.", "Ayuda a producir mapas y análisis geoespacial con herramientas accesibles.", "assets/img/cursos/curso-tecnologia-negocios.svg", "Desde S/ 149", "Desde USD 45 vía PayPal", "Virtual"),
  "software-medida": detail("Desarrollo de software a medida", "TW Innova", "Software", "Software empresarial", "Sistemas diseñados según procesos internos, usuarios, reportes y operación real.", "Digitaliza procesos que actualmente dependen de tareas manuales o herramientas dispersas.", "assets/img/software/software-comercial-dashboard.svg", "Desde S/ 1,200", "Desde USD 360 vía PayPal", "Proyecto por alcance"),
  "sistemas-web": detail("Sistemas web empresariales", "TW Innova", "Software", "Web apps", "Aplicaciones web para gestión, ventas, inscripciones, reportes y atención al cliente.", "Centraliza información y mejora la atención comercial u operativa.", "assets/img/software/software-comercial-campus.svg", "Desde S/ 1,500", "Desde USD 450 vía PayPal", "Proyecto"),
  "plugins-qgis": detail("Plugins QGIS", "TW Innova", "Software", "GIS", "Herramientas geoespaciales para automatizar procesos, validar datos y generar resultados.", "Ahorra tiempo en flujos GIS repetitivos y reduce errores de procesamiento.", "assets/img/servicios/servicio-implementacion-tecnologica.svg", "Desde S/ 1,200", "Desde USD 360 vía PayPal", "Cotización técnica"),
  "plugins-autocad": detail("Plugins AutoCAD", "TW Innova", "Software", "CAD", "Automatizaciones y rutinas para dibujo técnico, documentación y productividad.", "Mejora productividad en tareas CAD recurrentes.", "assets/img/software/software-open-source-tools.svg", "Desde S/ 1,300", "Desde USD 390 vía PayPal", "Cotización técnica"),
  "dashboards": detail("Dashboards", "TW Innova", "Software", "Analítica", "Paneles para visualizar indicadores, ventas, operaciones, proyectos y datos técnicos.", "Permite tomar decisiones con información clara y actualizada.", "assets/img/software/software-comercial-dashboard.svg", "Desde S/ 900", "Desde USD 270 vía PayPal", "Remoto"),
  "simulaciones-cfd": detail("Simulaciones CFD", "TW Innova", "Servicio", "Ingeniería aplicada", "Modelamiento, análisis y visualización de flujos para estudios técnicos especializados.", "Apoya decisiones técnicas mediante resultados visuales y criterios de ingeniería.", "assets/img/servicios/servicio-implementacion-tecnologica.svg", "Desde S/ 1,500", "Desde USD 450 vía PayPal", "Consultoría"),
  "modelamiento-hidraulico": detail("Modelamiento hidráulico", "TW Innova", "Servicio", "Hidráulica", "Evaluación técnica de sistemas hidráulicos, cauces, canales y escenarios de análisis.", "Permite analizar escenarios hidráulicos antes de tomar decisiones de proyecto.", "assets/img/banners/hero-tech.svg", "Desde S/ 1,200", "Desde USD 360 vía PayPal", "Consultoría"),
  "estudios-gis": detail("Estudios GIS", "TW Innova", "Servicio", "Geoespacial", "Procesamiento de capas, mapas, análisis espacial y entregables para proyectos.", "Convierte datos geográficos en entregables claros para gestión y proyectos.", "assets/img/cursos/curso-tecnologia-negocios.svg", "Desde S/ 700", "Desde USD 210 vía PayPal", "Remoto"),
  "procesamiento-datos": detail("Procesamiento de datos", "TW Innova", "Servicio", "Datos", "Limpieza, transformación, automatización y reportes para equipos técnicos y empresas.", "Reduce trabajo manual y mejora la calidad de información operativa.", "assets/img/servicios/servicio-soporte-tecnico.svg", "Desde S/ 600", "Desde USD 180 vía PayPal", "Remoto"),
  "expedientes-tecnicos": detail("Expedientes técnicos", "TW Construye", "Servicio", "Construcción", "Apoyo en documentación, metrados, presupuestos y revisión técnica por alcance.", "Ordena documentación técnica para proyectos y procesos de revisión.", "assets/img/servicios/servicio-desarrollo-software.svg", "Desde S/ 900", "Desde USD 270 vía PayPal", "Cotización"),
  "protesis": detail("Diseño de prótesis", "TW Salud y Vida / TW Bionic", "Servicio", "Prototipado biomédico", "Diseño, modelado y apoyo técnico para soluciones protésicas personalizadas.", "Contribuye al desarrollo de soluciones funcionales e inclusivas con enfoque técnico.", "assets/img/servicios/protesis_y_ortesis/TW_Salud_prtesis_manos.jpg", "Desde S/ 300", "Desde USD 90 vía PayPal", "Evaluación previa"),
  "ortesis": detail("Diseño de órtesis", "TW Salud y Vida / TW Bionic", "Servicio", "Tecnología médica", "Soporte técnico para diseño de órtesis, ajustes funcionales y prototipos.", "Facilita prototipos y apoyos funcionales según evaluación y alcance.", "assets/img/servicios/protesis_y_ortesis/TW_Salud_y_Vida_Prtesis_de_Pierna01.jpg", "Desde S/ 250", "Desde USD 75 vía PayPal", "Evaluación previa"),
  "cad-biomedico": detail("Modelado CAD biomédico", "TW Salud y Vida / TW Bionic", "Servicio", "CAD", "Modelado 3D, piezas funcionales y preparación para fabricación o impresión 3D.", "Convierte ideas y medidas en modelos digitales listos para revisión.", "assets/img/servicios/protesis_y_ortesis/TW_salud_y_vida_servicio_de_mantenimiento.png", "Desde S/ 180", "Desde USD 55 vía PayPal", "Remoto"),
  "impresion-3d": detail("Impresión 3D", "TW Salud y Vida / TW Bionic", "Servicio", "Prototipado", "Prototipos físicos, pruebas de forma y fabricación por coordinación técnica.", "Permite validar piezas y conceptos antes de una fabricación definitiva.", "assets/img/servicios/protesis_y_ortesis/TW_Salud_y_Vida_Mantenimiento_Unidad_Dental.jpg", "Desde S/ 120", "Desde USD 40 vía PayPal", "Cotización"),
  "plantillas-digitales": detail("Plantillas digitales", "Tecprog World Store", "Producto", "Recurso digital", "Plantillas para organizar cursos, ventas, reportes, presupuestos y entregables.", "Acelera la organización comercial y técnica con formatos listos para adaptar.", "assets/img/productos/producto-solucion-digital.svg", "Desde S/ 29", "Desde USD 10 vía PayPal", "Descarga digital"),
  "manuales-pdf": detail("Manuales PDF", "TW Educa", "Material", "Material educativo", "Materiales técnicos para cursos, talleres, ingeniería, programación y herramientas digitales.", "Complementa el aprendizaje con recursos estructurados y consultables.", "assets/img/descargas/descarga-manual-pdf.svg", "Desde S/ 29", "Desde USD 10 vía PayPal", "Descarga digital"),
  "recursos-ingenieria": detail("Recursos para ingeniería", "Tecprog World Store", "Producto", "Pack digital", "Archivos, guías, hojas de cálculo, scripts y recursos de apoyo técnico.", "Reúne herramientas útiles para estudio, análisis y entregables técnicos.", "assets/img/descargas/descarga-recursos-educativos.svg", "Desde S/ 49", "Desde USD 15 vía PayPal", "Entrega digital"),
  "packs-cursos": detail("Packs de cursos", "TW Educa", "Producto", "Formación", "Paquetes de cursos y materiales para rutas de aprendizaje especializadas.", "Ayuda a construir una ruta de formación completa por tema o herramienta.", "assets/img/productos/producto-kit-emprendedor.svg", "Desde S/ 149", "Desde USD 45 vía PayPal", "Virtual"),
  "licencias-demos": detail("Licencias o demos", "TW Innova", "Software", "Software", "Acceso a versiones comerciales, demos, instaladores o soluciones configurables.", "Permite evaluar o implementar soluciones digitales según necesidad.", "assets/img/descargas/descarga-instalador-demo.svg", "Desde S/ 99", "Desde USD 30 vía PayPal", "Digital")
};

function detail(title, line, type, category, description, problem, image, price, usd, modality) {
  return { title, line, type, category, description, problem, image, price, usd, modality };
}

function esc(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function detailWhatsapp(title) {
  const message = `Hola, deseo información sobre ${title}. Vengo desde la web de Tecprog World E.I.R.L.`;
  return `https://wa.me/${WHATSAPP_NUMBER_DETAIL}?text=${encodeURIComponent(message)}`;
}

function asset(path) {
  return `../${path}`;
}

function renderDetail() {
  const root = document.querySelector("[data-detail-root]");
  if (!root) return;

  const params = new URLSearchParams(window.location.search);
  const id = params.get("id") || "software-medida";
  const current = detailItems[id] || detailItems["software-medida"];

  document.title = `${current.title} | Tecprog World E.I.R.L.`;
  root.innerHTML = `
    <section class="detail-hero">
      <div class="section-shell detail-hero-grid">
        <div>
          <p class="eyebrow">${esc(current.line)} · ${esc(current.type)}</p>
          <h1>${esc(current.title)}</h1>
          <p>${esc(current.description)}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="${detailWhatsapp(current.title)}" target="_blank" rel="noopener">WhatsApp</a>
            <a class="btn btn-secondary" href="mailto:grupotecprog@gmail.com">Solicitar cotización</a>
            <a class="btn btn-gold" href="${PAYPAL_URL_DETAIL}" target="_blank" rel="noopener">Solicitar pago por PayPal</a>
          </div>
        </div>
        <figure class="detail-media">
          <img src="${asset(current.image)}" alt="${esc(current.title)}" onerror="this.closest('.detail-media').classList.add('has-fallback'); this.remove();">
          <figcaption>${esc(current.category)}</figcaption>
        </figure>
      </div>
    </section>
    <section class="section">
      <div class="section-shell detail-layout">
        <div class="detail-content">
          <article class="detail-block">
            <h2>Problema que resuelve</h2>
            <p>${esc(current.problem)}</p>
          </article>
          <article class="detail-block">
            <h2>Beneficios</h2>
            <ul class="check-list">
              <li>Orientación técnica y comercial según el alcance solicitado.</li>
              <li>Entrega coordinada con soporte por WhatsApp y correo.</li>
              <li>Enfoque aplicado para empresas, profesionales, estudiantes e instituciones.</li>
            </ul>
          </article>
          <article class="detail-block">
            <h2>Qué incluye</h2>
            <ul class="check-list">
              <li>Revisión de requerimientos o inscripción según corresponda.</li>
              <li>Material, entregable o propuesta de trabajo definida por alcance.</li>
              <li>Medios de pago nacionales e internacionales disponibles.</li>
            </ul>
          </article>
          <article class="detail-block">
            <h2>Público objetivo</h2>
            <p>Profesionales, estudiantes, emprendedores, empresas e instituciones que buscan soluciones tecnológicas, educativas o de ingeniería desde Perú.</p>
          </article>
        </div>
        <aside class="detail-sidebar">
          <article class="price-panel">
            <h2>Información comercial</h2>
            <dl>
              <div><dt>Línea</dt><dd>${esc(current.line)}</dd></div>
              <div><dt>Categoría</dt><dd>${esc(current.category)}</dd></div>
              <div><dt>Modalidad</dt><dd>${esc(current.modality)}</dd></div>
              <div><dt>Precio referencial</dt><dd>${esc(current.price)} · IGV incluido cuando corresponda</dd></div>
              <div><dt>Internacional</dt><dd>${esc(current.usd)}</dd></div>
            </dl>
            <div class="catalog-actions">
              <a class="btn btn-small btn-primary" href="${detailWhatsapp(current.title)}" target="_blank" rel="noopener">WhatsApp</a>
              <a class="btn btn-small btn-gold" href="${PAYPAL_URL_DETAIL}" target="_blank" rel="noopener">PayPal</a>
              <a class="btn btn-small" href="../index.html#productos">Volver al catálogo</a>
            </div>
            <p class="microcopy">Los precios son referenciales y pueden variar según alcance, modalidad, fecha de inscripción, requerimientos y promociones vigentes.</p>
          </article>
          <article class="detail-qr">
            <h2>Medios de pago</h2>
            <p>Pago nacional por QR Yape, transferencia previa coordinación y PayPal para clientes internacionales.</p>
            <div class="qr-frame">
              <img src="../assets/img/qr/QR_Yape.png" alt="QR Yape de Tecprog World">
              <span>Pago nacional por QR</span>
            </div>
          </article>
        </aside>
      </div>
    </section>
  `;
}

document.addEventListener("DOMContentLoaded", renderDetail);
