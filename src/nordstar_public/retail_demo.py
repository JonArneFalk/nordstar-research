"""Public-safe retail real estate signal demo.

This file shows how a high-level index can be communicated. It deliberately
does not include satellite processing, location extraction, computer vision,
PostGIS queries, or proprietary feature engineering.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RetailActivityInputs:
    """Synthetic public-safe inputs for a retail activity index."""

    parking_activity_proxy: float
    catchment_strength: float
    competition_pressure: float
    data_quality: float


@dataclass(frozen=True)
class RetailActivitySignal:
    """High-level public-facing retail intelligence output."""

    activity_index: float
    confidence: float
    interpretation: str


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def retail_activity_index(inputs: RetailActivityInputs) -> RetailActivitySignal:
    """Create a simple synthetic retail activity score."""

    parking_component = 0.45 * clamp(inputs.parking_activity_proxy)
    catchment_component = 0.35 * clamp(inputs.catchment_strength)
    competition_component = 0.20 * (1.0 - clamp(inputs.competition_pressure))

    activity_index = clamp(
        parking_component + catchment_component + competition_component
    )
    confidence = clamp(inputs.data_quality)

    if activity_index >= 0.67:
        interpretation = "high relative activity"
    elif activity_index >= 0.40:
        interpretation = "moderate relative activity"
    else:
        interpretation = "low relative activity"

    return RetailActivitySignal(
        activity_index=activity_index,
        confidence=confidence,
        interpretation=interpretation,
    )
