from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEX_DIR = Path(r"D:\DiskE01\Organizacionies\E-TW\Produccion_LaTeX_TW\catalogos_mensuales\2026-06\catalogo-lineas-negocio")
PDF_NAME = "catalogo-lineas-negocio-tecprog-world-2026-06.pdf"
PUBLIC_PDF = ROOT / "assets" / "pdf" / "catalogos" / PDF_NAME
FILES = {
    "tw_salud.tex": ROOT / "data" / "catalogo-tw-salud.json",
    "tw_innova.tex": ROOT / "data" / "catalogo-tw-innova.json",
    "tw_inox.tex": ROOT / "data" / "catalogo-tw-inox.json",
    "tw_construye.tex": ROOT / "data" / "catalogo-tw-construye.json",
}


def esc(value: object) -> str:
    text = str(value or "")
    for bad, good in {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}"}.items():
        text = text.replace(bad, good)
    return text


def write(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def offers_tex(title: str, data_path: Path) -> str:
    items = json.loads(data_path.read_text(encoding="utf-8"))
    body = [rf"\section*{{{esc(title)}}}"]
    for item in items:
        body.append(
            rf"\subsection*{{{esc(item['oferta'])}}}"
            + "\n"
            + rf"\textbf{{Categoria:}} {esc(item['categoria'])}\quad \textbf{{Tipo:}} {esc(item['tipo'])}\quad \textbf{{Madurez:}} {esc(item['madurez'])}\\"
            + "\n"
            + rf"\textbf{{Precio Peru:}} {esc(item['precio_soles_texto'])}\quad \textbf{{Internacional:}} {esc(item['precio_usd_texto'])}\\"
            + "\n"
            + esc(item["descripcion_corta"])
            + r"\par\vspace{0.5em}\hrule\vspace{0.8em}"
        )
    return "\n".join(body)


def main() -> int:
    LATEX_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_PDF.parent.mkdir(parents=True, exist_ok=True)
    write(
        LATEX_DIR / "main.tex",
        r"""
\documentclass[11pt,a4paper]{article}
\usepackage[spanish]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\usepackage{xcolor}
\geometry{margin=1.8cm}
\definecolor{twblue}{HTML}{061326}
\begin{document}
\input{portada}
\input{tw_salud}
\input{tw_innova}
\input{tw_inox}
\input{tw_construye}
\input{condiciones_comerciales}
\input{pagos}
\input{contacto}
\end{document}
""",
    )
    write(
        LATEX_DIR / "portada.tex",
        r"""
\begin{titlepage}
\centering
{\Huge\bfseries Catalogo de lineas de negocio\par}
\vspace{0.4cm}
{\Large Tecprog World E.I.R.L.\par}
\vfill
TW Salud, TW Innova, TW Inox y TW Construye\\
Junio 2026\\
RUC: 20608743252
\end{titlepage}
""",
    )
    titles = {
        "tw_salud.tex": "TW Salud",
        "tw_innova.tex": "TW Innova",
        "tw_inox.tex": "TW Inox",
        "tw_construye.tex": "TW Construye",
    }
    for tex_name, data_path in FILES.items():
        write(LATEX_DIR / tex_name, offers_tex(titles[tex_name], data_path))
    write(
        LATEX_DIR / "condiciones_comerciales.tex",
        r"""
\section*{Condiciones comerciales}
Los precios son referenciales y se muestran como desde. El precio final depende de alcance, ubicacion, materiales, modalidad, urgencia y validacion tecnica. No se afirma certificacion externa, autorizacion sanitaria, alianza clinica ni representacion de marcas.
""",
    )
    write(
        LATEX_DIR / "pagos.tex",
        r"""
\section*{Pagos}
Pagos Peru por QR Yape o transferencia previa coordinacion. Clientes internacionales pueden solicitar enlace PayPal. Confirmar disponibilidad antes de realizar cualquier operacion.
""",
    )
    write(
        LATEX_DIR / "contacto.tex",
        r"""
\section*{Contacto}
WhatsApp: +51 952 354 282\\
Correo: grupotecprog@gmail.com\\
Web: https://tecprog-world-store.github.io
""",
    )
    write(
        LATEX_DIR / "referencias.bib",
        r"""
@misc{tecprog2026lineas,
  title = {Catalogo de lineas de negocio Tecprog World},
  author = {{Tecprog World E.I.R.L.}},
  year = {2026}
}
""",
    )
    write(
        LATEX_DIR / "build.bat",
        rf"""
@echo off
cd /d "%~dp0"
pdflatex -halt-on-error -interaction=nonstopmode main.tex
copy /Y main.pdf "{PDF_NAME}"
""",
    )
    write(
        LATEX_DIR / "README.md",
        f"# Catalogo lineas de negocio\n\nCompilar con `build.bat`. PDF final: `{PDF_NAME}`.",
    )
    result = subprocess.run(["cmd", "/c", "build.bat"], cwd=LATEX_DIR, text=True, capture_output=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        return result.returncode
    compiled = LATEX_DIR / PDF_NAME
    if compiled.exists():
        PUBLIC_PDF.write_bytes(compiled.read_bytes())
        print(f"Copiado {compiled} -> {PUBLIC_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
