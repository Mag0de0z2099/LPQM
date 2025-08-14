# Changelog

## v0.1.0 — 14/08/2025

### Contenido de la versión
- Operadores básicos: `→P` (onda → partícula) y `→W` (partícula → onda).
- Simulador de referencia en Python.
- Especificaciones iniciales (`lpqm-operators.md`).
- Documentación base (`README.md`, `ROADMAP.md`, `CONTRIBUTING.md`).
- Licencia **Apache 2.0**.
- Código de Conducta (Contributor Covenant v2.1).

### Notas
Esta es la primera versión pública del prototipo LPQM.  
Sirve como punto de partida para exploración y desarrollo colaborativo.

📄 **Ver diagrama**: [https://github.com/Mag0de0z2099/LPQM/releases/tag/v0.1.0]

## v0.2.0 — 14/08/2025

### Mejoras
- Añadidos operadores condicionados por eventos:
  - `op_P_evento` (colapso →P activado por condición externa).
  - `op_W_evento` (dispersión →W activada por condición externa).
- Incorporada visualización ASCII simple para observar el estado en tiempo real.
- Soporte de parámetros por línea de comandos para:
  - Probabilidades (`--probP`, `--probW`).
  - Factores de ruido y entorno (`--amortiguacion`, `--estimulo`, `--impacto`, `--restriccion`).
  - Temperatura simulada (`--temp-start`, `--temp-step`) como disparador de eventos.
  - Número de ciclos (`--cycles`) y retardo (`--delay`).
- Registro de eventos con timestamp para trazabilidad.

### Notas
Esta versión marca el inicio de un simulador más flexible, con soporte de eventos y control completo desde la terminal.  
La visualización ASCII es opcional (`--no-ascii`) y puede ser el paso previo a la visualización avanzada planificada para v0.3.0.
