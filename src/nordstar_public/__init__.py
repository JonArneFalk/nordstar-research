"""Public-safe Nordstar Research demo utilities.

These modules are illustrative only. They do not contain proprietary data,
production signal logic, satellite workflows, or database integrations.
"""

__all__ = [
    "momentum_score",
    "rank_assets_by_momentum",
    "retail_activity_index",
    "walk_forward_splits",
]

from .momentum_demo import momentum_score, rank_assets_by_momentum
from .retail_demo import retail_activity_index
from .validation import walk_forward_splits
