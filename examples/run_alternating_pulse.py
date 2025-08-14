# Pulso alternante: favorece cambios rápidos onda↔partícula con probabilidades altas
import os, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM = os.path.join(ROOT, "sim", "simulator.py")

cmd = [
    sys.executable, SIM,
    "--cycles", "10",
    "--delay", "0.10",
    "--probP", "0.90",
    "--probW", "0.90",
    "--impacto", "0.10",
    "--restriccion", "0.10",
    "--amortiguacion", "0.10",
    "--estimulo", "0.40",
    "--temp-start", "0.20",
    "--temp-step", "0",
]
subprocess.run(cmd, check=True)
