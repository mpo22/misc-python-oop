import json
import logging.config
import sys


class Initializer:
    """logging helper"""

    def setup(self, json_config_file: str = "logging.json"):
        """
        Logging setup from config file

        see https://docs.python.org/3/library/logging.html#logrecord-attributes
        see https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
        see https://docs.python-guide.org/writing/logging/?highlight=logging
        """
        try:
            with open(json_config_file, encoding="utf-8") as logging_json_stream:
                logging.config.dictConfig(json.loads(logging_json_stream.read()))

        except Exception as exception:
            print("failed to load logging config file:", exception)

            logging.basicConfig(
                stream=sys.stdout,
                format="%(levelname)-5s [%(filename)s:%(lineno)d] [%(name)s:%(funcName)s] %(message)s",
                level=logging.INFO,
            )
        finally:
            logging.debug("logging initialized")
