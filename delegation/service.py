from abc import ABCMeta, abstractmethod


class Service(metaclass=ABCMeta):
    """A service interface"""

    @abstractmethod
    def service(self, arg: str) -> str:
        """pure virtual service method"""
