# Changelog

## [Unreleased]

### 新增

- 补充 `tests/` 下的公开 API 测试，覆盖 `godwill()`、`BChanges.yoyo()` 的正常路径与边界（种子 0、种子不足/超量）。
- 补充 `BChanges.change`、`BChanges.chaos`、`BChanges.draw_yo` 及 `DrawGossip` 全部公开方法的测试（绘图类用 mock 画笔隔离真实 turtle/tkinter GUI）。
- 开发依赖加入 `ruff`，并补充 `[tool.ruff]` 配置；README 安装方式改为基于 `uv` 的说明（`uv sync` / `uv run pytest`）。

### 修复

- 修复 `fungod/changes/b_changes.py`（原 `BChanges.py`）中残留的历史导入 `from gwill.conf.GuaCi import *`，改为 `from fungod.conf.gua_ci import gua_ci`；`godwill()` 此前会直接抛出 `ModuleNotFoundError: No module named 'gwill'`，现已可正常调用。
- 修复 `example/fungod_test.py`（原 `example/notegod_test.py`）中同样残留的 `gwill` 导入。
- 修复 README 中用法示例的错误路径：`fungod/changes/GuaCi.py` 实际不存在，正确路径为 `src/fungod/conf/gua_ci.py`。
- 修复 README 末尾数据模块说明里的仓库路径：源码迁为 `src/` 布局后，`fungod/conf/gua_ci.py`、`fungod/data/gua_ci/gwill_solution.py` 在仓库里定位不到，改为带 `src/` 前缀的真实路径。
- 移除模块导入时读取 `sys.argv` 并 `print` 的副作用（原 `BChanges.py` 顶层代码），改为 `godwill(seeds: list[int] | None = None)` 显式参数，避免 import 时产生不可控的诊断输出。
- 删除过期的 `script/__version__.md`（`0.0.2`，与 `pyproject.toml` 的 `0.0.3` 不一致），版本号统一以 `pyproject.toml` 为唯一来源。
- `DrawGossip.get_screen` 补充返回类型标注 `TurtleScreen`。
- 修复 `BChanges.draw_yo` 阴阳爻判断与实现相反的 bug：`yo == 0`（阴爻）此前错误地画成单条通线，非 0（阳爻）反而画成断开两段线，与同文件 docstring、`godwill()` 的编码约定（`int(yo) & 1`）及 `DrawGossip.draw_yo` 的既有约定相矛盾；该方法此前无测试覆盖，也未被生产代码调用。
- `godwill()` 的结果日志误用 stdlib logging 的 `%s` 占位符，farlog（loguru）不支持该语法，参数被静默丢弃、日志里只剩字面量 `%s`；改为 `{}` 占位符。

### 变更

- **Breaking**：包改名历史（`notegod` → `fungod`）延续自此前版本，导入名与 PyPI 发布名统一为 `fungod`；`notegod` 从未发布到 PyPI（确认 `pypi.org/pypi/notegod/json` 返回 404），无需发转发版本。
- 源码目录迁移为标准 `src/fungod/` 布局（原顶层 `fungod/`）。
- 模块与公开方法统一改为 snake_case：`BChanges.py` → `changes/b_changes.py`、`DrawGossip.py` → `changes/draw_gossip.py`、`GuaCi.py` → `conf/gua_ci.py`；`drawYo` → `draw_yo`、`drawGossip` → `draw_gossip`、`drawOctagonalLine` → `draw_octagonal_line`、`getScreen` → `get_screen`、`closeWindow` → `close_window`。
- 日志改用 `farlog`，替换原有的 `print()` 诊断输出。
- 为所有公开类、函数、方法补充类型标注（3.10 风格）与中文 docstring。
- 兼容模块 `BChanges.py`、`DrawGossip.py`、`GuaCi.py` 的模块 docstring 由英文改为中文，与仓库其余模块的注释语言保持一致（弃用迁移信息保留）。
- 依赖调整：移除未使用的 `readme-renderer`（无版本下限且源码中未被引用），改为声明 `farlog>=1.1.8`。
- 停止跟踪 `uv.lock`；构建依赖由 `pyproject.toml` 中的声明管理。

### 废弃

- 旧模块路径 `fungod.changes.BChanges`、`fungod.changes.DrawGossip`、`fungod.conf.GuaCi` 仍可导入，但会发出 `DeprecationWarning`，请分别迁移到 `b_changes`、`draw_gossip`、`gua_ci`。
- `BChanges.drawYo`、`DrawGossip.drawGossip`、`DrawGossip.drawOctagonalLine`、`DrawGossip.getScreen` 和 `DrawGossip.closeWindow` 仍可调用，但会发出 `DeprecationWarning`；请改用相应的 snake_case 名称。上述兼容接口将在 `1.0.0` 移除。
