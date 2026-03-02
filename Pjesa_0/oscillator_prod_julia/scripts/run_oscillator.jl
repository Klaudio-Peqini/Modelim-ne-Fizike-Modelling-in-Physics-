using ArgParse
using DelimitedFiles
using OscillatorProdDemo

function build_parser()
    s = ArgParseSettings()
    @add_arg_table s begin
        "--omega"
            help = "frekuenca këndore ω"
            arg_type = Float64
            default = 2.0
        "--dt"
            help = "hapi kohor"
            arg_type = Float64
            default = 0.05
        "--t_end"
            help = "koha finale"
            arg_type = Float64
            default = 50.0
        "--x0"
            help = "kushti fillestar x0"
            arg_type = Float64
            default = 1.0
        "--v0"
            help = "kushti fillestar v0"
            arg_type = Float64
            default = 0.0
        "--method"
            help = "metoda (euler|rk4|verlet)"
            arg_type = String
            default = "verlet"
        "--out"
            help = "skedari CSV output"
            arg_type = String
            default = "out.csv"
    end
    return s
end

function main()
    args = parse_args(build_parser())
    p = OscillatorParams(args["omega"])
    s0 = (args["x0"], args["v0"])

    t, y = if args["method"] == "euler"
        simulate_euler(s0, p, args["t_end"], args["dt"])
    elseif args["method"] == "rk4"
        simulate_rk4(s0, p, args["t_end"], args["dt"])
    elseif args["method"] == "verlet"
        simulate_verlet(s0, p, args["t_end"], args["dt"])
    else
        error("Metodë e panjohur: $(args["method"])")
    end

    E0 = energy(y[1], p)
    E1 = energy(y[end], p)
    drift = (E1 - E0) / E0
    println("Drift relativ i energjisë: ", drift)

    M = hcat(t, [s[1] for s in y], [s[2] for s in y])
    open(args["out"], "w") do io
        write(io, "t,x,v\n")
        writedlm(io, M, ',')
    end
    println("U shkrua: ", args["out"])
end

main()
