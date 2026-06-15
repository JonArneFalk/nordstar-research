"""Run the public-safe Nordstar Research demo.

Usage:
    python examples/run_public_demo.py
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from nordstar_public import rank_assets_by_momentum, retail_activity_index
from nordstar_public.retail_demo import RetailActivityInputs
from nordstar_public.validation import walk_forward_splits


def main() -> None:
    synthetic_prices = {
        "TTF_NATURAL_GAS": [31.0, 32.5, 32.2, 34.8, 35.6, 37.1],
        "URANIUM": [88.0, 89.2, 91.5, 90.4, 92.8, 94.0],
        "COCOA": [7200.0, 7100.0, 7350.0, 7600.0, 7550.0, 7800.0],
    }

    print("Momentum demo ranking")
    for item in rank_assets_by_momentum(synthetic_prices):
        print(
            f"- {item.asset}: score={item.score:.2f}, "
            f"return={item.lookback_return:.1%}, vol={item.volatility:.1%}"
        )

    retail_signal = retail_activity_index(
        RetailActivityInputs(
            parking_activity_proxy=0.68,
            catchment_strength=0.74,
            competition_pressure=0.42,
            data_quality=0.81,
        )
    )

    print("\nRetail activity demo")
    print(
        f"- index={retail_signal.activity_index:.2f}, "
        f"confidence={retail_signal.confidence:.2f}, "
        f"interpretation={retail_signal.interpretation}"
    )

    print("\nWalk-forward folds")
    for split in walk_forward_splits(sample_count=24, train_size=12, test_size=4):
        print(
            f"- train=[{split.train_start}:{split.train_end}) "
            f"test=[{split.test_start}:{split.test_end})"
        )


if __name__ == "__main__":
    main()
