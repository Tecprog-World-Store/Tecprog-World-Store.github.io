const LINE_CATALOGS = {
  "tw-salud": {
    data: "../data/catalogo-tw-salud.json",
    title: "Catalogo TW Salud",
    subtitle: "Diseno tecnico, prototipado, soporte tecnico, accesibilidad e investigacion aplicada en salud con validacion profesional cuando corresponda.",
    legal: "Los servicios de TW Salud se orientan a diseño, prototipado, soporte técnico, accesibilidad e investigación aplicada. La evaluación clínica, prescripción, adaptación médica y validación de uso deben realizarse con profesionales de salud competentes cuando corresponda.",
  },
  "tw-innova": {
    data: "../data/catalogo-tw-innova.json",
    title: "Catalogo TW Innova",
    subtitle: "Software, hardware, automatizacion, XR, IA, soporte tecnologico y mantenimiento preventivo especializado.",
    legal: "No se realizan acciones que anulen garantias ni manipulaciones peligrosas; se prioriza diagnostico, configuracion, software y mantenimiento preventivo.",
  },
  "tw-interactive": {
    data: "../data/catalogo-tw-interactive.json",
    title: "Catalogo TW Interactive",
    subtitle: "Servicios de ingenieria mecanica de fluidos, hidrologia, hidraulica, CFD, termofluidos, energia, aerodinamica, automatizacion de calculos y documentacion tecnica.",
    legal: "Servicio tecnico de ingenieria y consultoria. Los resultados son referenciales segun datos disponibles, alcance contratado, supuestos de calculo, normativa aplicable y revision profesional competente cuando corresponda.",
  },
  "tw-inox": {
    data: "../data/catalogo-tw-inox.json",
    title: "Catalogo TW Inox",
    subtitle: "Acero inoxidable, metalmecanica ligera, fabricacion coordinada, mantenimiento y soluciones a medida.",
    legal: "Los servicios se coordinan con tecnicos, soldadores o talleres competentes segun alcance y requerimientos.",
  },
  "tw-construye": {
    data: "../data/catalogo-tw-construye.json",
    title: "Catalogo TW Construye",
    subtitle: "Construccion civil, metrados, presupuestos, planos, remodelacion y asistencia tecnica.",
    legal: "Cuando el servicio requiera firma, licencia, colegiatura o responsabilidad formal, se coordina con profesionales habilitados.",
  },
};

const OFFER_WHATSAPP = "51952354282";

