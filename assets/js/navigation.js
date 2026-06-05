const TW_OFFICIAL = {
  whatsapp: "51952354282",
  email: "grupotecprog@gmail.com",
  web: "https://tecprog-world-store.github.io",
  ruc: "20608743252",
  address: "Mz. C Lote. 43 Urb. Los Nisperos, San Martin de Porres, Lima, Peru",
  maps: "https://www.google.com/maps/search/?api=1&query=Mz.%20C%20Lote.%2043%20Urb.%20Los%20Nisperos%20San%20Martin%20de%20Porres%20Lima%20Peru"
};

window.TW_OFFICIAL = TW_OFFICIAL;

function twPath(path) {
  const depth = location.pathname.split("/").filter(Boolean).length - 1;
  const prefix = depth > 0 ? "../".repeat(depth) : "";
  return `${prefix}${path}`;
}

function twExternalAttrs() {
  document.querySelectorAll('a[href^="http"], a[href^="https://wa.me"]').forEach((link) => {
    const url = new URL(link.href, location.href);
    if (url.origin !== location.origin) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    }
  });
}

function twWhatsappHref(text = "Hola, deseo informacion desde la web de Tecprog World E.I.R.L.") {
  return `https://wa.me/${TW_OFFICIAL.whatsapp}?text=${encodeURIComponent(text)}`;
}

function renderStandardTopNav() {
  document.querySelectorAll(".site-nav").forEach((nav) => {
    if (nav.dataset.skipStandardNav === "true") return;
    nav.innerHTML = `
      <a href="${twPath("index.html")}#inicio">Inicio</a>
      <a href="${twPath("empresa/nosotros.html")}">Empresa</a>
      <a href="${twPath("lineas/tw-investiga.html")}">TW Investiga</a>
      <a href="${twPath("lineas/tw-innova.html")}">TW Innova</a>
      <a href="${twPath("lineas/tw-educa.html")}">TW Educa</a>
      <a href="${twPath("lineas/tw-construye.html")}">TW Construye</a>
      <a href="${twPath("lineas/tw-inox.html")}">TW Inox</a>
      <a href="${twPath("lineas/tw-protesis-ortesis.html")}">TW Protesis y Ortesis</a>
      <a href="${twPath("pagos/peru.html")}">Pagos Peru</a>
      <a href="${twPath("pagos/internacionales.html")}">Pagos Internacionales</a>
    `;
  });
}

function setupMobileSideIndex() {
  document.querySelectorAll(".with-side-nav > .side-nav").forEach((nav) => {
    if (nav.previousElementSibling?.classList.contains("side-index-toggle")) return;
    const button = document.createElement("button");
    button.className = "side-index-toggle";
    button.type = "button";
    button.textContent = "Indice de esta pagina";
    button.addEventListener("click", () => nav.classList.toggle("is-open"));
    nav.before(button);
  });
}

function renderFloatingWhatsApp() {
  if (document.querySelector(".whatsapp-float")) return;
  const link = document.createElement("a");
  link.className = "whatsapp-float";
  link.href = twWhatsappHref();
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.setAttribute("aria-label", "Contactar por WhatsApp");
  link.innerHTML = `
    <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16.01 3.2A12.66 12.66 0 0 0 5.2 26.43L3.6 31l4.72-1.51A12.67 12.67 0 1 0 16.01 3.2Zm0 2.28a10.38 10.38 0 0 1 8.82 15.85 10.31 10.31 0 0 1-12.5 4.24l-.43-.18-2.74.88.9-2.6-.24-.45A10.38 10.38 0 0 1 16 5.48Zm-4.1 5.39c-.23 0-.6.09-.91.43-.31.34-1.19 1.16-1.19 2.82 0 1.66 1.22 3.27 1.39 3.5.17.22 2.35 3.76 5.82 5.12 2.88.99 3.48.79 4.1.74.63-.06 2.02-.83 2.3-1.62.28-.8.28-1.48.2-1.63-.08-.14-.31-.22-.65-.39-.34-.17-2.02-.99-2.33-1.1-.31-.12-.54-.17-.77.17-.23.34-.88 1.1-1.08 1.33-.2.23-.4.25-.74.09-.34-.17-1.44-.53-2.74-1.69-1.01-.9-1.7-2.02-1.9-2.36-.2-.34-.02-.52.15-.69.15-.15.34-.4.51-.6.17-.2.23-.34.34-.57.11-.23.06-.43-.03-.6-.08-.17-.77-1.85-1.05-2.53-.27-.66-.55-.57-.77-.58l-.66-.01Z"/></svg>
    <span>WhatsApp</span>
  `;
  document.body.appendChild(link);
}

