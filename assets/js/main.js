const WHATSAPP_NUMBER = "51999999999";
const CONTACT_EMAIL = "contacto@tecprogworld.com";
const DEFAULT_PAYPAL_URL = "https://www.paypal.com/paypalme/editar-enlace";

const catalogSources = {
  cursos: "data/cursos.json",
  servicios: "data/servicios.json",
  productos: "data/productos.json",
  software: "data/software.json",
  descargas: "data/descargas.json"
};

function buildWhatsAppUrl(itemName) {
  const message = `Hola, deseo información sobre: ${itemName}. Vengo desde la web de Tecprog World.`;
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
}

function setSafeText(value, fallback = "Tecprog World") {
  return String(value || fallback)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

// Controla el menú móvil y conserva una navegación compacta en GitHub Pages.
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

// Convierte cualquier enlace con data-whatsapp en un flujo de contacto prellenado.
function setupWhatsAppLinks() {
  document.querySelectorAll("[data-whatsapp]").forEach((link) => {
    const topic = link.getAttribute("data-whatsapp");
    link.setAttribute("href", buildWhatsAppUrl(topic));
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener");
  });
}

// Carrusel liviano para banners comerciales, sin dependencias externas.
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
    slides.forEach((slide, slideIndex) => {
      slide.classList.toggle("is-active", slideIndex === activeIndex);
    });
    dots.forEach((dot, dotIndex) => {
      dot.classList.toggle("is-active", dotIndex === activeIndex);
    });
  }

  showSlide(activeIndex);
  window.setInterval(() => showSlide((activeIndex + 1) % slides.length), 6500);
}

function mediaMarkup(item, fallbackLabel) {
  const label = setSafeText(item.categoria || item.tipo || item.etiqueta || fallbackLabel);
  const image = item.imagen ? setSafeText(item.imagen, "") : "";
  const imageMarkup = image
    ? `<img src="${image}" alt="${setSafeText(item.nombre)}" loading="lazy" onerror="this.closest('.catalog-media').classList.add('has-fallback'); this.remove();">`
    : "";

  return `
    <div class="catalog-media ${image ? "" : "has-fallback"}">
      ${imageMarkup}
      <span>${label}</span>
    </div>
  `;
}

function createCommerceCard(item, type) {
  const card = document.createElement("article");
  card.className = "catalog-card reveal";
  const name = setSafeText(item.nombre);

  card.innerHTML = `
    ${mediaMarkup(item, type)}
    <div class="catalog-body">
      <p class="catalog-category">${setSafeText(item.categoria || item.tipo || "Disponible")}</p>
      <h3>${name}</h3>
      <p>${setSafeText(item.descripcion, "Descripción pendiente.")}</p>
      <strong>${setSafeText(item.precio || "Cotizar")}</strong>
      <div class="catalog-actions">
        <a class="btn btn-small btn-primary" href="${buildWhatsAppUrl(item.nombre)}" target="_blank" rel="noopener">Comprar por WhatsApp</a>
        <a class="btn btn-small" href="${setSafeText(item.paypal || DEFAULT_PAYPAL_URL)}" target="_blank" rel="noopener">PayPal</a>
      </div>
    </div>
  `;

  return card;
}

function createSoftwareCard(item) {
  const card = document.createElement("article");
  card.className = "software-card";
  const isOpen = item.modelo === "open-source";

  const actions = isOpen
    ? `
      <a class="btn btn-small btn-primary" href="${setSafeText(item.repositorio || "#")}" target="_blank" rel="noopener">Ver repositorio</a>
      <a class="btn btn-small" href="${setSafeText(item.descarga || "#")}" target="_blank" rel="noopener">Descargar</a>
      <a class="btn btn-small" href="${setSafeText(item.documentacion || "#")}" target="_blank" rel="noopener">Documentación</a>
    `
    : `
      <a class="btn btn-small btn-primary" href="${buildWhatsAppUrl(`${item.nombre} - demo`)}" target="_blank" rel="noopener">Solicitar demo</a>
      <a class="btn btn-small" href="${buildWhatsAppUrl(`${item.nombre} - implementación`)}" target="_blank" rel="noopener">Cotizar implementación</a>
      <a class="btn btn-small btn-gold" href="${buildWhatsAppUrl(item.nombre)}" target="_blank" rel="noopener">Comprar por WhatsApp</a>
    `;

  card.innerHTML = `
    ${mediaMarkup(item, item.modelo)}
    <div class="catalog-body">
      <p class="catalog-category">${setSafeText(item.linea || "TW Innova")}</p>
      <h3>${setSafeText(item.nombre)}</h3>
      <p>${setSafeText(item.descripcion)}</p>
      <div class="tag-row">
        <span>${setSafeText(item.modelo)}</span>
        <span>${setSafeText(item.licencia || "Licencia pendiente")}</span>
      </div>
      <div class="catalog-actions">${actions}</div>
    </div>
  `;

  return card;
}

