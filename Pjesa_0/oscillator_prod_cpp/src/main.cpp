#include "oscillator.hpp"
#include "integrators.hpp"
#include "cli.hpp"
#include <fstream>
#include <iostream>

static void write_csv(const std::string& path, const Trajectory& tr) {
    std::ofstream f(path);
    f << "t,x,v\n";
    for (size_t i=0; i<tr.t.size(); ++i) {
        f << tr.t[i] << "," << tr.y[i][0] << "," << tr.y[i][1] << "\n";
    }
}

int main(int argc, char** argv) {
    Args args;
    try {
        args = parse_args(argc, argv);
    } catch (const std::exception& e) {
        std::cerr << "Gabim: " << e.what() << "\n";
        std::cerr << "Përdorim: ./oscillator --omega 2.0 --dt 0.05 --t_end 50 --method verlet --out out.csv\n";
        return 1;
    }

    OscillatorParams p{args.omega};
    State s0{args.x0, args.v0};

    Trajectory tr;
    if (args.method == "euler") tr = simulate_euler(s0, p, args.t_end, args.dt);
    else if (args.method == "rk4") tr = simulate_rk4(s0, p, args.t_end, args.dt);
    else if (args.method == "verlet") tr = simulate_verlet(s0, p, args.t_end, args.dt);
    else {
        std::cerr << "Metodë e panjohur: " << args.method << " (euler|rk4|verlet)\n";
        return 1;
    }

    const double E0 = energy(tr.y.front(), p);
    const double E1 = energy(tr.y.back(), p);
    const double drift = (E1 - E0) / E0;
    std::cout << "Drift relativ i energjisë: " << drift << "\n";

    write_csv(args.out, tr);
    std::cout << "U shkrua: " << args.out << "\n";
    return 0;
}
