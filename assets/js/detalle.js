const WHATSAPP_NUMBER_DETAIL = "51952354282";
const PAYPAL_URL_DETAIL = "https://www.paypal.com/paypalme/grupotecprog";

const DETAIL_SOURCES = [
  { url: "../data/catalogo-general-cursos.json", type: "general" },
  { url: "../data/cursos/2026-06.json", type: "periodo" },
  { url: "../data/cursos.json", type: "base" },
];

function esc(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function slugifyDetail(text) {
  return String(text || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function asset(path) {
  if (!path) return "../assets/img/cursos/capacitacion-empresarial.svg";
  return path.startsWith("../") ? path : `../${path}`;
}

function detailWhatsapp(message) {
  return `https://wa.me/${WHATSAPP_NUMBER_DETAIL}?text=${encodeURIComponent(message)}`;
}

async function fetchJson(url) {
  const response = await fetch(url);
  if (!response.ok) return [];
  return response.json();
}

function normalizeCourse(item, sourceType) {
  if (sourceType === "general") {
    return {
      id: item.id,
      sourceType,
      title: item.curso,
      line: item.linea,
      category: item.categoria,
      level: item.nivel,
      hours: item.horas_certificables,
      duration: item.duracion_referencial,
      modality: item.modalidad,
      pricePen: item.precio_peru_igv_soles ? `S/ ${item.precio_peru_igv_soles} IGV incluido` : "Consultar",
      priceUsd: item.precio_internacional_usd ? `USD ${item.precio_internacional_usd}` : "Consultar",
      shortDescription: item.descripcion_corta,
      longDescription: item.descripcion_larga,
      syllabus: item.temario_base || [],
      audience: item.publico_objetivo || [],
      includes: item.incluye || [],
      certification: item.certificacion,
      image: item.imagen,
      whatsappMessage: item.whatsapp_message,
      backHref: "../catalogo/catalogo-general-tw-educa.html",
      backLabel: "Volver al catalogo general",
    };
  }

  const title = item.titulo || item.nombre || "Curso Tecprog World";
  return {
    id: item.id || slugifyDetail(title),
    sourceType,
    title,
    line: item.linea || "TW Educa",
    category: item.categoria || item.etiqueta || "Curso",
    level: item.nivel || "Segun convocatoria",
    hours: item.horas_certificables || "Consultar",
    duration: item.duracion_referencial || "Consultar",
    modality: item.modalidad || "Virtual",
    pricePen: item.precio_desde || item.precio || "Consultar",
    priceUsd: item.precio_usd || "Consultar",
    shortDescription: item.descripcion_corta || item.descripcion || "",
    longDescription: item.descripcion_larga || item.descripcion || "",
    syllabus: buildFallbackSyllabus(title, item.horas_certificables || 24),
    audience: ["Estudiantes, profesionales y equipos tecnicos interesados en formacion aplicada."],
    includes: ["Material digital segun alcance.", "Orientacion por WhatsApp o correo.", "Acceso segun modalidad coordinada."],
    certification: "Constancia o certificado de participacion emitido por Tecprog World E.I.R.L. segun modalidad y cumplimiento acordado.",
    image: item.imagen || "assets/img/cursos/capacitacion-empresarial.svg",
    whatsappMessage: item.whatsapp_message || `Hola, deseo informacion sobre ${title}.`,
    backHref: sourceType === "periodo" ? "../catalogo/cursos-junio-2026.html" : "../catalogo/cursos.html",
    backLabel: "Volver a cursos",
  };
}

function fallbackModuleCount(hours) {
  const value = Number(hours || 0);
  if (80 <= value && value <= 120) return 8;
  if (value >= 48) return 6;
  if (value >= 32) return 5;
  if (value >= 20) return 4;
  return 3;
}

function buildFallbackSyllabus(title, hours) {
  const count = fallbackModuleCount(hours);
  const titles = [
    "Fundamentos y objetivos",
    "Herramientas y preparacion",
    "Ejercicios guiados",
    "Aplicacion tecnica",
    "Proyecto integrador",
    "Cierre y recomendaciones",
    "Portafolio tecnico",
    "Ruta de continuidad",
  ];
  return Array.from({ length: count }, (_, index) => ({
    modulo: index + 1,
    titulo: titles[index],
    contenidos: [`Conceptos aplicados de ${title}`, "Practica guiada", "Revision de entregables"],
  }));
}

async function findCourse(id, catalog) {
  const preferred = catalog === "general" ? ["general", "periodo", "base"] : ["periodo", "base", "general"];
  const sources = DETAIL_SOURCES.slice().sort((a, b) => preferred.indexOf(a.type) - preferred.indexOf(b.type));
  for (const source of sources) {
    const data = await fetchJson(source.url);
    const found = data.find((item) => (item.id || slugifyDetail(item.titulo || item.nombre || item.curso)) === id);
    if (found) return normalizeCourse(found, source.type);
  }
  return null;
}

function listItems(items) {
  return `<ul class="check-list">${items.map((item) => `<li>${esc(item)}</li>`).join("")}</ul>`;
}

function syllabusMarkup(modules) {
  return modules.map((module) => `
    <article class="detail-block">
      <h3>Modulo ${esc(module.modulo)}: ${esc(module.titulo)}</h3>
      ${listItems(module.contenidos || [])}
    </article>
  `).join("");
}

async function renderDetail() {
  const root = document.querySelector("[data-detail-root]");
  if (!root) return;

  const params = new URLSearchParams(window.location.search);
  const id = params.get("id") || "qgis-basico";
  const catalog = params.get("catalogo") || "";
  const current = await findCourse(id, catalog);

  if (!current) {
    root.innerHTML = `<section class="section"><div class="section-shell"><article class="detail-block"><h1>Curso no encontrado</h1><p>Revisa el enlace o vuelve al catalogo de cursos.</p><a class="btn btn-primary" href="../catalogo/catalogo-general-tw-educa.html">Volver al catalogo general</a></article></div></section>`;
    return;
  }

  document.title = `${current.title} | Tecprog World E.I.R.L.`;
  root.innerHTML = `
    <section class="detail-hero">
      <div class="section-shell detail-hero-grid">
        <div>
          <p class="eyebrow">${esc(current.category)} · ${esc(current.level)}</p>
          <h1>${esc(current.title)}</h1>
          <p>${esc(current.shortDescription)}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="${detailWhatsapp(current.whatsappMessage)}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
            <a class="btn btn-secondary" href="mailto:grupotecprog@gmail.com">Solicitar cotizacion</a>
            <a class="btn btn-gold" href="${PAYPAL_URL_DETAIL}" target="_blank" rel="noopener noreferrer">Solicitar pago PayPal</a>
            <a class="btn btn-secondary" href="${current.backHref}">${current.backLabel}</a>
          </div>
        </div>
        <figure class="detail-media">
          <img src="${asset(current.image)}" alt="${esc(current.title)}" onerror="this.closest('.detail-media').classList.add('has-fallback'); this.remove();">
          <figcaption>${esc(current.modality)}</figcaption>
        </figure>
      </div>
    </section>
    <section class="section">
      <div class="section-shell detail-layout">
        <div class="detail-content">
          <article class="detail-block">
            <h2>Descripcion</h2>
            <p>${esc(current.longDescription)}</p>
          </article>
          <article class="detail-block">
            <h2>Temario base</h2>
            <p>Temario referencial sujeto a ajuste segun modalidad, nivel y alcance comercial.</p>
          </article>
          ${syllabusMarkup(current.syllabus)}
          <article class="detail-block">
            <h2>Publico objetivo</h2>
            ${listItems(current.audience)}
          </article>
          <article class="detail-block">
            <h2>Que incluye</h2>
            ${listItems(current.includes)}
          </article>
          <article class="detail-block">
            <h2>Certificacion</h2>
            <p>${esc(current.certification)}</p>
          </article>
        </div>
        <aside class="detail-sidebar">
          <article class="price-panel">
            <h2>Ficha del curso</h2>
            <dl>
              <div><dt>Categoria</dt><dd>${esc(current.category)}</dd></div>
              <div><dt>Nivel</dt><dd>${esc(current.level)}</dd></div>
              <div><dt>Horas certificables</dt><dd>${esc(current.hours)}</dd></div>
              <div><dt>Duracion</dt><dd>${esc(current.duration)}</dd></div>
              <div><dt>Modalidad</dt><dd>${esc(current.modality)}</dd></div>
              <div><dt>Precio Peru</dt><dd>${esc(current.pricePen)}</dd></div>
              <div><dt>Internacional</dt><dd>${esc(current.priceUsd)}</dd></div>
            </dl>
            <div class="catalog-actions">
              <a class="btn btn-small btn-primary" href="${detailWhatsapp(current.whatsappMessage)}" target="_blank" rel="noopener noreferrer">Inscripcion por WhatsApp</a>
              <a class="btn btn-small btn-gold" href="${PAYPAL_URL_DETAIL}" target="_blank" rel="noopener noreferrer">PayPal</a>
              <a class="btn btn-small" href="${detailWhatsapp(`Hola, deseo una cotizacion institucional para ${current.title}.`)}" target="_blank" rel="noopener noreferrer">Cotizacion institucional</a>
              <a class="btn btn-small" href="${current.backHref}">${current.backLabel}</a>
            </div>
            <p class="microcopy">Los precios son referenciales y pueden variar segun alcance, modalidad, fecha de inscripcion, requerimientos y promociones vigentes.</p>
          </article>
        </aside>
      </div>
    </section>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  renderDetail().catch(console.error);
});
