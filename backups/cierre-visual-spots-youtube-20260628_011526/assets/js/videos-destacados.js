(function () {
  const DATA_URL = "data/videos_destacados.json?v=videos-20260628";
  const PLAYER_ORIGIN = "https://www.youtube.com";
  const modalId = "video-showcase-modal";
  let videosCache = null;
  let modal = null;
  let lastTrigger = null;

  const normalizeBase = () => {
    const path = window.location.pathname;
    if (path.includes("/catalogo/cursos/")) return "../../";
    if (path.includes("/catalogo/") || path.includes("/innova/") || path.includes("/educa/") || path.includes("/servicios/") || path.includes("/empresa/")) return "../";
    return "";
  };

  const basePath = normalizeBase();
  const toAsset = (path) => {
    if (!path || /^https?:\/\//.test(path) || path.startsWith("/")) return path;
    return `${basePath}${path}`;
  };

  const escapeHtml = (value) =>
    String(value || "").replace(/[&<>"']/g, (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    })[char]);

  const fetchVideos = async () => {
    if (videosCache) return videosCache;
    const response = await fetch(toAsset(DATA_URL), { cache: "no-store" });
    if (!response.ok) throw new Error(`No se pudo cargar videos destacados: ${response.status}`);
    videosCache = await response.json();
    return videosCache;
  };

  const createModal = () => {
    if (modal) return modal;
    modal = document.createElement("div");
    modal.className = "video-modal";
    modal.id = modalId;
    modal.hidden = true;
    modal.innerHTML = `
      <div class="video-modal__backdrop" data-video-close></div>
      <div class="video-modal__dialog" role="dialog" aria-modal="true" aria-labelledby="video-modal-title">
        <button class="video-modal__close" type="button" data-video-close aria-label="Cerrar video">&times;</button>
        <div class="video-responsive-frame" data-video-frame></div>
        <div class="video-modal__body">
          <p class="eyebrow" data-video-line></p>
          <h2 id="video-modal-title" data-video-title></h2>
          <p data-video-description></p>
          <p class="video-modal__note">La disponibilidad, precios y alcance se confirman por el canal comercial de Tecprog World.</p>
        </div>
      </div>`;
    document.body.appendChild(modal);
    modal.addEventListener("click", (event) => {
      if (event.target.closest("[data-video-close]")) closeModal();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && modal && !modal.hidden) closeModal();
    });
    return modal;
  };

  const openModal = (video, trigger) => {
    lastTrigger = trigger;
    const activeModal = createModal();
    activeModal.querySelector("[data-video-line]").textContent = `${video.linea} - ${video.categoria}`;
    activeModal.querySelector("[data-video-title]").textContent = video.titulo;
    activeModal.querySelector("[data-video-description]").textContent = video.subtitulo;
    activeModal.querySelector("[data-video-frame]").innerHTML = `
      <iframe
        title="${escapeHtml(video.titulo)}"
        src="${PLAYER_ORIGIN}/embed/${encodeURIComponent(video.youtubeId)}"
        allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy"></iframe>`;
    activeModal.hidden = false;
    document.body.classList.add("video-modal-open");
    activeModal.querySelector("[data-video-close]").focus();
  };

  const closeModal = () => {
    if (!modal) return;
    modal.querySelector("[data-video-frame]").innerHTML = "";
    modal.hidden = true;
    document.body.classList.remove("video-modal-open");
    if (lastTrigger) lastTrigger.focus();
  };

  const renderCard = (video) => {
    const article = document.createElement("article");
    article.className = "video-card";
    article.innerHTML = `
      <button class="video-card__media" type="button" aria-label="${escapeHtml(video.cta)}: ${escapeHtml(video.titulo)}">
        <img src="${escapeHtml(toAsset(video.thumbnail))}" alt="${escapeHtml(video.alt)}" loading="lazy">
        <span class="video-card__play" aria-hidden="true">&#9658;</span>
      </button>
      <div class="video-card__body">
        <p class="video-card__meta">${escapeHtml(video.linea)} - ${escapeHtml(video.categoria)}</p>
        <h3>${escapeHtml(video.titulo)}</h3>
        <p>${escapeHtml(video.subtitulo)}</p>
        <div class="video-card__actions">
          <button class="btn btn-small btn-primary" type="button">${escapeHtml(video.cta)}</button>
          ${video.secondaryUrl ? `<a class="btn btn-small" href="${escapeHtml(video.secondaryUrl)}">${escapeHtml(video.secondaryCta || "Consultar")}</a>` : ""}
        </div>
      </div>`;
    article.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => openModal(video, button));
    });
    return article;
  };

  const renderShowcase = (container, videos) => {
    const section = container.dataset.videosSection;
    const matches = videos.filter((video) => Array.isArray(video.secciones) && video.secciones.includes(section));
    if (!matches.length) {
      container.hidden = true;
      return;
    }

    container.classList.add("video-showcase");
    container.innerHTML = `
      <div class="section-shell">
        <div class="section-heading">
          <p class="eyebrow">Spots destacados</p>
          <h2>Videos destacados</h2>
          <p>Material comercial de Tecprog World para revisar cursos, servicios y soluciones antes de consultar disponibilidad.</p>
        </div>
        <div class="video-showcase-grid"></div>
      </div>`;

    const grid = container.querySelector(".video-showcase-grid");
    matches.forEach((video) => grid.appendChild(renderCard(video)));
  };

  const init = async () => {
    const containers = Array.from(document.querySelectorAll("[data-videos-section]"));
    if (!containers.length) return;
    try {
      const videos = await fetchVideos();
      containers.forEach((container) => renderShowcase(container, videos));
    } catch (error) {
      console.error(error);
      containers.forEach((container) => {
        container.hidden = true;
      });
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
