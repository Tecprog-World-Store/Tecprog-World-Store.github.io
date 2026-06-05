from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "catalogo-general-cursos.json"
LATEX_DIR = Path(r"D:\DiskE01\Organizacionies\E-TW\Produccion_LaTeX_TW\catalogos_mensuales\2026-06")
PDF_NAME = "catalogo-general-tw-educa-2026-06.pdf"
PUBLIC_PDF = ROOT / "assets" / "pdf" / "catalogos" / PDF_NAME


def tex_escape(value: object) -> str:
    text = str(value or "")
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text


def write(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def course_rows(courses: list[dict], limit: int = 60) -> str:
    rows = []
    for item in courses[:limit]:
        rows.append(
            r"\TWCourse{%s}{%s}{%s}{%s}{%s}{%s}"
            % (
                tex_escape(item["curso"]),
                tex_escape(item["categoria"]),
                tex_escape(item["nivel"]),
                tex_escape(item["horas_certificables"]),
                tex_escape(item["precio_peru_igv_soles"]),
                tex_escape(item["descripcion_corta"]),
            )
        )
    return "\n".join(rows)


def grouped_summary(courses: list[dict]) -> str:
    categories: dict[str, int] = {}
    for item in courses:
        categories[item["categoria"]] = categories.get(item["categoria"], 0) + 1
    rows = [r"\begin{itemize}"]
    for category, count in sorted(categories.items()):
        rows.append(r"\item %s: %s cursos" % (tex_escape(category), count))
    rows.append(r"\end{itemize}")
    return "\n".join(rows)


def main() -> int:
    courses = json.loads(DATA.read_text(encoding="utf-8"))
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
\usepackage{longtable}
\usepackage{array}
\usepackage{enumitem}
\geometry{margin=1.8cm}
\definecolor{twblue}{HTML}{061326}
\definecolor{twgold}{HTML}{D5A12F}
\newcommand{\TWCourse}[6]{%
\section*{#1}
\textbf{Categoria:} #2\quad
\textbf{Nivel:} #3\quad
\textbf{Horas:} #4\quad
\textbf{Precio Peru:} S/ #5\\
#6\par\vspace{0.5em}\hrule\vspace{0.8em}
}
\begin{document}
\input{portada}
\input{presentacion}
\input{catalogo_general_tw_educa}
\input{cursos_destacados}
\input{precios_y_horas}
\input{pagos_peru}
\input{pagos_internacionales}
\input{condiciones_comerciales}
\input{contacto}
\end{document}
""",
    )
    write(
        LATEX_DIR / "portada.tex",
        r"""
\begin{titlepage}
\centering
{\Huge\bfseries Catalogo general TW Educa\par}
\vspace{0.5cm}
{\Large Tecprog World E.I.R.L.\par}
\vspace{0.4cm}
{\large Junio 2026\par}
\vfill
{\large Cursos tecnicos, cientificos y profesionales para ingenieria, software, inteligencia artificial, electronica, fluidos, energia, GIS y gestion tecnologica.\par}
\vfill
RUC: 20608743252\\
WhatsApp: +51 952 354 282\\
grupotecprog@gmail.com
\end{titlepage}
""",
    )
    write(
        LATEX_DIR / "presentacion.tex",
        rf"""
\section*{{Presentacion}}
Tecprog World E.I.R.L. presenta este catalogo general de TW Educa como una base comercial y tecnica para cursos virtuales, grabados e institucionales. El catalogo contiene {len(courses)} cursos derivados de fuentes academicas, tecnicas y cursos vigentes definidos por la empresa.
""",
    )
    write(
        LATEX_DIR / "catalogo_general_tw_educa.tex",
        r"\section*{Catalogo general de cursos}" + "\n" + course_rows(courses),
    )
    featured = [item for item in courses if item.get("prioridad_web", "").lower() == "alta"][:12]
    write(
        LATEX_DIR / "cursos_destacados.tex",
        r"\section*{Cursos destacados}" + "\n" + course_rows(featured or courses[:12], 12),
    )
    write(
        LATEX_DIR / "precios_y_horas.tex",
        r"""
\section*{Precios y horas}
Los precios son referenciales, incluyen IGV para Peru cuando corresponda y pueden variar segun alcance, modalidad, calendario, numero de participantes y requerimientos institucionales.
"""
        + "\n"
        + grouped_summary(courses),
    )
    write(
        LATEX_DIR / "pagos_peru.tex",
        r"""
\section*{Pagos Peru}
Pagos nacionales por QR Yape, transferencia bancaria o coordinacion directa. Confirmar disponibilidad antes de realizar cualquier operacion.
""",
    )
    write(
        LATEX_DIR / "pagos_internacionales.tex",
        r"""
\section*{Pagos internacionales}
Clientes internacionales pueden solicitar enlace PayPal o coordinacion de pago segun el curso, paquete o propuesta institucional.
""",
    )
    write(
        LATEX_DIR / "condiciones_comerciales.tex",
        r"""
\section*{Condiciones comerciales}
No se afirma representacion oficial de universidades, softwares o marcas mencionadas. Las certificaciones corresponden a constancias o certificados de participacion emitidos por Tecprog World E.I.R.L. segun modalidad y cumplimiento acordado.
""",
    )
    write(
        LATEX_DIR / "contacto.tex",
        r"""
\section*{Contacto}
Web: https://tecprog-world-store.github.io\\
Correo: grupotecprog@gmail.com\\
WhatsApp: +51 952 354 282
""",
    )
    write(
        LATEX_DIR / "referencias.bib",
        r"""
@misc{tecprog2026catalogo,
  title = {Catalogo general TW Educa},
  author = {{Tecprog World E.I.R.L.}},
  year = {2026},
  note = {Catalogo comercial generado desde data/catalogo-general-cursos.json}
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
        rf"""
# Catalogo general TW Educa 2026-06

Fuente web: `{DATA}`

Compilar con:

```bat
build.bat
```

PDF final esperado:

```text
{PDF_NAME}
```
""",
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
