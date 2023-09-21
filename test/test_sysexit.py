# https://docs.pytest.org/en/7.4.x/getting-started.html#run-multiple-tests
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
