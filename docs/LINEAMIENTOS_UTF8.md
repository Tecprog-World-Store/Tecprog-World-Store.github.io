# Lineamientos de codificacion UTF-8 para Tecprog World

## A. Regla general

Todos los archivos HTML, CSS, JS, JSON, MD, TEX y BIB deben guardarse como UTF-8.

## B. HTML

Cada HTML debe tener en el `head`:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## C. JSON

Los JSON deben guardarse en UTF-8 y validarse antes de publicar.

## D. LaTeX

Los documentos LaTeX deben usar preferentemente XeLaTeX.

Si se usa pdfLaTeX, incluir:

```tex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
```

Si se usa XeLaTeX, incluir:

```tex
\usepackage{fontspec}
\usepackage[spanish]{babel}
```

## E. Errores prohibidos

No deben aparecer en la web:

- TecnologÃƒÂ­a
- EducaciÃƒÂ³n
- ConstrucciÃƒÂ³n
- PrÃƒÂ³tesis
- ÃƒÂ³
- ÃƒÂ¡
- ÃƒÂ©
- ÃƒÂ­
- ÃƒÂº
- ÃƒÂ±
- Ã‚

## F. Como detectar problemas

Lista de busqueda recomendada para VS Code:

```text
Ãƒ
Ã‚
ï¿¾
```

Tambien ejecutar:

```bat
scripts\revisar_utf8.bat
```

## G. Como corregir

- Guardar archivo como UTF-8.
- Revisar que el navegador no este leyendo ISO-8859-1.
- Revisar meta charset.
- Revisar exportacion desde scripts Python.
- En Python usar `encoding="utf-8"`.

## H. Regla para CODEX

Antes de finalizar cualquier cambio, revisar mojibake en HTML, JSON, JS, CSS, Markdown, TEX y BIB.
