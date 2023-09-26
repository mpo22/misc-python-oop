from abc import ABCMeta, abstractmethod


class Service1(metaclass=ABCMeta):
    """A service interface"""

    @abstractmethod
    def service1(self, arg: str) -> str:
        """pure virtual service method"""
