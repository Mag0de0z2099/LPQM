import sim.simulator as sim


class DummyEstado(sim.Estado):
    pass


class EventoSumar:
    def __call__(self, estado, *_, **__):
        # Suma 1 y devuelve un nuevo Estado (tolerante a args extra como ctx)
        return sim.Estado(getattr(estado, "valor", 0) + 1)


def test_op_P_dispara_con_random_bajo(monkeypatch):
    # Forzamos random.random() a 0.0 => siempre < prob y dispara
    monkeypatch.setattr(sim.random, "random", lambda: 0.0)

    e0 = DummyEstado(0)
    ctx = {}
    #          estado, evento,        probP, ruido,               entorno,                   boost, ctx
    e1 = sim.op_P_evento(e0, EventoSumar(), 1.0,   {"impacto": 0.0}, {"amortiguación": 0.0}, 0.0,   ctx)
    assert e1.valor == 1


def test_op_P_no_dispara_con_random_alto(monkeypatch):
    # Forzamos random.random() a 1.0 => siempre >= prob y NO dispara
    monkeypatch.setattr(sim.random, "random", lambda: 1.0)

    e0 = DummyEstado(0)
    ctx = {}
    e1 = sim.op_P_evento(e0, EventoSumar(), 0.0,   {"impacto": 0.0}, {"amortiguación": 0.0}, 0.0,   ctx)
    assert e1.valor == 0


def test_op_W_dispara_con_random_bajo(monkeypatch):
    monkeypatch.setattr(sim.random, "random", lambda: 0.0)

    e0 = DummyEstado(0)
    ctx = {}
    #          estado, evento,        probW, ruido,               entorno,                   boost, ctx
    e1 = sim.op_W_evento(e0, EventoSumar(), 1.0,   {"impacto": 0.0}, {"amortiguación": 0.0}, 0.0,   ctx)
    assert e1.valor == 1
