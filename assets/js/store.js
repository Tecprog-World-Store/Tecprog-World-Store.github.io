const STORE_DATA_URL = "../data/productos_store.json";
const STORE_WHATSAPP = "51952354282";
const STORE_CATEGORIES = ["Todos", "Celulares", "Laptops", "Monitores", "Audio", "Apple", "Realidad Virtual", "Accesorios"];
const STORE_PLACEHOLDERS = {
  Celulares: "../assets/img/store/placeholders/celular.svg",
  Laptops: "../assets/img/store/placeholders/laptop.svg",
  Monitores: "../assets/img/store/placeholders/monitor.svg",
  Audio: "../assets/img/store/placeholders/audifonos.svg",
  Apple: "../assets/img/store/placeholders/accesorio.svg",
  "Realidad Virtual": "../assets/img/store/placeholders/realidad-virtual.svg",
  Accesorios: "../assets/img/store/placeholders/accesorio.svg"
};

function storeCleanText(value) {
  const text = String(value || "");
  if (!/[ÃÂâ]/.test(text)) return text;
  try {
    return decodeURIComponent(escape(text));
  } catch {
    return text;
  }
}

function storeEscape(value) {
  return storeCleanText(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function storePlaceholder(category) {
  return STORE_PLACEHOLDERS[storeCleanText(category)] || "../assets/img/store/placeholders/producto-generico.svg";
}

function storeAsset(path, category) {
  if (!path || path.includes("producto-generico.webp")) return storePlaceholder(category);
  return path.startsWith("../") ? path : `../${path}`;
}

function storeWhatsappProduct(nombre) {
  const productName = storeCleanText(nombre);
  const message = `Hola Tecprog World, deseo cotizar el producto: ${productName}. ¿Esta disponible para envio?`;
  return `https://wa.me/${STORE_WHATSAPP}?text=${encodeURIComponent(message)}`;
}

function storeWhatsappTopic(topic) {
  return `https://wa.me/${STORE_WHATSAPP}?text=${encodeURIComponent(`Hola Tecprog World, deseo cotizar ${topic}.`)}`;
}

function storeMoney(value) {
  if (typeof value === "number") {
    return `S/ ${value.toLocaleString("es-PE", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
  }
  return String(value || "Cotizar");
}

function storeLabel(value) {
  return storeCleanText(value)
    .replaceAll("_", " ")
    .replace(/\b\w/g, (letter) => letter.toUpperCase());
}

async function loadStoreProducts() {
  const response = await fetch(STORE_DATA_URL);
  if (!response.ok) throw new Error("No se pudo cargar data/productos_store.json");
  const products = await response.json();
  if (!Array.isArray(products)) throw new Error("El catalogo de TW Store no tiene el formato esperado.");
  return products;
}

function storeTagClass(tag) {
  return String(tag || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-");
}

function storeTagMarkup(tags = []) {
  return tags.map((tag) => `<span class="store-tag ${storeTagClass(tag)}">${storeEscape(storeLabel(tag))}</span>`).join("");
}

function storeCard(product) {
  const nombre = storeCleanText(product.nombre);
  const categoria = storeCleanText(product.categoria);
  const precioFuente = storeMoney(product.precio_fuente);
  const precioPublico = product.precio_tw_store || storeMoney(product.precio_publico);
  const margen = product.margen_sugerido || `8%: ${storeMoney(product.precio_tw_8)} · 12%: ${storeMoney(product.precio_tw_12)} · 18%: ${storeMoney(product.precio_tw_18)}`;
  const descripcion = storeCleanText(product.descripcion || product.gancho || "Producto tecnológico bajo cotización.");
  const estado = storeLabel(product.estado || "stock_por_confirmar");
  const imageSrc = storeAsset(product.imagen, categoria);
  const fallbackSrc = storePlaceholder(categoria);

  return `
    <article class="store-card"
      data-category="${storeEscape(categoria)}"
      data-search="${storeEscape(`${nombre} ${categoria} ${(product.etiquetas || []).join(" ")} ${descripcion} ${product.fuente || ""}`).toLowerCase()}">
      <div class="store-card-media">
        <img src="${imageSrc}" alt="${storeEscape(nombre)}" loading="lazy" onerror="this.onerror=null;this.src='${fallbackSrc}';">
        <div class="store-tag-row">${storeTagMarkup(product.etiquetas)}</div>
      </div>
      <div class="store-card-body">
        <p class="catalog-category">TW Store · ${storeEscape(categoria)}</p>
        <h3>${storeEscape(nombre)}</h3>
        <p>${storeEscape(descripcion)}</p>
        <dl class="store-price-list">
          <div><dt>Precio fuente</dt><dd>${storeEscape(precioFuente)}</dd></div>
          <div><dt>Precio TW Store</dt><dd>${storeEscape(precioPublico)}</dd></div>
          <div><dt>Margen sugerido</dt><dd>${storeEscape(margen)}</dd></div>
        </dl>
        <p class="microcopy">${storeEscape(estado)}. Producto sujeto a disponibilidad, confirmación de precio, garantía y condiciones de entrega.</p>
        <a class="btn btn-gold store-whatsapp-btn" href="${storeWhatsappProduct(nombre)}" target="_blank" rel="noopener noreferrer">Cotizar por WhatsApp</a>
      </div>
    </article>
  `;
}

function renderStoreFilters(products) {
  const target = document.querySelector("[data-store-filters]");
  if (!target) return;
  const available = new Set(products.map((product) => storeCleanText(product.categoria)));
  target.innerHTML = STORE_CATEGORIES
    .filter((category) => category === "Todos" || available.has(category))
    .map((category, index) => `<button class="${index === 0 ? "is-active" : ""}" type="button" data-store-category="${storeEscape(category)}">${storeEscape(category)}</button>`)
    .join("");
}

function applyStoreFilters() {
  const active = document.querySelector("[data-store-category].is-active")?.dataset.storeCategory || "Todos";
  const search = document.querySelector("[data-store-search]")?.value.trim().toLowerCase() || "";
  document.querySelectorAll(".store-card").forEach((card) => {
    const categoryMatch = active === "Todos" || card.dataset.category === active;
    const searchMatch = !search || card.dataset.search.includes(search);
    card.hidden = !(categoryMatch && searchMatch);
  });
}

async function renderStore() {
  const grid = document.querySelector("[data-store-grid]");
  if (!grid) return;
  const products = await loadStoreProducts();
  renderStoreFilters(products);
  grid.innerHTML = products.map(storeCard).join("");
  const count = document.querySelector("[data-store-count]");
  if (count) count.textContent = `${products.length} productos`;
  document.querySelector("[data-store-filters]")?.addEventListener("click", (event) => {
    const button = event.target.closest("[data-store-category]");
    if (!button) return;
    document.querySelectorAll("[data-store-category]").forEach((item) => item.classList.toggle("is-active", item === button));
    applyStoreFilters();
  });
  document.querySelector("[data-store-search]")?.addEventListener("input", applyStoreFilters);
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-store-whatsapp]").forEach((link) => {
    link.href = storeWhatsappTopic(link.dataset.storeWhatsapp);
    link.target = "_blank";
    link.rel = "noopener noreferrer";
  });
  renderStore().catch((error) => {
    const grid = document.querySelector("[data-store-grid]");
    if (grid) grid.innerHTML = `<article class="detail-block"><h2>No se pudo cargar la tienda</h2><p>${storeEscape(error.message)}</p></article>`;
  });
});
