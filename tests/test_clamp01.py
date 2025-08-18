import sim.simulator as sim

def test_clamp01_menor_que_0():
    assert sim.clamp01(-100.0) == 0.0

def test_clamp01_mayor_que_1():
    assert sim.clamp01(9.9) == 1.0

def test_clamp01_en_rango():
    assert sim.clamp01(0.42) == 0.42
