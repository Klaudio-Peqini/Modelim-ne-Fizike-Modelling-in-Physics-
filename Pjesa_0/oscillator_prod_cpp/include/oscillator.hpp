#pragma once
#include <array>

struct OscillatorParams {
    double omega{2.0};
};

using State = std::array<double, 2>; // [x, v]

State rhs(const State& s, const OscillatorParams& p);
double energy(const State& s, const OscillatorParams& p);
