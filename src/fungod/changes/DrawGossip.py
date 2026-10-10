"""已弃用的兼容模块：请改用 :mod:`fungod.changes.draw_gossip`，本模块将于 1.0.0 移除。"""

import warnings

from fungod.changes.draw_gossip import DrawGossip, main

warnings.warn(
    "fungod.changes.DrawGossip is deprecated; use fungod.changes.draw_gossip instead. It will be removed in 1.0.0.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["DrawGossip", "main"]
