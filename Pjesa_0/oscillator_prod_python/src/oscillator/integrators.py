"""Integratorë numerikë: Euler, RK4, Velocity-Verlet.

Dizajni është minimal por i pastër: stepper + simulate.
"""

from __future__ import annotations
from typing import Callable, Tuple
import numpy as np

State = np.ndarray

def step_euler(rhs: Callable, state: State, p, dt: float) -> State:
    return state + dt * rhs(state, p)

def step_rk4(rhs: Callable, state: State, p, dt: float) -> State:
    k1 = rhs(state, p)
    k2 = rhs(state + 0.5*dt*k1, p)
    k3 = rhs(state + 0.5*dt*k2, p)
    k4 = rhs(state + dt*k3, p)
    return state + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)

def step_velocity_verlet(state: State, omega: float, dt: float) -> State:
    """Velocity-Verlet për oscilatorin harmonik (përdor omega direkt)."""
    x, v = float(state[0]), float(state[1])
    a = -(omega**2) * x
    x_new = x + v*dt + 0.5*a*dt*dt
    a_new = -(omega**2) * x_new
    v_new = v + 0.5*(a + a_new)*dt
    return np.array([x_new, v_new], dtype=float)

def simulate(rhs: Callable,
             stepper: Callable,
             state0: State,
             p,
             t_end: float,
             dt: float) -> Tuple[np.ndarray, np.ndarray]:
    t = np.arange(0.0, t_end + dt, dt)
    y = np.zeros((len(t), len(state0)), dtype=float)
    y[0] = state0
    for n in range(len(t)-1):
        y[n+1] = stepper(rhs, y[n], p, dt)
    return t, y

def simulate_verlet_oscillator(state0: State, omega: float, t_end: float, dt: float) -> Tuple[np.ndarray, np.ndarray]:
    t = np.arange(0.0, t_end + dt, dt)
    y = np.zeros((len(t), len(state0)), dtype=float)
    y[0] = state0
    for n in range(len(t)-1):
        y[n+1] = step_velocity_verlet(y[n], omega, dt)
    return t, y
