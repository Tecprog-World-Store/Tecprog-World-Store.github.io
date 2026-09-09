const CATALOG_GENERAL_SOURCE = "../data/catalogo-general-cursos.json";
const CATALOG_WHATSAPP = "51952354282";

function catalogEscape(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function catalogAsset(path) {
  return `../${path}`;
}

function catalogImage(item) {
  return item.thumbnail || item.imagen_portada || item.imagen || "assets/img/cursos/capacitacion-empresarial.svg";
}

function catalogWhatsapp(message) {
  return `https://wa.me/${CATALOG_WHATSAPP}?text=${encodeURIComponent(message)}`;
}

async function loadCatalogGeneral() {
  const response = await fetch(`${CATALOG_GENERAL_SOURCE}?v=img-final-20260628`, { cache: "no-store" });
  if (!response.ok) throw new Error("No se pudo cargar el catalogo general");
  return response.json();
}

function uniqueCatalog(items, key) {
  return [...new Set(items.map((item) => item[key]).filter(Boolean))].sort((a, b) => String(a).localeCompare(String(b), "es"));
}

function selectFilter(items, key, label) {
  return `
    <label class="select-filter">
      <span>${label}</span>
      <select data-course-filter="${key}">
        <option value="">Todos</option>
        ${uniqueCatalog(items, key).map((value) => `<option value="${catalogEscape(value)}">${catalogEscape(value)}</option>`).join("")}
      </select>
    </label>
  `;
}

function priceBucket(price) {
  const value = Number(price || 0);
  if (value <= 0) return "Sin precio";
  if (value <= 199) return "Hasta USD 199";
  if (value <= 299) return "USD 200 a USD 299";
  return "USD 300 o más";
}

function moocText(item) {
  return item.mooc_texto || "Consulta de inscripcion";
}

function certificateText(item) {
  return item.certificado_texto || (item.certificado_desde_soles ? `Certificado desde S/ ${item.certificado_desde_soles}` : "Certificado: consultar");
}

function modalityTagString(item) {
  return (item.modalidad_tags || []).join(" ");
}

function hoursBucket(hours) {
  const value = Number(hours || 0);
  if (value <= 24) return "12 a 24 h";
  if (value <= 40) return "32 a 40 h";
  if (value <= 79) return "48 a 79 h";
  return "80 h o mas";
}

function courseCard(item) {
  const detailHref = `../detalle/curso.html?id=${encodeURIComponent(item.id)}&catalogo=general`;
  return `
    <article class="catalog-card course-general-card" data-course-card-id="${catalogEscape(item.id)}"
      data-categoria="${catalogEscape(item.categoria)}"
      data-nivel="${catalogEscape(item.nivel)}"
      data-horas="${catalogEscape(hoursBucket(item.horas_certificables))}"
      data-fuente="${catalogEscape(item.fuente_base)}"
      data-precio="${catalogEscape(priceBucket(item.precio_venta_usd))}"
      data-mooc="${item.precio_peru_igv_soles ? "Inscripcion con precio" : "Consultar inscripcion"}"
      data-certificado="${item.certificado_desde_soles ? "Certificado pagado" : ""}"
      data-en-vivo="${(item.modalidad_tags || []).includes("En vivo") ? "En vivo" : ""}"
      data-grabado="${(item.modalidad_tags || []).includes("Grabado") ? "Grabado" : ""}"
      data-especializacion="${(item.modalidad_tags || []).includes("Especializacion") ? "Especializacion" : ""}"
      data-prioridad="${catalogEscape(item.prioridad_web)}"
      data-search="${catalogEscape(`${item.curso} ${item.categoria} ${item.descripcion_corta} ${item.fuente_base} ${modalityTagString(item)}`).toLowerCase()}">
      <div class="catalog-media">
        <img src="${catalogAsset(catalogImage(item))}" alt="${catalogEscape(item.alt || item.curso)}" loading="lazy">
        <span>${catalogEscape(item.horas_certificables)} h</span>
      </div>
      <div class="catalog-body">
        <p class="catalog-category">${catalogEscape(item.categoria)} · ${catalogEscape(item.nivel)}</p>
        <h3>${catalogEscape(item.curso)}</h3>
        <p>${catalogEscape(item.descripcion_corta)}</p>
        <p>Matrícula abierta · ${catalogEscape(item.modalidad)}</p>
        <strong>${catalogEscape(window.TWPrecio(item))}</strong>
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="${detailHref}">Ver más</a>
        </div>
      </div>
    </article>
  `;
}

function renderCatalogFilters(items) {
  const target = document.querySelector("[data-general-course-filters]");
  if (!target) return;
  const withBuckets = items.map((item) => ({
    ...item,
    horas_bucket: hoursBucket(item.horas_certificables),
    precio_bucket: priceBucket(item.precio_venta_usd),
  }));
  target.innerHTML = `
    <label class="select-filter search-filter">
      <span>Buscar</span>
      <input type="search" data-course-search placeholder="Curso, categoria, fuente...">
    </label>
    ${selectFilter(withBuckets, "categoria", "Categoria")}
    ${selectFilter(withBuckets, "nivel", "Nivel")}
    ${selectFilter(withBuckets, "horas_bucket", "Horas certificables")}
    ${selectFilter(withBuckets, "fuente_base", "Fuente base")}
    ${selectFilter(withBuckets, "precio_bucket", "Precio")}
    ${selectFilter(withBuckets, "prioridad_web", "Prioridad")}
    <label class="select-filter">
      <span>Oferta</span>
      <select data-course-filter="oferta_mooc">
        <option value="">Todos</option>
        <option value="Inscripcion con precio">Inscripcion con precio</option>
        <option value="Consultar inscripcion">Consultar inscripcion</option>
        <option value="Certificado pagado">Certificado pagado</option>
        <option value="En vivo">En vivo</option>
        <option value="Grabado">Grabado</option>
        <option value="Especializacion">Especializacion</option>
      </select>
    </label>
  `;
}

function applyCourseFilters() {
  const filterRoot = document.querySelector("[data-general-course-filters]");
  const search = filterRoot?.querySelector("[data-course-search]")?.value.trim().toLowerCase() || "";
  const datasetKey = {
    categoria: "categoria",
    nivel: "nivel",
    horas_bucket: "horas",
    fuente_base: "fuente",
    precio_bucket: "precio",
    prioridad_web: "prioridad",
  };
  const filters = [...(filterRoot?.querySelectorAll("[data-course-filter]") || [])].map((select) => ({
    key: datasetKey[select.dataset.courseFilter] || select.dataset.courseFilter,
    value: select.value,
  }));
  document.querySelectorAll(".course-general-card").forEach((card) => {
    const textMatch = !search || card.dataset.search.includes(search);
    const filterMatch = filters.every((filter) => {
      if (!filter.value) return true;
      if (filter.key === "oferta_mooc") {
        const specialKey = {
          "MOOC gratuito": "mooc",
          "Certificado pagado": "certificado",
          "En vivo": "enVivo",
          "Grabado": "grabado",
          "Especializacion": "especializacion",
        }[filter.value];
        return specialKey ? card.dataset[specialKey] === filter.value : true;
      }
      return card.dataset[filter.key] === filter.value;
    });
    card.hidden = !(textMatch && filterMatch);
  });
}

async function renderCatalogGeneral() {
  const grid = document.querySelector("[data-general-course-grid]");
  if (!grid) return;
  const items = await loadCatalogGeneral();
  renderCatalogFilters(items);
  grid.innerHTML = items.map(courseCard).join("");
  if (window.TWCursoSchedule) {
    void window.TWCursoSchedule.enhanceCards(grid);
  }
  document.querySelector("[data-course-count]").textContent = `${items.length} cursos`;
  document.querySelector("[data-general-course-filters]").addEventListener("input", applyCourseFilters);
  document.querySelector("[data-general-course-filters]").addEventListener("change", applyCourseFilters);
}

document.addEventListener("DOMContentLoaded", () => {
  renderCatalogGeneral().catch(console.error);
});
