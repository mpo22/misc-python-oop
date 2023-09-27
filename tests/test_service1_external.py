from pytest_mock import MockerFixture

from oop.core.service1 import BackwardImpl1
from oop.core.service1 import Delegator1, Delegatee1
from oop.core.service1 import ForwardImpl1


def test_backward_impl():
    """test using implementation"""

    # given
    delegator = Delegator1(BackwardImpl1())

    # when
    result = delegator.service1("42")

    # then
    assert result == "24"


def test_forward_impl():
    """test using implementation"""

    # given
    delegator = Delegator1(ForwardImpl1())

    # when
    result = delegator.service1("42")

    # then
    assert result == "42"


def test_mock(mocker: MockerFixture):
    """test using mock"""

    # given
    delegatee_mock = mocker.Mock(spec=Delegatee1)
    delegatee_mock.service1.return_value = "24"

    delegator = Delegator1(delegatee_mock)

    # when
    result = delegator.service1("42")

    # then
    assert result == "24"
    delegatee_mock.service1.assert_called_with("42")
