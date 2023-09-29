from .delegation import Delegatee


class BackwardDelegatee(Delegatee):
    """A dummy delegatee implementation"""

    def service1(self, arg: str) -> str:
        """ " return the arg reversed"""
        self.logger.debug("%s ", arg)
        result = arg[::-1]
        self.logger.debug("%s", result)
        return result
