from .delegation import Delegatee1


class BackwardImpl1(Delegatee1):
    """A dummy delegatee implementation"""

    def service1(self, arg: str) -> str:
        """ " return the arg reversed"""
        self.logger.debug("%s ", arg)
        result = arg[::-1]
        self.logger.debug("%s", result)
        return result
