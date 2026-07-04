(function () {
  const WHATSAPP_PHONE = "51952354282";
  const DEFAULT_IMAGE = "assets/img/store/placeholders/producto-generico.svg";
  const NOTICE = "Precios, disponibilidad y alcance sujetos a confirmación.";
  const DEFAULT_CURRENCY = "USD";
  const SCRIPT_SRC = document.currentScript?.getAttribute("src") || "";
  const BASE_PREFIX = SCRIPT_SRC
    ? new URL("../../", new URL(SCRIPT_SRC, document.baseURI)).href
    : "/";

  const LINE_LABELS = {
    "tw-store": "TW Store",
    "tw-disfruta": "TW Disfruta",
    "tw-educa": "TW Educa",
    "tw-innova": "TW Innova",
    "tw-salud": "TW Salud",
    "tw-interactive": "TW Interactive",
    "tw-construye": "TW Construye",
    "tw-inox": "TW Inox",
    "tw-investiga": "TW Investiga"
  };

  const LINE_PANEL_COPY = {
    "tw-store": {
      action: "Confirma precio, disponibilidad, garantía y envío antes de cerrar una compra.",
      whatsapp: "Hola Tecprog World, deseo cotizar desde TW Store.",
      quickTitle: "Productos",
      resources: [["Pagos Perú", "pagos/peru.html"], ["Pagos Internacionales", "pagos/internacionales.html"], ["Catálogo global", "store/index.html"]]
    },
    "tw-educa": {
      action: "Consulta cursos, cronograma, modalidad e inversión antes de inscribirte.",
      whatsapp: "Hola Tecprog World, deseo información sobre cursos de TW Educa.",
      quickTitle: "Cursos y recursos",
      resources: [["Cronograma público", "docs/operacion/cursos_tw_educa_cronograma_publico.md"], ["Guías", "catalogo/guias.html"], ["Cursos", "catalogo/cursos.html"]]
    },
    "tw-innova": {
      action: "Cuéntanos el alcance de software, hardware o automatización que necesitas.",
      whatsapp: "Hola Tecprog World, deseo cotizar una solución de TW Innova.",
      quickTitle: "Soluciones digitales",
      resources: [["Software", "catalogo/tw-innova.html"], ["Pagos Perú", "pagos/peru.html"], ["Contacto", "index.html#contacto"]]
    },
    "tw-salud": {
      action: "Solicita evaluación técnica sin prometer resultados clínicos.",
      whatsapp: "Hola Tecprog World, deseo consultar una solución técnica de TW Salud.",
      quickTitle: "Consulta técnica",
      resources: [["TW Salud", "salud/index.html"], ["Pagos Perú", "pagos/peru.html"], ["Contacto", "index.html#contacto"]]
    },
    "tw-interactive": {
      action: "Cotiza consultoría, simulación o análisis técnico según datos y alcance.",
      whatsapp: "Hola Tecprog World, deseo cotizar consultoría de ingeniería con TW Interactive.",
      quickTitle: "Ingeniería",
      resources: [["Servicios", "catalogo/tw-interactive.html"], ["Pagos Perú", "pagos/peru.html"], ["Contacto", "index.html#contacto"]]
    },
    "tw-construye": {
      action: "Solicita una cotización de obra, remodelación o asistencia técnica por alcance.",
      whatsapp: "Hola Tecprog World, deseo cotizar un servicio de TW Construye.",
      quickTitle: "Obra y remodelación",
      resources: [["Servicios", "catalogo/tw-construye.html"], ["Pagos Perú", "pagos/peru.html"], ["Contacto", "index.html#contacto"]]
    },
    "tw-inox": {
      action: "Cotiza fabricación, soldadura o proyecto metalmecánico según medidas y material.",
      whatsapp: "Hola Tecprog World, deseo cotizar un proyecto de TW Inox.",
      quickTitle: "Metalmecánica",
      resources: [["Servicios", "catalogo/tw-inox.html"], ["Pagos Perú", "pagos/peru.html"], ["Contacto", "index.html#contacto"]]
    },
    "tw-investiga": {
      action: "Consulta asesoría científica, datos, metodología o software por alcance.",
      whatsapp: "Hola Tecprog World, deseo cotizar un servicio de TW Investiga.",
      quickTitle: "Investigación",
      resources: [["Servicios", "investiga/index.html"], ["Pagos Perú", "pagos/peru.html"], ["Contacto", "index.html#contacto"]]
    },
    "tw-disfruta": {
      action: "Cotiza videojuegos, demos, assets digitales o merchandising según alcance.",
      whatsapp: "Hola Tecprog World, deseo cotizar una experiencia de TW Disfruta.",
      quickTitle: "Entretenimiento",
      resources: [["Videojuegos", "disfruta/index.html"], ["Pagos Perú", "pagos/peru.html"], ["Contacto", "index.html#contacto"]]
    }
  };

  const state = {
    items: [],
    banners: null,
    roots: []
  };

  function pathPrefix() {
    return BASE_PREFIX;
  }

  function localPath(path) {
    if (!path) return "";
    if (/^(https?:)?\/\//.test(path) || path.startsWith("data:")) return path;
    if (path.startsWith("../") || path.startsWith("./")) return path;
    return `${pathPrefix()}${path}`;
  }

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function normalizeText(value) {
    return String(value ?? "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .trim();
  }

  function readable(value) {
    return String(value || "")
      .replaceAll("_", " ")
      .replaceAll("-", " ")
      .replace(/\b\p{L}/gu, (letter) => letter.toUpperCase());
  }

  function money(value, currency = "PEN") {
    if (typeof value !== "number") return "Cotizar";
    const prefix = currency === "USD" ? "US$" : "S/";
    return `${prefix} ${value.toLocaleString("es-PE", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
  }

  function itemCurrency(item) {
    return item.moneda_principal || item.moneda || DEFAULT_CURRENCY;
  }

  function itemPrimaryPrice(item) {
    if (typeof item.precio_soles === "number") return { value: item.precio_soles, currency: item.moneda_principal || "PEN" };
    if (typeof item.precio_dolares === "number") return { value: item.precio_dolares, currency: "USD" };
    if (typeof item.precio_publico === "number") return { value: item.precio_publico, currency: itemCurrency(item) };
    return { value: null, currency: itemCurrency(item) };
  }

  function itemPriceValue(item) {
    const price = itemPrimaryPrice(item);
    return typeof price.value === "number" ? price.value : Number.POSITIVE_INFINITY;
  }

  function whatsappHref(item) {
    const message = item.whatsapp_mensaje || `Hola Tecprog World, deseo cotizar: ${item.nombre}.`;
    return `https://wa.me/${WHATSAPP_PHONE}?text=${encodeURIComponent(message)}`;
  }

  async function loadItems() {
    if (state.items.length) return state.items;
    const response = await fetch(localPath("data/catalogo_global.json"));
    if (!response.ok) throw new Error("No se pudo cargar data/catalogo_global.json");
    const items = await response.json();
    state.items = Array.isArray(items) ? items.filter((item) => item.visible_cliente !== false) : [];
    return state.items;
  }

  async function loadBanners() {
    if (state.banners) return state.banners;
    try {
      const response = await fetch(localPath("data/banners_lineas.json"));
      state.banners = response.ok ? await response.json() : {};
    } catch {
      state.banners = {};
    }
    return state.banners;
  }

  function imageExists(src) {
    return new Promise((resolve) => {
      if (!src) return resolve(false);
      const image = new Image();
      image.onload = () => resolve(true);
      image.onerror = () => resolve(false);
      image.src = src;
    });
  }

  async function applyBanner(slug) {
    const hero = document.querySelector(".commerce-hero");
    if (!hero || !slug) return;
    const banners = await loadBanners();
    const config = banners[slug];
    if (!config) return;
    const banner = localPath(config.banner);
    const fallback = localPath(config.fallback);
    const selected = await imageExists(banner) ? banner : (await imageExists(fallback) ? fallback : "");
    hero.style.backgroundImage = selected
      ? `linear-gradient(135deg, rgba(6, 19, 38, 0.96), rgba(11, 36, 72, 0.9)), url("${selected}")`
      : "linear-gradient(135deg, rgba(6, 19, 38, 0.96), rgba(11, 36, 72, 0.9))";
  }

  function unique(items, key) {
    return [...new Set(items.map((item) => item[key]).filter(Boolean))]
      .sort((a, b) => String(a).localeCompare(String(b), "es"));
  }

  function optionList(values, labelAll) {
    return `<option value="">${escapeHtml(labelAll)}</option>${values
      .map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(LINE_LABELS[value] || value)}</option>`)
      .join("")}`;
  }

  function card(item) {
    const line = LINE_LABELS[item.linea_negocio] || readable(item.linea_negocio);
    const image = localPath(item.imagen || DEFAULT_IMAGE);
    const fallback = localPath(DEFAULT_IMAGE);
    const primaryPrice = itemPrimaryPrice(item);
    const priceText = money(primaryPrice.value, primaryPrice.currency);
    const priceDollars = primaryPrice.currency !== "USD" && typeof item.precio_dolares === "number" ? `<span>${money(item.precio_dolares, "USD")}</span>` : "";
    const publicStatus = item.estado_publico || readable(item.estado || "cotizar");
    const courseMeta = item.tipo_item === "curso"
      ? [item.fecha_inicio_publica || item.fecha_inicio, item.modalidad].filter(Boolean).join(" · ")
      : "";
    const detail = item.url_detalle
      ? `<a class="btn btn-small btn-secondary" href="${localPath(item.url_detalle)}">Ver detalle</a>`
      : "";

    return `
      <article class="commerce-card" data-commerce-item="${escapeHtml(item.id)}">
        <div class="commerce-card-media">
          <img src="${image}" alt="${escapeHtml(item.nombre)}" loading="lazy" onerror="this.onerror=null;this.src='${fallback}';">
          <div class="commerce-badge-row">
            ${item.oferta ? '<span class="commerce-badge is-offer">Oferta</span>' : ""}
            ${item.destacado ? '<span class="commerce-badge is-featured">Destacado</span>' : ""}
          </div>
        </div>
        <div class="commerce-card-body">
          <p class="commerce-kicker">${escapeHtml(line)} · ${escapeHtml(item.categoria || "Catálogo")}</p>
          <h3>${escapeHtml(item.nombre)}</h3>
          <p>${escapeHtml(item.descripcion_corta || "")}</p>
          <div class="commerce-price">
            <strong>${escapeHtml(priceText)}</strong>
            ${priceDollars}
          </div>
          <p class="commerce-status">${escapeHtml(publicStatus)}</p>
          ${courseMeta ? `<p class="commerce-status-meta">${escapeHtml(courseMeta)}</p>` : ""}
          <p class="commerce-notice">${NOTICE}</p>
          <div class="commerce-card-actions">
            <a class="btn btn-small btn-gold" href="${whatsappHref(item)}" target="_blank" rel="noopener noreferrer">Cotizar por WhatsApp</a>
            ${detail}
          </div>
        </div>
      </article>
    `;
  }

  function applyFilters(items, filters) {
    const search = normalizeText(filters.search);
    return items.filter((item) => {
      if (filters.line && item.linea_negocio !== filters.line) return false;
      if (filters.fixedLine && item.linea_negocio !== filters.fixedLine) return false;
      if (filters.category && item.categoria !== filters.category) return false;
      if (filters.currency && itemCurrency(item) !== filters.currency) return false;
      if (filters.status && item.estado !== filters.status) return false;
      if (filters.minPrice && (typeof item.precio_soles !== "number" || item.precio_soles < Number(filters.minPrice))) return false;
      if (filters.maxPrice && (typeof item.precio_soles !== "number" || item.precio_soles > Number(filters.maxPrice))) return false;
      if (!search) return true;
      const haystack = normalizeText([
        item.nombre,
        item.descripcion_corta,
        item.descripcion_larga,
        item.categoria,
        item.linea_negocio,
        ...(item.tags || [])
      ].join(" "));
      return haystack.includes(search);
    });
  }

  function sortItems(items, sort) {
    const list = [...items];
    if (sort === "precio-asc") return list.sort((a, b) => itemPriceValue(a) - itemPriceValue(b));
    if (sort === "precio-desc") return list.sort((a, b) => itemPriceValue(b) - itemPriceValue(a));
    if (sort === "nombre-az") return list.sort((a, b) => String(a.nombre).localeCompare(String(b.nombre), "es"));
    if (sort === "ofertas") return list.sort((a, b) => Number(Boolean(b.oferta)) - Number(Boolean(a.oferta)));
    return list.sort((a, b) => Number(Boolean(b.destacado)) - Number(Boolean(a.destacado)));
  }

  function readFilters(root) {
    return {
      fixedLine: root.dataset.catalogLine || "",
      line: root.querySelector("[data-commerce-line]")?.value || "",
      category: root.querySelector("[data-commerce-category]")?.value || "",
      currency: root.querySelector("[data-commerce-currency]")?.value || "",
      status: root.querySelector("[data-commerce-status]")?.value || "",
      minPrice: root.querySelector("[data-commerce-min]")?.value || "",
      maxPrice: root.querySelector("[data-commerce-max]")?.value || "",
      search: root.querySelector("[data-commerce-search-main]")?.value || root.querySelector("[data-commerce-search]")?.value || "",
      sort: root.querySelector("[data-commerce-sort]")?.value || "destacados"
    };
  }

  function renderResults(root, items) {
    const results = root.querySelector("[data-commerce-results]");
    const count = root.querySelector("[data-commerce-count]");
    if (count) count.textContent = `${items.length} resultado${items.length === 1 ? "" : "s"}`;
    if (!results) return;
    results.innerHTML = items.length
      ? items.map(card).join("")
      : '<article class="commerce-empty"><h3>No encontramos resultados</h3><p>Prueba con otra búsqueda o solicita una cotización personalizada por WhatsApp.</p></article>';
  }

  function renderHighlights(root, items) {
    const offers = root.querySelector("[data-commerce-offers]");
    const featured = root.querySelector("[data-commerce-featured]");
    if (offers) offers.innerHTML = items.filter((item) => item.oferta).slice(0, 4).map(card).join("");
    if (featured) featured.innerHTML = items.filter((item) => item.destacado).slice(0, 4).map(card).join("");
  }

  function update(root) {
    const filters = readFilters(root);
    const filtered = sortItems(applyFilters(state.items, filters), filters.sort);
    const hasActiveFilter = Boolean(filters.search || filters.line || filters.category || filters.currency || filters.status || filters.minPrice || filters.maxPrice);
    const results = root.dataset.catalogMode === "home" && !hasActiveFilter ? filtered.slice(0, 12) : filtered;
    renderResults(root, results);
    renderHighlights(root, applyFilters(state.items, { fixedLine: filters.fixedLine }));
  }

  function controls(root, items) {
    const fixedLine = root.dataset.catalogLine || "";
    const scopedItems = fixedLine ? items.filter((item) => item.linea_negocio === fixedLine) : items;
    const categories = unique(scopedItems, "categoria");
    const statuses = unique(scopedItems, "estado");
    const currencies = [...new Set(scopedItems.map(itemCurrency))].filter(Boolean).sort();
    const lines = unique(items, "linea_negocio");
    const lineFilter = fixedLine ? "" : `
      <label class="select-filter">
        <span>Línea</span>
        <select data-commerce-line>${optionList(lines, "Todas")}</select>
      </label>`;

    return `
      <div class="commerce-toolbar" data-commerce-controls>
        <label class="select-filter commerce-search">
          <span>Buscar</span>
          <input type="search" data-commerce-search placeholder="Producto, servicio, curso, proyecto...">
        </label>
        ${lineFilter}
        <label class="select-filter">
          <span>Categoría</span>
          <select data-commerce-category>${optionList(categories, "Todas")}</select>
        </label>
        <label class="select-filter">
          <span>Moneda</span>
          <select data-commerce-currency>${optionList(currencies, "Todas")}</select>
        </label>
        <label class="select-filter">
          <span>Estado</span>
          <select data-commerce-status>${optionList(statuses, "Todos")}</select>
        </label>
        <label class="select-filter">
          <span>Mín. S/</span>
          <input type="number" min="0" step="1" data-commerce-min placeholder="0">
        </label>
        <label class="select-filter">
          <span>Máx. S/</span>
          <input type="number" min="0" step="1" data-commerce-max placeholder="5000">
        </label>
        <label class="select-filter">
          <span>Ordenar</span>
          <select data-commerce-sort>
            <option value="destacados">Destacados primero</option>
            <option value="ofertas">Ofertas primero</option>
            <option value="precio-asc">Precio menor a mayor</option>
            <option value="precio-desc">Precio mayor a menor</option>
            <option value="nombre-az">Nombre A-Z</option>
          </select>
        </label>
      </div>
    `;
  }

  function centralSearch(title, subtitle, fixedLine) {
    return `
      <div class="commerce-central-search">
        <p class="eyebrow">${fixedLine ? "Catálogo por línea" : "Buscador comercial"}</p>
        <h2>${escapeHtml(title)}</h2>
        <p>${escapeHtml(subtitle)}</p>
        <label class="select-filter commerce-search-main">
          <span>Buscar</span>
          <input type="search" data-commerce-search-main placeholder="Producto, servicio, curso, tema o herramienta...">
        </label>
      </div>`;
  }

  function resourceLinks(slug) {
    const copy = LINE_PANEL_COPY[slug] || LINE_PANEL_COPY["tw-store"];
    return copy.resources
      .map(([label, href]) => `<a href="${localPath(href)}">${escapeHtml(label)}</a>`)
      .join("");
  }

  async function render(root) {
    const items = await loadItems();
    const mode = root.dataset.catalogMode || "full";
    const fixedLine = root.dataset.catalogLine || "";
    applyBanner(fixedLine || (mode === "store" ? "tw-store" : ""));
    const visibleItems = fixedLine ? items.filter((item) => item.linea_negocio === fixedLine) : items;
    const title = root.dataset.catalogTitle || (fixedLine ? LINE_LABELS[fixedLine] : "Catálogo comercial");
    const subtitle = root.dataset.catalogSubtitle || "Busca productos, servicios, cursos y proyectos de Tecprog World.";

    if (mode === "home") {
      root.innerHTML = `
        <div class="section-shell">
          <div class="section-heading">
            <p class="eyebrow">Buscador comercial</p>
            <h2>${escapeHtml(title)}</h2>
            <p>${escapeHtml(subtitle)}</p>
          </div>
          ${controls(root, items)}
          <h3 class="commerce-subtitle">Ofertas destacadas</h3>
          <div class="commerce-grid is-compact" data-commerce-offers></div>
          <h3 class="commerce-subtitle">Productos y servicios destacados</h3>
          <div class="commerce-grid is-compact" data-commerce-featured></div>
          <h3 class="commerce-subtitle">Explorar catálogo</h3>
          <div class="commerce-section-head"><strong data-commerce-count></strong></div>
          <div class="commerce-grid is-compact" data-commerce-results></div>
        </div>`;
    } else if (mode === "store") {
      const copy = LINE_PANEL_COPY["tw-store"];
      root.innerHTML = `
        <aside class="commerce-filters commerce-left-panel">
          <h2>Panel comercial</h2>
          ${controls(root, items)}
          <article class="quick-panel-card">
            <h2>Cotización</h2>
            <p>${escapeHtml(copy.action)}</p>
            <a class="btn btn-gold" href="https://wa.me/${WHATSAPP_PHONE}?text=${encodeURIComponent(copy.whatsapp)}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
          </article>
          <article class="quick-panel-card">
            <h2>Pagos</h2>
            <div class="quick-link-grid">
              <a href="${localPath("pagos/peru.html")}">Pagos Perú</a>
              <a href="${localPath("pagos/internacionales.html")}">Internacional</a>
            </div>
          </article>
          <article class="quick-panel-card">
            <h2>Aviso</h2>
            <p>Precios, disponibilidad, garantía y envío sujetos a confirmación.</p>
          </article>
        </aside>
        <section class="commerce-results">
          ${centralSearch(title, subtitle, fixedLine)}
          <div class="commerce-section-head"><strong data-commerce-count></strong></div>
          <h3 class="commerce-subtitle">Ofertas destacadas</h3>
          <div class="commerce-grid is-compact" data-commerce-offers></div>
          <h3 class="commerce-subtitle">Productos y servicios destacados</h3>
          <div class="commerce-grid is-compact" data-commerce-featured></div>
          <h3 class="commerce-subtitle">Catálogo completo</h3>
          <div class="commerce-grid" data-commerce-results></div>
        </section>
        <aside class="commerce-aside">
          <article class="quick-panel-card">
            <h2>Acciones rápidas</h2>
            <div class="quick-link-grid">
              ${resourceLinks("tw-store")}
            </div>
          </article>
          <article class="quick-panel-card"><h2>Aviso comercial</h2><p>Precios, disponibilidad, garantía, alcance y envío sujetos a confirmación.</p></article>
        </aside>`;
    } else {
      const copy = LINE_PANEL_COPY[fixedLine] || LINE_PANEL_COPY["tw-store"];
      root.innerHTML = `
        <aside class="commerce-filters commerce-left-panel">
          <h2>Panel comercial</h2>
          ${controls(root, visibleItems)}
          <article class="quick-panel-card">
            <h2>Solicitar alcance</h2>
            <p>${escapeHtml(copy.action)}</p>
            <a class="btn btn-gold" href="https://wa.me/${WHATSAPP_PHONE}?text=${encodeURIComponent(copy.whatsapp)}" target="_blank" rel="noopener noreferrer">Cotizar</a>
          </article>
          <article class="quick-panel-card"><h2>Aviso comercial</h2><p>${NOTICE}</p></article>
        </aside>
        <section class="commerce-results">
          ${centralSearch(title, subtitle, fixedLine)}
          <div class="commerce-section-head"><strong data-commerce-count></strong></div>
          <h3 class="commerce-subtitle">Destacados</h3>
          <div class="commerce-grid is-compact" data-commerce-featured></div>
          <h3 class="commerce-subtitle">Resultados</h3>
          <div class="commerce-grid" data-commerce-results></div>
        </section>
        <aside class="commerce-aside">
          <article class="quick-panel-card">
            <h2>${escapeHtml(copy.quickTitle)}</h2>
            <div class="quick-link-grid">
              <a href="https://wa.me/${WHATSAPP_PHONE}?text=${encodeURIComponent(copy.whatsapp)}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
              <a href="mailto:grupotecprog@gmail.com">Enviar correo</a>
              ${resourceLinks(fixedLine)}
            </div>
          </article>
          <article class="quick-panel-card"><h2>Confianza comercial</h2><p>Coordinamos alcance, precio, disponibilidad y condiciones antes de cualquier pago.</p></article>
        </aside>`;
    }

    root.addEventListener("input", () => update(root));
    root.addEventListener("change", () => update(root));
    update(root);
  }

  async function init(selector = "[data-commerce-catalog]") {
    const roots = [...document.querySelectorAll(selector)];
    state.roots = roots;
    await Promise.all(roots.map(render));
  }

  window.TWCatalogoGlobal = {
    init,
    render,
    filtrar: applyFilters,
    buscar: normalizeText
  };

  document.addEventListener("DOMContentLoaded", () => {
    init().catch((error) => {
      document.querySelectorAll("[data-commerce-catalog]").forEach((root) => {
        root.innerHTML = `<article class="detail-block"><h2>No se pudo cargar el catálogo</h2><p>${escapeHtml(error.message)}</p></article>`;
      });
    });
  });
})();
