"""
service1 package
with aliasing on public classes
"""

from .backward import BackwardDelegatee as Service1BackwardDelegatee
from .delegation import Delegatee as Service1Delegatee
from .delegation import Delegator as Service1Delegator
from .forward import ForwardDelegatee as Service1ForwardDelegatee
from .interface import Service1
