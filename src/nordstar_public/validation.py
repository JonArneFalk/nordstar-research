"""Small public-safe validation helpers.

The core principle is chronological evaluation. This avoids look-ahead bias and
keeps public examples aligned with how serious time-series research should be
communicated.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Sequence


@dataclass(frozen=True)
class WalkForwardSplit:
    """Index ranges for a single walk-forward fold."""

    train_start: int
    train_end: int
    test_start: int
    test_end: int


def walk_forward_splits(
    sample_count: int,
    train_size: int,
    test_size: int,
    step_size: int | None = None,
) -> list[WalkForwardSplit]:
    """Create chronological train/test folds.

    This helper is intentionally generic. It demonstrates validation discipline
    without exposing proprietary model logic.
    """

    if sample_count <= 0:
        raise ValueError("sample_count must be positive")
    if train_size <= 0 or test_size <= 0:
        raise ValueError("train_size and test_size must be positive")

    step = step_size or test_size
    if step <= 0:
        raise ValueError("step_size must be positive")

    splits: list[WalkForwardSplit] = []
    train_start = 0

    while True:
        train_end = train_start + train_size
        test_start = train_end
        test_end = test_start + test_size
        if test_end > sample_count:
            break

        splits.append(
            WalkForwardSplit(
                train_start=train_start,
                train_end=train_end,
                test_start=test_start,
                test_end=test_end,
            )
        )
        train_start += step

    return splits


def rmse(actual: Sequence[float], predicted: Sequence[float]) -> float:
    """Root mean squared error for public demo diagnostics."""

    if len(actual) != len(predicted):
        raise ValueError("actual and predicted must have the same length")
    if not actual:
        raise ValueError("actual cannot be empty")

    squared_errors = [(a - p) ** 2 for a, p in zip(actual, predicted)]
    return sqrt(sum(squared_errors) / len(squared_errors))
