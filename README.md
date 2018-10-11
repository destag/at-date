# at-date

[![Build Status](https://travis-ci.org/destag/at-date.svg?branch=master)](https://travis-ci.org/destag/at-date)
[![codecov](https://codecov.io/gh/destag/at-date/branch/master/graph/badge.svg)](https://codecov.io/gh/destag/at-date)
[![CodeFactor](https://www.codefactor.io/repository/github/destag/at-date/badge)](https://www.codefactor.io/repository/github/destag/at-date)
[![PyPI version](https://badge.fury.io/py/atdate.svg)](https://badge.fury.io/py/atdate)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/atdate.svg)](https://pypi.python.org/pypi/atdate/)

Simple Python library for parsing **at command** string into datetime objects.

```
noon next day -> 2018-10-11 12:00:00
```

## Installation

To install **at-date** simply use pip:

```bash
pip install atdate
```

## Getting started

To use **at-date** simply import **parse** function.

```python
>>> from atdate import parse

>>> parse('noon next day')
datetime.datetime(2018, 10, 11, 12, 0)

>>> parse('now + 8 hours')
datetime.datetime(2018, 10, 10, 15, 42, 24)
```

More info can be found in **/docs** directory or in [docs](#) page.

## How to Contribute

Take a look at [CONTRIBUTING](CONTRIBUTING.md) guide.

## License

**At-date** is licensed under MIT License. See [LICENSE](LICENSE) for more information.
