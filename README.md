# fungod

周易六十四卦占卜工具：用大衍之数算法模拟蓍草占卜过程，生成一个六爻卦象，再查表输出卦名和卦辞。

注意：该包**未发布到 PyPI**，只能从源码安装。

## 安装

未发布到 PyPI，需要从源码安装：

```bash
git clone https://github.com/farfarfun/fungod.git
cd fungod
pip install .
```

## 用法示例

```python
from fungod.conf.GuaCi import gua_ci          # 六十四卦卦名/卦象字典
from fungod.data.gua_ci.gwill_solution import solution_dict  # 每一卦的原文/白话解读

print(gua_ci["i_111111"])   # ['乾卦', '乾为天', '刚健中正']
print(solution_dict["i_111111"])
```

`fungod/changes/GuaCi.py` 和 `fungod/data/gua_ci/gwill_solution.py` 这两个数据模块可以正常单独导入使用。

已知问题：`fungod/changes/BChanges.py`（对外暴露的占卜入口 `godwill()` 以及 `BChanges` 类所在文件）顶部残留了一处历史导入 `from gwill.conf.GuaCi import *`，指向一个不存在的 `gwill` 包（应为 `fungod`），导致目前 `from fungod.changes.BChanges import godwill` 会直接抛出 `ModuleNotFoundError: No module named 'gwill'`，这部分占卜功能和基于 `turtle` 的卦象绘图（`DrawGossip.py`）暂时无法使用，需要修复导入路径。
