from sim.simulator import EventoSumar

class DummyEstado(sim.Estado):
    """Estado mínimo para pruebas (hereda de sim.Estado)."""
    pass

class EventoSumar:
    """Callback de evento: suma 1 al valor del estado y devuelve un nuevo Estado.
       Acepta *args/**kwargs para tolerar ctx u otros parámetros sin fallar."""
    def __call__(self, estado, *_args, **_kwargs):
        return sim.Estado(getattr(estado, "valor", 0) + 1)



def test_op_P_dispara_con_random_bajo(monkeypatch):
    # random() = 0.0  ->  siempre < prob  ->  dispara
    monkeypatch.setattr(sim.random, "random", lambda: 0.0)

    e0 = DummyEstado(0)
    ruido = {"impacto": 0.0}
    entorno = {"amortiguacion": 0.0}
    ctx = {"estimulo": 0.0}

    e1 = sim.op_P_evento(e0, EventoSumar(), 1.0, ruido, entorno, 0.0, ctx)
    assert e1.valor == 1


def test_op_P_no_dispara_con_random_alto(monkeypatch):
    # random() = 1.0  ->  siempre >= prob  ->  NO dispara
    monkeypatch.setattr(sim.random, "random", lambda: 1.0)

    e0 = DummyEstado(0)
    ruido = {"impacto": 0.0}
    entorno = {"amortiguacion": 0.0}
    ctx = {"estimulo": 0.0}

    e1 = sim.op_P_evento(e0, EventoSumar(), 0.0, ruido, entorno, 0.0, ctx)
    assert e1.valor == 0


def test_op_W_dispara_con_random_bajo(monkeypatch):
    # random() = 0.0  ->  dispara rama W
    monkeypatch.setattr(sim.random, "random", lambda: 0.0)

    e0 = DummyEstado(0)
    ruido = {"impacto": 0.0}
    entorno = {"amortiguacion": 0.0}
    ctx = {"estimulo": 0.0}

    e1 = sim.op_W_evento(e0, EventoSumar(), 1.0, ruido, entorno, 0.0, ctx)
    assert e1.valor == 1
