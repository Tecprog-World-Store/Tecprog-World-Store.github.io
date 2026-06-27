const GUIAS_SOURCE = "../data/guias.json";
const GUIAS_WHATSAPP = "51952354282";

function guiaEscape(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function guiaFromSubdir(path) {
  return `../${path}`;
}

function guiaWhatsapp(message) {
  return `https://wa.me/${GUIAS_WHATSAPP}?text=${encodeURIComponent(message)}`;
}

async function loadGuias() {
  const response = await fetch(GUIAS_SOURCE);
  if (!response.ok) throw new Error("No se pudo cargar data/guias.json");
  return response.json();
}

function uniqueGuias(items, key) {
  return [...new Set(items.map((item) => item[key]).filter(Boolean))];
}

function renderGuideCard(item) {
  return `
    <article class="catalog-card guia-card"
      data-linea="${guiaEscape(item.linea)}"
      data-categoria="${guiaEscape(item.categoria)}"
      data-tipo="${guiaEscape(item.tipo)}"
      data-nivel="${guiaEscape(item.nivel)}"
      data-estado="${guiaEscape(item.estado)}">
      <div class="catalog-media">
        <img src="${guiaFromSubdir(item.imagen_portada)}" alt="${guiaEscape(item.titulo)}" loading="lazy">
        <span>${guiaEscape(item.paginas)} paginas</span>
      </div>
      <div class="catalog-body">
        <p class="catalog-category">${guiaEscape(item.linea)} · ${guiaEscape(item.categoria)}</p>
        <h3>${guiaEscape(item.titulo)}</h3>
        <p>${guiaEscape(item.descripcion_corta)}</p>
        <div class="catalog-meta">
          <span>${guiaEscape(item.tipo)} · ${guiaEscape(item.nivel)}</span>
          <strong>${guiaEscape(item.precio)}</strong>
        </div>
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="../detalle/guia.html?id=${encodeURIComponent(item.id)}">Ver guia</a>
          <a class="btn btn-small" href="${guiaFromSubdir(item.archivo_pdf)}" download>Descargar PDF</a>
          <a class="btn btn-small btn-gold" href="${guiaWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener noreferrer">Consultar WhatsApp</a>
        </div>
      </div>
    </article>
  `;
}

function renderFilterGroup(items, key, label) {
  const values = uniqueGuias(items, key);
  return `
    <label class="select-filter">
      <span>${label}</span>
      <select data-guide-filter="${key}">
        <option value="">Todos</option>
        ${values.map((value) => `<option value="${guiaEscape(value)}">${guiaEscape(value)}</option>`).join("")}
      </select>
    </label>
  `;
}

function setupGuideFilters(items) {
  const filters = document.querySelector("[data-guias-filters]");
  if (!filters) return;
  filters.innerHTML = [
    renderFilterGroup(items, "linea", "Linea"),
    renderFilterGroup(items, "categoria", "Categoria"),
    renderFilterGroup(items, "tipo", "Tipo"),
    renderFilterGroup(items, "nivel", "Nivel"),
    renderFilterGroup(items, "estado", "Estado")
  ].join("");

  filters.addEventListener("change", () => {
    const active = [...filters.querySelectorAll("[data-guide-filter]")].map((select) => ({
      key: select.dataset.guideFilter,
      value: select.value
    }));
    document.querySelectorAll(".guia-card").forEach((card) => {
      const show = active.every((filter) => !filter.value || card.dataset[filter.key] === filter.value);
      card.hidden = !show;
    });
  });
}

async function renderGuiasCatalog() {
  const target = document.querySelector("[data-guias-grid]");
  if (!target) return;
  const items = await loadGuias();
  target.innerHTML = items.map(renderGuideCard).join("");
  setupGuideFilters(items);
}

function renderList(values) {
  if (!values?.length) return "<p>No especificado.</p>";
  return `<ul class="check-list">${values.map((value) => `<li>${guiaEscape(value)}</li>`).join("")}</ul>`;
}

async function renderGuiaDetail() {
  const root = document.querySelector("[data-guia-detail]");
  if (!root) return;
  const id = new URLSearchParams(window.location.search).get("id");
  const items = await loadGuias();
  const item = items.find((entry) => entry.id === id) || items[0];
  document.title = `${item.titulo} | Guia tecnica Tecprog World`;

  root.innerHTML = `
    <section class="detail-hero">
      <div class="section-shell detail-hero-grid">
        <div>
          <p class="eyebrow">${guiaEscape(item.linea)} · ${guiaEscape(item.categoria)}</p>
          <h1>${guiaEscape(item.titulo)}</h1>
          <p>${guiaEscape(item.descripcion_larga)}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#visor-pdf">Ver PDF embebido</a>
            <a class="btn btn-secondary" href="${guiaFromSubdir(item.archivo_pdf)}" download>Descargar PDF</a>
            <a class="btn btn-gold" href="${guiaWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener noreferrer">Consultar por WhatsApp</a>
          </div>
        </div>
        <figure class="detail-media">
          <img src="${guiaFromSubdir(item.imagen_portada)}" alt="${guiaEscape(item.titulo)}">
          <figcaption>${guiaEscape(item.tipo)}</figcaption>
        </figure>
      </div>
    </section>
    <section class="section">
      <div class="section-shell detail-layout">
        <div class="detail-content">
          <article class="detail-block">
            <h2>Descripcion tecnica</h2>
            <p>${guiaEscape(item.descripcion_larga)}</p>
          </article>
          <article class="detail-block">
            <h2>Software relacionado</h2>
            ${renderList(item.software_relacionado)}
          </article>
          <article id="visor-pdf" class="detail-block pdf-viewer-block">
            <h2>Visor PDF</h2>
            <iframe class="pdf-viewer" src="${guiaFromSubdir(item.archivo_pdf)}" title="${guiaEscape(item.titulo)}"></iframe>
            <p class="microcopy">Si el visor no carga, <a href="${guiaFromSubdir(item.archivo_pdf)}" download>descargue el PDF aqui</a>.</p>
          </article>
        </div>
        <aside class="detail-sidebar">
          <article class="price-panel">
            <h2>Ficha tecnica</h2>
            <dl>
              <div><dt>Linea</dt><dd>${guiaEscape(item.linea)}</dd></div>
              <div><dt>Categoria</dt><dd>${guiaEscape(item.categoria)}</dd></div>
              <div><dt>Tipo</dt><dd>${guiaEscape(item.tipo)}</dd></div>
              <div><dt>Nivel</dt><dd>${guiaEscape(item.nivel)}</dd></div>
              <div><dt>Sistema operativo</dt><dd>${guiaEscape(item.sistema_operativo)}</dd></div>
              <div><dt>Fecha</dt><dd>${guiaEscape(item.fecha)}</dd></div>
              <div><dt>Version</dt><dd>${guiaEscape(item.version)}</dd></div>
              <div><dt>Paginas</dt><dd>${guiaEscape(item.paginas)}</dd></div>
              <div><dt>Precio</dt><dd>${guiaEscape(item.precio)}</dd></div>
              <div><dt>Estado</dt><dd>${guiaEscape(item.estado)}</dd></div>
            </dl>
            <div class="catalog-actions">
              <a class="btn btn-small btn-primary" href="../catalogo/guias.html">Volver al catalogo de guias</a>
              <a class="btn btn-small" href="${guiaFromSubdir(item.archivo_pdf)}" download>Descargar PDF</a>
              <a class="btn btn-small btn-gold" href="${guiaWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
            </div>
          </article>
        </aside>
      </div>
    </section>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  renderGuiasCatalog().catch(console.error);
  renderGuiaDetail().catch(console.error);
});
