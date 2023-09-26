import json
import logging
import logging.config
import sys

from oop.core.service1.backward import BackwardImpl1
from oop.core.service1.delegation import Delegator1


def logging_config():
    """
    Logging setup

    see https://docs.python.org/3/library/logging.html#logrecord-attributes
    see https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
    see https://docs.python-guide.org/writing/logging/?highlight=logging
    """
    try:
        with open("logging.json", encoding="utf-8") as logging_json_stream:
            logging.config.dictConfig(json.loads(logging_json_stream.read()))

    except Exception as error:
        print("failed to load logging config file:", error)

        logging.basicConfig(
            stream=sys.stdout,
            format="%(levelname)-5s [%(filename)s:%(lineno)d] [%(name)s:%(funcName)s] %(message)s",
            level=logging.INFO,
        )
    finally:
        logging.debug("logging initialized")


def main():
    """demonstration of a Service"""
    logging_config()

    delegator = Delegator1(BackwardImpl1())
    result = delegator.service1("42")
    logging.info("result=%s", result)
    print(result)


if __name__ == "__main__":
    main()
