from pytest_mock import MockerFixture

from oop.core.service1 import Service1BackwardDelegatee
from oop.core.service1 import Service1Delegator, Service1Delegatee
from oop.core.service1 import Service1ForwardDelegatee


def test_backward_impl():
    """test using implementation"""

    # given
    delegator = Service1Delegator(Service1BackwardDelegatee())

    # when
    result = delegator.method1("42")

    # then
    assert result == "24"


def test_forward_impl():
    """test using implementation"""

    # given
    delegator = Service1Delegator(Service1ForwardDelegatee())

    # when
    result = delegator.method1("42")

    # then
    assert result == "42"


def test_mock(mocker: MockerFixture):
    """test using mock"""

    # given
    delegatee = mocker.Mock(spec=Service1Delegatee)
    delegatee.service1.return_value = "24"

    delegator = Service1Delegator(delegatee)

    # when
    result = delegator.method1("42")

    # then
    assert result == "24"
    delegatee.service1.assert_called_with("42")
