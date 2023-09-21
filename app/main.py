import json
import logging
import logging.config
import sys

from delegation.delegatees import DelegateeImpl1
from delegation.delegator import Delegator


def logging_config():
    """
    Logging setup

    see https://docs.python.org/3/library/logging.html#logrecord-attributes
    see https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
    see https://docs.python-guide.org/writing/logging/?highlight=logging
    """
    try:
        with open("logging.json") as logging_json_stream:
            logging.config.dictConfig(json.loads(logging_json_stream.read()))

    except Exception as error:
        print('failed to load logging config file:', error)

        logging.basicConfig(
            stream=sys.stdout,
            format="%(levelname)-5s [%(filename)s:%(lineno)d] [%(name)s:%(funcName)s] %(message)s",
            level=logging.INFO,
        )
    finally:
        logging.debug("logging initialized")


def main():
    logging_config()

    delegator = Delegator(DelegateeImpl1())
    result = delegator.service(1, 2)
    logging.info(f"result={result}")
    print(result)


if __name__ == "__main__":
    main()
