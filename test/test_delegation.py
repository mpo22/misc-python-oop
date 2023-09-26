import pytest_mock

import delegation.delegatees
import delegation.delegator
import delegation.service


def test_reverse_implementation():
    """test using implementation"""

    # given
    delegator = delegation.delegator.Delegator(delegation.delegatees.ReverseImpl())

    # when
    result = delegator.service("42")

    # then
    assert result == "24"


def test_unchange_implementation():
    """test using implementation"""

    # given
    delegator = delegation.delegator.Delegator(delegation.delegatees.UnchangeImpl())

    # when
    result = delegator.service("42")

    # then
    assert result == "42"


def test_mock(mocker: pytest_mock.MockerFixture):
    """test using mock"""

    # given
    delegatee_mock = mocker.Mock(spec=delegation.service.Service)
    delegatee_mock.service.return_value = "24"

    delegator = delegation.delegator.Delegator(delegatee_mock)

    # when
    result = delegator.service("42")

    # then
    assert result == "24"
    delegatee_mock.service.assert_called_with("42")
