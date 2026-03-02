#include "cli.hpp"
#include <stdexcept>
#include <string>

Args parse_args(int argc, char** argv) {
    Args a;
    for (int i=1; i<argc; ++i) {
        std::string key = argv[i];
        auto require_value = [&](const std::string& k) {
            if (i+1 >= argc) throw std::runtime_error("Mungon vlera për " + k);
            return std::string(argv[++i]);
        };

        if (key == "--omega") a.omega = std::stod(require_value(key));
        else if (key == "--dt") a.dt = std::stod(require_value(key));
        else if (key == "--t_end") a.t_end = std::stod(require_value(key));
        else if (key == "--x0") a.x0 = std::stod(require_value(key));
        else if (key == "--v0") a.v0 = std::stod(require_value(key));
        else if (key == "--method") a.method = require_value(key);
        else if (key == "--out") a.out = require_value(key);
        else {
            throw std::runtime_error("Argument i panjohur: " + key);
        }
    }
    return a;
}
