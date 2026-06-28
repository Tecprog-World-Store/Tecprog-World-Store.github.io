const WHATSAPP_NUMBER = "51952354282";
const CONTACT_EMAIL = "grupotecprog@gmail.com";
const DEFAULT_PAYPAL_URL = "https://www.paypal.com/paypalme/grupotecprog";

function twRootPath(path) {
  return `/${String(path || "").replace(/^\/+/, "")}`;
}

const businessLines = [
  {
    id: "tw-investiga",
    name: "TW Investiga",
    icon: "assets/icons/innovation.svg",
    image: "assets/img/store/carruseles/tw-investiga-01.webp",
    description: "Investigación aplicada, desarrollo experimental, prototipos, estudios técnicos, documentación científica y transferencia tecnológica.",
    url: "lineas/tw-investiga.html",
    chips: ["Investigación", "Prototipos", "I+D"]
  },
  {
    id: "tw-innova",
    name: "TW Innova",
    icon: "assets/icons/innovation.svg",
    image: "assets/img/store/carruseles/tw-innova-01.webp",
    description: "Desarrollo de software comercial y open-source, hardware aplicado, automatización, visión artificial, plugins y sistemas web.",
    url: "lineas/tw-innova.html",
    chips: ["Software", "Hardware", "Automatización"]
  },
  {
    id: "tw-educa",
    name: "TW Educa",
    icon: "assets/icons/education.svg",
    image: "assets/img/store/carruseles/tw-educa-01.webp",
    description: "Cursos técnicos, científicos y profesionales para ingeniería, programación, GIS, CFD, métodos numéricos y herramientas aplicadas.",
    url: "lineas/tw-educa.html",
    chips: ["Cursos", "Compendios", "Ingeniería"]
  },
  {
    id: "tw-interactive",
    name: "TW Interactive",
    icon: "assets/icons/innovation.svg",
    image: "assets/img/store/carruseles/tw-interactive-01.webp",
    description: "Ingeniería mecánica de fluidos, hidrología, hidráulica, CFD, termofluidos, energía, aerodinámica y documentación técnica.",
    url: "lineas/tw-interactive.html",
    chips: ["Hidráulica", "CFD", "Python"]
  },
  {
    id: "tw-construye",
    name: "TW Construye",
    icon: "assets/icons/build.svg",
    image: "assets/img/store/carruseles/tw-construye-01.webp",
    description: "Asistencia técnica para construcción civil, metrados, presupuestos, planos, modelamiento y revisión de proyectos.",
    url: "lineas/tw-construye.html",
    chips: ["Servicios", "Proyectos", "Consultoría"]
  },
  {
    id: "tw-inox",
    name: "TW Inox",
    icon: "assets/icons/build.svg",
    image: "assets/img/store/carruseles/tw-inox-01.webp",
    description: "Proyectos en metales, estructuras, soportes, fabricación, pintura, automatización de procesos y prototipado.",
    url: "lineas/tw-inox.html",
    chips: ["Metalmecánica", "Fabricación", "Prototipos"]
  },
  {
    id: "tw-salud",
    name: "TW Salud",
    icon: "assets/icons/health.svg",
    image: "assets/img/store/carruseles/tw-salud-01.webp",
    description: "Diseño, prototipado, soporte técnico, accesibilidad, tecnología médica e investigación aplicada en salud.",
    url: "lineas/tw-salud.html",
    chips: ["Prótesis y órtesis", "Tecnología médica", "Accesibilidad"]
  },
  {
    id: "tw-store",
    name: "TW Store",
    icon: "assets/icons/store.svg",
    image: "assets/img/store/carruseles/tw-store-01.webp",
    description: "Tecnología bajo pedido por Tecprog World: celulares, laptops, monitores, audio, Apple, realidad virtual y accesorios con cotización por WhatsApp.",
    url: "store/index.html",
    chips: ["E-commerce", "Bajo pedido", "WhatsApp"]
  },
  {
    id: "tw-disfruta",
    name: "TW Disfruta",
    icon: "assets/icons/store.svg",
    image: "assets/img/store/carruseles/tw-disfruta-01.webp",
    description: "Entretenimiento digital, videojuegos, demos interactivas, assets 3D, widgets y experiencias creativas sujetas a alcance y licencia.",
    url: "disfruta/index.html",
    chips: ["Entretenimiento", "Demos", "Experiencias"]
  }
];

