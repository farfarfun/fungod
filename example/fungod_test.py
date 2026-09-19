"""最小可运行示例：调用公开入口 godwill() 完成一次占卜。"""


class TestFunGod:
    def test_godwill(self):
        from fungod.changes.b_changes import godwill

        key, name, solution = godwill()
        assert key.startswith("i_")
        assert name
        assert solution
