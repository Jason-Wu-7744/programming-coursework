"""Check all three course archives without executing financial coursework."""
from pathlib import Path
from urllib.parse import unquote
import ast
import re
import runpy

ROOT = Path(__file__).resolve().parent
COURSES = ("financial-numerical-analysis", "financial-engineering", "big-data-financial-computing")
for course in COURSES:
    print("Checking " + course)
    runpy.run_path(str(ROOT / course / "tools" / "check_archive.py"), run_name="__main__")
ast.parse(Path(__file__).read_text(encoding="utf-8"))
for p in ROOT.glob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
        target = target.strip().split("#", 1)[0]
        if target and ":" not in target:
            assert (p.parent / unquote(target)).exists(), (p.name, target)
print("All course syntax checks and local documentation links passed.")
print("Historical algorithms, data-dependent execution and financial conclusions are not certified.")