const carouselData = {
  cursos: [
    item("delft3d-wave-flow", "Delft3D Wave and Flow", "TW Educa", "Modelamiento numérico", "Curso aplicado para modelamiento hidrodinámico, oleaje y análisis costero con enfoque técnico.", "Acceso MOOC: Gratis", "Certificado desde S/ 49", "Virtual en vivo / grabado", "assets/img/servicios/cursos_ingenieros_y_cientificos/TW_EDUCA_MOOC_DELFT3D.jpg", "detalle/curso.html?id=delft3d-wave-flow&periodo=2026-06"),
    item("admision-unac", "Preparación examen de admisión UNAC", "TW Educa", "Preparación académica", "Programa para modalidades especiales con práctica guiada, materiales y orientación por objetivos.", "Acceso MOOC: Gratis", "Certificado desde S/ 49", "Virtual / grabado", "assets/img/cursos/capacitacion-empresarial.svg", "detalle/curso.html?id=admision-unac&periodo=2026-06"),
    item("matlab-programacion", "Programación de MATLAB", "TW Educa", "Programación científica", "Fundamentos, scripts, funciones, gráficos y métodos de cálculo para ingeniería y ciencia.", "Acceso MOOC: Gratis", "Certificado desde S/ 49", "Virtual / grabado", "assets/img/cursos/curso-tecnologia-negocios.svg", "detalle/curso.html?id=matlab-programacion&periodo=2026-06"),
    item("openfoam-cfd", "CFD con OpenFOAM", "TW Educa", "CFD e ingeniería", "Introducción práctica al flujo de trabajo CFD para casos educativos y simulación técnica.", "Acceso MOOC: Gratis", "Certificado desde S/ 49", "Virtual / grabado", "assets/img/cursos/capacitacion-empresarial.svg", "detalle/curso.html?id=openfoam-cfd&periodo=2026-06"),
    item("python-poo", "Programación Orientada a Objetos con Python", "TW Educa", "Software", "Clases, objetos, módulos, buenas prácticas y automatización con ejemplos aplicados.", "Acceso MOOC: Gratis", "Certificado desde S/ 49", "Virtual / grabado", "assets/img/servicios/cursos_ingenieros_y_cientificos/Curso_Python01.png", "detalle/curso.html?id=python-poo&periodo=2026-06"),
    item("hp50g", "Programación HP 50G", "TW Educa", "Calculadoras científicas", "Programación aplicada para automatizar cálculos y rutinas técnicas en HP 50G.", "Acceso MOOC: Gratis", "Certificado desde S/ 19", "Virtual / grabado", "assets/img/servicios/cursos_ingenieros_y_cientificos/Curso_Programacion_HP50G.JPG", "detalle/curso.html?id=hp50g&periodo=2026-06"),
    item("latex", "LaTeX", "TW Educa", "Redacción técnica", "Documentos técnicos, tesis, informes, ecuaciones, tablas y plantillas profesionales.", "Acceso MOOC: Gratis", "Certificado desde S/ 49", "Virtual / grabado", "assets/img/cursos/taller-innovacion-prototipado.svg", "detalle/curso.html?id=latex&periodo=2026-06"),
    item("odoo-erp", "Odoo ERP", "TW Educa", "Gestión empresarial", "Introducción a módulos, ventas, inventario, clientes y procesos para pequeños negocios.", "Acceso MOOC: Gratis", "Certificado desde S/ 49", "Virtual / grabado", "assets/img/software/software-comercial-campus.svg", "detalle/curso.html?id=odoo-erp&periodo=2026-06"),
    item("qgis-basico", "QGIS Básico", "TW Educa", "GIS", "Mapas, capas, simbología, procesamiento espacial y entregables para proyectos.", "Acceso MOOC: Gratis", "Certificado desde S/ 49", "Virtual / grabado", "assets/img/cursos/curso-tecnologia-negocios.svg", "detalle/curso.html?id=qgis-basico&periodo=2026-06")
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
    item("protesis", "Diseño de prótesis", "TW Salud", "Prototipado biomédico", "Diseño, modelado y apoyo técnico para soluciones protésicas personalizadas.", "Desde S/ 300", "Desde USD 90 vía PayPal", "Evaluación previa", "assets/img/servicios/protesis_y_ortesis/TW_Salud_prtesis_manos.jpg", "detalle/servicio.html?id=protesis"),
    item("ortesis", "Diseño de órtesis", "TW Salud", "Tecnología médica", "Soporte técnico para diseño de órtesis, ajustes funcionales y prototipos.", "Desde S/ 250", "Desde USD 75 vía PayPal", "Evaluación previa", "assets/img/servicios/protesis_y_ortesis/TW_Salud_y_Vida_Prtesis_de_Pierna01.jpg", "detalle/servicio.html?id=ortesis"),
    item("cad-biomedico", "Modelado CAD biomédico", "TW Salud", "CAD", "Modelado 3D, piezas funcionales y preparación para fabricación o impresión 3D.", "Desde S/ 180", "Desde USD 55 vía PayPal", "Remoto", "assets/img/servicios/protesis_y_ortesis/TW_salud_y_vida_servicio_de_mantenimiento.png", "detalle/servicio.html?id=cad-biomedico"),
    item("impresion-3d", "Impresión 3D", "TW Salud", "Prototipado", "Prototipos físicos, pruebas de forma y fabricación por coordinación técnica.", "Desde S/ 120", "Desde USD 40 vía PayPal", "Cotización", "assets/img/servicios/protesis_y_ortesis/TW_Salud_y_Vida_Mantenimiento_Unidad_Dental.jpg", "detalle/servicio.html?id=impresion-3d")
  ],
  productos: [
    item("plantillas-digitales", "Plantillas digitales", "TW Store", "Recurso digital", "Plantillas para organizar cursos, ventas, reportes, presupuestos y entregables.", "Desde S/ 29", "Desde USD 10 vía PayPal", "Descarga digital", "assets/img/productos/producto-solucion-digital.svg", "detalle/producto.html?id=plantillas-digitales"),
    item("manuales-pdf", "Manuales PDF", "TW Educa", "Material educativo", "Materiales técnicos para cursos, talleres, ingeniería, programación y herramientas digitales.", "Desde S/ 29", "Desde USD 10 vía PayPal", "Descarga digital", "assets/img/descargas/descarga-manual-pdf.svg", "detalle/material.html?id=manuales-pdf"),
    item("recursos-ingenieria", "Recursos para ingeniería", "TW Store", "Pack digital", "Archivos, guías, hojas de cálculo, scripts y recursos de apoyo técnico.", "Desde S/ 49", "Desde USD 15 vía PayPal", "Entrega digital", "assets/img/descargas/descarga-recursos-educativos.svg", "detalle/producto.html?id=recursos-ingenieria"),
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
    link.rel = "noopener noreferrer";
  });
}

