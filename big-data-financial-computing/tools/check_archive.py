"""Check archive syntax and local Markdown links without executing coursework."""
from pathlib import Path
from urllib.parse import unquote
import ast
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]
scripts=[]
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or any(p in {".git",".venv","__pycache__"} for p in path.relative_to(ROOT).parts):
        continue
    if path.suffix==".py":
        scripts.append(path)
        try:
            compile(path.read_text(encoding="utf-8-sig"),str(path.relative_to(ROOT)),"exec")
        except (SyntaxError,UnicodeError) as exc:
            errors.append(str(path.relative_to(ROOT))+": "+str(exc))
    if path.suffix==".md":
        text=path.read_text(encoding="utf-8-sig")
        for target in re.findall(r"\]\(([^)]+)\)",text):
            target=target.strip().split("#",1)[0]
            if not target or ":" in target:
                continue
            if not (path.parent/unquote(target)).exists():
                errors.append(str(path.relative_to(ROOT))+": missing link "+target)
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Syntax and local Markdown links passed ({len(scripts)} Python files including this checker).")
print("Course scripts were not executed; this does not verify financial or statistical results.")
