# LPQM

[![CI](https://github.com/Mag0de0z2099/LPQM/actions/workflows/ci.yml/badge.svg)](https://github.com/Mag0de0z2099/LPQM/actions/workflows/ci.yml)
[![Deploy Release](https://github.com/Mag0de0z2099/LPQM/actions/workflows/deploy.yml/badge.svg)](https://github.com/Mag0de0z2099/LPQM/actions/workflows/deploy.yml)
[![Quality](https://github.com/Mag0de0z2099/LPQM/actions/workflows/quality.yml/badge.svg)](https://github.com/Mag0de0z2099/LPQM/actions/workflows/quality.yml)
[![codecov](https://codecov.io/gh/Mag0de0z2099/LPQM/branch/main/graph/badge.svg)](https://codecov.io/gh/Mag0de0z2099/LPQM)


# LPQM
LPQM — Lenguaje de Proyección Cuántica Multidireccional Prototipo de un lenguaje experimental inspirado en la mecánica cuántica.
# LPQM — Lenguaje de Proyección Cuántica Multidireccional (prototipo)

**Estado:** v0.1.0 (exploratorio)  
**Idea central:** modelar **vibras/ondas ↔ partículas** con operadores de transición probabilísticos que incorporan ruido y entorno.

![Diagrama]https://github.com/Mag0de0z2099/LPQM/releases/tag/v0.1.0
## ¿Por qué?
LPQM explora una DSL donde la **incertidumbre** es una característica del lenguaje, no una excepción. Los operadores `→P` (onda→partícula) y `→W` (partícula→onda) permiten simular colapsos y recomposición bajo parámetros de **probabilidad, ruido y entorno**.

## Ejemplo mínimo
Ver [`examples/duality_basic.lpqm`](examples/duality_basic.lpqm).

## Simulador de referencia
Un prototipo en Python para probar la lógica: [`sim/simulator.py`](sim/simulator.py).

## Hoja de ruta
Mira [`ROADMAP.md`](ROADMAP.md).

## Cómo contribuir
Lee [`CONTRIBUTING.md`](CONTRIBUTING.md) y abre un issue con propuesta. Etiquetas útiles: `idea`, `spec`, `sim`, `good first issue`.

## Licencia
Apache 2.0 (ver `LICENSE`).

### v0.2.0
- Colapso/Dispersión **condicionados por eventos** (`op_P_evento`, `op_W_evento`).
- Visualización ASCII simple para observar el estado.
- Parámetros por CLI (ciclos, delay, ruido/entorno, temperatura simulada).

**Ejemplo:**
```bash
cd sim
python3 simulator.py --cycles 30 --delay 0.1 --temp-start 0.2 --temp-step 0.04

### ▶️ Scripts de ejemplo (Windows/Linux/Mac)
En `examples/` hay tres scripts Python que ejecutan el simulador con configuraciones listas:

- `run_simple_collapse.py` — Prueba corta sin eventos.
- `run_temp_event.py` — Eventos de temperatura (temp sube por ciclo).
- `run_alternating_pulse.py` — Pulso alternante con probabilidades altas.

**Cómo correrlos** (desde la raíz del repo):
```bash
python examples/run_simple_collapse.py
python examples/run_temp_event.py
python examples/run_alternating_pulse.py
