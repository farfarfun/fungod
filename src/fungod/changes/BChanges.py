"""Deprecated compatibility module for :mod:`fungod.changes.b_changes`."""

import warnings

from fungod.changes.b_changes import BChanges, godwill

warnings.warn(
    "fungod.changes.BChanges is deprecated; use fungod.changes.b_changes instead. It will be removed in 1.0.0.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["BChanges", "godwill"]
