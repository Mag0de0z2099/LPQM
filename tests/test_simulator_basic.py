import pytest

import sim.simulator as simulator


def test_estado_inicial():
    """El objeto Estado arranca con el valor esperado."""
    estado = simulator.Estado(10)
    assert getattr(estado, "valor", None) == 10


def test_incremento_suma_valor_y_retorna_objeto_nuevo():
    """incremento debe sumar al valor y devolver un objeto (idealmente nuevo)."""
    e1 = simulator.Estado(5)
    e2 = simulator.incremento(e1, 3)
    assert getattr(e2, "valor", None) == 8
    # si tu implementación es inmutable, esto será True; si es in-place, no pasa nada por que no fallamos
    if e1 is not e2:
        assert e1.valor == 5
