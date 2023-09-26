import logging
from abc import abstractmethod

from delegation.service import Service


class Delegatee(Service):
    """A dummy delegatee abstract base class"""

    @abstractmethod
    def service(self, arg: str) -> str:
        pass

    def __init__(self):
        self._logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self._logger.debug("%s ctor", __class__.__name__)

    @property
    def logger(self):
        """logger getter"""
        return self._logger


class ReverseImpl(Delegatee):
    """A dummy delegatee implementation"""

    def service(self, arg: str) -> str:
        self.logger.debug("%s ", arg)
        result = arg[::-1]
        self.logger.debug("%s", result)
        return result


class UnchangeImpl(Delegatee):
    """Another dummy delegatee implementation"""

    def service(self, arg: str) -> str:
        self.logger.debug("%s", arg)
        result = arg
        self.logger.debug("%s", result)
        return result
