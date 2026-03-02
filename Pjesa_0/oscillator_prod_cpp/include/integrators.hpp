#pragma once
#include "oscillator.hpp"
#include <vector>

struct Trajectory {
    std::vector<double> t;
    std::vector<State> y;
};

Trajectory simulate_euler(const State& s0, const OscillatorParams& p, double t_end, double dt);
Trajectory simulate_rk4(const State& s0, const OscillatorParams& p, double t_end, double dt);
Trajectory simulate_verlet(const State& s0, const OscillatorParams& p, double t_end, double dt);
