import sim.simulator as sim

def test_estado_inicial_por_defecto():
    e = sim.Estado()
    assert hasattr(e, "valor")

def test_estado_inicial_con_valor():
    e = sim.Estado(10)
    assert e.valor == 10

def test_incremento_devuelve_nuevo_estado():
    e1 = sim.Estado(5)
    e2 = sim.incremento(e1, 3)
    assert e2.valor == 8
    # si tu implementación es inmutable, e1 y e2 serán distintos; si no, no importa
    if e1 is not e2:
        assert e1.valor == 5
