import logging


class Delegator:
    """A dummy delegator"""

    def __init__(self, delegatee):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.debug(f"delegatee={delegatee}")
        self.delegatee = delegatee

    def service(self, arg1, arg2):
        self.logger.debug(f"{arg1} {arg2}")
        result = self.delegatee.service(arg1, arg2)
        self.logger.debug(f"{result}")
        return result
