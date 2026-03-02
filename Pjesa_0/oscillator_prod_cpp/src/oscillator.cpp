#include "oscillator.hpp"

State rhs(const State& s, const OscillatorParams& p) {
    const double x = s[0];
    const double v = s[1];
    return State{ v, -(p.omega*p.omega) * x };
}

double energy(const State& s, const OscillatorParams& p) {
    const double x = s[0];
    const double v = s[1];
    return 0.5*v*v + 0.5*(p.omega*p.omega)*x*x;
}
