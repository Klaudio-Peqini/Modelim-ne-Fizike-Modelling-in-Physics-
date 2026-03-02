"""Modele të thjeshta ODE për kursin 'Modellimi në Fizikë'."""

from __future__ import annotations
from dataclasses import dataclass
import numpy as np

State = np.ndarray  # shape (2,) për [x, v]

@dataclass(frozen=True)
class OscillatorParams:
    omega: float

def oscillator_rhs(state: State, p: OscillatorParams) -> State:
    """RHS për oscilatorin harmonik: x' = v, v' = -omega^2 x."""
    x, v = float(state[0]), float(state[1])
    return np.array([v, -(p.omega**2) * x], dtype=float)

def energy(state: State, p: OscillatorParams) -> float:
    """Energjia totale E = 1/2 v^2 + 1/2 omega^2 x^2."""
    x, v = float(state[0]), float(state[1])
    return 0.5 * v*v + 0.5 * (p.omega**2) * x*x
