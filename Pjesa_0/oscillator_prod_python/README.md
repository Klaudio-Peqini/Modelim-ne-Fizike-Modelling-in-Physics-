# Oscillator Production Demo (Python)

Ky repository është një “mini-produkt” didaktik që tregon si kalohet nga një Notebook (eksplorim) në një strukturë **prodhimi**:

- `src/oscillator/` – paketë Python me modele, integratorë dhe diagnostikë
- `scripts/` – skripte ekzekutimi (CLI) për simulim/plot
- `tests/` – teste minimale (pytest)

## Instalimi (rekomanduar)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements-dev.txt
```

## Shembull ekzekutimi

```bash
python scripts/run_oscillator.py --omega 2.0 --dt 0.05 --t-end 50 --method verlet --out out_verlet.csv
python scripts/plot_results.py --csv out_verlet.csv --omega 2.0
```

## Qëllimi pedagogjik
- “Funksione të pastra” (input → output)
- Ndarje përgjegjësish (model / integrator / diagnostikë / CLI)
- Parametrizim me argumenta
- Testim minimal i sjelljes numerike

