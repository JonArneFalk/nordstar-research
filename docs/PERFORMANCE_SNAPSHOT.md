# Performance Snapshot

Last reviewed: 2026-06-15

This page summarizes selected public-safe performance evidence from Nordstar's commodity research stack. The figures below are based on internal research runs and are shared for technical credibility. They are not investment advice and do not represent live trading returns.

## TTF European Gas

Source: MomentumAlpha Modal TTF snapshot run, dated 2026-05-24.

Evaluation setup:

- Instrument: TTF European Gas
- Horizon: 10 trading days
- Training window: 2020-01-01 to 2024-12-31
- Test window: 2025-01-01 onward
- Validation style: strict out-of-sample snapshot plus walk-forward review
- Risk controls: volatility filter, storage regime filter, model agreement, confidence sizing

Best strict out-of-sample snapshot:

| Metric | Value |
|---|---:|
| Rank IC | +0.1098 |
| Hit rate | 50.9% |
| Sharpe | +1.28 |
| Max drawdown | -10.9% |
| Total return | +36.8% |
| Active time | 72.1% |

Walk-forward check on the same candidate configuration:

| Metric | Value |
|---|---:|
| Folds | 11 |
| Avg Rank IC | +0.0160 |
| Avg hit rate | 49.8% |
| Avg Sharpe | -0.03 |
| Worst fold drawdown | -33.4% |
| Folds with IC > 5% | 4 / 11 |

Interpretation: the strict out-of-sample TTF candidate is promising, but the walk-forward review is much flatter. Public communication should emphasize that this is an active research candidate, not a finished live trading product.

## Gold

Source: local MomentumAlpha walk-forward baseline evaluation on `GC=F`, run 2026-06-15.

Evaluation setup:

- Instrument: Gold futures
- Horizon: 20 trading days
- Data window: 2006-01-03 to 2026-05-14
- Test window: 2015-03-02 to 2026-05-14
- Validation style: chronological walk-forward
- Feature scope: price and cross-asset baseline features only

Baseline walk-forward result:

| Metric | Value |
|---|---:|
| AUC | 0.594 |
| Hit rate | 53.9% |
| IC | +0.215 |
| Sharpe | +0.335 |
| Max drawdown | -85.4% |
| Active time | 89.7% |

Interpretation: Gold shows directional signal quality in the baseline evaluation, but the drawdown profile is not publication-grade as a standalone trading system. It is better positioned as a research candidate pending stronger regime filters and paper-trading logs.

## Paper-Trading Rules

Current public-safe rules from the paper-trading engine:

- Starting capital: EUR 8,000
- Fees: 0.10%
- Slippage: 0.05%
- Maximum holding period: 25 days
- Default minimum confidence: 0.30
- Maximum leverage: 2.0x globally, with per-asset caps
- Position sizing: confidence/risk-tier based
- Exits: max holding period, trailing stop, and model-driven exit actions

Selected per-asset paper profiles:

| Asset | Tier | Min confidence | Risk budget | Max leverage |
|---|---:|---:|---:|---:|
| TTF | Watch | 0.62 | 12% | 1.0x |
| Gold | Research | 0.65 | 5% | 1.0x |

## Publication Caveat

The strongest public claim today is not "live profitable trading." The stronger and more defensible claim is:

> Nordstar is building a disciplined commodity research stack with walk-forward validation, paper-trading infrastructure, explicit risk controls, and early evidence of signal quality in TTF gas and gold.

