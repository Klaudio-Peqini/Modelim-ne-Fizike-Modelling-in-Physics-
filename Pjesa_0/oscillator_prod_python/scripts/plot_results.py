#!/usr/bin/env python3
"""Lexon CSV (t,x,v) dhe vizaton x(t) dhe energjinë."""
from __future__ import annotations
import argparse
import numpy as np
import matplotlib.pyplot as plt
from oscillator.models import OscillatorParams, energy

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--omega", type=float, default=2.0, help="duhet për energjinë")
    args = ap.parse_args()

    data = np.loadtxt(args.csv, delimiter=",", skiprows=1)
    t, x, v = data[:,0], data[:,1], data[:,2]
    p = OscillatorParams(omega=args.omega)
    E = np.array([energy(np.array([x[i], v[i]]), p) for i in range(len(t))])

    plt.figure()
    plt.plot(t, x, label="x(t)")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(t, E - E[0], label="E - E0")
    plt.xlabel("t")
    plt.ylabel("Devijimi i energjisë")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
