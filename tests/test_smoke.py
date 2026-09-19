"""公开 API 的正常路径与边界测试。"""

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
