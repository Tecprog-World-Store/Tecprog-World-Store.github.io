const WHATSAPP_NUMBER = "51952354282";
const CONTACT_EMAIL = "grupotecprog@gmail.com";
const DEFAULT_PAYPAL_URL = "https://www.paypal.com/paypalme/grupotecprog";

const businessLines = [
  {
    id: "tw-educa",
    name: "TW Educa",
    icon: "assets/icons/education.svg",
    image: "assets/img/cursos/capacitacion-empresarial.svg",
    description: "Cursos técnicos, científicos y profesionales para ingeniería, software, GIS, datos, programación y herramientas digitales.",
    url: "lineas/tw-educa.html",
    chips: ["Cursos", "Materiales", "Software"]
  },
  {
    id: "tw-innova",
    name: "TW Innova",
    icon: "assets/icons/innovation.svg",
    image: "assets/img/software/software-comercial-dashboard.svg",
    description: "Desarrollo de software, automatización, portales web, plugins, dashboards y soluciones digitales empresariales.",
    url: "lineas/tw-innova.html",
    chips: ["Software", "Servicios", "Proyectos"]
  },
  {
    id: "tw-store",
    name: "Tecprog World Store",
    icon: "assets/icons/store.svg",
    image: "assets/img/productos/producto-kit-emprendedor.svg",
    description: "Productos tecnológicos, recursos digitales, licencias, plantillas, materiales descargables y packs comerciales.",
    url: "lineas/tw-store.html",
    chips: ["Productos", "Materiales", "Licencias"]
  },
  {
    id: "tw-taller",
    name: "TW Taller",
    icon: "assets/icons/workshop.svg",
    image: "assets/img/servicios/servicio-soporte-tecnico.svg",
    description: "Soporte técnico, mantenimiento, diagnóstico, implementación y asistencia operativa para equipos y procesos.",
    url: "lineas/tw-taller.html",
    chips: ["Servicios", "Soporte", "Proyectos"]
  },
  {
    id: "tw-construye",
    name: "TW Construye",
    icon: "assets/icons/build.svg",
    image: "assets/img/servicios/servicio-implementacion-tecnologica.svg",
    description: "Asistencia técnica para construcción civil, metrados, presupuestos, planos, modelamiento y revisión de proyectos.",
    url: "lineas/tw-construye.html",
    chips: ["Servicios", "Proyectos", "Consultoría"]
  },
  {
    id: "tw-salud-vida",
    name: "TW Salud y Vida / TW Bionic",
    icon: "assets/icons/health.svg",
    image: "assets/img/servicios/protesis_y_ortesis/TW_Salud_prtesis_manos.jpg",
    description: "Innovación médica, prótesis, órtesis, prototipado biomédico, instrumentación aplicada y soluciones inclusivas.",
    url: "lineas/tw-salud-vida.html",
    chips: ["Salud", "Prototipos", "Servicios"]
  },
  {
    id: "tw-interactive",
    name: "TW Interactive",
    icon: "assets/icons/innovation.svg",
    image: "assets/img/banners/software-suite.svg",
    description: "Experiencias interactivas, visualización técnica, laboratorios digitales, simuladores y herramientas educativas.",
    url: "lineas/tw-interactive.html",
    chips: ["Software", "Proyectos", "Cursos"]
  },
  {
    id: "tw-inox",
    name: "TW Inox",
    icon: "assets/icons/build.svg",
    image: "assets/img/banners/card-pattern.svg",
    description: "Soluciones técnicas, fabricación, diseño y apoyo comercial para aplicaciones con enfoque industrial y funcional.",
    url: "lineas/tw-inox.html",
    chips: ["Productos", "Servicios", "Proyectos"]
  }
];

