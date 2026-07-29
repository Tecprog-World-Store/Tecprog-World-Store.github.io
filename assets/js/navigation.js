const TW_OFFICIAL = {
  whatsapp: "51952354282",
  email: "grupotecprog@gmail.com",
  web: "https://tecprog-world-store.github.io",
  ruc: "20608743252",
  address: "Mz. C Lote. 43 Urb. Los Nisperos, San Martin de Porres, Lima, Peru",
  maps: "https://maps.app.goo.gl/NVBub1HAjNhARpsTA"
};

window.TW_OFFICIAL = TW_OFFICIAL;

function twPath(path) {
  return `/${String(path || "").replace(/^\/+/, "")}`;
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

function twAppContentTarget() {
  return document.querySelector("#app-content, [data-app-content], .page-main");
}

function twShouldBypassProgressiveNavigation(link, event) {
  if (!link || event.defaultPrevented) return true;
  if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return true;
  if (link.target && link.target !== "_self") return true;
  if (link.hasAttribute("download") || link.dataset.noSpa === "true") return true;

  const rawHref = link.getAttribute("href") || "";
  if (!rawHref || rawHref.startsWith("#")) return true;
  if (/^(mailto:|tel:|sms:|whatsapp:|javascript:)/i.test(rawHref)) return true;

  const url = new URL(rawHref, location.href);
  if (url.origin !== location.origin) return true;
  if (url.pathname === location.pathname && url.search === location.search && url.hash) return true;
  if (/\.(pdf|mp3|wav|ogg|zip|rar|7z|png|jpe?g|webp|svg|gif|json|xml|txt|docx?|xlsx?|pptx?)$/i.test(url.pathname)) return true;
  return false;
}

function twRewriteProgressiveUrls(root, url) {
  root.querySelectorAll("a[href], img[src], source[src], video[poster]").forEach((node) => {
    ["href", "src", "poster"].forEach((attr) => {
      const value = node.getAttribute(attr);
      if (!value || value.startsWith("#") || /^(https?:|mailto:|tel:|sms:|whatsapp:|javascript:|data:)/i.test(value)) return;
      node.setAttribute(attr, new URL(value, url.href).pathname + new URL(value, url.href).search + new URL(value, url.href).hash);
    });
  });
}

function twExtractProgressiveContent(doc, url) {
  const sourceMain = doc.querySelector("main");
  if (!sourceMain) return null;

  if (sourceMain.matches("[data-detail-root]")) return `<div data-detail-root></div>`;
  if (sourceMain.matches("[data-compendio-detail]")) return `<div data-compendio-detail></div>`;
  if (sourceMain.matches("[data-guia-detail]")) return `<div data-guia-detail></div>`;

  const nestedPageMain = sourceMain.querySelector(".page-main");
  if (nestedPageMain) {
    const nestedClone = nestedPageMain.cloneNode(true);
    twRewriteProgressiveUrls(nestedClone, url);
    return nestedClone.innerHTML;
  }

  const clone = sourceMain.cloneNode(true);
  const shellPageMain = clone.querySelector(".page-main");
  twRewriteProgressiveUrls(shellPageMain || clone, url);
  return shellPageMain ? shellPageMain.innerHTML : clone.innerHTML;
}

function twUpdateHeadFromDocument(doc, url) {
  const incomingTitle = doc.querySelector("title")?.textContent;
  if (incomingTitle) document.title = incomingTitle;

  const description = doc.querySelector('meta[name="description"]')?.getAttribute("content");
  let currentDescription = document.querySelector('meta[name="description"]');
  if (description) {
    if (!currentDescription) {
      currentDescription = document.createElement("meta");
      currentDescription.name = "description";
      document.head.appendChild(currentDescription);
    }
    currentDescription.setAttribute("content", description);
  }

  const canonical = doc.querySelector('link[rel="canonical"]')?.getAttribute("href") || url.href;
  let currentCanonical = document.querySelector('link[rel="canonical"]');
  if (!currentCanonical) {
    currentCanonical = document.createElement("link");
    currentCanonical.rel = "canonical";
    document.head.appendChild(currentCanonical);
  }
  currentCanonical.setAttribute("href", canonical);
}

async function twLoadPageScripts(doc, url) {
  const scripts = [...doc.querySelectorAll("script[src]")];
  const persistentShellScripts = new Set([
    "/assets/js/catalogo-global.js",
    "/assets/js/navigation.js",
    "/assets/js/main.js"
  ]);
  for (const script of scripts) {
    const src = new URL(script.getAttribute("src"), url.href);
    if (persistentShellScripts.has(src.pathname)) continue;
    const alreadyLoaded = [...document.scripts].some((existing) => {
      if (!existing.src) return false;
      const existingUrl = new URL(existing.src, location.href);
      return existingUrl.pathname === src.pathname;
    });
    if (alreadyLoaded) continue;
    await new Promise((resolve, reject) => {
      const dynamicScript = document.createElement("script");
      dynamicScript.src = src.href;
      dynamicScript.onload = resolve;
      dynamicScript.onerror = reject;
      document.body.appendChild(dynamicScript);
    });
  }
}

async function twRehydrateProgressiveContent() {
  try {
    if (typeof renderStandardTopNav === "function") renderStandardTopNav();
    if (typeof setupTopNavigation === "function") setupTopNavigation();
    if (typeof twExternalAttrs === "function") twExternalAttrs();
    if (typeof setupPayPalButtons === "function") setupPayPalButtons();
    if (typeof setupWhatsAppLinks === "function") setupWhatsAppLinks();
    if (typeof setupExternalLinks === "function") setupExternalLinks();
    if (typeof setupContextNav === "function") setupContextNav();
    if (typeof renderBusinessLines === "function") renderBusinessLines();
    if (typeof setupCommerceCarousels === "function") setupCommerceCarousels();
    if (window.TWCatalogoGlobal?.init) await window.TWCatalogoGlobal.init();
    if (typeof renderCatalogGeneral === "function") await renderCatalogGeneral();
    if (typeof renderCompendiosCatalog === "function") await renderCompendiosCatalog();
    if (typeof renderCompendioDetail === "function") await renderCompendioDetail();
    if (typeof renderGuiasCatalog === "function") await renderGuiasCatalog();
    if (typeof renderGuiaDetail === "function") await renderGuiaDetail();
    if (typeof renderDetail === "function") await renderDetail();
    if (typeof renderCommercialLocationSection === "function") renderCommercialLocationSection();
    if (typeof observeReveals === "function") observeReveals();
  } catch (error) {
    console.warn("La navegación progresiva cargó la página, pero un módulo no pudo rehidratarse.", error);
  }
}

async function twNavigateProgressively(url, options = {}) {
  const target = twAppContentTarget();
  if (!target) {
    location.href = url.href;
    return;
  }

  let response;
  try {
    response = await fetch(url.href, { credentials: "same-origin" });
  } catch {
    location.href = url.href;
    return;
  }
  if (!response.ok) {
    location.href = url.href;
    return;
  }

  const html = await response.text();
  const doc = new DOMParser().parseFromString(html, "text/html");
  const nextContent = twExtractProgressiveContent(doc, url);
  if (!nextContent?.trim()) {
    location.href = url.href;
    return;
  }

  if (options.push !== false) history.pushState({ twProgressive: true }, "", url.href);
  twUpdateHeadFromDocument(doc, url);
  target.innerHTML = nextContent;
  await twLoadPageScripts(doc, url);
  await twRehydrateProgressiveContent();

  if (url.hash) {
    document.querySelector(url.hash)?.scrollIntoView({ behavior: "smooth", block: "start" });
  } else {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
}

function setupProgressiveNavigation() {
  const persistentAudio = document.querySelector("[data-audio-widget]");
  const target = twAppContentTarget();
  if (!persistentAudio || !target || window.__twProgressiveNavigationReady) return;
  window.__twProgressiveNavigationReady = true;

  document.addEventListener("click", (event) => {
    const link = event.target.closest("a[href]");
    if (twShouldBypassProgressiveNavigation(link, event)) return;
    const url = new URL(link.getAttribute("href"), location.href);
    event.preventDefault();
    twNavigateProgressively(url).catch(() => {
      location.href = url.href;
    });
  });

  window.addEventListener("popstate", () => {
    twNavigateProgressively(new URL(location.href), { push: false }).catch(() => {
      location.reload();
    });
  });
}

function twWhatsappHref(text = "Hola, deseo informacion desde la web de Tecprog World E.I.R.L.") {
  return `https://wa.me/${TW_OFFICIAL.whatsapp}?text=${encodeURIComponent(text)}`;
}

function renderStandardTopNav() {
  document.querySelectorAll(".site-nav").forEach((nav) => {
    if (nav.dataset.skipStandardNav === "true") return;
    nav.classList.remove("is-static");
    nav.id ||= "site-nav";
    nav.setAttribute("data-nav", "");
    nav.innerHTML = `
      <a href="${twPath("index.html")}#inicio">Inicio</a>
      <a href="${twPath("store/index.html")}">TW Store</a>
      <a href="${twPath("disfruta/index.html")}">TW Disfruta</a>
      <a href="${twPath("educa/index.html")}">TW Educa</a>
      <a href="${twPath("innova/index.html")}">TW Innova</a>
      <a href="${twPath("salud/index.html")}">TW Salud</a>
      <a href="${twPath("interactive/index.html")}">TW Interactive</a>
      <a href="${twPath("construye/index.html")}">TW Construye</a>
      <a href="${twPath("inox/index.html")}">TW Inox</a>
      <a href="${twPath("investiga/index.html")}">TW Investiga</a>
      <a href="${twPath("empresa/nosotros.html")}">Empresa</a>
      <a href="${twPath("pagos/peru.html")}">Pagos Perú</a>
      <a href="${twPath("pagos/internacionales.html")}">Pagos Internacionales</a>
    `;
    nav.querySelectorAll("a").forEach((link) => {
      const target = new URL(link.href, location.href);
      const active = target.pathname === location.pathname ||
        (location.pathname === "/" && target.pathname === "/index.html");
      link.classList.toggle("is-active", active);
      if (active) link.setAttribute("aria-current", "page");
    });
  });
}

function setupTopNavigation() {
  document.querySelectorAll(".site-header").forEach((header) => {
    const nav = header.querySelector(".site-nav");
    if (!nav) return;
    let toggle = header.querySelector("[data-nav-toggle]");
    if (!toggle) {
      toggle = document.createElement("button");
      toggle.className = "nav-toggle";
      toggle.type = "button";
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-controls", nav.id || "site-nav");
      toggle.setAttribute("aria-label", "Abrir menu principal");
      toggle.setAttribute("data-nav-toggle", "");
      toggle.innerHTML = '<span></span><span></span><span></span><span class="sr-only">Abrir menu</span>';
      nav.before(toggle);
    }
    if (toggle.dataset.navReady === "true") return;
    toggle.dataset.navReady = "true";
    toggle.addEventListener("click", () => {
      const isOpen = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(isOpen));
    });
    nav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
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

function renderCommercialLocationSection() {
  if (document.body?.dataset.disableCommercialLocation === "true") return;
  const main = document.querySelector("main.central-page, main");
  if (!main) return;

  const target = main.querySelector(".page-main") || main;
  target.querySelector(".location-section")?.remove();

  const section = document.createElement("section");
  section.id = "ubicacion-comercial";
  section.className = "location-section section section-anchor reveal";
  section.setAttribute("aria-labelledby", "ubicacion-comercial-title");
  section.innerHTML = `
    <div class="section-shell location-card">
      <div class="location-copy">
        <p class="eyebrow">Ubicaci&oacute;n empresarial</p>
        <h2 id="ubicacion-comercial-title">Ubicaci&oacute;n y atenci&oacute;n comercial</h2>
        <p class="location-subtitle">Tecprog World E.I.R.L. atiende solicitudes comerciales, cotizaciones y coordinaci&oacute;n de servicios mediante canales digitales.</p>
        <p>Encu&eacute;ntranos en Google Maps como <strong>Tecprog World E.I.R.L.</strong></p>
        <p class="location-note">La atenci&oacute;n comercial, disponibilidad y coordinaci&oacute;n se confirman previamente por WhatsApp.</p>
        <div class="location-actions">
          <a class="btn btn-primary" href="${TW_OFFICIAL.maps}" target="_blank" rel="noopener noreferrer">Ver ubicaci&oacute;n en Google Maps</a>
          <a class="btn btn-gold" href="${twWhatsappHref("Hola, deseo consultar la ubicacion y atencion comercial de Tecprog World E.I.R.L.")}" target="_blank" rel="noopener noreferrer">Consultar por WhatsApp</a>
        </div>
      </div>
      <div class="location-map-placeholder" aria-label="Referencia de ubicaci&oacute;n comercial de Tecprog World E.I.R.L.">
        <!-- Si se obtiene un iframe oficial de Google Maps, reemplazar este placeholder por el embed validado. -->
        <div class="location-pin" aria-hidden="true">
          <svg viewBox="0 0 32 32" focusable="false"><path d="M16 2.8c-5.1 0-9.2 4.1-9.2 9.2 0 6.9 9.2 17.2 9.2 17.2S25.2 18.9 25.2 12c0-5.1-4.1-9.2-9.2-9.2Zm0 12.7a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z"/></svg>
        </div>
        <span class="location-map-label">Tecprog World E.I.R.L.</span>
        <p>Referencia comercial en Google Maps</p>
        <a class="btn btn-secondary" href="${TW_OFFICIAL.maps}" target="_blank" rel="noopener noreferrer">Abrir en Google Maps</a>
      </div>
    </div>
  `;
  target.appendChild(section);
  twExternalAttrs();
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
          <a href="https://www.facebook.com/twbionic/">Facebook TW Salud</a>
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
        <a href="${twPath("catalogo/tw-salud.html")}">Catalogo TW Salud</a>
        <a href="${twPath("catalogo/tw-innova.html")}">Catalogo TW Innova</a>
        <a href="${twPath("catalogo/tw-interactive.html")}">Catalogo TW Interactive</a>
        <a href="${twPath("catalogo/tw-inox.html")}">Catalogo TW Inox</a>
        <a href="${twPath("catalogo/tw-construye.html")}">Catalogo TW Construye</a>
        <a href="${twPath("store/index.html")}">TW Store tecnologia</a>
        <a href="${twPath("assets/pdf/catalogos/catalogo-lineas-negocio-tecprog-world-2026-06.pdf")}">PDF lineas de negocio</a>
        <a href="${twPath("catalogo/catalogo-mensual.html")}">Catalogo mensual</a>
        <a href="${twPath("pagos/peru.html")}">Pagos Perú</a>
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
  window.TWProgressiveNavigate = twNavigateProgressively;
  renderStandardTopNav();
  setupTopNavigation();
  renderFloatingWhatsApp();
  renderCommercialLocationSection();
  renderInstitutionalFooter();
  setupPayPalButtons();
  twExternalAttrs();
  window.setTimeout(setupProgressiveNavigation, 0);
});
