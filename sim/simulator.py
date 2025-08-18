# simulator.py — v0.2.0
import argparse
import random
import sys
import time

# --- normalizador de claves para tolerar acentos / variantes ---
def _norm_dict(d):
    if d is None:
        return {"impacto": 0.0, "amortiguacion": 0.0}
    return {
        "impacto": d.get("impacto", d.get("impact", 0.0)),
        "amortiguacion": d.get("amortiguacion", d.get("amortiguación", d.get("damping", 0.0))),
    }

def _norm_ctx(ctx):
    if ctx is None:
        return {"estimulo": 0.0}
    return {
        "estimulo": ctx.get("estimulo", ctx.get("estímulo", ctx.get("stimulus", 0.0))),
    }

class Estado:
    def __init__(self, valor="onda"):
        # Valor inicial configurable: "onda" | "partícula" | número
        self.valor = valor

    def __repr__(self):
        return f"Estado(valor={self.valor!r})"


def registrar_evento(msg, estado, params=None):
    t = time.time()
    payload = f" | {params}" if params else ""
    print(f"[{t:.3f}] {msg} | estado={estado.valor}{payload}")


def clamp01(x):
    return max(0.0, min(1.0, x))


def op_P(estado, prob, ruido, entorno):
    p = prob + entorno["impacto"] - ruido["amortiguacion"]
    if random.random() < clamp01(p):
        estado.valor = "particula"
        registrar_evento("Colapso a particula (→P)", estado, {"p": round(p, 3)})
    return estado.valor


def op_W(estado, prob, ruido, entorno):
    p = prob + ruido["estimulo"] - entorno["restriccion"]
    if random.random() < clamp01(p):
        estado.valor = "onda"
        registrar_evento("Dispersion a onda (→W)", estado, {"p": round(p, 3)})
    return estado.valor


# --- v0.2.0: colapso/dispersion condicionados por evento ---
def op_P_evento(estado, cond, prob_base, ruido, entorno, boost=0.2, ctx=None):
    """Colapso a partícula si se cumple un evento (condición) con refuerzo de probabilidad."""
    prob = prob_base + (boost if cond(ctx or {}) else 0.0)
    return op_P(estado, prob, ruido, entorno)


def op_W_evento(estado, cond, prob_base, ruido, entorno, boost=0.2, ctx=None):
    """Dispersión a onda si se cumple un evento (condición) con refuerzo de probabilidad."""
    prob = prob_base + (boost if cond(ctx or {}) else 0.0)
    return op_W(estado, prob, ruido, entorno)


# --- v0.2.0: visualización ASCII simple ---
def render_ascii(estado, width=40):
    if estado.valor == "onda":
        print("~" * width)
    else:
        mid = width // 2
        print(" " * mid + "*")


def main(argv=None):
    ap = argparse.ArgumentParser(description="LPQM simulator v0.2.0 (ondas ↔ particulas)")
    ap.add_argument("--cycles", type=int, default=20, help="Número de ciclos de simulacion")
    ap.add_argument("--delay", type=float, default=0.2, help="Segundos entre ciclos")
    ap.add_argument("--probP", type=float, default=0.5, help="Probabilidad base →P (colapso)")
    ap.add_argument("--probW", type=float, default=0.6, help="Probabilidad base →W (dispersión)")
    ap.add_argument("--impacto", type=float, default=0.10, help="Entorno.impacto (favorece →P)")
    ap.add_argument(
        "--restriccion", type=float, default=0.30, help="Entorno.restriccion (dificulta →W)"
    )
    ap.add_argument(
        "--amortiguacion", type=float, default=0.40, help="Ruido.amortiguacion (frena →P)"
    )
    ap.add_argument("--estimulo", type=float, default=0.20, help="Ruido.estimulo (favorece →W)")
    ap.add_argument("--temp-start", type=float, default=0.2, help="Temperatura inicial [0..1]")
    ap.add_argument(
        "--temp-step", type=float, default=0.03, help="Incremento de temperatura por ciclo"
    )
    ap.add_argument(
        "--boost", type=float, default=0.25, help="Refuerzo de prob si el evento se cumple"
    )
    ap.add_argument("--ascii-width", type=int, default=40, help="Ancho de la visualización ASCII")
    ap.add_argument("--no-ascii", action="store_true", help="Desactiva la visualización ASCII")
    args = ap.parse_args(argv)

    estado = Estado()
    entorno = {"impacto": args.impacto, "restriccion": args.restriccion}
    ruido = {"amortiguacion": args.amortiguacion, "estimulo": args.estimulo}

    temperatura = args.temp_start

    # Eventos de ejemplo (puedes cambiarlos):
    def evento_colapso(ctx):  # dispare →P si temperatura > 0.65
        return ctx.get("temp", 0.0) > 0.65

    def evento_dispersion(ctx):  # dispare →W si temperatura < 0.35
        return ctx.get("temp", 0.0) < 0.35

    print("Estado inicial:", estado.valor)
    for i in range(1, args.cycles + 1):
        ctx = {"temp": temperatura, "tick": i}

        # 1) Intentar colapso condicionado
        op_P_evento(estado, evento_colapso, args.probP, ruido, entorno, args.boost, ctx)

        # 2) Intentar dispersión condicionada
        op_W_evento(estado, evento_dispersion, args.probW, ruido, entorno, args.boost, ctx)

        # 3) Render
        if not args.no_ascii:
            render_ascii(estado, width=args.ascii_width)

        # 4) Actualizar “temperatura” (simula entorno cambiante)
        temperatura = clamp01(temperatura + args.temp_step)

        time.sleep(args.delay)

    print("Estado final:", estado.valor)


# ... aquí van todas tus funciones existentes ...


def incremento(estado, delta):
    """Incrementa el estado en delta y devuelve un nuevo objeto Estado"""
    try:
        nuevo_valor = float(estado.valor) + delta
    except ValueError:
        # Si el estado no es numérico, lo dejamos igual
        nuevo_valor = estado.valor
    return Estado(nuevo_valor)
