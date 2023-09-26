import logging
from abc import abstractmethod

from oop.core.service1.interface import Service1


class Delegator1(Service1):
    """A dummy delegator"""

    def __init__(self, delegatee: Service1):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.debug("delegatee=%s", delegatee)
        self.delegatee = delegatee

    def service1(self, arg: str) -> str:
        """forwards the call to the delegatee"""
        self.logger.debug("%s", arg)
        result = self.delegatee.service1(arg)
        self.logger.debug("%s", result)
        return result


class Delegatee1(Service1):
    """A dummy delegatee abstract base class"""

    @abstractmethod
    def service1(self, arg: str) -> str:
        pass

    def __init__(self):
        self._logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self._logger.debug("%s ctor", __class__.__name__)

    @property
    def logger(self):
        """logger getter"""
        return self._logger