function createDownloadCard(item) {
  const card = document.createElement("article");
  card.className = "download-card reveal";

  card.innerHTML = `
    ${mediaMarkup(item, item.tipo)}
    <div class="catalog-body">
      <p class="catalog-category">${setSafeText(item.etiqueta)}</p>
      <h3>${setSafeText(item.nombre)}</h3>
      <p>${setSafeText(item.descripcion)}</p>
      <dl class="download-meta">
        <div><dt>Tipo</dt><dd>${setSafeText(item.tipo)}</dd></div>
        <div><dt>Línea</dt><dd>${setSafeText(item.linea_negocio)}</dd></div>
        <div><dt>Versión</dt><dd>${setSafeText(item.version)}</dd></div>
        <div><dt>Sistema</dt><dd>${setSafeText(item.sistema_operativo)}</dd></div>
        <div><dt>Licencia</dt><dd>${setSafeText(item.licencia)}</dd></div>
      </dl>
      <div class="catalog-actions">
        <a class="btn btn-small btn-primary" href="${setSafeText(item.url_descarga || "#")}" target="_blank" rel="noopener">Descargar</a>
        <a class="btn btn-small" href="${setSafeText(item.url_documentacion || "#")}" target="_blank" rel="noopener">Documentación</a>
      </div>
    </div>
  `;

  return card;
}

function renderRevealObserver() {
  const elements = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    elements.forEach((element) => element.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  elements.forEach((element) => observer.observe(element));
}

async function loadJson(sourceKey) {
  const response = await fetch(catalogSources[sourceKey]);
  if (!response.ok) throw new Error(`No se pudo cargar ${sourceKey}`);
  return response.json();
}

async function renderCommerce(type) {
  const target = document.querySelector(`[data-render="${type}"]`);
  if (!target) return;
  target.innerHTML = `<p class="loading">Cargando ${type}...</p>`;

  try {
    const items = await loadJson(type);
    target.innerHTML = "";
    items.forEach((item) => target.appendChild(createCommerceCard(item, type)));
    renderRevealObserver();
  } catch (error) {
    renderError(target, type);
  }
}

async function renderSoftware() {
  const commercialTarget = document.querySelector('[data-render="software-comercial"]');
  const openTarget = document.querySelector('[data-render="software-open"]');
  if (!commercialTarget || !openTarget) return;

  commercialTarget.innerHTML = `<p class="loading">Cargando software comercial...</p>`;
  openTarget.innerHTML = `<p class="loading">Cargando software open-source...</p>`;

  try {
    const items = await loadJson("software");
    commercialTarget.innerHTML = "";
    openTarget.innerHTML = "";
    items
      .filter((item) => item.modelo === "comercial")
      .forEach((item) => commercialTarget.appendChild(createSoftwareCard(item)));
    items
      .filter((item) => item.modelo === "open-source")
      .forEach((item) => openTarget.appendChild(createSoftwareCard(item)));
    renderRevealObserver();
  } catch (error) {
    renderError(commercialTarget, "software comercial");
    renderError(openTarget, "software open-source");
  }
}

async function renderDownloads() {
  const target = document.querySelector('[data-render="descargas"]');
  if (!target) return;
  target.innerHTML = `<p class="loading">Cargando descargas...</p>`;

  try {
    const items = await loadJson("descargas");
    target.innerHTML = "";
    items.forEach((item) => target.appendChild(createDownloadCard(item)));
    renderRevealObserver();
  } catch (error) {
    renderError(target, "descargas");
  }
}

function renderError(target, type) {
  target.innerHTML = `
    <article class="catalog-card catalog-error">
      <div class="catalog-body">
        <h3>Contenido no disponible</h3>
        <p>Revisa el archivo JSON de ${setSafeText(type)} o prueba el sitio desde un servidor local.</p>
        <a class="btn btn-small btn-primary" href="mailto:${CONTACT_EMAIL}">Contactar soporte</a>
      </div>
    </article>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  setupNavigation();
  setupWhatsAppLinks();
  setupCarousel();
  renderRevealObserver();
  ["cursos", "servicios", "productos"].forEach(renderCommerce);
  renderSoftware();
  renderDownloads();
});
