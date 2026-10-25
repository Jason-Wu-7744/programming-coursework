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
for p in (ROOT / "tools").glob("*.py"):
    compile(p.read_text(encoding="utf-8"), str(p.relative_to(ROOT)), "exec")
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or p.name.endswith(".zh-CN.md"):
        continue
    companion = p.with_name(p.stem + ".zh-CN.md")
    assert companion.exists(), ("Missing Chinese documentation option", str(p.relative_to(ROOT)))
    assert companion.name in p.read_text(encoding="utf-8"), ("Missing Chinese language link", str(p.relative_to(ROOT)))
    assert p.name in companion.read_text(encoding="utf-8"), ("Missing English language link", str(companion.relative_to(ROOT)))
for p in ROOT.glob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
        target = target.strip().split("#", 1)[0]
        if target and ":" not in target:
            assert (p.parent / unquote(target)).exists(), (p.name, target)
print("All course syntax checks, bilingual documentation pairs and local links passed.")
print("Historical algorithms, data-dependent execution and financial conclusions are not certified.")
