const TEC_SITE = {
  whatsapp: "51952354282",
  email: "grupotecprog@gmail.com",
  qrPath: "assets/img/qr/QR_Yape.png",
  paypalRequestUrl: "https://www.paypal.com/paypalme/grupotecprog"
};

const MATERIALS_JSON = "data/materiales.json";
const MATERIALS_SCRIPT_SRC = document.currentScript ? document.currentScript.getAttribute("src") || "" : "";

function rootPrefix() {
  const marker = "assets/js/materiales.js";
  const index = MATERIALS_SCRIPT_SRC.replaceAll("\\", "/").indexOf(marker);
  return index >= 0 ? MATERIALS_SCRIPT_SRC.slice(0, index) : "";
}

function sitePath(path) {
  if (!path) return "";
  if (/^https?:\/\//i.test(path)) return path;
  return `${rootPrefix()}${path}`.replace(/\/{2,}/g, "/");
}

function encodePath(path) {
  return path.split("/").map(encodeURIComponent).join("/");
}

function text(value, fallback = "") {
  return String(value || fallback);
}

function escapeHtml(value, fallback = "") {
  return text(value, fallback)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function whatsappUrl(message) {
  return `https://wa.me/${TEC_SITE.whatsapp}?text=${encodeURIComponent(message)}`;
}

function materialUrl(id) {
  return `${sitePath("detalle/material.html")}?id=${encodeURIComponent(id)}`;
}

async function loadMaterials() {
  const response = await fetch(sitePath(MATERIALS_JSON));
  if (!response.ok) throw new Error("No se pudo cargar data/materiales.json");
  return response.json();
}

function listMarkup(items) {
  if (!items.length) {
    return `<p class="loading">No hay materiales disponibles todavía.</p>`;
  }

  return items.map((item) => `
    <article class="material-card reveal" data-category="${escapeHtml(item.categoria)}">
      <a class="material-thumb" href="${materialUrl(item.id)}" aria-label="Ver detalle de ${escapeHtml(item.titulo)}">
        ${item.imagen ? `<img src="${encodePath(sitePath(item.imagen))}" alt="${escapeHtml(item.titulo)}" loading="lazy" onerror="this.parentElement.classList.add('has-fallback'); this.remove();">` : ""}
        <span>${escapeHtml(item.tipo)}</span>
      </a>
      <div class="material-card-body">
        <p class="catalog-category">${escapeHtml(item.linea)} ? ${escapeHtml(item.subcategoria || item.categoria)}</p>
        <h3>${escapeHtml(item.titulo)}</h3>
        <p>${escapeHtml(item.descripcion_corta)}</p>
        <strong>${escapeHtml(item.precio_desde_soles_igv || "Cotizar")}</strong>
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="${whatsappUrl(item.whatsapp_message)}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
          <a class="btn btn-small btn-gold" href="${materialUrl(item.id)}">Ver detalle</a>
        </div>
      </div>
    </article>
  `).join("");
}

function renderFeatureList(title, items) {
  if (!items || !items.length) return "";
  return `
    <section class="detail-block">
      <h2>${escapeHtml(title)}</h2>
      <ul class="check-list">
        ${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}
      </ul>
    </section>
  `;
}

function renderQrBlock() {
  return `
    <aside class="detail-qr">
      <h2>Medios de pago</h2>
      <p>QR Yape preparado para pagos coordinados previamente por WhatsApp o correo.</p>
      <div class="qr-frame">
        <img src="${encodePath(sitePath(TEC_SITE.qrPath))}" alt="QR de pago Yape Tecprog World" loading="lazy" onerror="this.closest('.qr-frame').classList.add('has-fallback'); this.remove();">
        <span>QR de pago no disponible</span>
      </div>
      <p class="microcopy">No se muestran datos bancarios sensibles. Solicita confirmación antes de pagar.</p>
    </aside>
  `;
}

function updateMeta(item) {
  document.title = item.seo_title || `${item.titulo} | Tecprog World E.I.R.L.`;
  const description = document.querySelector('meta[name="description"]');
  if (description) description.setAttribute("content", item.seo_description || item.descripcion_corta || "");
}

async function renderMaterialDetail() {
  const target = document.querySelector("[data-material-detail]");
  if (!target) return;

  try {
    const id = new URLSearchParams(window.location.search).get("id");
    const materials = await loadMaterials();
    const item = materials.find((material) => material.id === id);

    if (!item) {
      target.innerHTML = `
        <section class="legal-card">
          <p class="eyebrow">Material no encontrado</p>
          <h1>No encontramos este recurso</h1>
          <p>Revisa el enlace o vuelve al catálogo de materiales.</p>
          <a class="btn btn-primary" href="${sitePath("catalogo/materiales-educativos.html")}">Volver al catálogo</a>
        </section>
      `;
      return;
    }

    updateMeta(item);
    target.innerHTML = `
      <section class="detail-hero">
        <div class="section-shell detail-hero-grid">
          <div>
            <p class="eyebrow">${escapeHtml(item.linea)}</p>
            <h1>${escapeHtml(item.titulo)}</h1>
            <p>${escapeHtml(item.descripcion_corta)}</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="${whatsappUrl(item.whatsapp_message)}" target="_blank" rel="noopener noreferrer">Consultar por WhatsApp</a>
              <a class="btn btn-secondary" href="${whatsappUrl(`Hola, deseo solicitar una cotización sobre ${item.titulo}. Vengo desde la web de Tecprog World E.I.R.L.`)}" target="_blank" rel="noopener noreferrer">Solicitar cotización</a>
              <a class="btn btn-gold" href="${TEC_SITE.paypalRequestUrl}" target="_blank" rel="noopener noreferrer">Pedir pago por PayPal</a>
              <a class="btn btn-ghost" href="${sitePath("index.html")}#productos">Volver al catálogo</a>
            </div>
          </div>
          <figure class="detail-media">
            ${item.imagen ? `<img src="${encodePath(sitePath(item.imagen))}" alt="${escapeHtml(item.titulo)}" onerror="this.parentElement.classList.add('has-fallback'); this.remove();">` : ""}
            <figcaption>${escapeHtml(item.categoria)}${item.subcategoria ? ` ? ${escapeHtml(item.subcategoria)}` : ""}</figcaption>
          </figure>
        </div>
      </section>

      <section class="section">
        <div class="section-shell detail-layout">
          <div class="detail-content">
            <section class="detail-block">
              <h2>Descripción técnica y comercial</h2>
              <p>${escapeHtml(item.descripcion_larga)}</p>
            </section>
            ${renderFeatureList("Problema que resuelve", item.problema_que_resuelve)}
            ${renderFeatureList("Público objetivo", item.publico_objetivo)}
            ${renderFeatureList("Beneficios", item.beneficios)}
            ${renderFeatureList("Qué incluye", item.incluye)}
            ${renderFeatureList("Entregables", item.entregables)}
            <section class="detail-block">
              <h2>Metodología</h2>
              <p>${escapeHtml(item.metodologia)}</p>
            </section>
            <section class="detail-block">
              <h2>Nota independiente</h2>
              <p>Tecprog World E.I.R.L. desarrolla formación, servicios y materiales de manera independiente. Las marcas, softwares o instituciones mencionadas pertenecen a sus respectivos titulares y se emplean únicamente como referencia técnica o académica.</p>
            </section>
          </div>
          <aside class="detail-sidebar">
            <div class="price-panel">
              <h2>Información comercial</h2>
              <dl>
                <div><dt>Duración</dt><dd>${escapeHtml(item.duracion_referencial)}</dd></div>
                <div><dt>Modalidad</dt><dd>${escapeHtml(item.modalidad)}</dd></div>
                <div><dt>Precio Perú</dt><dd>${escapeHtml(item.precio_desde_soles_igv)}</dd></div>
                <div><dt>Exterior</dt><dd>${escapeHtml(item.precio_exterior_usd)}</dd></div>
              </dl>
              <p>${escapeHtml(item.nota_comercial)}</p>
            </div>
            ${renderQrBlock()}
          </aside>
        </div>
      </section>
    `;
    observeMaterialReveals();
  } catch (error) {
    target.innerHTML = `<section class="legal-card"><h1>No se pudo cargar el material</h1><p>${escapeHtml(error.message)}</p></section>`;
  }
}

function createFilters(container, items, grid) {
  const categories = [...new Set(items.map((item) => item.subcategoria || item.categoria).filter(Boolean))].sort();
  if (!categories.length) return;
  container.innerHTML = `
    <button class="is-active" type="button" data-filter="all">Todos</button>
    ${categories.map((category) => `<button type="button" data-filter="${escapeHtml(category)}">${escapeHtml(category)}</button>`).join("")}
  `;

  container.addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (!button) return;
    container.querySelectorAll("button").forEach((item) => item.classList.toggle("is-active", item === button));
    const filter = button.dataset.filter;
    grid.querySelectorAll(".material-card").forEach((card) => {
      const visible = filter === "all" || card.textContent.includes(filter);
      card.hidden = !visible;
    });
  });
}

async function renderMaterialIndex() {
  const grid = document.querySelector("[data-material-list]");
  if (!grid) return;
  const type = grid.dataset.materialList;
  const filterBox = document.querySelector("[data-material-filters]");
  grid.innerHTML = `<p class="loading">Cargando materiales...</p>`;

  try {
    const materials = await loadMaterials();
    const filtered = materials.filter((item) => {
      if (type === "protesis") return item.linea === "TW Salud";
      if (type === "hp50g") return item.subcategoria === "HP 50G" || item.id.includes("hp-50g");
      if (type === "educativos") return item.linea === "TW Educa para Ingenieros y Científicos";
      return true;
    });
    grid.innerHTML = listMarkup(filtered);
    if (filterBox) createFilters(filterBox, filtered, grid);
    observeMaterialReveals();
  } catch (error) {
    grid.innerHTML = `<article class="catalog-card"><div class="catalog-body"><h3>No se pudo cargar el catálogo</h3><p>${escapeHtml(error.message)}</p></div></article>`;
  }
}

function observeMaterialReveals() {
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
  renderMaterialDetail();
  renderMaterialIndex();
});
