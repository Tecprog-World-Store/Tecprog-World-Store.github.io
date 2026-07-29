(function () {
  "use strict";

  const SCRIPT_SRC = document.currentScript?.getAttribute("src") || "";
  const BASE_PREFIX = SCRIPT_SRC
    ? new URL("../../", new URL(SCRIPT_SRC, document.baseURI)).href
    : "/";
  const DATA_ROOT = new URL("data/cronogramas/", BASE_PREFIX);
  const LIMA_ZONE = "America/Lima";
  const state = {
    ready: null,
    configuration: null,
    metadata: null,
    courses: [],
    courseMap: new Map(),
    convocations: [],
    byCourse: new Map()
  };

  function localPath(path) {
    if (!path) return "";
    if (/^(https?:)?\/\//.test(path) || path.startsWith("data:")) return path;
    return new URL(path.replace(/^\/+/, ""), BASE_PREFIX).href;
  }

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function normalize(value) {
    return String(value ?? "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .trim();
  }

  async function fetchJson(path) {
    const response = await fetch(new URL(path, DATA_ROOT), { cache: "no-store" });
    if (!response.ok) throw new Error(`No se pudo cargar ${path}`);
    return response.json();
  }

  async function load() {
    if (state.ready) return state.ready;
    state.ready = (async () => {
      const [configuration, metadata, courseData] = await Promise.all([
        fetchJson("configuracion.json"),
        fetchJson("actual.json"),
        fetchJson("cursos.json")
      ]);
      const months = await Promise.all(
        metadata.periodos_disponibles.map((period) => fetchJson(`${period}.json`))
      );
      state.configuration = configuration;
      state.metadata = metadata;
      state.courses = courseData.cursos || [];
      state.courseMap = new Map(state.courses.map((course) => [course.id, course]));
      state.convocations = months.flatMap((month) => month.convocatorias || []);
      state.byCourse = new Map();
      state.convocations.forEach((convocation) => {
        if (!state.byCourse.has(convocation.curso_id)) state.byCourse.set(convocation.curso_id, []);
        state.byCourse.get(convocation.curso_id).push(convocation);
      });
      state.byCourse.forEach((items) => items.sort((a, b) => a.fecha_inicio.localeCompare(b.fecha_inicio)));
      return state;
    })();
    return state.ready;
  }

  function startDate(convocation) {
    return new Date(`${convocation.fecha_inicio}T${convocation.hora_inicio}:00-05:00`);
  }

  function endDate(convocation) {
    const start = startDate(convocation);
    const [startHour, startMinute] = convocation.hora_inicio.split(":").map(Number);
    const [endHour, endMinute] = convocation.hora_fin.split(":").map(Number);
    let minutes = (endHour * 60 + endMinute) - (startHour * 60 + startMinute);
    if (minutes <= 0) minutes += 1440;
    return new Date(start.getTime() + minutes * 60000);
  }

  function formatDate(value, timeZone, includeYear = true) {
    return new Intl.DateTimeFormat("es-PE", {
      timeZone,
      weekday: "long",
      day: "numeric",
      month: "long",
      ...(includeYear ? { year: "numeric" } : {})
    }).format(value);
  }

  function formatDateTime(value, timeZone) {
    return new Intl.DateTimeFormat("es-PE", {
      timeZone,
      weekday: "long",
      day: "numeric",
      month: "long",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      hour12: false
    }).format(value);
  }

  function formatTime(value, timeZone) {
    return new Intl.DateTimeFormat("es-PE", {
      timeZone,
      hour: "2-digit",
      minute: "2-digit",
      hour12: false
    }).format(value);
  }

  function localTimezone() {
    return Intl.DateTimeFormat().resolvedOptions().timeZone || LIMA_ZONE;
  }

  function periodLabel(period) {
    const [year, month] = period.split("-").map(Number);
    const label = new Intl.DateTimeFormat("es-PE", {
      month: "long",
      year: "numeric",
      timeZone: "UTC"
    }).format(new Date(Date.UTC(year, month - 1, 1)));
    return label.charAt(0).toUpperCase() + label.slice(1);
  }

  function officialDateText(convocation) {
    return formatDate(startDate(convocation), LIMA_ZONE);
  }

  function localEquivalent(convocation) {
    const zone = localTimezone();
    if (zone === LIMA_ZONE) return "";
    return `${formatDateTime(startDate(convocation), zone)}–${formatTime(endDate(convocation), zone)}`;
  }

  function timeBucket(time) {
    const hour = Number(String(time).slice(0, 2));
    if (hour < 12) return "Mañana";
    if (hour < 18) return "Tarde";
    return "Noche";
  }

  function nextDateMarkup(item) {
    return `
      <p><strong>${escapeHtml(officialDateText(item))}</strong></p>
      <p><strong>Horario:</strong><br>${escapeHtml(item.dias_clase)}, ${escapeHtml(item.hora_inicio)}–${escapeHtml(item.hora_fin)}</p>
      <p><strong>Hora de referencia:</strong><br>Lima, Perú — UTC-05:00</p>
      <p><strong>Grupo:</strong><br>Mínimo ${escapeHtml(item.minimo_inscritos)} participantes</p>
      <p><strong>Estado:</strong><br>${escapeHtml(item.estado)}</p>`;
  }

  function dateList(items) {
    return items.map((item) => `
      <p>
        <strong>${escapeHtml(periodLabel(item.periodo))}</strong><br>
        ${escapeHtml(officialDateText(item))}<br>
        ${escapeHtml(item.dias_clase)}, ${escapeHtml(item.hora_inicio)}–${escapeHtml(item.hora_fin)}
      </p>
    `).join("");
  }

  function compactSchedule(items) {
    const next = items[0];
    return `
      <section class="course-card-schedule" aria-label="Próximas fechas de inicio">
        <p class="eyebrow">Próximo inicio</p>
        ${nextDateMarkup(next)}
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="${escapeHtml(next.enlace_inscripcion)}" target="_blank" rel="noopener noreferrer">Inscribirme por WhatsApp</a>
        </div>
        <details>
          <summary>Ver próximas fechas</summary>
          <div class="course-card-schedule-list">
            ${dateList(items)}
          </div>
        </details>
      </section>`;
  }

  async function enhanceCards(root = document) {
    await load();
    const cards = [...root.querySelectorAll("[data-commerce-item], [data-course-card-id]")];
    cards.forEach((card) => {
      if (card.dataset.courseScheduleCardReady === "true") return;
      const courseId = card.dataset.commerceItem || card.dataset.courseCardId;
      const course = state.courseMap.get(courseId);
      const items = state.byCourse.get(courseId);
      if (!course || !items?.length) return;
      const body = card.querySelector(".commerce-card-body, .catalog-body") || card;
      body.insertAdjacentHTML("beforeend", compactSchedule(items));
      card.dataset.courseScheduleCardReady = "true";
    });
  }

  function detailRow(item, includeLocal) {
    const local = includeLocal ? localEquivalent(item) : "";
    return `
      <tr>
        <td>${escapeHtml(periodLabel(item.periodo))}</td>
        <td>
          ${escapeHtml(officialDateText(item))}
          ${local ? `<small class="schedule-local-time"><strong>En tu zona:</strong> ${escapeHtml(local)}</small>` : ""}
        </td>
        <td>${escapeHtml(item.dias_clase)}</td>
        <td>${escapeHtml(item.hora_inicio)}–${escapeHtml(item.hora_fin)}</td>
        <td><span class="schedule-status">${escapeHtml(item.estado)}</span></td>
        <td><a class="btn btn-small btn-primary" href="${escapeHtml(item.enlace_inscripcion)}" target="_blank" rel="noopener noreferrer">WhatsApp</a></td>
      </tr>`;
  }

  function detailTable(items, label, includeLocal) {
    return `
      <div class="schedule-table-wrap" role="region" aria-label="${escapeHtml(label)}" tabindex="0">
        <table class="schedule-table">
          <thead>
            <tr><th>Mes</th><th>Fecha de inicio</th><th>Días</th><th>Horario</th><th>Estado</th><th>Inscripción</th></tr>
          </thead>
          <tbody>${items.map((item) => detailRow(item, includeLocal)).join("")}</tbody>
        </table>
      </div>`;
  }

  function schedulePolicy() {
    return `
      <div class="schedule-policy">
        <p>Las fechas y horarios son tentativos. La apertura de cada grupo está sujeta al mínimo de participantes indicado. Cuando no se alcance el mínimo, el estudiante podrá trasladar su reserva a la siguiente convocatoria o coordinar una alternativa, de acuerdo con las condiciones comerciales vigentes.</p>
        <p>Los horarios se expresan en la hora de Lima, Perú (UTC-05:00). Si visitas la página desde otra zona horaria, se mostrará una equivalencia local orientativa.</p>
      </div>`;
  }

  async function renderDetail(root, requestedId) {
    await load();
    if (!root) return;
    const courseId = requestedId || root.dataset.courseId;
    const course = state.courseMap.get(courseId);
    const items = state.byCourse.get(courseId) || [];
    if (!course || items.length !== 12) {
      root.innerHTML = "";
      const wrapper = root.closest(".section");
      if (wrapper) wrapper.hidden = true;
      return;
    }
    root.dataset.courseScheduleReady = "true";
    root.innerHTML = `
      <div class="section-heading">
        <p class="eyebrow">Agosto 2026–julio 2027</p>
        <h2>Próximas fechas de inicio</h2>
        <p>Modalidad: ${escapeHtml(course.modalidad)} · Hora de referencia: Lima, Perú — UTC-05:00 · Apertura: mínimo ${escapeHtml(course.minimo_inscritos)} participantes.</p>
      </div>
      ${detailTable(items.slice(0, 4), "Primeras cuatro fechas de inicio", true)}
      <details class="schedule-all-dates">
        <summary>Mostrar las 12 fechas</summary>
        ${detailTable(items.slice(4), "Ocho fechas de inicio adicionales", true)}
      </details>
      ${schedulePolicy()}`;
  }

  function unique(values) {
    return [...new Set(values.filter(Boolean))].sort((a, b) => String(a).localeCompare(String(b), "es"));
  }

  function annualControls() {
    const periods = state.metadata.periodos_disponibles;
    const categories = unique(state.courses.map((course) => course.categoria));
    return `
      <div class="annual-schedule-controls" data-annual-controls>
        <label><span>Mes</span><select data-annual-filter="periodo">${periods.map((period) => `<option value="${period}">${escapeHtml(periodLabel(period))}</option>`).join("")}<option value="">Todos los meses</option></select></label>
        <label><span>Curso</span><input type="search" data-annual-search placeholder="Nombre del curso"></label>
        <label><span>Categoría</span><select data-annual-filter="categoria"><option value="">Todas</option>${categories.map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(value)}</option>`).join("")}</select></label>
      </div>`;
  }

  function annualFiltered(root) {
    const controls = root.querySelector("[data-annual-controls]");
    const period = controls.querySelector('[data-annual-filter="periodo"]').value;
    const category = controls.querySelector('[data-annual-filter="categoria"]').value;
    const search = normalize(controls.querySelector("[data-annual-search]").value);
    return state.convocations.filter((item) => {
      const course = state.courseMap.get(item.curso_id);
      if (!course || (period && item.periodo !== period) || (category && course.categoria !== category)) return false;
      return !search || normalize(`${course.nombre} ${course.categoria}`).includes(search);
    });
  }

  function annualCard(item) {
    const course = state.courseMap.get(item.curso_id);
    return `
      <article class="schedule-card"
        data-schedule-period="${escapeHtml(item.periodo)}"
        data-schedule-course="${escapeHtml(item.curso_id)}"
        data-schedule-category="${escapeHtml(course.categoria)}"
        data-schedule-time="${escapeHtml(timeBucket(item.hora_inicio))}">
        <div class="schedule-card-heading">
          <div><p class="eyebrow">${escapeHtml(periodLabel(item.periodo))}</p><h3>${escapeHtml(course.nombre)}</h3></div>
          <span class="schedule-status">${escapeHtml(item.estado)}</span>
        </div>
        <p><strong>Fecha y horario:</strong><br>${escapeHtml(officialDateText(item))}, ${escapeHtml(item.hora_inicio)}–${escapeHtml(item.hora_fin)}</p>
        <p><strong>Días:</strong> ${escapeHtml(item.dias_clase)}</p>
        <p><strong>Referencia horaria:</strong> Lima, Perú — UTC-05:00</p>
        <p><strong>Apertura:</strong> mínimo ${escapeHtml(item.minimo_inscritos)} participantes</p>
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="${escapeHtml(item.enlace_inscripcion)}" target="_blank" rel="noopener noreferrer">Inscribirme por WhatsApp</a>
          <a class="btn btn-small btn-secondary" href="${escapeHtml(localPath(course.url_detalle))}">Ver curso</a>
        </div>
      </article>`;
  }

  function updateAnnual(root) {
    const items = annualFiltered(root);
    root.querySelector("[data-annual-count]").textContent = `${items.length} convocatoria${items.length === 1 ? "" : "s"}`;
    root.querySelector("[data-annual-results]").innerHTML = items.length
      ? items.map(annualCard).join("")
      : `<article class="detail-block"><h2>Sin resultados</h2><p>Ajusta los filtros.</p></article>`;
  }

  async function renderAnnual(root) {
    await load();
    if (!root || root.dataset.annualScheduleReady === "true") return;
    root.innerHTML = `
      ${annualControls()}
      <div class="annual-schedule-summary">
        <strong data-annual-count></strong>
        <span>37 cursos publicados · 444 convocatorias · Lima UTC-05:00</span>
      </div>
      <div class="annual-schedule-grid" data-annual-results></div>
      ${schedulePolicy()}`;
    root.addEventListener("input", () => updateAnnual(root));
    root.addEventListener("change", () => updateAnnual(root));
    root.dataset.annualScheduleReady = "true";
    updateAnnual(root);
  }

  async function initAll() {
    await load();
    await Promise.all([
      ...[...document.querySelectorAll("[data-course-schedule]")].map((root) => renderDetail(root)),
      ...[...document.querySelectorAll("[data-annual-schedule]")].map((root) => renderAnnual(root))
    ]);
    await enhanceCards(document);
  }

  window.TWCursoSchedule = { load, initAll, renderDetail, renderAnnual, enhanceCards };

  document.addEventListener("DOMContentLoaded", () => {
    initAll().catch((error) => {
      document.querySelectorAll("[data-course-schedule], [data-annual-schedule]").forEach((root) => {
        root.innerHTML = `<article class="detail-block"><h2>Cronograma temporalmente no disponible</h2><p>${escapeHtml(error.message)}</p></article>`;
      });
    });
  });
})();
