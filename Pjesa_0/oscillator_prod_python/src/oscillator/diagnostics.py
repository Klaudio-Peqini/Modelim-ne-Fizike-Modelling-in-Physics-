"""Diagnostikë numerike për shembullin e oscilatorit."""

from __future__ import annotations
import numpy as np
from .models import energy, OscillatorParams

def energy_series(y: np.ndarray, p: OscillatorParams) -> np.ndarray:
    return np.array([energy(state, p) for state in y], dtype=float)

def rel_energy_drift(y: np.ndarray, p: OscillatorParams) -> float:
    E = energy_series(y, p)
    return float((E[-1] - E[0]) / E[0])
