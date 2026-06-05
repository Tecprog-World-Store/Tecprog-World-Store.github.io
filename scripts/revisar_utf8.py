from __future__ import annotations

import argparse
from pathlib import Path


EXTENSIONS = {".html", ".css", ".js", ".json", ".md", ".tex", ".bib"}
BAD_PATTERNS = ["Ãƒ", "Ã‚", "ï¿¾", "ï¿½"]
ALLOWLIST = {Path("docs/LINEAMIENTOS_UTF8.md")}
FIX_MAP = {
    "ÃƒÂ¡": "á",
    "ÃƒÂ©": "é",
    "ÃƒÂ­": "í",
    "ÃƒÂ³": "ó",
    "ÃƒÂº": "ú",
    "ÃƒÂ±": "ñ",
    "ÃƒÂ": "Á",
    "ÃƒÂ‰": "É",
    "ÃƒÂ": "Í",
    "ÃƒÂ“": "Ó",
    "ÃƒÂš": "Ú",
    "ÃƒÂ‘": "Ñ",
    "Ã‚": "",
}


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    try:
        relative = path.relative_to(Path(__file__).resolve().parents[1])
        if relative in ALLOWLIST:
            return True
    except ValueError:
        pass
    return any(part in parts for part in {".git", ".idea", "node_modules"})


def iter_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in EXTENSIONS and not should_skip(path):
            yield path


def scan_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [(path, 0, f"No se pudo leer como UTF-8: {exc}")]

    findings = []
    for number, line in enumerate(text.splitlines(), start=1):
        if any(pattern in line for pattern in BAD_PATTERNS):
            findings.append((path, number, line.strip()))
    return findings


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    fixed = text
    for bad, good in FIX_MAP.items():
        fixed = fixed.replace(bad, good)
    if fixed != text:
        path.write_text(fixed, encoding="utf-8", newline="")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Revisa mojibake y errores de codificacion UTF-8.")
    parser.add_argument("--fix", action="store_true", help="Aplica correcciones conocidas. Por defecto solo reporta.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    all_findings = []

    for path in iter_files(root):
        findings = scan_file(path)
        all_findings.extend(findings)
        if args.fix and findings:
            fix_file(path)

    if not all_findings:
        print("OK: no se detectaron patrones mojibake prohibidos.")
        return 0

    print("Se detectaron posibles problemas UTF-8:")
    for path, line, text in all_findings:
        relative = path.relative_to(root)
        print(f"{relative}:{line}: {text}")
    if not args.fix:
        print("No se modifico ningun archivo. Use --fix para aplicar correcciones conocidas.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
