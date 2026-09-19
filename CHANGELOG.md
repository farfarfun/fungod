# Changelog

## [Unreleased]

### 新增

- 补充 `tests/` 下的公开 API 测试，覆盖 `godwill()`、`BChanges.yoyo()` 的正常路径与边界（种子 0、种子不足/超量）。

### 修复

- 修复 `fungod/changes/b_changes.py`（原 `BChanges.py`）中残留的历史导入 `from gwill.conf.GuaCi import *`，改为 `from fungod.conf.gua_ci import gua_ci`；`godwill()` 此前会直接抛出 `ModuleNotFoundError: No module named 'gwill'`，现已可正常调用。
- 修复 `example/fungod_test.py`（原 `example/notegod_test.py`）中同样残留的 `gwill` 导入。
- 修复 README 中用法示例的错误路径：`fungod/changes/GuaCi.py` 实际不存在，正确路径为 `fungod/conf/gua_ci.py`。
- 移除模块导入时读取 `sys.argv` 并 `print` 的副作用（原 `BChanges.py` 顶层代码），改为 `godwill(seeds: list[int] | None = None)` 显式参数，避免 import 时产生不可控的诊断输出。

### 变更

- **Breaking**：包改名历史（`notegod` → `fungod`）延续自此前版本，导入名与 PyPI 发布名统一为 `fungod`；`notegod` 从未发布到 PyPI（确认 `pypi.org/pypi/notegod/json` 返回 404），无需发转发版本。
- 源码目录迁移为标准 `src/fungod/` 布局（原顶层 `fungod/`）。
- 模块与公开方法统一改为 snake_case：`BChanges.py` → `changes/b_changes.py`、`DrawGossip.py` → `changes/draw_gossip.py`、`GuaCi.py` → `conf/gua_ci.py`；`drawYo` → `draw_yo`、`drawGossip` → `draw_gossip`、`drawOctagonalLine` → `draw_octagonal_line`、`getScreen` → `get_screen`、`closeWindow` → `close_window`。
- 日志改用 `farlog`，替换原有的 `print()` 诊断输出。
- 为所有公开类、函数、方法补充类型标注（3.10 风格）与中文 docstring。
- 依赖调整：移除未使用的 `readme-renderer`（无版本下限且源码中未被引用），改为声明 `farlog>=1.1.8`。
- 提交 `uv.lock` 以保证可复现构建。

### 废弃

- 无。
