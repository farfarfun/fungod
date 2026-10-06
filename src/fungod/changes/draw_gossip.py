"""基于 turtle 的卦象绘图：把六爻绘制为图形，并支持绘制正多边形装饰线。"""

from __future__ import annotations

import warnings
from turtle import TK, Turtle, TurtleScreen


class DrawGossip:
    """用 turtle 画笔绘制六爻卦象。"""

    def __init__(self, pen: Turtle) -> None:
        """克隆传入的画笔并初始化绘图状态。

        Args:
            pen: 作为绘图起点的 ``turtle.Turtle`` 实例，内部会被克隆使用。
        """
        self.pen = pen.clone()
        self.pen.showturtle()
        self.pen.speed(1)
        self.pen.begin_fill()

    def draw_gossip(self, yo1: int, yo2: int, yo3: int, yo4: int, yo5: int, yo6: int) -> None:
        """自下而上绘制六爻，每爻下移 10 像素。

        Args:
            yo1: 初爻类型（0 为阴爻，其他为阳爻）。
            yo2: 二爻类型。
            yo3: 三爻类型。
            yo4: 四爻类型。
            yo5: 五爻类型。
            yo6: 上爻类型。
        """
        self.draw_yo(yo1)
        self.pen.penup()
        self.pen.goto(x=0, y=-10)
        self.draw_yo(yo2)
        self.pen.penup()
        self.pen.goto(x=0, y=-20)
        self.draw_yo(yo3)
        self.pen.penup()
        self.pen.goto(x=0, y=-30)
        self.draw_yo(yo4)
        self.pen.penup()
        self.pen.goto(x=0, y=-40)
        self.draw_yo(yo5)
        self.pen.penup()
        self.pen.goto(x=0, y=-50)
        self.draw_yo(yo6)
        self.pen.end_fill()
        self.pen.hideturtle()

    def draw_yo(self, yo: int) -> None:
        """绘制一爻：阳爻为一条通线，阴爻为断开的两段线。

        Args:
            yo: 爻的类型，1 为阳爻，其他为阴爻。
        """
        self.pen.pensize(5)
        if yo == 1:
            self.pen.color("yellow", "red")
            self.pen.pendown()
            self.pen.forward(200)
        else:
            self.pen.color("black", "red")
            self.pen.pendown()
            self.pen.forward(90)
            self.pen.penup()
            self.pen.setx(x=110)
            self.pen.pendown()
            self.pen.forward(90)

    def draw_octagonal_line(self, side_length: float, lines_count: float) -> None:
        """绘制一个正多边形装饰线，并绑定空格键关闭窗口。

        Args:
            side_length: 每条边的长度（像素）。
            lines_count: 边的数量。
        """
        self.pen.pensize(1)
        degree = 360 / lines_count
        for _ in range(int(lines_count)):
            self.pen.forward(side_length)
            self.pen.right(degree)
        self.pen.hideturtle()
        screen = self.pen.getscreen()
        screen.onkey(self.close_window, "space")
        screen.listen()

    def get_screen(self) -> TurtleScreen:
        """返回当前画笔所在的 ``turtle`` 屏幕对象。"""
        return self.pen.getscreen()

    def close_window(self) -> None:
        """关闭 turtle 绘图窗口。"""
        TK._exit(0)

    def drawGossip(self, yo1: int, yo2: int, yo3: int, yo4: int, yo5: int, yo6: int) -> None:
        """Deprecated compatibility wrapper for :meth:`draw_gossip`."""
        warnings.warn(
            "DrawGossip.drawGossip() is deprecated; use DrawGossip.draw_gossip() instead. It will be removed in 1.0.0.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.draw_gossip(yo1, yo2, yo3, yo4, yo5, yo6)

    def drawOctagonalLine(self, side_length: float, lines_count: float) -> None:
        """Deprecated compatibility wrapper for :meth:`draw_octagonal_line`."""
        warnings.warn(
            "DrawGossip.drawOctagonalLine() is deprecated; use "
            "DrawGossip.draw_octagonal_line() instead. It will be removed in 1.0.0.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.draw_octagonal_line(side_length, lines_count)

    def getScreen(self) -> TurtleScreen:
        """Deprecated compatibility wrapper for :meth:`get_screen`."""
        warnings.warn(
            "DrawGossip.getScreen() is deprecated; use DrawGossip.get_screen() instead. It will be removed in 1.0.0.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.get_screen()

    def closeWindow(self) -> None:
        """Deprecated compatibility wrapper for :meth:`close_window`."""
        warnings.warn(
            "DrawGossip.closeWindow() is deprecated; use DrawGossip.close_window() instead. "
            "It will be removed in 1.0.0.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.close_window()


def main() -> str:
    """交互式绘制一个正多边形装饰线，供手动调试使用。"""
    gossip = DrawGossip(Turtle())
    side_length = gossip.get_screen().numinput("边长", "请输入边长（像素值）：", 0, 1, 500)
    lines_count = gossip.get_screen().numinput("边数", "多边形边的数量：", 3, 3, 100)
    gossip.draw_octagonal_line(side_length, lines_count)
    return "EVENTLOOP"
