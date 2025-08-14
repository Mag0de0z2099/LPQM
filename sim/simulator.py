import random, time

class Estado:
    def __init__(self):
        self.valor = "onda"

def registrar_evento(msg, estado, params):
    t = time.time()
    print(f"[{t:.3f}] {msg} | estado={estado.valor} | {params}")

def op_P(estado, prob, ruido, entorno):
    p = prob + entorno["impacto"] - ruido["amortiguación"]
    if random.random() < max(0.0, min(1.0, p)):
        estado.valor = "partícula"
        registrar_evento("Colapso a partícula", estado, {"p": round(p,3)})

def op_W(estado, prob, ruido, entorno):
    p = prob + ruido["estímulo"] - entorno["restricción"]
    if random.random() < max(0.0, min(1.0, p)):
        estado.valor = "onda"
        registrar_evento("Dispersión a onda", estado, {"p": round(p,3)})

if __name__ == "__main__":
    estado   = Estado()
    entorno  = {"impacto":0.10, "restricción":0.30}
    ruido    = {"amortiguación":0.40, "estímulo":0.20}

    print("Estado inicial:", estado.valor)
    op_P(estado, 0.50, ruido, entorno)
    op_W(estado, 0.60, ruido, entorno)
    print("Estado final:", estado.valor)
