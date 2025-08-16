# scripts/ci_smoke.py
import sys, os, platform, pathlib

print("🔎 Smoke run LPQM")
print(f"Python: {platform.python_version()}  |  OS: {platform.system()} {platform.release()}")
print(f"CWD: {os.getcwd()}")

# Señal simple de salud del repo
paths = [p for p in ("examples", "sim", "README.md", "pyproject.toml", "main.py") if pathlib.Path(p).exists()]
print("Rutas detectadas:", ", ".join(map(str, paths)) or "(ninguna)")

print("✅ Smoke OK")
