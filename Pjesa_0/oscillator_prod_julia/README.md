# Oscillator Production Demo (Julia)

Mini-repo në Julia për oscilatorin harmonik me Euler, RK4 dhe Velocity-Verlet.
Shkruan CSV (`t,x,v`) dhe ofron skript vizatimi.

## Ekzekutimi (Julia)

Nga rrënja e repo-s:

```julia
julia --project=. scripts/run_oscillator.jl --omega 2.0 --dt 0.05 --t_end 50 --method verlet --out out.csv
julia --project=. scripts/plot_results.jl --csv out.csv --omega 2.0
```

## Qëllim pedagogjik
Julia është shumë e përshtatshme për modelim: sintaksë e pastër, performancë e lartë,
dhe ekosistem i mirë për shkencë numerike.
