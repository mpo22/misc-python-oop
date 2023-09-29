import logging

from oop.core.logging import LoggingInitializer
from oop.core.service1 import Service1BackwardDelegatee
from oop.core.service1 import Service1Delegator


def main():
    """dummy cli application"""

    LoggingInitializer().setup()

    delegator = Service1Delegator(Service1BackwardDelegatee())
    result = delegator.method1("42")
    logging.info("result=%s", result)
    print(result)


if __name__ == "__main__":
    main()
