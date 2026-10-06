# fungod

周易六十四卦占卜工具：用大衍之数算法模拟蓍草占卜过程，生成一个六爻卦象，再查表输出卦名和卦辞。

注意：该包**未发布到 PyPI**，只能从源码安装。

## 安装

未发布到 PyPI，需要从源码安装，推荐用 [uv](https://docs.astral.sh/uv/) 管理虚拟环境与依赖：

```bash
git clone https://github.com/farfarfun/fungod.git
cd fungod
uv sync              # 创建虚拟环境并安装运行时 + 开发依赖
uv run pytest        # 运行测试
```

也可以只装运行时依赖并以当前目录作为包安装：

```bash
uv pip install .
```

## 用法示例

```python
from fungod.changes.b_changes import godwill

# 执行一次占卜，返回 (卦象编码, 卦名信息, 卦辞原文)。结果会随随机状态变化。
key, name, solution = godwill()
print(key)  # 形如 'i_101011' 的六位爻象编码
print(name)  # 对应卦象的 [卦名, 别名, 断语]
print(solution)  # 该卦的卦辞原文
```

也可以直接查表：

```python
from fungod.conf.gua_ci import gua_ci  # 六十四卦卦名/断语字典
from fungod.data.gua_ci.gwill_solution import solution_dict  # 每一卦的原文/白话解读

print(gua_ci["i_111111"])  # ['乾卦', '乾为天', '刚健中正']
print(solution_dict["i_111111"])  # 乾卦原文
```

`fungod/conf/gua_ci.py` 和 `fungod/data/gua_ci/gwill_solution.py` 这两个数据模块可以正常单独导入使用。

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
