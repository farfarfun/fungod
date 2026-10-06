"""Deprecated compatibility module for :mod:`fungod.conf.gua_ci`."""

import warnings

from fungod.conf.gua_ci import gua_ci

warnings.warn(
    "fungod.conf.GuaCi is deprecated; use fungod.conf.gua_ci instead. It will be removed in 1.0.0.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["gua_ci"]
