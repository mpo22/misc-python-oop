import logging
from abc import ABCMeta, abstractmethod


class Delegatee(metaclass=ABCMeta):
    """A dummy delegatee abstract base class"""

    def __init__(self):
        self._logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self._logger.debug("%s ctor", __class__.__name__)

    @property
    def logger(self):
        """logger getter"""
        return self._logger

    @abstractmethod
    def service(self, arg1, arg2):
        """pure virtual service method"""


class DelegateeImpl1(Delegatee):
    """A dummy delegatee implementation"""

    def service(self, arg1, arg2):
        self.logger.debug("%s %s", arg1, arg2)
        result = arg1 + arg2
        self.logger.debug("%s", result)
        return result


class DelegateeImpl2(Delegatee):
    """An adder operator"""

    def service(self, arg1, arg2):
        self.logger.debug("%s %s", arg1, arg2)
        result = arg1 - arg2
        self.logger.debug("%s", result)
        return result
