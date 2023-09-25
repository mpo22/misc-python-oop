# pylint: skip-file
# content of test_class.py


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        self.x = "hello"
        assert hasattr(self, "x")
