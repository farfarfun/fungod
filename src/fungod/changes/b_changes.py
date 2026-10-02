"""大衍之数起卦算法：模拟蓍草占卜的分二、挂一、揲四、归奇过程，生成六爻卦象。"""

from __future__ import annotations

import random
from typing import Any

from farlog import getLogger

from fungod.conf.gua_ci import gua_ci
from fungod.data.gua_ci.gwill_solution import solution_dict

logger = getLogger("fungod")


def godwill(seeds: list[int] | None = None) -> tuple[str, list[str], str]:
    """执行一次完整的周易占卜（六爻大衍之数起卦），返回卦象与卦辞。

    Args:
        seeds: 起卦用的随机种子列表，每个种子对应一爻；最多使用前 6 个，
            不足 6 个时其余爻用种子 0 补齐；为 ``None`` 时全部使用种子 0。

    Returns:
        三元组 ``(卦象编码, 卦名信息, 卦辞原文)``：
        - 卦象编码：形如 ``"i_111111"`` 的六位二进制编码
        - 卦名信息：``[卦名, 别名, 断语]``，取自 :data:`fungod.conf.gua_ci.gua_ci`
        - 卦辞原文：取自 :data:`fungod.data.gua_ci.gwill_solution.solution_dict`
    """
    bc = BChanges()
    seed_list = list(seeds) if seeds else []
    yoyo: list[float] = []
    for seed in seed_list[:6]:
        yoyo.append(bc.yoyo(int(seed)))
    while len(yoyo) < 6:
        yoyo.append(bc.yoyo(0))

    gwill_key = "i_" + "".join(str(int(yo) & 1) for yo in yoyo)
    gwill_name = gua_ci[gwill_key]
    gwill_solution = solution_dict[gwill_key]

    logger.info("卦象编码: %s, 卦名: %s", gwill_key, gwill_name)

    return gwill_key, gwill_name, gwill_solution


class BChanges:
    """大衍之数算法的核心实现：模拟蓍草分二、挂一、揲四、归奇的起卦过程。"""

    def yoyo(self, seed: int) -> float:
        """完成一爻的三变过程，返回该爻的策数（除以 4 后的值）。

        Args:
            seed: 随机种子；传入 0 时内部替换为 10，避免 ``random.randrange`` 报错。

        Returns:
            该爻的策数（4 的倍数除以 4 后的结果）。
        """
        if seed == 0:
            seed = 10
        # 第一变
        sky, land, human = self.chaos(49, seed)
        sky, land, human = self.change(sky, land, human)
        grass = sky + land
        # 第二变
        sky, land, human = self.chaos(grass, seed)
        sky, land, human = self.change(sky, land, human)
        grass = sky + land
        # 第三变
        sky, land, human = self.chaos(grass, seed)
        sky, land, human = self.change(sky, land, human)
        grass = sky + land
        return grass / 4

    def change(self, sky: int, land: int, human: int) -> tuple[int, int, int]:
        """一变：天、地两部分各自揲四归奇，余数归入人部分。

        Args:
            sky: 天部分算子数。
            land: 地部分算子数。
            human: 人部分（挂一）算子数。

        Returns:
            变化后的 ``(天, 地, 人)`` 三元组。
        """
        sky_change = sky % 4
        land_change = land % 4
        if sky_change == 0:
            sky_change = 4
        sky = sky - sky_change
        human = human + sky_change
        if land_change == 0:
            land_change = 4
        land = land - land_change
        human = human + land_change
        return sky, land, human

    def chaos(self, grass: int, seed: int) -> tuple[int, int, int]:
        """混沌初开：将 ``grass`` 颗算子随机分为天、地两部分，并挂一为人。

        Args:
            grass: 当前参与分二的算子总数。
            seed: 随机种子，作为 ``random.randrange`` 的步长。

        Returns:
            ``(天, 地, 人)`` 三元组，其中人固定为 1（挂一）。
        """
        sky = random.randrange(1, grass, seed)
        land = grass - sky - 1
        human = 1
        return sky, land, human

    def draw_yo(self, yo: int, pen: Any, x: float, y: float) -> None:
        """用 turtle 画笔在 ``(x, y)`` 处绘制一爻。

        Args:
            yo: 爻的类型，0 为阴爻（断开的两段线），其他为阳爻（一条通线）。
            pen: 具备 ``turtle.Turtle`` 接口的画笔对象。
            x: 起始横坐标。
            y: 起始纵坐标。
        """
        if yo == 0:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.forward(90)
            pen.penup()
            pen.goto(x + 20, y)
            pen.pendown()
            pen.forward(90)
        else:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.forward(200)
