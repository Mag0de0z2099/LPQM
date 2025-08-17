import pytest
import sim.simulator as simulator

@pytest.fixture
def estado10():
    return simulator.Estado(10)
