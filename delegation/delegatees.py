import logging
from abc import ABCMeta, abstractmethod


class Delegatee(metaclass=ABCMeta):
    """A dummy delegatee abstract base class"""

    def __init__(self):
        self._logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self._logger.debug(f"{__class__.__name__} ctor")

    @property
    def logger(self):
        return self._logger

    @abstractmethod
    def service(self, arg1, arg2):
        pass


class DelegateeImpl1(Delegatee):
    """A dummy delegatee implementation"""

    def service(self, arg1, arg2):
        self.logger.debug(f"{arg1} {arg2}")
        result = arg1 + arg2
        self.logger.debug(f"{result}")
        return result


class DelegateeImpl2(Delegatee):
    """An adder operator"""

    def service(self, arg1, arg2):
        self.logger.debug(f"{arg1} {arg2}")
        result = arg1 - arg2
        self.logger.debug(f"{result}")
        return result
