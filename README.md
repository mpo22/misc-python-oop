# python sanbox / object-oriented programming

## setup

```bash
sudo dnf -y install python3 python3-devel python3-devtools
```

```bash
python3 -m venv .venv
source .venv/bin/activate
```

```bash
python -m pip install -r requirements.txt
```

## run

```bash
python main.py
```

## update requirements.txt (optional)

```bash
python -m pip install -U pip-chill
python -m pip install -U pip-review
```

```bash
pip-review -a
pip-chill > requirements.txt
```

teardown

```bash
deactivate
```

### beautifier

- uniformize code style
- improved code quality
- **reduced merge diffs and conflicts**

#### black

- https://black.readthedocs.io
- https://pypi.org/project/black/

```bash
python -m pip install -U black
```

```bash
python -m black --fast --check  .
```

```bash
python -m black --fast  .
```

### linters

- uniformize code style
- improved code quality
- **reduced bugs and code smells**

### pylint

- https://www.pylint.org/
- https://pypi.org/project/pylint/

```bash
python -m pip install -U pylint
```

```bash
python -m pylint delegation app tests
```

### flake8 (???)

```bash
python -m pip install -U flake8
```

### test

- https://pytest.org
- https://pypi.org/project/pytest/

```bash
python -m pip install -U pytest
```

```bash
python -m pytest
```

### coverage

- https://coverage.readthedocs.io/en/latest/

```bash
python -m pip install -U coverage
```

```bash
python -m coverage run -m pytest
python -m coverage report -m
python -m coverage html
firefox htmlcov/index.html
```

### doc

```bash
python -m pip install -U sphinx
```

### PyCharm IDE (optional)

#### PyCharm Community Edition

https://www.jetbrains.com/fr-fr/pycharm/download/other.html

#### pylint integration

- https://plugins.jetbrains.com/plugin/11084-pylint
- https://github.com/leinardi/pylint-pycharm

#### flake8 integration (?not well integrated?)

https://gitlab.com/ramast/flake8-for-pycharm/ :

```bash
python -m pip install -U flake8-for-pycharm
```

#### test 

- https://www.jetbrains.com/help/pycharm/pytest.html

#### coveragev (only in PyCharm Professional)

- https://www.jetbrains.com/help/pycharm/code-coverage.html

## resources

### reference

- [Python documentation](https://docs.python.org/3/)


- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)

### project structure

- [Pypa's sample Python project](https://github.com/pypa/sampleproject)
- [Hitchhiker’s sample Module Repository](https://github.com/navdeep-G/samplemod)
- https://pypi.org/project/python_boilerplate_template/


- https://setuptools.pypa.io/en/latest/userguide/package_discovery.html

- https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
- https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html
=> flat layout is simple for in-development packages


- [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)

### object-oriented design

- [SOLID](https://en.wikipedia.org/wiki/SOLID)
- [GRASP](https://en.wikipedia.org/wiki/GRASP_(object-oriented_design))


- [Design patterns](https://refactoring.guru/design-patterns/python)
- [DI](https://python-dependency-injector.ets-labs.org/)

### plugins

- https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/


- https://mwax911.medium.com/building-a-plugin-architecture-with-python-7b4ab39ad4fc


### test

- [Python Testing Tools Taxonomy](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)


- [unittest](https://docs.python.org/3.11/library/unittest.html)
- [pytest](https://docs.pytest.org/en/latest/contents.html) documentation
- *TDD* and *Red Green Refactor*

#### Stubs vs Mocks vs Fakes vs Spy

- https://www.martinfowler.com/articles/mocksArentStubs.html
- https://www.ankursheel.com/blog/difference-stubs-mocks-fakes-spies
- https://stackoverflow.com/questions/346372/whats-the-difference-between-faking-mocking-and-stubbing