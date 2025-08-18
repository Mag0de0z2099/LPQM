import sim.simulator as sim


class DummyEstado(sim.Estado):
    """Estado mínimo para pruebas (hereda de sim.Estado)."""
    pass


class EventoSumar:
    """Callback de evento: suma 1 al valor del estado y devuelve un nuevo Estado.

    Acepta *args/**kwargs para ser tolerante si el motor llama con ctx u otros.
    """
    def __call__(self, estado, *_, **__):
        return sim.Estado(getattr(estado, "valor", 0) + 1)


def test_op_P_dispara_con_random_bajo(monkeypatch):
    # Forzamos random.random() a 0.0 => siempre < prob y dispara
    monkeypatch.setattr(sim.random, "random", lambda: 0.0)

    e0 = DummyEstado(0)
    ruido = {"impacto": 0.0}
    entorno = {"amortiguacion": 0.0}
    ctx = {"estimulo": 0.0}

    #       estado, evento,      probP, ruido, entorno, boost, ctx
    e1 = sim.op_P_evento(e0, EventoSumar(), 1.0,  ruido,  entorno,  0.0,   ctx)
    assert e1.valor == 1


def test_op_P_no_dispara_con_random_alto(monkeypatch):
    # Fuerza random.random() = 1.0 => siempre >= prob => NO dispara
    monkeypatch.setattr(sim.random, "random", lambda: 1.0)

    e0 = DummyEstado(0)
    ruido = {"impacto": 0.0}
    entorno = {"amortiguacion": 0.0}
    ctx = {"estimulo": 0.0}

    e1 = sim.op_P_evento(e0, EventoSumar(), 0.0, ruido, entorno, 0.0, ctx)
    assert e1.valor == 0


def test_op_W_dispara_con_random_bajo(monkeypatch):
    # Fuerza random.random() = 0.0 => dispara rama W
    monkeypatch.setattr(sim.random, "random", lambda: 0.0)

    e0 = DummyEstado(0)
    ruido = {"impacto": 0.0}
    entorno = {"amortiguacion": 0.0}
    ctx = {"estimulo": 0.0}

    e1 = sim.op_W_evento(e0, EventoSumar(), 1.0, ruido, entorno, 0.0, ctx)
    assert e1.valor == 1
