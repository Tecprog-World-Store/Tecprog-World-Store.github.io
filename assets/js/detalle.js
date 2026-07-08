const WHATSAPP_NUMBER_DETAIL = "51952354282";
const PAYPAL_URL_DETAIL = "https://www.paypal.com/paypalme/grupotecprog";
const EDUCA_PRICE_NOTE = "Consulta disponibilidad, fecha de inicio, modalidad, horario y forma de pago antes de reservar tu vacante.";

const DETAIL_SOURCES = [
  { url: "/data/cursos_tw_educa.json", type: "tw-educa-vivo" },
  { url: "/data/catalogo-general-cursos.json", type: "general" },
  { url: "/data/cursos/2026-06.json", type: "periodo" },
  { url: "/data/cursos.json", type: "base" },
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
  if (!path) return "/assets/img/cursos/capacitacion-empresarial.svg";
  if (/^(https?:)?\/\//.test(path) || path.startsWith("/")) return path;
  return `/${path.replace(/^(\.\.\/)+/, "")}`;
}

function absoluteDetailUrl(path) {
  if (!path) return "";
  if (/^https?:\/\//.test(path)) return path;
  return `https://tecprog-world-store.github.io${asset(path)}`;
}

function detailWhatsapp(message) {
  return `https://wa.me/${WHATSAPP_NUMBER_DETAIL}?text=${encodeURIComponent(message)}`;
}

function commercialInquiryMessage(course) {
  return `Hola, deseo información para inscribirme en el curso "${course.title}".\n\nDeseo conocer disponibilidad de vacantes, próxima fecha de inicio, modalidad, horario, forma de pago y requisitos para reservar mi vacante.\n\nGracias.`;
}

function modalityInquiryMessage(course, price) {
  const values = [
    price.preventa_soles ? `preventa S/ ${price.preventa_soles}` : "",
    price.lanzamiento_soles ? `lanzamiento S/ ${price.lanzamiento_soles}` : "",
    price.regular_soles ? `regular S/ ${price.regular_soles}` : "",
  ].filter(Boolean).join(", ");
  return `Hola, deseo inscribirme en el curso "${course.title}" con la modalidad "${price.publico}".\n\nPrecios publicados: ${values || "consultar inversión"}.\n\nPor favor, confirmen disponibilidad, fecha de inicio y medios de pago.`;
}

async function fetchJson(url) {
  const response = await fetch(url);
  if (!response.ok) return [];
  return response.json();
}

function normalizeCourse(item, sourceType) {
  if (sourceType === "tw-educa-vivo") {
    return {
      id: item.id,
      sourceType,
      title: item.nombre,
      line: item.linea_nombre || "TW Educa",
      category: item.categoria,
      level: item.nivel || item.estado_publico || "Inscripciones abiertas",
      hours: item.duracion || "16 horas",
      duration: item.duracion || "4 sesiones en vivo",
      modality: item.modalidad || "Online",
      pricePen: item.precio || "Consultar inversión",
      priceUsd: "Consultar",
      moocText: item.estado_publico || "Curso próximo",
      moocButton: "Consultar vacantes",
      certificateText: "Certificado físico y firmado según modalidad",
      paidText: item.precio || "Consultar inversión",
      priceNote: item.nota_cronograma || "Inicio sujeto a confirmación de grupo mínimo.",
      modalityTags: [item.estado_publico, item.fecha_inicio_publica, item.modalidad].filter(Boolean),
      shortDescription: item.descripcion_corta,
      longDescription: item.descripcion_larga,
      syllabus: item.temario_base || buildFallbackSyllabus(item.nombre, 16),
      sessionSyllabus: item.temario_por_sesion || item.temario_base || [],
      audience: item.publico_objetivo || [],
      includes: item.incluye || [],
      certification: item.certificacion || "Certificado físico y firmado por Tecprog World E.I.R.L., según asistencia, modalidad y cumplimiento acordado.",
      image: item.imagen,
      urlPublica: item.url_publica,
      whatsappMessage: item.whatsapp_mensaje,
      backHref: "/educa/index.html",
      backLabel: "Volver a TW Educa",
      startDate: item.fecha_inicio_publica,
      schedule: item.cronograma || [],
      scheduleNote: item.nota_cronograma,
      sessionCount: item.numero_sesiones,
      scheduleText: item.horario,
      requirements: item.requisitos || [],
      learning: item.que_aprenderas || [],
      outcomes: item.resultados_aprendizaje || [],
      tools: item.herramientas || [],
      methodology: item.metodologia || [],
      deliverables: item.entregables || [],
      prices: item.precios || [],
      legalNotice: item.marca_legal,
      benefits: item.beneficios || [],
      finalProject: item.proyecto_final,
      faq: item.faq || [],
      relatedHref: "/educa/index.html",
      seoDescription: item.seo?.description || item.descripcion_corta,
      ogImage: item.seo?.og_image || item.imagen,
    };
  }

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
      moocText: item.mooc_texto || "Consulta de inscripción",
      moocButton: item.boton_mooc || "Consultar inscripción",
      certificateText: item.certificado_texto || (item.certificado_desde_soles ? `Certificado desde S/ ${item.certificado_desde_soles}` : "Certificado: consultar"),
      paidText: item.precio_pago_texto || (item.precio_peru_igv_soles ? `Acceso completo desde S/ ${item.precio_peru_igv_soles}` : "Acceso completo: consultar"),
      priceNote: item.nota_precio_mooc || item.politica_precio || EDUCA_PRICE_NOTE,
      modalityTags: item.modalidad_tags || [],
      shortDescription: item.descripcion_corta,
      longDescription: item.descripcion_larga,
      syllabus: item.temario_base || [],
      audience: item.publico_objetivo || [],
      includes: item.incluye || [],
      certification: item.certificacion,
      image: item.thumbnail || item.imagen_portada || item.imagen,
      whatsappMessage: item.whatsapp_message,
      backHref: "../catalogo/catálogo-general-tw-educa.html",
      backLabel: "Volver al catálogo general",
      requirements: [],
      learning: [],
      tools: [],
      benefits: [],
      faq: [],
      seoDescription: item.shareDescription || item.descripcion_corta,
      ogImage: item.ogImage || item.thumbnail || item.imagen,
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
    moocText: item.mooc_texto || "Consulta de inscripción",
    moocButton: item.boton_mooc || "Consultar inscripción",
    certificateText: item.certificado_texto || (item.certificado_desde_soles ? `Certificado desde S/ ${item.certificado_desde_soles}` : "Certificado: consultar"),
    paidText: item.precio_pago_texto || item.precio_desde || item.precio || "Acceso completo: consultar",
    priceNote: item.nota_precio_mooc || EDUCA_PRICE_NOTE,
    modalityTags: item.modalidad_tags || [],
    shortDescription: item.descripcion_corta || item.descripcion || "",
    longDescription: item.descripcion_larga || item.descripcion || "",
    syllabus: buildFallbackSyllabus(title, item.horas_certificables || 24),
    audience: ["Estudiantes, profesionales y equipos técnicos interesados en formación aplicada."],
    includes: ["Material digital según alcance.", "Orientacion por WhatsApp o correo.", "Acceso según modalidad coordinada."],
    certification: "Constancia o certificado de participacion emitido por Tecprog World E.I.R.L. según modalidad y cumplimiento acordado.",
    image: item.thumbnail || item.imagen_portada || item.imagen || "assets/img/cursos/capacitacion-empresarial.svg",
    whatsappMessage: item.whatsapp_message || `Hola, deseo información sobre ${title}.`,
    backHref: sourceType === "periodo" ? "../catalogo/cursos-junio-2026.html" : "../catalogo/cursos.html",
    backLabel: "Volver a cursos",
    requirements: [],
    learning: [],
    tools: [],
    benefits: [],
    faq: [],
    seoDescription: item.shareDescription || item.descripcion_corta || item.descripcion || "",
    ogImage: item.ogImage || item.thumbnail || item.imagen,
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
    "Aplicación técnica",
    "Proyecto integrador",
    "Cierre y recomendaciones",
    "Portafolio técnico",
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
      ${module.proposito ? `<p>${esc(module.proposito)}</p>` : ""}
      ${listItems(module.contenidos || [])}
      ${module.practica ? `<p><strong>Práctica:</strong> ${esc(module.practica)}</p>` : ""}
      ${module.resultado ? `<p><strong>Resultado:</strong> ${esc(module.resultado)}</p>` : ""}
      ${module.tarea ? `<p><strong>Tarea o avance:</strong> ${esc(module.tarea)}</p>` : ""}
    </article>
  `).join("");
}

function optionalList(title, items) {
  return Array.isArray(items) && items.length
    ? `<article class="detail-block"><h2>${esc(title)}</h2>${listItems(items)}</article>`
    : "";
}

function optionalParagraph(title, value) {
  return value
    ? `<article class="detail-block"><h2>${esc(title)}</h2><p>${esc(value)}</p></article>`
    : "";
}

function faqMarkup(items) {
  return Array.isArray(items) && items.length
    ? `<article class="detail-block"><h2>Preguntas frecuentes</h2>${items.map((item) => `<h3>${esc(item.pregunta)}</h3><p>${esc(item.respuesta)}</p>`).join("")}</article>`
    : "";
}

function investmentMarkup(items) {
  if (!Array.isArray(items) || !items.length) return "";
  return `
    <article class="detail-block">
      <h2>Inversion referencial</h2>
      <div class="table-scroll">
        <table>
          <thead>
            <tr><th>Publico</th><th>Preventa</th><th>Lanzamiento</th><th>Regular</th></tr>
          </thead>
          <tbody>
            ${items.map((item) => `
              <tr>
                <td>${esc(item.publico)}</td>
                <td>S/ ${esc(item.preventa_soles)}</td>
                <td>S/ ${esc(item.lanzamiento_soles)}</td>
                <td>S/ ${esc(item.regular_soles)}</td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      </div>
      <p>Precios referenciales en PEN${items.some((item) => item.incluye_igv) ? ", IGV incluido cuando se indique en la convocatoria" : ""}. Confirma la etapa vigente antes de pagar.</p>
    </article>
  `;
}

function modalityButtons(course) {
  if (!Array.isArray(course.prices) || !course.prices.length) {
    return `<a class="btn btn-small btn-primary" href="${detailWhatsapp(course.whatsappMessage || commercialInquiryMessage(course))}" target="_blank" rel="noopener noreferrer">Consultar inversión y próxima convocatoria</a>`;
  }
  return course.prices.map((price) => `
    <a class="btn btn-small btn-primary" href="${detailWhatsapp(modalityInquiryMessage(course, price))}" target="_blank" rel="noopener noreferrer">${esc(price.publico)}</a>
  `).join("");
}

function setMeta(selector, attr, value) {
  const tag = document.querySelector(selector);
  if (tag && value) tag.setAttribute(attr, value);
}

function setCanonical(value) {
  const tag = document.querySelector('link[rel="canonical"]');
  if (tag && value) tag.setAttribute("href", value);
}

async function renderDetail() {
  const root = document.querySelector("[data-detail-root]");
  if (!root) return;

  const params = new URLSearchParams(window.location.search);
  const id = root.dataset.courseId || params.get("id") || "qgis-basico";
  const catalog = root.dataset.catalog || params.get("catalogo") || "";
  const current = await findCourse(id, catalog);

  if (!current) {
    root.innerHTML = `<section class="section"><div class="section-shell"><article class="detail-block"><h1>Curso no encontrado</h1><p>Revisa el enlace o vuelve al catálogo de cursos.</p><a class="btn btn-primary" href="../catalogo/catálogo-general-tw-educa.html">Volver al catálogo general</a></article></div></section>`;
    return;
  }

  document.title = `${current.title} | Tecprog World E.I.R.L.`;
  const publicUrl = `https://tecprog-world-store.github.io/detalle/curso.html?id=${encodeURIComponent(current.id)}&catalogo=${encodeURIComponent(current.sourceType)}`;
  const canonicalUrl = current.urlPublica
    ? `https://tecprog-world-store.github.io/${current.urlPublica.replace(/^\/+/, "")}`
    : publicUrl;
  const metaDescription = current.seoDescription || current.shortDescription;
  const metaImage = absoluteDetailUrl(current.ogImage || current.image);
  setMeta('meta[name="description"]', "content", metaDescription);
  setMeta('meta[property="og:title"]', "content", `${current.title} | TW Educa`);
  setMeta('meta[property="og:description"]', "content", metaDescription);
  setMeta('meta[property="og:image"]', "content", metaImage);
  setMeta('meta[property="og:url"]', "content", canonicalUrl);
  setMeta('meta[name="twitter:title"]', "content", `${current.title} | TW Educa`);
  setMeta('meta[name="twitter:description"]', "content", metaDescription);
  setMeta('meta[name="twitter:image"]', "content", metaImage);
  setCanonical(canonicalUrl);
  root.innerHTML = `
    <section class="detail-hero">
      <div class="section-shell detail-hero-grid">
        <div>
          <p class="eyebrow">${esc(current.category)} · ${esc(current.level)}</p>
          <h1>${esc(current.title)}</h1>
          <p>${esc(current.shortDescription)}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="${detailWhatsapp(current.whatsappMessage)}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
            <a class="btn btn-secondary" href="${detailWhatsapp(commercialInquiryMessage(current))}" target="_blank" rel="noopener noreferrer">${esc(current.moocButton)}</a>
            <a class="btn btn-secondary" href="mailto:grupotecprog@gmail.com">Consultar inscripción</a>
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
          ${optionalList("Que aprenderas", current.learning)}
          ${optionalList("Resultados de aprendizaje", current.outcomes)}
          ${optionalParagraph("Proyecto final", current.finalProject)}
          ${optionalList("Entregables", current.deliverables)}
          ${optionalList("Herramientas y tecnologias", current.tools)}
          ${optionalList("Metodologia", current.methodology)}
          ${investmentMarkup(current.prices)}
          <article class="detail-block">
            <h2>Inscripcion y certificacion</h2>
            <p>${esc(current.priceNote)}</p>
            <ul class="check-list">
              <li>${esc(current.moocText)}: confirma vacantes, fecha de inicio y etapa comercial vigente.</li>
              <li>${esc(current.certificateText)}: sujeto a asistencia, participacion y condiciones de la convocatoria.</li>
              <li>${esc(current.paidText)}: clases, evaluación, acompañamiento o acceso completo según modalidad.</li>
            </ul>
          </article>
          <article class="detail-block">
            <h2>Temario base</h2>
            <p>Temario referencial sujeto a ajuste según modalidad, nivel y alcance comercial.</p>
          </article>
          ${syllabusMarkup(current.syllabus)}
          ${optionalList("Cronograma", current.schedule)}
          <article class="detail-block">
            <h2>Publico objetivo</h2>
            ${listItems(current.audience)}
          </article>
          ${optionalList("Requisitos", current.requirements)}
          <article class="detail-block">
            <h2>Que incluye</h2>
            ${listItems(current.includes)}
          </article>
          ${optionalList("Beneficios realistas", current.benefits)}
          <article class="detail-block">
            <h2>Certificacion</h2>
            <p>${esc(current.certification)}</p>
          </article>
          ${faqMarkup(current.faq)}
          ${optionalParagraph("Aviso sobre marcas y software", current.legalNotice)}
          <article class="detail-block">
            <h2>Cursos relacionados TW Educa</h2>
            <p>Explora otros cursos técnicos online en Perú sobre programación, GIS, simulación, inteligencia artificial y herramientas aplicadas.</p>
            <a class="btn btn-primary" href="${current.relatedHref || "../educa/index.html"}">Ver catálogo TW Educa</a>
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
              ${current.sessionCount ? `<div><dt>Sesiones</dt><dd>${esc(current.sessionCount)}</dd></div>` : ""}
              <div><dt>Modalidad</dt><dd>${esc(current.modality)}</dd></div>
              ${current.startDate ? `<div><dt>Inicio</dt><dd>${esc(current.startDate)}</dd></div>` : ""}
              ${current.scheduleText ? `<div><dt>Horario</dt><dd>${esc(current.scheduleText)}</dd></div>` : ""}
              <div><dt>Inscripcion</dt><dd>${esc(current.moocText)}</dd></div>
              <div><dt>Certificado</dt><dd>${esc(current.certificateText)}</dd></div>
              <div><dt>Acceso completo</dt><dd>${esc(current.paidText)}</dd></div>
              <div><dt>Inversion publicada</dt><dd>${esc(current.pricePen)}</dd></div>
              <div><dt>Internacional</dt><dd>${esc(current.priceUsd)}</dd></div>
            </dl>
            <div class="catalog-actions">
              ${modalityButtons(current)}
              <a class="btn btn-small btn-primary" href="${detailWhatsapp(current.whatsappMessage)}" target="_blank" rel="noopener noreferrer">Inscripcion por WhatsApp</a>
              <a class="btn btn-small btn-gold" href="${PAYPAL_URL_DETAIL}" target="_blank" rel="noopener noreferrer">PayPal</a>
              <a class="btn btn-small" href="${detailWhatsapp(`Hola, deseo información institucional para inscribir a un equipo en el curso ${current.title}.`)}" target="_blank" rel="noopener noreferrer">Inscripción institucional</a>
              <a class="btn btn-small" href="${current.backHref}">${current.backLabel}</a>
            </div>
            <p class="microcopy">${esc(current.priceNote)}</p>
          </article>
        </aside>
      </div>
    </section>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  renderDetail().catch(console.error);
});
