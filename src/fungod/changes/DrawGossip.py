"""Deprecated compatibility module for :mod:`fungod.changes.draw_gossip`."""

import warnings

from fungod.changes.draw_gossip import DrawGossip, main

warnings.warn(
    "fungod.changes.DrawGossip is deprecated; use fungod.changes.draw_gossip instead. It will be removed in 1.0.0.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["DrawGossip", "main"]
