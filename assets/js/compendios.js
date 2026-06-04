const TW_COMPENDIOS_WHATSAPP = "51952354282";
const COMPENDIOS_SOURCE = "../data/compendios.json";

function twEscape(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function twWhatsapp(message) {
  return `https://wa.me/${TW_COMPENDIOS_WHATSAPP}?text=${encodeURIComponent(message)}`;
}

function fromSubdir(path) {
  return `../${path}`;
}

async function loadCompendios() {
  const response = await fetch(COMPENDIOS_SOURCE);
  if (!response.ok) throw new Error("No se pudo cargar compendios");
  return response.json();
}

function renderCompendioCard(item) {
  return `
    <article class="catalog-card compendio-card" data-linea="${twEscape(item.linea)}" data-categoria="${twEscape(item.categoria)}" data-nivel="${twEscape(item.nivel)}">
      <div class="catalog-media">
        <img src="${fromSubdir(item.imagen_portada)}" alt="${twEscape(item.titulo)}" loading="lazy">
        <span>${twEscape(item.nivel)}</span>
      </div>
      <div class="catalog-body">
        <p class="catalog-category">${twEscape(item.linea)} · ${twEscape(item.categoria)}</p>
        <h3>${twEscape(item.titulo)}</h3>
        <p>${twEscape(item.descripcion)}</p>
        <div class="catalog-meta">
          <span>${twEscape(item.paginas_estimadas)} paginas · ${twEscape(item.version)}</span>
          <strong>${twEscape(item.precio_material_soles)}</strong>
        </div>
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="../detalle/compendio.html?id=${encodeURIComponent(item.id)}">Ver PDF</a>
          <a class="btn btn-small" href="${fromSubdir(item.archivo_pdf)}" download>Descargar PDF</a>
          <a class="btn btn-small btn-gold" href="${twWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener">Inscribirme</a>
        </div>
      </div>
    </article>
  `;
}

function unique(items, key) {
  return [...new Set(items.map((item) => item[key]).filter(Boolean))];
}

function setupFilters(items) {
  const filters = document.querySelector("[data-compendio-filters]");
  if (!filters) return;
  const values = ["Todos", ...unique(items, "categoria"), ...unique(items, "nivel")];
  filters.innerHTML = values.map((value, index) => `<button type="button" class="${index === 0 ? "is-active" : ""}" data-filter="${twEscape(value)}">${twEscape(value)}</button>`).join("");
  filters.addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (!button) return;
    filters.querySelectorAll("button").forEach((item) => item.classList.remove("is-active"));
    button.classList.add("is-active");
    const filter = button.dataset.filter;
    document.querySelectorAll(".compendio-card").forEach((card) => {
      const show = filter === "Todos" || card.dataset.categoria === filter || card.dataset.nivel === filter || card.dataset.linea === filter;
      card.hidden = !show;
    });
  });
}

async function renderCompendiosCatalog() {
  const target = document.querySelector("[data-compendios-grid]");
  if (!target) return;
  const items = await loadCompendios();
  target.innerHTML = items.map(renderCompendioCard).join("");
  setupFilters(items);
}

async function renderCompendioDetail() {
  const root = document.querySelector("[data-compendio-detail]");
  if (!root) return;
  const id = new URLSearchParams(window.location.search).get("id");
  const items = await loadCompendios();
  const item = items.find((entry) => entry.id === id) || items[0];
  document.title = `${item.titulo} | Tecprog World E.I.R.L.`;
  root.innerHTML = `
    <section class="detail-hero">
      <div class="section-shell detail-hero-grid">
        <div>
          <p class="eyebrow">${twEscape(item.linea)} · ${twEscape(item.categoria)}</p>
          <h1>${twEscape(item.titulo)}</h1>
          <p>${twEscape(item.descripcion)}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#visor-pdf">Ver PDF embebido</a>
            <a class="btn btn-secondary" href="${fromSubdir(item.archivo_pdf)}" download>Descargar</a>
            <a class="btn btn-gold" href="${twWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener">WhatsApp</a>
          </div>
        </div>
        <figure class="detail-media">
          <img src="${fromSubdir(item.imagen_portada)}" alt="${twEscape(item.titulo)}">
          <figcaption>${twEscape(item.version)}</figcaption>
        </figure>
      </div>
    </section>
    <section class="section">
      <div class="section-shell detail-layout">
        <div class="detail-content">
          <article class="detail-block">
            <h2>Indice resumido</h2>
            <ul class="check-list">
              <li>Presentacion, objetivos, resultados de aprendizaje y publico objetivo.</li>
              <li>Fundamentos teoricos, modulos desarrollados y ejemplos practicos.</li>
              <li>Ejercicios propuestos, proyecto final, anexos y bibliografia.</li>
            </ul>
          </article>
          <article class="detail-block">
            <h2>Notas legales y comerciales</h2>
            <p>Este material forma parte del ecosistema educativo de Tecprog World E.I.R.L. y puede ser usado como apoyo en cursos en vivo, cursos grabados o asesorias. Su venta, distribucion o reutilizacion no autorizada puede estar restringida segun las condiciones comerciales del servicio.</p>
            <p class="microcopy">Las marcas, softwares e instituciones mencionadas pertenecen a sus respectivos titulares.</p>
          </article>
          <article id="visor-pdf" class="detail-block pdf-viewer-block">
            <h2>Visor PDF</h2>
            <iframe class="pdf-viewer" src="${fromSubdir(item.archivo_pdf)}" title="${twEscape(item.titulo)}"></iframe>
            <p class="microcopy">Si el visor no carga, <a href="${fromSubdir(item.archivo_pdf)}" download>descarga el PDF aqui</a>.</p>
          </article>
        </div>
        <aside class="detail-sidebar">
          <article class="price-panel">
            <h2>Datos del compendio</h2>
            <dl>
              <div><dt>Curso asociado</dt><dd>${twEscape(item.curso_relacionado)}</dd></div>
              <div><dt>Paginas</dt><dd>${twEscape(item.paginas_estimadas)}</dd></div>
              <div><dt>Version</dt><dd>${twEscape(item.version)}</dd></div>
              <div><dt>Fecha</dt><dd>${twEscape(item.fecha_publicacion)}</dd></div>
              <div><dt>Material</dt><dd>${item.incluido_en_curso ? "Incluido en el curso segun promocion o alcance" : twEscape(item.precio_material_soles)}</dd></div>
            </dl>
            <div class="catalog-actions">
              <a class="btn btn-small btn-primary" href="../catalogo/compendios.html">Volver al catalogo</a>
              <a class="btn btn-small btn-gold" href="${twWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener">Solicitar material completo</a>
            </div>
          </article>
        </aside>
      </div>
    </section>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  renderCompendiosCatalog().catch(console.error);
  renderCompendioDetail().catch(console.error);
});
