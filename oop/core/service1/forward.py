from .delegation import Delegatee


class ForwardDelegatee(Delegatee):
    """A dummy delegatee implementation"""

    def service1(self, arg: str) -> str:
        """ " return the arg unchanged"""
        self.logger.debug("%s ", arg)
        result = arg
        self.logger.debug("%s", result)
        return result
