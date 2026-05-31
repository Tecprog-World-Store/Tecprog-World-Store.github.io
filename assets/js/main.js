const WHATSAPP_NUMBER = "51999999999";
const CONTACT_EMAIL = "contacto@tecprogworld.com";
const DEFAULT_PAYPAL_URL = "https://www.paypal.com/paypalme/editar-enlace";

const catalogSources = {
  cursos: "data/cursos.json",
  servicios: "data/servicios.json",
  productos: "data/productos.json"
};

function buildWhatsAppUrl(itemName) {
  const message = `Hola, deseo información para comprar: ${itemName}`;
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
}

// Controla el menú móvil sin depender de librerías externas.
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

// Carrusel liviano para banners comerciales, apto para GitHub Pages.
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
  window.setInterval(() => {
    showSlide((activeIndex + 1) % slides.length);
  }, 6500);
}

// Construye tarjetas comerciales desde JSON para productos, cursos y servicios.
function createCatalogCard(item) {
  const card = document.createElement("article");
  card.className = "catalog-card";

  const imageMarkup = item.imagen
    ? `<img src="${item.imagen}" alt="${item.nombre}" loading="lazy" onerror="this.closest('.catalog-media').classList.add('has-fallback'); this.remove();">`
    : "";

  card.innerHTML = `
    <div class="catalog-media ${item.imagen ? "" : "has-fallback"}">
      ${imageMarkup}
      <span>${item.categoria || "Tecprog World"}</span>
    </div>
    <div class="catalog-body">
      <p class="catalog-category">${item.categoria || "Disponible"}</p>
      <h3>${item.nombre}</h3>
      <p>${item.descripcion}</p>
      <strong>${item.precio || "Cotizar"}</strong>
      <div class="catalog-actions">
        <a class="btn btn-small btn-primary" href="${buildWhatsAppUrl(item.nombre)}" target="_blank" rel="noopener">Comprar por WhatsApp</a>
        <a class="btn btn-small" href="${item.paypal || DEFAULT_PAYPAL_URL}" target="_blank" rel="noopener">PayPal</a>
      </div>
    </div>
  `;

  return card;
}

// Carga datos editables desde /data y muestra un mensaje claro si se abre sin servidor local.
async function renderCatalog(type) {
  const target = document.querySelector(`[data-render="${type}"]`);
  if (!target) return;

  target.innerHTML = `<p class="loading">Cargando ${type}...</p>`;

  try {
    const response = await fetch(catalogSources[type]);
    if (!response.ok) throw new Error(`No se pudo cargar ${type}`);
    const items = await response.json();
    target.innerHTML = "";
    items.forEach((item) => target.appendChild(createCatalogCard(item)));
  } catch (error) {
    target.innerHTML = `
      <article class="catalog-card catalog-error">
        <div class="catalog-body">
          <h3>Contenido no disponible</h3>
          <p>Revisa el archivo JSON de ${type} o prueba el sitio desde un servidor local.</p>
          <a class="btn btn-small btn-primary" href="mailto:${CONTACT_EMAIL}">Contactar soporte</a>
        </div>
      </article>
    `;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  setupNavigation();
  setupWhatsAppLinks();
  setupCarousel();
  Object.keys(catalogSources).forEach(renderCatalog);
});
