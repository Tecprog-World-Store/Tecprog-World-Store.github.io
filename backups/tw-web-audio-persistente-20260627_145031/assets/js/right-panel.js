function ensureThreeColumnShell(main) {
  let shell = main.querySelector(":scope > .page-shell-three-columns");
  if (shell) return shell;

  const toggle = main.querySelector(":scope > .side-index-toggle, :scope > .side-nav-toggle");
  const sideNav = main.querySelector(":scope > .side-nav");
  const panel = main.querySelector(":scope > .side-panel-right");
  const pageMain = document.createElement("div");
  pageMain.className = "page-main";
  shell = document.createElement("div");
  shell.className = "page-shell page-shell-three-columns";

  const children = [...main.children];
  children.forEach((child) => {
    if (child === toggle) return;
    if (child === sideNav || child === panel) return;
    pageMain.appendChild(child);
  });

  if (toggle) toggle.after(shell);
  else main.appendChild(shell);
  if (sideNav) shell.appendChild(sideNav);
  shell.appendChild(pageMain);
  if (panel) shell.appendChild(panel);
  return shell;
}

function renderRightPanel() {
  document.querySelectorAll(".with-side-nav").forEach((main) => {
    const shell = ensureThreeColumnShell(main);
    if (shell.querySelector(".side-panel-right")) return;
    const panel = document.createElement("aside");
    panel.className = "side-panel-right";
    panel.setAttribute("aria-label", "Recursos rapidos");
    panel.innerHTML = `
      <article class="quick-panel-card">
        <h2>Acciones rapidas</h2>
        <div class="quick-link-grid">
          <a href="${twWhatsappHref("Hola, deseo cotizar un proyecto con Tecprog World E.I.R.L.")}">WhatsApp</a>
          <a href="mailto:${TW_OFFICIAL.email}">Enviar correo</a>
          <button type="button" data-copy-current>Copiar enlace</button>
          <button type="button" data-share-current>Compartir pagina</button>
          <button type="button" data-audio-focus>Música ambiental</button>
          <a href="${twWhatsappHref("Hola, deseo cotizar un proyecto con Tecprog World E.I.R.L.")}">Cotizar proyecto</a>
          <a href="${twPath("catalogo/tw-interactive.html")}">Servicios de ingenieria</a>
        </div>
      </article>
      <article class="quick-panel-card">
        <h2>Recursos destacados</h2>
        <div class="quick-link-grid">
          <a href="${twPath("catalogo/catalogo-general-tw-educa.html")}">Catalogo general TW Educa</a>
          <a href="${twPath("catalogo/tw-salud.html")}">Catalogo TW Salud</a>
          <a href="${twPath("catalogo/tw-innova.html")}">Catalogo TW Innova</a>
          <a href="${twPath("catalogo/tw-interactive.html")}">Catalogo TW Interactive</a>
          <a href="${twPath("catalogo/tw-inox.html")}">Catalogo TW Inox</a>
          <a href="${twPath("catalogo/tw-construye.html")}">Catalogo TW Construye</a>
          <a href="${twPath("store/index.html")}">TW Store tecnologia</a>
          <a href="${twPath("catalogo/catalogo-general-tw-educa-pdf.html")}">Catalogo mensual PDF</a>
          <a href="${twPath("catalogo/guias.html")}">Guias tecnicas</a>
          <a href="${twPath("catalogo/descargas.html")}">Zona de Descargas</a>
          <a href="${twPath("lineas/tw-innova.html#opensource")}">Software open-source</a>
          <a href="${twPath("catalogo/compendios.html")}">Compendios y libros</a>
          <a href="${twPath("catalogo/catalogo-mensual.html")}">Catalogo mensual</a>
          <a href="${twPath("catalogo/cursos-junio-2026.html")}">Cursos vigentes</a>
          <a href="${twPath("pagos/peru.html")}">Pagos Peru</a>
          <a href="${twPath("pagos/internacionales.html")}">Pagos Internacionales</a>
          <a href="${twPath("empresa/mapa-del-sitio.html")}">Mapa del sitio</a>
        </div>
      </article>
      <article class="quick-panel-card">
        <h2>Siguenos</h2>
        <div class="quick-link-grid">
          <a href="https://www.facebook.com/tecprogworld">Facebook</a>
          <a href="https://www.tiktok.com/@tecprogworld">TikTok</a>
          <a href="https://www.youtube.com/@tecprogworld">YouTube</a>
          <a href="https://www.linkedin.com/company/tecprog-world">LinkedIn</a>
        </div>
      </article>
      <article class="quick-panel-card">
        <h2>Video destacado</h2>
        <a class="video-thumb-link" href="https://www.youtube.com/watch?v=WyYhiA8Djyg&t=135s">
          <img src="https://img.youtube.com/vi/WyYhiA8Djyg/hqdefault.jpg" alt="Entrevista institucional de Tecprog World" loading="lazy">
        </a>
        <p>Conoce la historia y vision de Tecprog World.</p>
      </article>
      <article class="quick-panel-card">
        <h2>Compartir</h2>
        <div class="quick-link-grid">
          <a href="https://wa.me/?text=${encodeURIComponent(location.href)}">WhatsApp</a>
          <a href="https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(location.href)}">Facebook</a>
          <a href="https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(location.href)}">LinkedIn</a>
        </div>
      </article>
    `;
    shell.appendChild(panel);
  });
}

function setupRightPanelActions() {
  document.addEventListener("click", async (event) => {
    const copy = event.target.closest("[data-copy-current]");
    if (copy) {
      await navigator.clipboard.writeText(location.href);
      copy.textContent = "Enlace copiado";
    }
    const share = event.target.closest("[data-share-current]");
    if (share) {
      if (navigator.share) {
        await navigator.share({ title: document.title, url: location.href });
      } else {
        await navigator.clipboard.writeText(location.href);
        share.textContent = "Enlace copiado";
      }
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderRightPanel();
  setupRightPanelActions();
  twExternalAttrs();
});
