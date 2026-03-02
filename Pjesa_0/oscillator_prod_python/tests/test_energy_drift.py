import numpy as np
from oscillator.models import OscillatorParams, oscillator_rhs
from oscillator.integrators import simulate, step_rk4, simulate_verlet_oscillator
from oscillator.diagnostics import rel_energy_drift

def test_verlet_has_small_drift_for_small_dt():
    p = OscillatorParams(omega=2.0)
    state0 = np.array([1.0, 0.0])
    _, y = simulate_verlet_oscillator(state0, omega=p.omega, t_end=100.0, dt=0.01)
    drift = rel_energy_drift(y, p)
    assert abs(drift) < 1e-3

def test_rk4_reasonable_drift_for_small_dt():
    p = OscillatorParams(omega=2.0)
    state0 = np.array([1.0, 0.0])
    _, y = simulate(oscillator_rhs, step_rk4, state0, p, t_end=100.0, dt=0.01)
    drift = rel_energy_drift(y, p)
    assert abs(drift) < 1e-2