function setupExternalLinks() {
  document.querySelectorAll('a[href^="http"], a[href^="https://wa.me"]').forEach((link) => {
    const url = new URL(link.href, window.location.href);
    if (url.origin !== window.location.origin) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    }
  });
}

function setupContextNav() {
  const items = document.querySelectorAll("[data-side-nav] a[href^='#']");
  if (!items.length) return;

  const sections = [...items]
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  if (!sections.length || !("IntersectionObserver" in window)) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      items.forEach((link) => {
        link.classList.toggle("is-active", link.getAttribute("href") === `#${entry.target.id}`);
      });
    });
  }, { rootMargin: "-35% 0px -55% 0px", threshold: 0.01 });

  sections.forEach((section) => observer.observe(section));
}

async function loadBusinessLineData() {
  try {
    const response = await fetch(twRootPath("data/lineas_negocio.json"));
    if (!response.ok) throw new Error("No se pudo cargar data/lineas_negocio.json");
    const items = await response.json();
    return items
      .filter((line) => line.activo !== false)
      .sort((a, b) => Number(a.prioridad || 999) - Number(b.prioridad || 999));
  } catch {
    return businessLines.map((line, index) => ({
      nombre: line.name,
      slug: line.id,
      pagina: line.url,
      descripcion: line.description,
      categoria_principal: line.chips?.[0] || "Tecprog World",
      imagen: line.image,
      prioridad: index + 1,
      alt: line.name
    }));
  }
}

