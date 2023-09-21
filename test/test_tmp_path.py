"""
see https://docs.pytest.org/en/7.4.x/getting-started.html#request-a-unique-temporary-directory-for-functional-tests

pytest --fixtures # shows builtin and custom fixtures

see https://docs.pytest.org/en/7.4.x/how-to/tmp_path.html#tmp-path-handling
"""


def test_needsfiles(tmp_path):
    print(tmp_path)
    # assert 0
