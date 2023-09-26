# pylint: skip-file
# https://docs.pytest.org/en/7.4.x/getting-started.html#create-your-first-test

import unittest


class SampleTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == "__main__":
    unittest.main()
