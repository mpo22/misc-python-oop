import logging


class Delegator:
    """A dummy delegator"""

    def __init__(self, delegatee):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.debug("delegatee=%s", delegatee)
        self.delegatee = delegatee

    def service(self, arg1, arg2):
        """forward the call to the delegatee"""
        self.logger.debug("%s %s", arg1, arg2)
        result = self.delegatee.service(arg1, arg2)
        self.logger.debug("%s", result)
        return result
