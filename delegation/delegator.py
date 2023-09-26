import logging

from delegation.service import Service


class Delegator(Service):
    """A dummy delegator"""

    def __init__(self, delegatee: Service):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.debug("delegatee=%s", delegatee)
        self.delegatee = delegatee

    def service(self, arg: str) -> str:
        """forwards the call to the delegatee"""
        self.logger.debug("%s", arg)
        result = self.delegatee.service(arg)
        self.logger.debug("%s", result)
        return result
