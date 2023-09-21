# https://docs.pytest.org/en/7.4.x/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions
import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
