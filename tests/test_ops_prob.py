import sim.simulator as sim
import types

class DummyEstado(sim.Estado):
    pass

def dummy_evento(estado, ctx):
    # cambia el valor para verificar que la rama se ejecutó
    return sim.Estado(getattr(estado, "valor", 0) + 1)

def test_op_P_dispara_con_random_bajo(monkeypatch):
    # Forzar random.random() a 0.0 => siempre < prob y dispara
    monkeypatch.setattr(sim.random, "random", lambda: 0.0)

    e0 = DummyEstado(0)
    ctx = {}
    e1 = sim.op_P_evento(
        e0, dummy_evento, prob=1.0, ruido={"impacto": 0.0}, entorno={"amortiguación": 0.0}, boost=0.0, ctx=ctx
    )
    assert e1.valor == 1  # ejecutó dummy_evento

def test_op_P_no_dispara_con_random_alto(monkeypatch):
    # Forzar random.random() a 1.0 => siempre >= prob y NO dispara
    monkeypatch.setattr(sim.random, "random", lambda: 1.0)

    e0 = DummyEstado(0)
    ctx = {}
    e1 = sim.op_P_evento(
        e0, dummy_evento, prob=0.0, ruido={"impacto": 0.0}, entorno={"amortiguación": 0.0}, boost=0.0, ctx=ctx
    )
    assert e1.valor == 0  # no cambió

def test_op_W_dispara_con_random_bajo(monkeypatch):
    monkeypatch.setattr(sim.random, "random", lambda: 0.0)

    e0 = DummyEstado(0)
    ctx = {}
    e1 = sim.op_W_evento(
        e0, dummy_evento, probW=1.0, ruido={"impacto": 0.0}, entorno={"amortiguación": 0.0}, boost=0.0, ctx=ctx
    )
    assert e1.valor == 1
