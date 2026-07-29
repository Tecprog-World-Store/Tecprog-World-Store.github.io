(function () {
  "use strict";

  const SCRIPT_SRC = document.currentScript?.getAttribute("src") || "";
  const BASE_PREFIX = SCRIPT_SRC
    ? new URL("../../", new URL(SCRIPT_SRC, document.baseURI)).href
    : "/";
  const DATA_ROOT = new URL("data/cronogramas/", BASE_PREFIX);
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

  function officialDate(convocation) {
    return new Date(`${convocation.fecha_inicio}T${convocation.hora_inicio}:00-05:00`);
  }

  function endDate(convocation) {
    const start = officialDate(convocation);
    const [startHour, startMinute] = convocation.hora_inicio.split(":").map(Number);
    const [endHour, endMinute] = convocation.hora_fin.split(":").map(Number);
    let minutes = (endHour * 60 + endMinute) - (startHour * 60 + startMinute);
    if (minutes <= 0) minutes += 24 * 60;
    return new Date(start.getTime() + minutes * 60 * 1000);
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
    return Intl.DateTimeFormat().resolvedOptions().timeZone || "Zona local";
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

  function officialText(convocation) {
    return `${formatDateTime(officialDate(convocation), "America/Lima")}–${formatTime(endDate(convocation), "America/Lima")}`;
  }

  function localText(convocation) {
    const zone = localTimezone();
    return `${formatDateTime(officialDate(convocation), zone)}–${formatTime(endDate(convocation), zone)}`;
  }

  function priceText(convocation) {
    return `S/ ${convocation.precio_pen} PEN | USD ${convocation.precio_usd}`;
  }

  function timezoneBlock(convocation) {
    return `
      <div class="schedule-timezones">
        <p><strong>Hora oficial:</strong> ${escapeHtml(officialText(convocation))}, Lima, Perú.</p>
        <p><strong>En tu zona horaria:</strong> ${escapeHtml(localText(convocation))}.</p>
        <p><strong>Zona detectada:</strong> ${escapeHtml(localTimezone())}. Conversión referencial.</p>
      </div>`;
  }

  function convocationCard(convocation, course, options = {}) {
    const compact = options.compact === true;
    return `
      <article class="schedule-card${compact ? " is-compact" : ""}"
        data-schedule-period="${escapeHtml(convocation.periodo)}"
        data-schedule-course="${escapeHtml(convocation.curso_id)}"
        data-schedule-category="${escapeHtml(course.categoria)}"
        data-schedule-day="${escapeHtml(convocation.dias_clase)}"
        data-schedule-modality="${escapeHtml(convocation.modalidad)}"
        data-schedule-status="${escapeHtml(convocation.estado)}"
        data-schedule-time="${escapeHtml(timeBucket(convocation.hora_inicio))}">
        <div class="schedule-card-heading">
          <div>
            <p class="eyebrow">${escapeHtml(periodLabel(convocation.periodo))}</p>
            ${compact ? "" : `<h3>${escapeHtml(course.nombre)}</h3>`}
          </div>
          <span class="schedule-status">${escapeHtml(convocation.estado)}</span>
        </div>
        <p><strong>Inicio tentativo:</strong> ${escapeHtml(officialText(convocation))}.</p>
        <p><strong>Días:</strong> ${escapeHtml(convocation.dias_clase)} · <strong>Modalidad:</strong> ${escapeHtml(convocation.modalidad)}.</p>
        <p><strong>Hora de Lima:</strong> America/Lima · UTC-05:00.</p>
        <p><strong>Mínimo:</strong> ${escapeHtml(convocation.minimo_inscritos)} participantes. ${escapeHtml(convocation.condicion)}.</p>
        <p class="schedule-price"><strong>${escapeHtml(priceText(convocation))}</strong></p>
        ${compact ? "" : timezoneBlock(convocation)}
        <p class="schedule-note">${escapeHtml(convocation.nota_confirmacion)}</p>
        <div class="catalog-actions">
          <a class="btn btn-small btn-primary" href="${escapeHtml(convocation.enlace_inscripcion)}" target="_blank" rel="noopener noreferrer">Inscribirme por WhatsApp</a>
          ${options.detailLink ? `<a class="btn btn-small btn-secondary" href="${escapeHtml(localPath(course.url_detalle))}">Ver curso</a>` : ""}
        </div>
      </article>`;
  }

  function schedulePolicy() {
    return `
      <aside class="schedule-policy">
        <p><strong>Fechas tentativas:</strong> Las fechas y horarios son tentativos. La apertura de cada grupo está sujeta al mínimo de participantes indicado. Cuando no se alcance el mínimo, el estudiante podrá trasladar su reserva a la siguiente convocatoria o coordinar una alternativa, de acuerdo con las condiciones comerciales vigentes.</p>
        <p>Los horarios se presentan en la hora oficial de Lima, Perú (UTC-05:00). Los participantes internacionales deben verificar la equivalencia con su zona horaria.</p>
        <p>El importe internacional es referencial y puede variar por conversión de moneda, comisión de PayPal o entidad financiera.</p>
      </aside>`;
  }

  async function renderDetail(root, requestedId) {
    await load();
    if (!root) return;
    const courseId = requestedId || root.dataset.courseId;
    const course = state.courseMap.get(courseId);
    const items = state.byCourse.get(courseId) || [];
    if (!course || !items.length) {
      root.innerHTML = `<article class="detail-block"><h2>Próximas convocatorias</h2><p>Solicita el cronograma vigente por WhatsApp.</p></article>`;
      return;
    }
    root.dataset.courseScheduleReady = "true";
    root.innerHTML = `
      <div class="section-heading">
        <p class="eyebrow">Programación agosto 2026–julio 2027</p>
        <h2>Próximas convocatorias</h2>
        <p>Doce oportunidades de inicio con fechas y horarios tentativos.</p>
      </div>
      <div class="schedule-month-grid">
        ${items.map((item) => convocationCard(item, course)).join("")}
      </div>
      ${schedulePolicy()}`;
  }

  function compactSchedule(items, course) {
    const next = items[0];
    const following = items.slice(0, 3);
    return `
      <section class="course-card-schedule" aria-label="Próximas convocatorias">
        <p class="eyebrow">Próximo inicio</p>
        <p><strong>${escapeHtml(periodLabel(next.periodo))}:</strong> ${escapeHtml(next.dias_clase)}, ${escapeHtml(next.hora_inicio)}–${escapeHtml(next.hora_fin)}.</p>
        <p>Hora de Lima · UTC-05:00 · ${escapeHtml(next.modalidad)}.</p>
        <p>Mínimo ${escapeHtml(next.minimo_inscritos)} · ${escapeHtml(next.estado)} · sujeto a mínimo.</p>
        <p class="schedule-price"><strong>${escapeHtml(priceText(next))}</strong></p>
        <details>
          <summary>Ver próximas fechas</summary>
          <div class="course-card-schedule-list">
            ${following.map((item) => `
              <p><strong>${escapeHtml(periodLabel(item.periodo))}</strong><br>
              ${escapeHtml(item.fecha_inicio)} · ${escapeHtml(item.hora_inicio)}–${escapeHtml(item.hora_fin)}</p>
            `).join("")}
          </div>
        </details>
        <a class="btn btn-small btn-primary" href="${escapeHtml(next.enlace_inscripcion)}" target="_blank" rel="noopener noreferrer">Inscribirme por WhatsApp</a>
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
      body.insertAdjacentHTML("beforeend", compactSchedule(items, course));
      card.dataset.courseScheduleCardReady = "true";
    });
  }

  function timeBucket(time) {
    const hour = Number(String(time).slice(0, 2));
    if (hour < 12) return "Mañana";
    if (hour < 18) return "Tarde";
    return "Noche";
  }

  function optionList(values, labelAll, formatter = (value) => value) {
    return `<option value="">${escapeHtml(labelAll)}</option>${values
      .map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(formatter(value))}</option>`)
      .join("")}`;
  }

  function unique(values) {
    return [...new Set(values.filter(Boolean))].sort((a, b) => String(a).localeCompare(String(b), "es"));
  }

  function annualControls() {
    const periods = state.metadata.periodos_disponibles;
    const categories = unique(state.courses.map((course) => course.categoria));
    const days = unique(state.convocations.map((item) => item.dias_clase));
    const modalities = unique(state.convocations.map((item) => item.modalidad));
    const statuses = unique(state.convocations.map((item) => item.estado));
    return `
      <div class="annual-schedule-controls" data-annual-controls>
        <label><span>Mes</span><select data-annual-filter="periodo">${periods.map((period) => `<option value="${period}">${escapeHtml(periodLabel(period))}</option>`).join("")}<option value="">Todos los meses</option></select></label>
        <label><span>Curso</span><input type="search" data-annual-search placeholder="Nombre del curso"></label>
        <label><span>Categoría</span><select data-annual-filter="categoria">${optionList(categories, "Todas")}</select></label>
        <label><span>Día</span><select data-annual-filter="dias">${optionList(days, "Todos")}</select></label>
        <label><span>Modalidad</span><select data-annual-filter="modalidad">${optionList(modalities, "Todas")}</select></label>
        <label><span>Estado</span><select data-annual-filter="estado">${optionList(statuses, "Todos")}</select></label>
        <label><span>Rango horario</span><select data-annual-filter="horario">${optionList(["Mañana", "Tarde", "Noche"], "Todos")}</select></label>
      </div>`;
  }

  function annualFiltered(root) {
    const controls = root.querySelector("[data-annual-controls]");
    const values = Object.fromEntries(
      [...controls.querySelectorAll("[data-annual-filter]")].map((element) => [element.dataset.annualFilter, element.value])
    );
    const search = normalize(controls.querySelector("[data-annual-search]").value);
    return state.convocations.filter((item) => {
      const course = state.courseMap.get(item.curso_id);
      if (!course) return false;
      if (values.periodo && item.periodo !== values.periodo) return false;
      if (values.categoria && course.categoria !== values.categoria) return false;
      if (values.dias && item.dias_clase !== values.dias) return false;
      if (values.modalidad && item.modalidad !== values.modalidad) return false;
      if (values.estado && item.estado !== values.estado) return false;
      if (values.horario && timeBucket(item.hora_inicio) !== values.horario) return false;
      return !search || normalize(`${course.nombre} ${course.categoria}`).includes(search);
    });
  }

  function updateAnnual(root) {
    const results = root.querySelector("[data-annual-results]");
    const count = root.querySelector("[data-annual-count]");
    const items = annualFiltered(root);
    count.textContent = `${items.length} convocatoria${items.length === 1 ? "" : "s"}`;
    results.innerHTML = items.length
      ? items.map((item) => convocationCard(item, state.courseMap.get(item.curso_id), { detailLink: true })).join("")
      : `<article class="detail-block"><h2>Sin resultados</h2><p>Ajusta los filtros o consulta por WhatsApp.</p></article>`;
  }

  async function renderAnnual(root) {
    await load();
    if (!root || root.dataset.annualScheduleReady === "true") return;
    root.innerHTML = `
      ${annualControls()}
      <div class="annual-schedule-summary">
        <strong data-annual-count></strong>
        <span>${state.courses.length} cursos · ${state.metadata.periodos_disponibles.length} meses · Hora de Lima UTC-05:00</span>
      </div>
      <div class="schedule-month-grid annual-schedule-grid" data-annual-results></div>
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

  window.TWCursoSchedule = {
    load,
    initAll,
    renderDetail,
    renderAnnual,
    enhanceCards
  };

  document.addEventListener("DOMContentLoaded", () => {
    initAll().catch((error) => {
      document.querySelectorAll("[data-course-schedule], [data-annual-schedule]").forEach((root) => {
        root.innerHTML = `<article class="detail-block"><h2>Cronograma temporalmente no disponible</h2><p>${escapeHtml(error.message)}</p></article>`;
      });
    });
  });
})();
