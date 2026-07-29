const OFFER_DETAIL_SOURCES = {
  "tw-salud": "../data/catalogo-tw-salud.json",
  "tw-innova": "../data/catalogo-tw-innova.json",
  "tw-interactive": "../data/catalogo-tw-interactive.json",
  "tw-inox": "../data/catalogo-tw-inox.json",
  "tw-construye": "../data/catalogo-tw-construye.json",
};
const OFFER_DETAIL_WHATSAPP = "51952354282";

function detailOfferEscape(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function detailOfferWhatsapp(message) {
  return `https://wa.me/${OFFER_DETAIL_WHATSAPP}?text=${encodeURIComponent(message)}`;
}

function detailOfferAsset(path) {
  return `../${path}`;
}

function detailOfferList(items) {
  return `<ul class="check-list">${(items || []).map((item) => `<li>${detailOfferEscape(item)}</li>`).join("")}</ul>`;
}

async function renderOfferDetail() {
  const root = document.querySelector("[data-offer-detail]");
  if (!root) return;
  const params = new URLSearchParams(location.search);
  const id = params.get("id");
  const line = params.get("linea");
  const source = OFFER_DETAIL_SOURCES[line];
  if (!id || !source) {
    root.innerHTML = `<section class="section"><div class="section-shell"><article class="detail-block"><h1>Oferta no encontrada</h1><a class="btn btn-primary" href="../index.html#lineas">Volver a lineas</a></article></div></section>`;
    return;
  }
  const response = await fetch(source);
  const items = response.ok ? await response.json() : [];
  const item = items.find((entry) => entry.id === id) || items[0];
  document.title = `${item.oferta} | Tecprog World E.I.R.L.`;
  root.innerHTML = `
    <section class="detail-hero">
      <div class="section-shell detail-hero-grid">
        <div>
          <p class="eyebrow">${detailOfferEscape(item.linea)} · ${detailOfferEscape(item.categoria)}</p>
          <h1>${detailOfferEscape(item.oferta)}</h1>
          <p>${detailOfferEscape(item.descripcion_corta)}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="${detailOfferWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener noreferrer">Solicitar cotizacion por WhatsApp</a>
            <a class="btn btn-secondary" href="mailto:grupotecprog@gmail.com">Enviar correo</a>
            <a class="btn btn-gold" href="../catalogo/${detailOfferEscape(item.linea_slug)}.html">Volver al catalogo</a>
          </div>
        </div>
        <figure class="detail-media">
          <img src="${detailOfferAsset(item.imagen)}" alt="${detailOfferEscape(item.oferta)}">
          <figcaption>${detailOfferEscape(item.tipo)}</figcaption>
        </figure>
      </div>
    </section>
    <section class="section">
      <div class="section-shell detail-layout">
        <div class="detail-content">
          <article class="detail-block"><h2>Descripcion</h2><p>${detailOfferEscape(item.descripcion_larga)}</p></article>
          <article class="detail-block"><h2>Publico objetivo</h2>${detailOfferList(item.publico_objetivo)}</article>
          <article class="detail-block"><h2>Entregables</h2>${detailOfferList(item.entregables)}</article>
          <article class="detail-block"><h2>Incluye</h2>${detailOfferList(item.incluye)}</article>
          <article class="detail-block"><h2>Condiciones</h2>${detailOfferList(item.condiciones)}</article>
        </div>
        <section class=\"detail-summary\">
          <article class="price-panel">
            <h2>Ficha comercial</h2>
            <dl>
              <div><dt>Linea</dt><dd>${detailOfferEscape(item.linea)}</dd></div>
              <div><dt>Categoria</dt><dd>${detailOfferEscape(item.categoria)}</dd></div>
              <div><dt>Tipo</dt><dd>${detailOfferEscape(item.tipo)}</dd></div>
              <div><dt>Madurez</dt><dd>${detailOfferEscape(item.madurez)}</dd></div>
              <div><dt>Peru</dt><dd>${detailOfferEscape(item.precio_soles_texto)} · referencial</dd></div>
              <div><dt>Internacional</dt><dd>${detailOfferEscape(item.precio_usd_texto)} · referencial</dd></div>
            </dl>
            <div class="catalog-actions">
              <a class="btn btn-small btn-primary" href="${detailOfferWhatsapp(item.whatsapp_message)}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
              <a class="btn btn-small" href="../catalogo/${detailOfferEscape(item.linea_slug)}.html">Catalogo</a>
            </div>
          </article>
        </section>
      </div>
    </section>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  renderOfferDetail().catch(console.error);
});
