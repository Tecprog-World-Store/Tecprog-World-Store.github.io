const WHATSAPP_NUMBER = "51952354282";
const CONTACT_EMAIL = "grupotecprog@gmail.com";
const DEFAULT_PAYPAL_URL = "https://www.paypal.com/paypalme/editar-enlace";

const catalogSources = {
  cursos: "data/cursos.json",
  servicios: "data/servicios.json",
  productos: "data/productos.json"
};

// Las líneas de negocio viven en JS porque son parte estable de la marca.
// Los catálogos comerciales se editan aparte desde archivos JSON.
const businessLines = [
  {
    name: "Tecprog World Store",
    icon: "assets/icons/store.svg",
    description: "Venta de productos tecnológicos, recursos digitales, herramientas, licencias, plantillas y servicios promocionales.",
    facebook: "https://www.facebook.com/"
  },
  {
    name: "TW Educa",
    icon: "assets/icons/education.svg",
    description: "Cursos técnicos, científicos y profesionales para ingeniería, software, GIS, datos, programación y herramientas digitales.",
    facebook: "https://www.facebook.com/"
  },
  {
    name: "TW Innova",
    icon: "assets/icons/innovation.svg",
    description: "Desarrollo de software, hardware, automatización, portales web, plugins, visión artificial y soluciones digitales.",
    facebook: "https://www.facebook.com/"
  },
  {
    name: "TW Taller",
    icon: "assets/icons/workshop.svg",
    description: "Soporte técnico, mantenimiento, diagnóstico, implementación y asistencia operativa para equipos y procesos.",
    facebook: "https://www.facebook.com/"
  },
  {
    name: "TW Construye",
    icon: "assets/icons/build.svg",
    description: "Proyectos de construcción civil, arquitectura, metrados, presupuestos, planos, modelamiento y asistencia técnica.",
    facebook: "https://www.facebook.com/"
  },
  {
    name: "TW Salud y Vida / TW Bionic",
    icon: "assets/icons/health.svg",
    description: "Innovación médica, prótesis, ingeniería biomédica, prototipado, simulación, instrumentación y soluciones inclusivas.",
    facebook: "https://www.facebook.com/"
  }
];

function safeText(value, fallback = "") {
  return String(value || fallback)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function whatsappUrl(itemName) {
  const message = `Hola, deseo información para comprar: ${itemName}`;
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
}

// Controla el menú móvil fijo sin depender de librerías externas.
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

// Carrusel ligero para banners de portada; suficiente para GitHub Pages.
function setupCarousel() {
  const carousel = document.querySelector("[data-carousel]");
  if (!carousel) return;

  const slides = [...carousel.querySelectorAll(".banner-slide")];
  const dotsBox = carousel.querySelector("[data-carousel-dots]");
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

// Renderiza tarjetas corporativas con enlaces temporales editables de Facebook.
function renderBusinessLines() {
  const target = document.querySelector("[data-business-lines]");
  if (!target) return;

  target.innerHTML = businessLines.map((line) => `
    <article class="business-card reveal">
      <img src="${safeText(line.icon)}" alt="" width="42" height="42">
      <h3>${safeText(line.name)}</h3>
      <p>${safeText(line.description)}</p>
      <div class="card-actions">
        <a class="btn btn-small" href="${safeText(line.facebook)}" target="_blank" rel="noopener">Facebook</a>
        <a class="btn btn-small btn-primary" href="${whatsappUrl(line.name)}" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </article>
  `).join("");
}

// Construye una imagen segura. Si el archivo no existe, mantiene un placeholder visual.
function mediaMarkup(item, fallbackLabel) {
  const image = safeText(item.imagen || "");
  const label = safeText(item.etiqueta || item.categoria || fallbackLabel);
  const img = image
    ? `<img src="${image}" alt="${safeText(item.nombre)}" loading="lazy" onerror="this.closest('.catalog-media').classList.add('has-fallback'); this.remove();">`
    : "";

  return `
    <div class="catalog-media ${image ? "" : "has-fallback"}">
      ${img}
      <span>${label}</span>
    </div>
  `;
}

// Tarjeta comercial común para cursos, servicios y productos.
function commerceCard(item, type) {
  const card = document.createElement("article");
  card.className = "catalog-card reveal";

  card.innerHTML = `
    ${mediaMarkup(item, type)}
    <div class="catalog-body">
      <p class="catalog-category">${safeText(item.linea || "Tecprog World")} · ${safeText(item.categoria || "Catálogo")}</p>
      <h3>${safeText(item.nombre)}</h3>
      <p>${safeText(item.descripcion, "Descripción pendiente.")}</p>
      <div class="catalog-meta">
        <span>${safeText(item.modalidad || "Consultar modalidad")}</span>
        <strong>${safeText(item.precio || "Cotizar")}</strong>
      </div>
      <div class="catalog-actions">
        <a class="btn btn-small btn-primary" href="${whatsappUrl(item.nombre)}" target="_blank" rel="noopener">Comprar por WhatsApp</a>
        <a class="btn btn-small btn-gold" href="${safeText(item.paypal || DEFAULT_PAYPAL_URL)}" target="_blank" rel="noopener">PayPal</a>
        <a class="btn btn-small" href="#contacto">Yape / QR</a>
      </div>
    </div>
  `;

  return card;
}

// Carga cada JSON y evita que una falla rompa el resto de la página.
async function renderCatalog(type) {
  const target = document.querySelector(`[data-render="${type}"]`);
  if (!target) return;
  target.innerHTML = `<p class="loading">Cargando ${type}...</p>`;

  try {
    const response = await fetch(catalogSources[type]);
    if (!response.ok) throw new Error(`No se pudo cargar ${type}`);
    const items = await response.json();
    target.innerHTML = "";
    items.forEach((item) => target.appendChild(commerceCard(item, type)));
    observeReveals();
  } catch (error) {
    target.innerHTML = `
      <article class="catalog-card catalog-error">
        <div class="catalog-body">
          <h3>Contenido no disponible</h3>
          <p>Revisa el archivo JSON de ${safeText(type)} o prueba el sitio con un servidor local.</p>
          <a class="btn btn-small btn-primary" href="mailto:${CONTACT_EMAIL}">Contactar soporte</a>
        </div>
      </article>
    `;
  }
}

// Anima las secciones al entrar en pantalla y respeta navegadores antiguos.
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
  setupCarousel();
  renderBusinessLines();
  ["cursos", "servicios", "productos"].forEach(renderCatalog);
  observeReveals();
});
