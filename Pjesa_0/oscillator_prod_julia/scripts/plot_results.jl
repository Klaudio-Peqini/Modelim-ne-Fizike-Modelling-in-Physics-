using ArgParse
using DelimitedFiles
using Plots
using OscillatorProdDemo

function build_parser()
    s = ArgParseSettings()
    @add_arg_table s begin
        "--csv"
            help = "skedari CSV (t,x,v)"
            arg_type = String
            required = true
        "--omega"
            help = "ω (për energjinë)"
            arg_type = Float64
            default = 2.0
    end
    return s
end

function main()
    args = parse_args(build_parser())
    lines = readlines(args["csv"])
    data = readdlm(IOBuffer(join(lines[2:end], "\n")), ',', Float64)
    t = data[:,1]; x = data[:,2]; v = data[:,3]
    p = OscillatorParams(args["omega"])
    E = [energy((x[i], v[i]), p) for i in eachindex(t)]

    plot(t, x, xlabel="t", ylabel="x", label="x(t)")
    display(current())

    plot(t, E .- E[1], xlabel="t", ylabel="E - E0", label="Devijimi i energjisë")
    display(current())
end

main()
