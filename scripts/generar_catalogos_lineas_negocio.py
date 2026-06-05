from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "tw-salud": {
        "txt": "catalogo_base_tw_salud.txt",
        "json": "catalogo-tw-salud.json",
        "public_name": "TW Salud",
        "image": "assets/img/servicios/protesis_y_ortesis/TW_Salud_prtesis_manos.jpg",
        "legal": "Servicios de diseno, prototipado, investigacion aplicada y soporte tecnico. No sustituyen evaluacion clinica, indicacion medica ni validacion por profesionales competentes cuando corresponda.",
    },
    "tw-innova": {
        "txt": "catalogo_base_tw_innova.txt",
        "json": "catalogo-tw-innova.json",
        "public_name": "TW Innova",
        "image": "assets/img/software/software-open-source-tools.svg",
        "legal": "Servicios tecnologicos sujetos a diagnostico y alcance. No se realizan acciones que anulen garantias, comprometan seguridad electrica o impliquen manipulacion peligrosa sin habilitacion tecnica.",
    },
    "tw-inox": {
        "txt": "catalogo_base_tw_inox.txt",
        "json": "catalogo-tw-inox.json",
        "public_name": "TW Inox",
        "image": "assets/img/banners/card-pattern.svg",
        "legal": "Servicios coordinados con tecnicos, soldadores o talleres competentes segun alcance, ubicacion y requerimientos del proyecto.",
    },
    "tw-construye": {
        "txt": "catalogo_base_tw_construye.txt",
        "json": "catalogo-tw-construye.json",
        "public_name": "TW Construye",
        "image": "assets/img/servicios/servicio-implementacion-tecnologica.svg",
        "legal": "Servicios de asistencia tecnica y documentacion. Cuando se requiera firma, licencia, colegiatura o responsabilidad formal, se coordina con profesionales habilitados.",
    },
}


def parse_price(value: str) -> int:
    digits = "".join(ch for ch in value if ch.isdigit())
    return int(digits) if digits else 0


def parse_source(path: Path, slug: str, config: dict) -> list[dict]:
    rows = []
    header_seen = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "|" not in line:
            continue
        parts = [part.strip() for part in line.split("|")]
        if parts[0] == "id":
            header_seen = True
            continue
        if not header_seen or len(parts) < 12:
            continue
        (
            offer_id,
            line_name,
            category,
            offer,
            offer_type,
            maturity,
            audience,
            deliverables,
            price_pen,
            price_usd,
            priority,
            short_description,
        ) = parts[:12]
        rows.append(
            {
                "id": offer_id,
                "linea_slug": slug,
                "linea": config["public_name"],
                "categoria": category,
                "oferta": offer,
                "tipo": offer_type,
                "madurez": maturity,
                "publico_objetivo": [item.strip() for item in audience.split(",") if item.strip()],
                "entregables": [item.strip() for item in deliverables.split(",") if item.strip()],
                "precio_desde_soles_igv": parse_price(price_pen),
                "precio_internacional_usd": parse_price(price_usd),
                "precio_soles_texto": f"Desde S/ {parse_price(price_pen)}",
                "precio_usd_texto": f"Desde USD {parse_price(price_usd)}",
                "prioridad": priority,
                "descripcion_corta": short_description,
                "descripcion_larga": (
                    f"{offer} es una oferta de {config['public_name']} orientada a {audience}. "
                    f"Se entrega mediante un alcance coordinado que puede incluir {deliverables}. "
                    "La disponibilidad, tiempos, condiciones tecnicas y precio final se confirman por cotizacion."
                ),
                "incluye": [
                    "Revision inicial del requerimiento y alcance.",
                    "Coordinacion por WhatsApp o correo institucional.",
                    "Documentacion o entregable acordado segun propuesta.",
                ],
                "condiciones": [
                    config["legal"],
                    "Precios referenciales. El precio final depende del alcance, ubicacion, materiales, modalidad, urgencia y validacion tecnica.",
                    "No se afirma representacion oficial, certificacion externa ni alianza con marcas o instituciones mencionadas.",
                ],
                "imagen": config["image"],
                "url_detalle": f"detalle/oferta.html?id={offer_id}&linea={slug}",
                "whatsapp_message": f"Hola, deseo cotizar {offer} de {config['public_name']}.",
            }
        )
    return rows


def main() -> int:
    for slug, config in SOURCES.items():
        src = ROOT / "data" / "fuentes" / config["txt"]
        if not src.exists():
            raise FileNotFoundError(src)
        data = parse_source(src, slug, config)
        out = ROOT / "data" / config["json"]
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{out}: {len(data)} ofertas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
