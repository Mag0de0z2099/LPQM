import sim.simulator as simulator


def test_incremento_con_cero():
    e = simulator.Estado(7)
    r = simulator.incremento(e, 0)
    assert r.valor == 7


def test_incremento_negativo_resta():
    e = simulator.Estado(10)
    r = simulator.incremento(e, -4)
    assert r.valor == 6
