#!/usr/bin/env python3
"""CLI për simulimin e oscilatorit harmonik.

Shembull:
  python scripts/run_oscillator.py --omega 2.0 --dt 0.05 --t-end 50 --method verlet --out out.csv
"""
from __future__ import annotations
import argparse
import numpy as np

from oscillator.models import OscillatorParams, oscillator_rhs
from oscillator.integrators import simulate, step_euler, step_rk4, simulate_verlet_oscillator
from oscillator.diagnostics import rel_energy_drift

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--omega", type=float, default=2.0)
    ap.add_argument("--dt", type=float, default=0.05)
    ap.add_argument("--t-end", type=float, default=50.0)
    ap.add_argument("--method", type=str, choices=["euler", "rk4", "verlet"], default="verlet")
    ap.add_argument("--x0", type=float, default=1.0)
    ap.add_argument("--v0", type=float, default=0.0)
    ap.add_argument("--out", type=str, default="out.csv")
    args = ap.parse_args()

    state0 = np.array([args.x0, args.v0], dtype=float)
    p = OscillatorParams(omega=args.omega)

    if args.method == "verlet":
        t, y = simulate_verlet_oscillator(state0, omega=args.omega, t_end=args.t_end, dt=args.dt)
    else:
        stepper = step_euler if args.method == "euler" else step_rk4
        t, y = simulate(oscillator_rhs, stepper, state0, p, t_end=args.t_end, dt=args.dt)

    drift = rel_energy_drift(y, p)
    print(f"Drift relativ i energjisë: {drift:.3e}")

    data = np.column_stack([t, y[:,0], y[:,1]])
    np.savetxt(args.out, data, delimiter=",", header="t,x,v", comments="")
    print(f"U shkrua: {args.out}")

if __name__ == "__main__":
    main()