function renderInstitutionalFooter() {
  let footer = document.querySelector(".site-footer");
  if (!footer) {
    footer = document.createElement("footer");
    footer.className = "site-footer";
    document.body.appendChild(footer);
  }
  footer.innerHTML = `
    <div class="section-shell footer-grid">
      <div>
        <div class="footer-logo-row">
          <img class="footer-logo" src="${twPath("assets/img/logos/logo-tecprog-world.png")}" alt="Tecprog World E.I.R.L." width="72" height="72">
          <div><strong>Tecprog World E.I.R.L.</strong><p>RUC: ${TW_OFFICIAL.ruc}</p></div>
        </div>
        <p>Empresa peruana de tecnologia aplicada.</p>
        <p>${TW_OFFICIAL.address}</p>
      </div>
      <div>
        <h2>Contacto</h2>
        <a href="${twWhatsappHref()}">WhatsApp: +51 952 354 282</a>
        <a href="mailto:${TW_OFFICIAL.email}">${TW_OFFICIAL.email}</a>
        <a href="${TW_OFFICIAL.web}">${TW_OFFICIAL.web}</a>
        <a href="${twPath("empresa/contacto.html")}">Contacto</a>
        <a href="${TW_OFFICIAL.maps}">Google Maps</a>
      </div>
      <div>
        <h2>Redes sociales</h2>
        <div class="footer-socials">
          <a href="https://www.facebook.com/tecprogworld">Facebook principal</a>
          <a href="https://www.facebook.com/tecprogworld.educa">Facebook TW Educa</a>
          <a href="https://www.facebook.com/tecprogworld.innova">Facebook TW Innova</a>
          <a href="https://www.facebook.com/tecprogworld.taller">Facebook TW Taller</a>
          <a href="https://www.facebook.com/tecprogworld.construye">Facebook TW Construye</a>
          <a href="https://www.facebook.com/twbionic/">Facebook TW Protesis y Ortesis</a>
          <a href="https://www.tiktok.com/@tecprogworld">TikTok</a>
          <a href="https://www.youtube.com/@tecprogworld">YouTube</a>
          <a href="https://www.linkedin.com/company/tecprog-world">LinkedIn</a>
        </div>
      </div>
      <div>
        <h2>Legales y recursos</h2>
        <a href="${twPath("legal/libro-reclamaciones.html")}">Libro de Reclamaciones</a>
        <a href="${twPath("legal/terminos-condiciones.html")}">Terminos y Condiciones</a>
        <a href="${twPath("legal/politicas-privacidad.html")}">Politicas de Privacidad</a>
        <a href="${twPath("legal/politicas-pagos-reembolsos.html")}">Politicas de Pagos y Reembolsos</a>
        <a href="${twPath("empresa/mapa-del-sitio.html")}">Mapa del sitio</a>
        <a href="${twPath("catalogo/guias.html")}">Guias tecnicas</a>
        <a href="${twPath("catalogo/catalogo-mensual.html")}">Catalogo mensual</a>
        <a href="${twPath("pagos/peru.html")}">Pagos Peru</a>
        <a href="${twPath("pagos/internacionales.html")}">Pagos Internacionales</a>
      </div>
    </div>
  `;
  twExternalAttrs();
}

async function setupPayPalButtons() {
  const buttons = [...document.querySelectorAll("[data-paypal-offer]")];
  if (!buttons.length) return;
  let payments = [];
  try {
    const response = await fetch(twPath("data/pagos.json"));
    payments = response.ok ? await response.json() : [];
  } catch {
    payments = [];
  }
  buttons.forEach((button) => {
    const offer = payments.find((item) => item.id === button.dataset.paypalOffer);
    const name = offer?.nombre || button.dataset.offerName || "Tecprog World E.I.R.L.";
    if (offer?.paypal_link) {
      button.href = offer.paypal_link;
      button.target = "_blank";
      button.rel = "noopener noreferrer";
      button.textContent = button.dataset.paypalLabel || "Pagar con PayPal";
    } else {
      button.href = twWhatsappHref(`Hola, deseo solicitar enlace PayPal para ${name}. Soy cliente internacional.`);
      button.target = "_blank";
      button.rel = "noopener noreferrer";
      button.textContent = button.dataset.paypalFallback || "Solicitar enlace PayPal";
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderStandardTopNav();
  setupMobileSideIndex();
  renderFloatingWhatsApp();
  renderInstitutionalFooter();
  setupPayPalButtons();
  twExternalAttrs();
});
