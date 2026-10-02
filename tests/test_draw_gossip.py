"""DrawGossip 公开方法的测试：用 mock 画笔隔离真实 turtle/tkinter GUI。"""

from unittest.mock import MagicMock

import pytest

# `turtle` 模块在 import 时会拉起 `tkinter`；没有安装 tkinter（例如精简服务器环境）
# 时整个模块都无法导入，这里按环境优雅跳过，而不是让测试报错。
pytest.importorskip("tkinter")

from fungod.changes.draw_gossip import DrawGossip  # noqa: E402


def _make_drawer() -> tuple[DrawGossip, MagicMock]:
    """构造一个绑定 mock 画笔的 DrawGossip，避免真实弹出绘图窗口。"""
    raw_pen = MagicMock(name="raw_pen")
    drawer = DrawGossip(raw_pen)
    # __init__ 内部用 pen.clone() 的返回值作为真正使用的画笔
    cloned_pen = raw_pen.clone.return_value
    return drawer, cloned_pen


def test_draw_yo_yang_line_draws_single_forward_segment():
    """阳爻（yo == 1）应画一条通线：只前进一次、颜色为黄底红边。"""
    drawer, pen = _make_drawer()
    pen.reset_mock()

    drawer.draw_yo(1)

    pen.color.assert_called_once_with("yellow", "red")
    pen.forward.assert_called_once_with(200)


def test_draw_yo_yin_line_draws_two_broken_segments():
    """阴爻（yo != 1）应画断开的两段线：前进两次、颜色为黑底红边。"""
    drawer, pen = _make_drawer()
    pen.reset_mock()

    drawer.draw_yo(0)

    pen.color.assert_called_once_with("black", "red")
    assert pen.forward.call_args_list == [((90,),), ((90,),)]


def test_draw_gossip_draws_all_six_lines_and_finishes_fill():
    """draw_gossip 应依次绘制六爻并在结束后收尾填充、隐藏画笔。"""
    drawer, pen = _make_drawer()
    pen.reset_mock()

    drawer.draw_gossip(1, 0, 1, 0, 1, 0)

    # 6 条爻线，每条至少 1 次 forward（阳爻 1 次、阴爻 2 次）：1+2+1+2+1+2 = 9
    assert pen.forward.call_count == 9
    pen.end_fill.assert_called_once()
    pen.hideturtle.assert_called_once()


def test_draw_octagonal_line_draws_each_side_and_binds_close_handler():
    """绘制正多边形应前进/转向 lines_count 次，并绑定空格键关闭窗口。"""
    drawer, pen = _make_drawer()
    pen.reset_mock()
    screen = pen.getscreen.return_value

    drawer.draw_octagonal_line(side_length=50, lines_count=4)

    assert pen.forward.call_count == 4
    assert pen.right.call_count == 4
    pen.hideturtle.assert_called_once()
    screen.onkey.assert_called_once_with(drawer.close_window, "space")
    screen.listen.assert_called_once()


def test_get_screen_returns_pen_screen():
    """get_screen 应直接透传画笔所在的 turtle 屏幕对象。"""
    drawer, pen = _make_drawer()

    result = drawer.get_screen()

    assert result is pen.getscreen.return_value


def test_close_window_raises_system_exit():
    """close_window 调用 tkinter 的 `_exit`，预期以 SystemExit 结束事件循环。"""
    drawer, _pen = _make_drawer()

    with pytest.raises(SystemExit):
        drawer.close_window()
