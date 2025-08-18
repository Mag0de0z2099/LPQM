import sim.simulator as sim


def test_render_ascii_no_crashea():
    e = sim.Estado(0.5)
    # width pequeñito para que sea rápido
    sim.render_ascii(e, width=8)
