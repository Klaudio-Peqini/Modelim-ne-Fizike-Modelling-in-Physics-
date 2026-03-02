# Oscillator Production Demo (C++)

Mini-repo për oscilatorin harmonik, me integratorë Euler, RK4 dhe Velocity-Verlet.
Shkruan rezultatet në CSV (`t,x,v`) për t'u vizatuar me mjetet tuaja (Python/gnuplot/Excel).

## Ndërtimi

```bash
mkdir -p build
cd build
cmake ..
cmake --build . -j
```

## Ekzekutimi

```bash
./oscillator --omega 2.0 --dt 0.05 --t_end 50 --method verlet --out out.csv
```

Parametrat:
- `--method` : `euler | rk4 | verlet`

## Qëllim pedagogjik
Të shihet “kontrasti” me Python: e njëjta logjikë, por me tipizim dhe kontroll të plotë mbi strukturën.
