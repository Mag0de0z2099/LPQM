# Ejecuta una simulación corta: →P y →W sin eventos (temperatura estable)
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM = os.path.join(ROOT, "sim", "simulator.py")

cmd = [
    sys.executable,
    SIM,
    "--cycles",
    "4",
    "--delay",
    "0.15",
    "--probP",
    "0.50",
    "--probW",
    "0.60",
    "--impacto",
    "0.10",
    "--restriccion",
    "0.30",
    "--amortiguacion",
    "0.40",
    "--estimulo",
    "0.20",
    "--temp-start",
    "0.20",
    "--temp-step",
    "0",
    "--no-ascii",
]

result = subprocess.run(cmd, capture_output=True, text=True)

print("---- STDOUT ----")
print(result.stdout)
print("---- STDERR ----")
print(result.stderr)
print(f"Exit code: {result.returncode}")
