#pragma once
#include <string>

struct Args {
    double omega{2.0};
    double dt{0.05};
    double t_end{50.0};
    double x0{1.0};
    double v0{0.0};
    std::string method{"verlet"};
    std::string out{"out.csv"};
};

Args parse_args(int argc, char** argv);