const carouselData = {
  cursos: [
    item("delft3d-wave-flow", "Delft3D Wave and Flow", "TW Educa", "Modelamiento numérico", "Curso aplicado para modelamiento hidrodinámico, oleaje y análisis costero con enfoque técnico.", "Desde S/ 249", "Desde USD 75 vía PayPal", "Virtual en vivo", "assets/img/servicios/cursos_ingenieros_y_cientificos/TW_EDUCA_MOOC_DELFT3D.jpg", "detalle/curso.html?id=delft3d-wave-flow&periodo=2026-06"),
    item("admision-unac", "Preparación examen de admisión UNAC", "TW Educa", "Preparación académica", "Programa para modalidades especiales con práctica guiada, materiales y orientación por objetivos.", "Desde S/ 149", "Desde USD 45 vía PayPal", "Virtual", "assets/img/cursos/capacitacion-empresarial.svg", "detalle/curso.html?id=admision-unac&periodo=2026-06"),
    item("matlab-programacion", "Programación de MATLAB", "TW Educa", "Programación científica", "Fundamentos, scripts, funciones, gráficos y métodos de cálculo para ingeniería y ciencia.", "Desde S/ 199", "Desde USD 60 vía PayPal", "Virtual", "assets/img/cursos/curso-tecnologia-negocios.svg", "detalle/curso.html?id=matlab-programacion&periodo=2026-06"),
    item("openfoam-cfd", "CFD con OpenFOAM", "TW Educa", "CFD e ingeniería", "Introducción práctica al flujo de trabajo CFD para casos educativos y simulación técnica.", "Desde S/ 249", "Desde USD 75 vía PayPal", "Virtual", "assets/img/cursos/capacitacion-empresarial.svg", "detalle/curso.html?id=openfoam-cfd&periodo=2026-06"),
    item("python-poo", "Programación Orientada a Objetos con Python", "TW Educa", "Software", "Clases, objetos, módulos, buenas prácticas y automatización con ejemplos aplicados.", "Desde S/ 199", "Desde USD 60 vía PayPal", "Virtual", "assets/img/servicios/cursos_ingenieros_y_cientificos/Curso_Python01.png", "detalle/curso.html?id=python-poo&periodo=2026-06"),
    item("hp50g", "Programación HP 50G", "TW Educa", "Calculadoras científicas", "Programación aplicada para automatizar cálculos y rutinas técnicas en HP 50G.", "Desde S/ 99", "Desde USD 30 vía PayPal", "Virtual", "assets/img/servicios/cursos_ingenieros_y_cientificos/Curso_Programacion_HP50G.JPG", "detalle/curso.html?id=hp50g&periodo=2026-06"),
    item("latex", "LaTeX", "TW Educa", "Redacción técnica", "Documentos técnicos, tesis, informes, ecuaciones, tablas y plantillas profesionales.", "Desde S/ 99", "Desde USD 30 vía PayPal", "Virtual", "assets/img/cursos/taller-innovacion-prototipado.svg", "detalle/curso.html?id=latex&periodo=2026-06"),
    item("odoo-erp", "Odoo ERP", "TW Educa", "Gestión empresarial", "Introducción a módulos, ventas, inventario, clientes y procesos para pequeños negocios.", "Desde S/ 199", "Desde USD 60 vía PayPal", "Virtual", "assets/img/software/software-comercial-campus.svg", "detalle/curso.html?id=odoo-erp&periodo=2026-06"),
    item("qgis-basico", "QGIS Básico", "TW Educa", "GIS", "Mapas, capas, simbología, procesamiento espacial y entregables para proyectos.", "Desde S/ 149", "Desde USD 45 vía PayPal", "Virtual", "assets/img/cursos/curso-tecnologia-negocios.svg", "detalle/curso.html?id=qgis-basico&periodo=2026-06")
  ],
  software: [
    item("software-medida", "Desarrollo de software a medida", "TW Innova", "Software empresarial", "Sistemas diseñados según procesos internos, usuarios, reportes y operación real.", "Desde S/ 1,200", "Desde USD 360 vía PayPal", "Proyecto por alcance", "assets/img/software/software-comercial-dashboard.svg", "detalle/software.html?id=software-medida"),
    item("sistemas-web", "Sistemas web empresariales", "TW Innova", "Web apps", "Aplicaciones web para gestión, ventas, inscripciones, reportes y atención al cliente.", "Desde S/ 1,500", "Desde USD 450 vía PayPal", "Proyecto", "assets/img/software/software-comercial-campus.svg", "detalle/software.html?id=sistemas-web"),
    item("plugins-qgis", "Plugins QGIS", "TW Innova", "GIS", "Herramientas geoespaciales para automatizar procesos, validar datos y generar resultados.", "Desde S/ 1,200", "Desde USD 360 vía PayPal", "Cotización técnica", "assets/img/servicios/servicio-implementacion-tecnologica.svg", "detalle/software.html?id=plugins-qgis"),
    item("plugins-autocad", "Plugins AutoCAD", "TW Innova", "CAD", "Automatizaciones y rutinas para dibujo técnico, documentación y productividad.", "Desde S/ 1,300", "Desde USD 390 vía PayPal", "Cotización técnica", "assets/img/software/software-open-source-tools.svg", "detalle/software.html?id=plugins-autocad"),
    item("dashboards", "Dashboards", "TW Innova", "Analítica", "Paneles para visualizar indicadores, ventas, operaciones, proyectos y datos técnicos.", "Desde S/ 900", "Desde USD 270 vía PayPal", "Remoto", "assets/img/software/software-comercial-dashboard.svg", "detalle/software.html?id=dashboards")
  ],
  servicios: [
    item("simulaciones-cfd", "Simulaciones CFD", "TW Innova", "Ingeniería aplicada", "Modelamiento, análisis y visualización de flujos para estudios técnicos especializados.", "Desde S/ 1,500", "Desde USD 450 vía PayPal", "Consultoría", "assets/img/servicios/servicio-implementacion-tecnologica.svg", "detalle/servicio.html?id=simulaciones-cfd"),
    item("modelamiento-hidraulico", "Modelamiento hidráulico", "TW Innova", "Hidráulica", "Evaluación técnica de sistemas hidráulicos, cauces, canales y escenarios de análisis.", "Desde S/ 1,200", "Desde USD 360 vía PayPal", "Consultoría", "assets/img/banners/hero-tech.svg", "detalle/servicio.html?id=modelamiento-hidraulico"),
    item("estudios-gis", "Estudios GIS", "TW Innova", "Geoespacial", "Procesamiento de capas, mapas, análisis espacial y entregables para proyectos.", "Desde S/ 700", "Desde USD 210 vía PayPal", "Remoto", "assets/img/cursos/curso-tecnologia-negocios.svg", "detalle/servicio.html?id=estudios-gis"),
    item("procesamiento-datos", "Procesamiento de datos", "TW Innova", "Datos", "Limpieza, transformación, automatización y reportes para equipos técnicos y empresas.", "Desde S/ 600", "Desde USD 180 vía PayPal", "Remoto", "assets/img/servicios/servicio-soporte-tecnico.svg", "detalle/servicio.html?id=procesamiento-datos"),
    item("expedientes-tecnicos", "Expedientes técnicos", "TW Construye", "Construcción", "Apoyo en documentación, metrados, presupuestos y revisión técnica por alcance.", "Desde S/ 900", "Desde USD 270 vía PayPal", "Cotización", "assets/img/servicios/servicio-desarrollo-software.svg", "detalle/servicio.html?id=expedientes-tecnicos")
  ],
  salud: [
    item("protesis", "Diseño de prótesis", "TW Salud y Vida / TW Bionic", "Prototipado biomédico", "Diseño, modelado y apoyo técnico para soluciones protésicas personalizadas.", "Desde S/ 300", "Desde USD 90 vía PayPal", "Evaluación previa", "assets/img/servicios/protesis_y_ortesis/TW_Salud_prtesis_manos.jpg", "detalle/servicio.html?id=protesis"),
    item("ortesis", "Diseño de órtesis", "TW Salud y Vida / TW Bionic", "Tecnología médica", "Soporte técnico para diseño de órtesis, ajustes funcionales y prototipos.", "Desde S/ 250", "Desde USD 75 vía PayPal", "Evaluación previa", "assets/img/servicios/protesis_y_ortesis/TW_Salud_y_Vida_Prtesis_de_Pierna01.jpg", "detalle/servicio.html?id=ortesis"),
    item("cad-biomedico", "Modelado CAD biomédico", "TW Salud y Vida / TW Bionic", "CAD", "Modelado 3D, piezas funcionales y preparación para fabricación o impresión 3D.", "Desde S/ 180", "Desde USD 55 vía PayPal", "Remoto", "assets/img/servicios/protesis_y_ortesis/TW_salud_y_vida_servicio_de_mantenimiento.png", "detalle/servicio.html?id=cad-biomedico"),
    item("impresion-3d", "Impresión 3D", "TW Salud y Vida / TW Bionic", "Prototipado", "Prototipos físicos, pruebas de forma y fabricación por coordinación técnica.", "Desde S/ 120", "Desde USD 40 vía PayPal", "Cotización", "assets/img/servicios/protesis_y_ortesis/TW_Salud_y_Vida_Mantenimiento_Unidad_Dental.jpg", "detalle/servicio.html?id=impresion-3d")
  ],
  productos: [
    item("plantillas-digitales", "Plantillas digitales", "Tecprog World Store", "Recurso digital", "Plantillas para organizar cursos, ventas, reportes, presupuestos y entregables.", "Desde S/ 29", "Desde USD 10 vía PayPal", "Descarga digital", "assets/img/productos/producto-solucion-digital.svg", "detalle/producto.html?id=plantillas-digitales"),
    item("manuales-pdf", "Manuales PDF", "TW Educa", "Material educativo", "Materiales técnicos para cursos, talleres, ingeniería, programación y herramientas digitales.", "Desde S/ 29", "Desde USD 10 vía PayPal", "Descarga digital", "assets/img/descargas/descarga-manual-pdf.svg", "detalle/material.html?id=manuales-pdf"),
    item("recursos-ingenieria", "Recursos para ingeniería", "Tecprog World Store", "Pack digital", "Archivos, guías, hojas de cálculo, scripts y recursos de apoyo técnico.", "Desde S/ 49", "Desde USD 15 vía PayPal", "Entrega digital", "assets/img/descargas/descarga-recursos-educativos.svg", "detalle/producto.html?id=recursos-ingenieria"),
    item("packs-cursos", "Packs de cursos", "TW Educa", "Formación", "Paquetes de cursos y materiales para rutas de aprendizaje especializadas.", "Desde S/ 149", "Desde USD 45 vía PayPal", "Virtual", "assets/img/productos/producto-kit-emprendedor.svg", "detalle/producto.html?id=packs-cursos"),
    item("licencias-demos", "Licencias o demos", "TW Innova", "Software", "Acceso a versiones comerciales, demos, instaladores o soluciones configurables.", "Desde S/ 99", "Desde USD 30 vía PayPal", "Digital", "assets/img/descargas/descarga-instalador-demo.svg", "detalle/software.html?id=licencias-demos")
  ]
};

