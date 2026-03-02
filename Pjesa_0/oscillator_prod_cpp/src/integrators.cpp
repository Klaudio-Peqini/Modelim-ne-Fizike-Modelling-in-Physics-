#include "integrators.hpp"
#include <cmath>

static inline State add(const State& a, const State& b) { return State{a[0]+b[0], a[1]+b[1]}; }
static inline State mul(double c, const State& a) { return State{c*a[0], c*a[1]}; }

Trajectory simulate_euler(const State& s0, const OscillatorParams& p, double t_end, double dt) {
    const int N = static_cast<int>(std::floor(t_end/dt)) + 1;
    Trajectory tr;
    tr.t.resize(N);
    tr.y.resize(N);
    tr.t[0] = 0.0;
    tr.y[0] = s0;
    for (int n=0; n<N-1; ++n) {
        tr.t[n+1] = tr.t[n] + dt;
        State k1 = rhs(tr.y[n], p);
        tr.y[n+1] = add(tr.y[n], mul(dt, k1));
    }
    return tr;
}

Trajectory simulate_rk4(const State& s0, const OscillatorParams& p, double t_end, double dt) {
    const int N = static_cast<int>(std::floor(t_end/dt)) + 1;
    Trajectory tr;
    tr.t.resize(N);
    tr.y.resize(N);
    tr.t[0] = 0.0;
    tr.y[0] = s0;
    for (int n=0; n<N-1; ++n) {
        tr.t[n+1] = tr.t[n] + dt;
        const State y = tr.y[n];
        const State k1 = rhs(y, p);
        const State k2 = rhs(add(y, mul(0.5*dt, k1)), p);
        const State k3 = rhs(add(y, mul(0.5*dt, k2)), p);
        const State k4 = rhs(add(y, mul(dt, k3)), p);
        const State incr = mul(dt/6.0, add(add(k1, mul(2.0,k2)), add(mul(2.0,k3), k4)));
        tr.y[n+1] = add(y, incr);
    }
    return tr;
}

Trajectory simulate_verlet(const State& s0, const OscillatorParams& p, double t_end, double dt) {
    const int N = static_cast<int>(std::floor(t_end/dt)) + 1;
    Trajectory tr;
    tr.t.resize(N);
    tr.y.resize(N);
    tr.t[0] = 0.0;
    tr.y[0] = s0;
    double x = s0[0];
    double v = s0[1];
    for (int n=0; n<N-1; ++n) {
        tr.t[n+1] = tr.t[n] + dt;
        const double a = -(p.omega*p.omega)*x;
        const double x_new = x + v*dt + 0.5*a*dt*dt;
        const double a_new = -(p.omega*p.omega)*x_new;
        const double v_new = v + 0.5*(a + a_new)*dt;
        x = x_new; v = v_new;
        tr.y[n+1] = State{x, v};
    }
    return tr;
}
