"""Public-safe momentum signal demo.

This is a toy example for communication purposes. It is not the production
research engine and does not include proprietary features, weights, data
sources, or portfolio construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, pstdev


@dataclass(frozen=True)
class AssetMomentum:
    """Simple public-facing momentum score."""

    asset: str
    lookback_return: float
    volatility: float
    score: float


def percentage_returns(prices: list[float]) -> list[float]:
    """Convert a price series into simple returns."""

    if len(prices) < 2:
        raise ValueError("At least two prices are required")
    if any(price <= 0 for price in prices):
        raise ValueError("Prices must be positive")

    return [
        (current / previous) - 1.0
        for previous, current in zip(prices[:-1], prices[1:])
    ]


def momentum_score(asset: str, prices: list[float]) -> AssetMomentum:
    """Score one asset with a generic return-over-volatility heuristic."""

    returns = percentage_returns(prices)
    lookback_return = (prices[-1] / prices[0]) - 1.0
    volatility = pstdev(returns) if len(returns) > 1 else 0.0

    # Public demo only: production research uses private feature sets.
    score = lookback_return / volatility if volatility > 0 else lookback_return

    return AssetMomentum(
        asset=asset,
        lookback_return=lookback_return,
        volatility=volatility,
        score=score,
    )


def rank_assets_by_momentum(price_history: dict[str, list[float]]) -> list[AssetMomentum]:
    """Rank assets by the public demo momentum score."""

    if not price_history:
        raise ValueError("price_history cannot be empty")

    scored_assets = [
        momentum_score(asset=asset, prices=prices)
        for asset, prices in price_history.items()
    ]
    average_score = mean(item.score for item in scored_assets)

    return sorted(
        (
            AssetMomentum(
                asset=item.asset,
                lookback_return=item.lookback_return,
                volatility=item.volatility,
                score=item.score - average_score,
            )
            for item in scored_assets
        ),
        key=lambda item: item.score,
        reverse=True,
    )
