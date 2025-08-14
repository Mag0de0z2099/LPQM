# LPQM
LPQM — Lenguaje de Proyección Cuántica Multidireccional Prototipo de un lenguaje experimental inspirado en la mecánica cuántica.
# LPQM — Lenguaje de Proyección Cuántica Multidireccional (prototipo)

**Estado:** v0.1.0 (exploratorio)  
**Idea central:** modelar **vibras/ondas ↔ partículas** con operadores de transición probabilísticos que incorporan ruido y entorno.

![Diagrama](docs/wave_particle_flowchart.png)

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
MIT (ver `LICENSE`).

