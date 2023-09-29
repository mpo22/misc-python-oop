from pytest_mock import MockerFixture

from oop.core.service1.backward import BackwardDelegatee
from oop.core.service1.delegation import Delegator, Delegatee
from oop.core.service1.forward import ForwardDelegatee


def test_backward():
    """test using implementation"""

    # given
    delegator = Delegator(BackwardDelegatee())

    # when
    result = delegator.method1("42")

    # then
    assert result == "24"


def test_forward():
    """test using implementation"""

    # given
    delegator = Delegator(ForwardDelegatee())

    # when
    result = delegator.method1("42")

    # then
    assert result == "42"


def test_mock(mocker: MockerFixture):
    """test using mock"""

    # given
    delegatee = mocker.Mock(spec=Delegatee)
    delegatee.service1.return_value = "24"

    delegator = Delegator(delegatee)

    # when
    result = delegator.method1("42")

    # then
    assert result == "24"
    delegatee.service1.assert_called_with("42")
