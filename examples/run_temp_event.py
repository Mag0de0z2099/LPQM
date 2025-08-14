# Usa eventos de temperatura: →P_evento cuando temp>0.65, →W_evento cuando temp<0.35
import os, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM = os.path.join(ROOT, "sim", "simulator.py")

cmd = [
    sys.executable, SIM,
    "--cycles", "30",
    "--delay", "0.10",
    "--probP", "0.50",
    "--probW", "0.60",
    "--impacto", "0.10",
    "--restriccion", "0.30",
    "--amortiguacion", "0.40",
    "--estimulo", "0.20",
    "--temp-start", "0.20",
    "--temp-step", "0.03",
    "--boost", "0.25",
]
subprocess.run(cmd, check=True)