function offerEscape(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function offerAsset(path) {
  return `../${path}`;
}

function offerWhatsapp(message) {
  return `https://wa.me/${OFFER_WHATSAPP}?text=${encodeURIComponent(message)}`;
}

async function loadLineCatalog(slug) {
  const config = LINE_CATALOGS[slug];
  const response = await fetch(config.data);
  if (!response.ok) throw new Error(`No se pudo cargar ${config.data}`);
  return response.json();
}

function uniqueOffer(items, key) {
  return [...new Set(items.map((item) => item[key]).filter(Boolean))].sort((a, b) => String(a).localeCompare(String(b), "es"));
}

function offerFilter(items, key, label) {
  return `
    <label class="select-filter">
      <span>${label}</span>
      <select data-offer-filter="${key}">
        <option value="">Todos</option>
        ${uniqueOffer(items, key).map((value) => `<option value="${offerEscape(value)}">${offerEscape(value)}</option>`).join("")}
      </select>
    </label>
  `;
}

function offerCard(item) {
  const detailHref = item.url_detalle
    ? offerAsset(item.url_detalle)
    : `../detalle/oferta.html?id=${encodeURIComponent(item.id)}&linea=${encodeURIComponent(item.linea_slug)}`;
  const actionLabel = item.accion_whatsapp || "Solicitar cotizacion por WhatsApp";
  return `
    <article class="catalog-card line-offer-card"
      data-categoria="${offerEscape(item.categoria)}"
      data-tipo="${offerEscape(item.tipo)}"
      data-madurez="${offerEscape(item.madurez)}"
      data-prioridad="${offerEscape(item.prioridad)}"
      data-search="${offerEscape(`${item.oferta} ${item.categoria} ${item.tipo} ${item.descripcion_corta}`).toLowerCase()}">
      <div class="catalog-media">
        <img src="${offerAsset(item.imagen)}" alt="${offerEscape(item.imagen_alt || item.oferta)}" loading="lazy">
        <span>${offerEscape(item.tipo)}</span>
      </div>
      <div class="catalog-body">
        <p class="catalog-category">${offerEscape(item.linea)} · ${offerEscape(item.categoria)}</p>
        <h3>${offerEscape(item.oferta)}</h3>
        <p>${offerEscape(item.descripcion_corta)}</p>
        <div class="catalog-meta">
          <span>${offerEscape(item.madurez)} · ${offerEscape(item.prioridad)}</span>
          <strong>${offerEscape(item.precio_soles_texto)}</strong>
        </div>
        <p class="usd-price">${offerEscape(item.precio_usd_texto)}</p>
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="${detailHref}">Ver detalle</a>
          <a class="btn btn-small btn-gold" href="${offerWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener noreferrer">${offerEscape(actionLabel)}</a>
        </div>
      </div>
    </article>
  `;
}

function applyOfferFilters() {
  const filterRoot = document.querySelector("[data-line-offer-filters]");
  const search = filterRoot?.querySelector("[data-offer-search]")?.value.trim().toLowerCase() || "";
  const filters = [...(filterRoot?.querySelectorAll("[data-offer-filter]") || [])].map((select) => ({
    key: select.dataset.offerFilter,
    value: select.value,
  }));
  document.querySelectorAll(".line-offer-card").forEach((card) => {
    const textMatch = !search || card.dataset.search.includes(search);
    const filterMatch = filters.every((filter) => !filter.value || card.dataset[filter.key] === filter.value);
    card.hidden = !(textMatch && filterMatch);
  });
}

async function renderLineCatalog() {
  const root = document.querySelector("[data-line-catalog]");
  if (!root) return;
  const slug = root.dataset.lineCatalog;
  const config = LINE_CATALOGS[slug];
  const items = await loadLineCatalog(slug);
  document.title = `${config.title} | Tecprog World E.I.R.L.`;
  root.innerHTML = `
    <nav class=\"local-nav\" data-local-nav aria-label="Navegacion ${offerEscape(config.title)}">
      <a href="#presentacion">Presentacion</a>
      <a href="#catalogo">Ofertas</a>
      <a href="#condiciones">Condiciones</a>
    </nav>
    <section id="presentacion" class="subpage-hero section-anchor">
      <div class="section-shell">
        <p class="eyebrow">Tecprog World E.I.R.L.</p>
        <h1>${offerEscape(config.title)}</h1>
        <p>${offerEscape(config.subtitle)}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#catalogo">Ver catalogo</a>
          <a class="btn btn-gold" data-whatsapp="${offerEscape(config.title)}" href="#">WhatsApp</a>
        </div>
      </div>
    </section>
    <section id="catalogo" class="section section-anchor">
      <div class="section-shell">
        <div class="section-heading">
          <p class="eyebrow">${items.length} ofertas</p>
          <h2>Ofertas disponibles</h2>
          <p>Precios referenciales desde, sujetos a alcance, disponibilidad, ubicacion, modalidad y validacion tecnica.</p>
        </div>
        <div class="filter-panel" data-line-offer-filters>
          <label class="select-filter search-filter"><span>Buscar</span><input type="search" data-offer-search placeholder="Oferta, categoria, tipo..."></label>
          ${offerFilter(items, "categoria", "Categoria")}
          ${offerFilter(items, "tipo", "Tipo")}
          ${offerFilter(items, "madurez", "Madurez")}
          ${offerFilter(items, "prioridad", "Prioridad")}
        </div>
        <div class="catalog-grid">${items.map(offerCard).join("")}</div>
      </div>
    </section>
    <section id="condiciones" class="section section-alt section-anchor">
      <div class="section-shell">
        <article class="detail-block">
          <h2>Nota legal y comercial</h2>
          <p>${offerEscape(config.legal)}</p>
          <p class="microcopy">Contacto unico: WhatsApp +51 952 354 282 y correo grupotecprog@gmail.com.</p>
        </article>
      </div>
    </section>
  `;
  document.querySelector("[data-line-offer-filters]").addEventListener("input", applyOfferFilters);
  document.querySelector("[data-line-offer-filters]").addEventListener("change", applyOfferFilters);
  if (typeof twExternalAttrs === "function") twExternalAttrs();
}

document.addEventListener("DOMContentLoaded", () => {
  renderLineCatalog().catch(console.error);
});
