"""公开 API 的正常路径与边界测试。"""

from unittest.mock import MagicMock

from fungod.changes.b_changes import BChanges, godwill
from fungod.conf.gua_ci import gua_ci
from fungod.data.gua_ci.gwill_solution import solution_dict


def test_import():
    import fungod  # noqa: F401


def test_gua_ci_and_solution_dict_cover_all_64_hexagrams():
    """卦名表与卦辞表应各自覆盖全部 64 个卦象编码，且键完全一致。"""
    assert len(gua_ci) == 64
    assert len(solution_dict) == 64
    assert set(gua_ci) == set(solution_dict)
    for key, value in gua_ci.items():
        assert key.startswith("i_") and len(key) == 8
        assert len(value) == 3


def test_bchanges_yoyo_returns_positive_multiple_of_quarter():
    bc = BChanges()
    result = bc.yoyo(1)
    assert result > 0
    assert result == int(result)


def test_bchanges_yoyo_seed_zero_is_treated_as_ten():
    """seed=0 时内部替换为 10，避免 random.randrange 因 step=0 报错。"""
    bc = BChanges()
    result = bc.yoyo(0)
    assert result > 0


def test_godwill_without_seeds_returns_valid_hexagram():
    key, name, solution = godwill()
    assert key in gua_ci
    assert name == gua_ci[key]
    assert solution == solution_dict[key]


def test_godwill_with_partial_seeds_pads_remaining_yao():
    """种子数少于 6 个时，剩余爻应自动用种子 0 补齐，不应抛异常。"""
    key, name, solution = godwill([1, 2, 3])
    assert key.startswith("i_") and len(key) == 8
    assert name == gua_ci[key]
    assert solution == solution_dict[key]


def test_godwill_with_extra_seeds_only_uses_first_six():
    """种子数多于 6 个时只取前 6 个，不应抛异常。"""
    key, _, _ = godwill([1, 2, 3, 4, 5, 6, 7, 8])
    assert key in gua_ci


def test_bchanges_change_normal_path_carries_remainder_into_human():
    """天、地余数非零时应各自扣除余数并计入人部分。"""
    bc = BChanges()
    sky, land, human = bc.change(sky=10, land=10, human=0)
    assert (sky, land, human) == (8, 8, 4)


def test_bchanges_change_boundary_when_remainder_is_zero():
    """天、地恰好整除 4 时，按规则扣 4（而非 0）并计入人部分。"""
    bc = BChanges()
    sky, land, human = bc.change(sky=8, land=8, human=0)
    assert (sky, land, human) == (4, 4, 8)


def test_bchanges_chaos_splits_grass_and_keeps_total_invariant():
    """chaos 应把 grass 分成天、地两部分，人固定为 1（挂一），三者之和为 grass。"""
    bc = BChanges()
    grass = 49
    sky, land, human = bc.chaos(grass, seed=10)
    assert human == 1
    assert 1 <= sky < grass
    assert sky + land + human == grass


def test_bchanges_draw_yo_yang_line_forwards_full_segment():
    """阳爻（yo != 0）应落笔画一条完整通线（一次 forward(200)），与 DrawGossip.draw_yo 的约定一致。"""
    bc = BChanges()
    pen = MagicMock()

    bc.draw_yo(yo=1, pen=pen, x=1, y=2)

    pen.forward.assert_called_once_with(200)
    pen.goto.assert_called_once_with(1, 2)


def test_bchanges_draw_yo_yin_line_forwards_two_broken_segments():
    """阴爻（yo == 0）应画断开的两段线（两次 forward(90)）。"""
    bc = BChanges()
    pen = MagicMock()

    bc.draw_yo(yo=0, pen=pen, x=0, y=0)

    assert pen.forward.call_args_list == [((90,),), ((90,),)]
    pen.goto.assert_any_call(0, 0)