function lineSlideImage(line) {
  const fallback = {
    "tw-store": "assets/img/store/carruseles/tw-store-01.webp",
    "tw-disfruta": "assets/img/store/carruseles/tw-disfruta-01.webp",
    "tw-educa": "assets/img/store/carruseles/tw-educa-01.webp",
    "tw-innova": "assets/img/store/carruseles/tw-innova-01.webp",
    "tw-salud": "assets/img/store/carruseles/tw-salud-01.webp",
    "tw-interactive": "assets/img/store/carruseles/tw-interactive-01.webp",
    "tw-construye": "assets/img/store/carruseles/tw-construye-01.webp",
    "tw-inox": "assets/img/store/carruseles/tw-inox-01.webp",
    "tw-investiga": "assets/img/store/carruseles/tw-investiga-01.webp"
  };
  return line.imagen || fallback[line.slug] || "assets/img/banners/hero-tech.svg";
}

async function setupBannerCarousel() {
  const carousel = document.querySelector("[data-carousel]");
  if (!carousel) return;

  const dotsBox = carousel.querySelector("[data-carousel-dots]");
  const lines = await loadBusinessLineData();
  if (lines.length && dotsBox) {
    carousel.querySelectorAll(".banner-slide").forEach((slide) => slide.remove());
    dotsBox.insertAdjacentHTML("beforebegin", lines.map((line, index) => `
      <article class="banner-slide ${index === 0 ? "is-active" : ""}" style="background-image: linear-gradient(125deg, rgba(10, 32, 67, 0.97), rgba(12, 79, 107, 0.88) 58%, rgba(65, 44, 4, 0.82)), url('${safeText(twRootPath(lineSlideImage(line)))}');">
        <span>${safeText(line.nombre_corto || line.nombre)}</span>
        <h2>${safeText(line.subtitulo || line.descripcion || line.categoria_principal)}</h2>
        <a href="${safeText(line.pagina ? twRootPath(line.pagina) : "#lineas")}" aria-label="Ver ${safeText(line.nombre)}">Ver sección</a>
      </article>
    `).join(""));
  }

  const slides = [...carousel.querySelectorAll(".banner-slide")];
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
      <a class="business-card-link" href="${safeText(twRootPath(line.url))}" aria-label="Ver ${safeText(line.name)}"></a>
      <div class="business-media">
        <img src="${safeText(twRootPath(line.image))}" alt="${safeText(line.name)}" loading="lazy">
      </div>
      <div class="business-head">
        <img src="${safeText(twRootPath(line.icon))}" alt="" width="42" height="42">
        <h3>${safeText(line.name)}</h3>
      </div>
      <p>${safeText(line.description)}</p>
      <div class="chip-row">${line.chips.map((chip) => `<span>${safeText(chip)}</span>`).join("")}</div>
      <div class="card-actions">
        <a class="btn btn-small btn-primary" href="${safeText(twRootPath(line.url))}">Ver linea</a>
        <a class="btn btn-small" href="${safeText(twRootPath(line.url))}#ofertas">Ver catalogo</a>
        <a class="btn btn-small btn-gold" href="${whatsappUrl(line.name)}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
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
      <a class="catalog-card-link" href="${safeText(twRootPath(entry.detailUrl))}" aria-label="Ver más sobre ${safeText(entry.title)}"></a>
      <div class="catalog-media">
        <img src="${safeText(twRootPath(entry.image))}" alt="${safeText(entry.title)}" loading="lazy" onerror="this.closest('.catalog-media').classList.add('has-fallback'); this.remove();">
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
          <a class="btn btn-small btn-primary" href="${safeText(twRootPath(entry.detailUrl))}">Ver más</a>
          <a class="btn btn-small btn-gold" href="${whatsappUrl(entry.title)}" target="_blank" rel="noopener noreferrer">Consultar</a>
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

async function setupAudioPlayer() {
  const widget = document.querySelector("[data-audio-widget]");
  const audio = widget?.querySelector("[data-audio-player]");
  if (!widget || !audio) return;
  const play = widget.querySelector("[data-audio-play]");
  const prev = widget.querySelector("[data-audio-prev]");
  const next = widget.querySelector("[data-audio-next]");
  const volume = widget.querySelector("[data-audio-volume]");
  const title = widget.querySelector("[data-audio-title]");
  let playlist = [];
  let currentIndex = 0;
  let userRequestedPlayback = false;

  function setStatus(text) {
    if (title) title.textContent = text;
  }

  function updatePlayButton(isPlaying = false) {
    if (!play) return;
    play.textContent = isPlaying ? "Pausar" : "Reproducir";
    play.setAttribute("aria-pressed", String(isPlaying));
  }

  function loadTrack(index) {
    if (!playlist.length) {
      audio.removeAttribute("src");
      setStatus("Audio no disponible");
      updatePlayButton(false);
      return;
    }
    currentIndex = (index + playlist.length) % playlist.length;
    const track = playlist[currentIndex];
    audio.src = track.src;
    audio.load();
    setStatus(track.title || `Pista ${currentIndex + 1}`);
  }

  async function playCurrent() {
    if (!playlist.length) {
      setStatus("Audio no disponible");
      updatePlayButton(false);
      return;
    }
    userRequestedPlayback = true;
    try {
      await audio.play();
      updatePlayButton(true);
    } catch (error) {
      console.warn("No se pudo reproducir la pista de audio.", playlist[currentIndex]?.src, error);
      if (audio.error) setStatus("Audio no disponible");
      else setStatus(playlist[currentIndex]?.title || `Pista ${currentIndex + 1}`);
      updatePlayButton(false);
    }
  }

  async function moveTrack(step, shouldPlay = userRequestedPlayback && !audio.paused) {
    if (!playlist.length) return;
    audio.pause();
    loadTrack(currentIndex + step);
    updatePlayButton(false);
    if (shouldPlay) await playCurrent();
  }

  audio.volume = Number(volume?.value || 0.35);

  try {
    const response = await fetch(twRootPath("assets/audio/playlist.json"), { cache: "no-store" });
    playlist = response.ok ? await response.json() : [];
    if (!Array.isArray(playlist)) playlist = [];
    playlist = playlist.filter((track) => track?.src);
  } catch (error) {
    console.warn("No se pudo cargar assets/audio/playlist.json.", error);
    playlist = [];
  }

  if (playlist.length) loadTrack(0);
  else setStatus("Audio no disponible");

  play?.addEventListener("click", async () => {
    if (!playlist.length) {
      setStatus("Audio no disponible");
      return;
    }
    if (audio.paused) await playCurrent();
    else {
      audio.pause();
      updatePlayButton(false);
    }
  });

  next?.addEventListener("click", () => {
    moveTrack(1);
  });

  prev?.addEventListener("click", () => {
    moveTrack(-1);
  });

  audio.addEventListener("ended", () => {
    moveTrack(1, userRequestedPlayback);
  });

  audio.addEventListener("error", () => {
    if (!playlist.length) return;
    console.warn("Pista no disponible, se intentará cargar la siguiente.", playlist[currentIndex]?.src);
    if (playlist.length === 1) {
      setStatus("Audio no disponible");
      updatePlayButton(false);
      return;
    }
    moveTrack(1, userRequestedPlayback);
  });

  volume?.addEventListener("input", () => {
    audio.volume = Number(volume.value || 0.35);
  });

  document.addEventListener("click", (event) => {
    if (!event.target.closest("[data-audio-focus]")) return;
    widget.scrollIntoView({ behavior: "smooth", block: "center" });
    widget.classList.add("is-highlighted");
    play?.focus();
    window.setTimeout(() => widget.classList.remove("is-highlighted"), 1200);
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
  setupExternalLinks();
  setupContextNav();
  setupBannerCarousel();
  renderBusinessLines();
  setupCommerceCarousels();
  observeReveals();
});
