document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-store-whatsapp]").forEach((link) => {
    const topic = link.dataset.storeWhatsapp || "catálogo TW Store";
    link.href = `https://wa.me/51952354282?text=${encodeURIComponent(`Hola Tecprog World, deseo cotizar ${topic}.`)}`;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
  });
});
