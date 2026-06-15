# Nordstar Research

Public research notes and demo code from Nordstar.

Nordstar works on commodity prediction, momentum alpha signals, and retail real estate intelligence using alternative data, geospatial signals, and machine learning.

This repository is intentionally selective. It contains public-safe notes and small illustrative code examples. The underlying data pipelines, signal database, satellite workflows, production models, and proprietary research edge remain private.

## Focus Areas

- Commodity prediction and momentum alpha research
- Retail real estate intelligence from alternative data
- Satellite, geospatial, and machine learning signals
- Walk-forward tested research and paper-trading diagnostics

## Public Demo Code

The code in this repository is designed to show research style, not production edge.

- `src/nordstar_public/momentum_demo.py` shows a generic momentum ranking pattern on synthetic prices.
- `src/nordstar_public/retail_demo.py` shows a high-level retail activity index on synthetic inputs.
- `src/nordstar_public/validation.py` shows chronological walk-forward split helpers.
- `examples/run_public_demo.py` runs the public demo end to end.
- `docs/PERFORMANCE_SNAPSHOT.md` summarizes selected actual research and paper-trading evidence.

Run:

```bash
python examples/run_public_demo.py
```

## What May Be Shared

- short research notes
- selected high-level charts
- non-sensitive case study summaries
- public-safe methodology comments
- illustrative demo code using synthetic inputs
- aggregate performance snapshots from actual research runs

## What Will Not Be Shared

- proprietary signal generation code
- satellite processing workflows
- raw datasets or database exports
- credentials, API keys, or infrastructure details
- client-specific locations, assets, or outputs
- production model weights, features, or database schemas
- raw trade logs or unreleased signal feeds

## Disclaimer

This repository is for research communication only. It is not investment advice, a trading recommendation, or an offer to buy or sell any asset.