function item(id, title, line, category, description, price, usd, modality, image, detailUrl) {
  return { id, title, line, category, description, price, usd, modality, image, detailUrl };
}

function safeText(value, fallback = "") {
  return String(value || fallback)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function whatsappUrl(itemName) {
  const message = `Hola, deseo información sobre ${itemName}. Vengo desde la web de Tecprog World E.I.R.L.`;
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
}

function setupNavigation() {
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector("[data-nav]");
  if (!toggle || !nav) return;

  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
}

function setupWhatsAppLinks() {
  document.querySelectorAll("[data-whatsapp]").forEach((link) => {
    const topic = link.getAttribute("data-whatsapp") || "Tecprog World";
    link.href = whatsappUrl(topic);
    link.target = "_blank";
    link.rel = "noopener";
  });
}

function setupBannerCarousel() {
  const carousel = document.querySelector("[data-carousel]");
  if (!carousel) return;

  const slides = [...carousel.querySelectorAll(".banner-slide")];
  const dotsBox = carousel.querySelector("[data-carousel-dots]");
  if (!slides.length || !dotsBox) return;

  let activeIndex = 0;
  slides.forEach((_, index) => {
    const dot = document.createElement("button");
    dot.type = "button";
    dot.setAttribute("aria-label", `Ver banner ${index + 1}`);
    dot.addEventListener("click", () => showSlide(index));
    dotsBox.appendChild(dot);
  });

  const dots = [...dotsBox.querySelectorAll("button")];
  function showSlide(index) {
    activeIndex = index;
    slides.forEach((slide, slideIndex) => slide.classList.toggle("is-active", slideIndex === activeIndex));
    dots.forEach((dot, dotIndex) => dot.classList.toggle("is-active", dotIndex === activeIndex));
  }

  showSlide(activeIndex);
  window.setInterval(() => showSlide((activeIndex + 1) % slides.length), 6200);
}

function renderBusinessLines() {
  const target = document.querySelector("[data-business-lines]");
  if (!target) return;

  target.innerHTML = businessLines.map((line) => `
    <article class="business-card reveal">
      <a class="business-card-link" href="${safeText(line.url)}" aria-label="Ver ${safeText(line.name)}"></a>
      <div class="business-media">
        <img src="${safeText(line.image)}" alt="${safeText(line.name)}" loading="lazy">
      </div>
      <div class="business-head">
        <img src="${safeText(line.icon)}" alt="" width="42" height="42">
        <h3>${safeText(line.name)}</h3>
      </div>
      <p>${safeText(line.description)}</p>
      <div class="chip-row">${line.chips.map((chip) => `<span>${safeText(chip)}</span>`).join("")}</div>
      <div class="card-actions">
        <a class="btn btn-small btn-primary" href="${safeText(line.url)}">Explorar unidad</a>
        <a class="btn btn-small" href="${safeText(line.url)}#ofertas">Ver ofertas</a>
        <a class="btn btn-small btn-gold" href="${whatsappUrl(line.name)}" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </article>
  `).join("");
}

function renderCarousel(containerId, data, options = {}) {
  const title = options.title || "Galería";
  const target = document.querySelector(`[data-render-carousel="${containerId}"]`);
  if (!target || !data) return;

  const trackId = `carousel-${containerId}`;
  target.innerHTML = `
    <div class="carousel-controls">
      <button class="carousel-button" type="button" data-carousel-prev="${trackId}" aria-label="Anterior">‹</button>
      <button class="carousel-button" type="button" data-carousel-next="${trackId}" aria-label="Siguiente">›</button>
    </div>
    <div id="${trackId}" class="commerce-carousel" role="list" aria-label="${safeText(title)}">
      ${data.map((entry) => carouselCard(entry)).join("")}
    </div>
  `;
}

function carouselCard(entry) {
  return `
    <article class="catalog-card reveal" role="listitem">
      <a class="catalog-card-link" href="${safeText(entry.detailUrl)}" aria-label="Ver más sobre ${safeText(entry.title)}"></a>
      <div class="catalog-media">
        <img src="${safeText(entry.image)}" alt="${safeText(entry.title)}" loading="lazy" onerror="this.closest('.catalog-media').classList.add('has-fallback'); this.remove();">
        <span>${safeText(entry.line)}</span>
      </div>
      <div class="catalog-body">
        <p class="catalog-category">${safeText(entry.category)}</p>
        <h3>${safeText(entry.title)}</h3>
        <p>${safeText(entry.description)}</p>
        <div class="catalog-meta">
          <span>${safeText(entry.modality)}</span>
          <strong>${safeText(entry.price)}</strong>
        </div>
        <p class="usd-price">${safeText(entry.usd)}</p>
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="${safeText(entry.detailUrl)}">Ver más</a>
          <a class="btn btn-small btn-gold" href="${whatsappUrl(entry.title)}" target="_blank" rel="noopener">Comprar / consultar</a>
        </div>
      </div>
    </article>
  `;
}

function setupCommerceCarousels() {
  Object.entries(carouselData).forEach(([key, data]) => renderCarousel(key, data, { title: key }));

  document.querySelectorAll("[data-carousel-prev], [data-carousel-next]").forEach((button) => {
    button.addEventListener("click", () => {
      const trackId = button.getAttribute("data-carousel-prev") || button.getAttribute("data-carousel-next");
      const track = document.getElementById(trackId);
      if (!track) return;
      const direction = button.hasAttribute("data-carousel-prev") ? -1 : 1;
      track.scrollBy({ left: direction * Math.max(280, track.clientWidth * 0.82), behavior: "smooth" });
    });
  });
}

function observeReveals() {
  const elements = document.querySelectorAll(".reveal:not(.is-visible)");
  if (!("IntersectionObserver" in window)) {
    elements.forEach((element) => element.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  elements.forEach((element) => observer.observe(element));
}

document.addEventListener("DOMContentLoaded", () => {
  setupNavigation();
  setupWhatsAppLinks();
  setupBannerCarousel();
  renderBusinessLines();
  setupCommerceCarousels();
  observeReveals();
});
