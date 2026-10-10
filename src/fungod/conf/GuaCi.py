"""已弃用的兼容模块：请改用 :mod:`fungod.conf.gua_ci`，本模块将于 1.0.0 移除。"""

import warnings

from fungod.conf.gua_ci import gua_ci

warnings.warn(
    "fungod.conf.GuaCi is deprecated; use fungod.conf.gua_ci instead. It will be removed in 1.0.0.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["gua_ci"]
