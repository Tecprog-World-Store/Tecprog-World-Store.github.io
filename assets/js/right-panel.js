function renderRightPanel() {
  document.querySelectorAll(".with-side-nav").forEach((shell) => {
    if (shell.querySelector(".side-panel-right")) return;
    const panel = document.createElement("aside");
    panel.className = "side-panel-right";
    panel.setAttribute("aria-label", "Recursos rápidos");
    panel.innerHTML = `
      <article class="quick-panel-card">
        <h2>Acciones rápidas</h2>
        <div class="quick-link-grid">
          <a href="${twWhatsappHref("Hola, deseo cotizar un proyecto con Tecprog World E.I.R.L.")}">WhatsApp</a>
          <a href="mailto:${TW_OFFICIAL.email}">Enviar correo</a>
          <button type="button" data-copy-current>Copiar enlace</button>
          <button type="button" data-share-current>Compartir página</button>
        </div>
      </article>
      <article class="quick-panel-card">
        <h2>Recursos destacados</h2>
        <div class="quick-link-grid">
          <a href="${twPath("catalogo/descargas.html")}">Zona de Descargas</a>
          <a href="${twPath("catalogo/compendios.html")}">Libros y guías técnicas</a>
          <a href="${twPath("catalogo/cursos-junio-2026.html")}">Cursos vigentes</a>
          <a href="${twPath("lineas/tw-innova.html#opensource")}">Software open-source</a>
          <a href="${twPath("legal/libro-reclamaciones.html")}">Libro de Reclamaciones</a>
          <a href="${twPath("empresa/mapa-del-sitio.html")}">Mapa del sitio</a>
        </div>
      </article>
      <article class="quick-panel-card">
        <h2>Síguenos</h2>
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
        <p>Conoce la historia y visión de Tecprog World.</p>
        <div class="quick-link-grid"><a href="https://www.youtube.com/watch?v=WyYhiA8Djyg&t=135s">Ver entrevista</a></div>
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
