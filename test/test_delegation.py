from delegation.delegatees import DelegateeImpl1
from delegation.delegator import Delegator


def test_forwarding():
    # given
    delegator = Delegator(DelegateeImpl1())
    # when
    result = delegator.service(1, 2)
    # then
    assert result == 3
