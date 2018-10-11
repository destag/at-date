# at-date

[![Build Status](https://travis-ci.org/destag/at-date.svg?branch=master)](https://travis-ci.org/destag/at-date)
[![codecov](https://codecov.io/gh/destag/at-date/branch/master/graph/badge.svg)](https://codecov.io/gh/destag/at-date)
[![CodeFactor](https://www.codefactor.io/repository/github/destag/at-date/badge)](https://www.codefactor.io/repository/github/destag/at-date)
[![PyPI version](https://badge.fury.io/py/atdate.svg)](https://badge.fury.io/py/atdate)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/atdate.svg)](https://pypi.python.org/pypi/atdate/)

Simple Python library for parsing **at command** string into datetime objects.

## Content

- [Installation](#installation)
- [Guide](#guide)
  - [Basic Usage](#basic-usage)
  - [Function parse](#function-parse)
  - [At date string](#at-date-string)
  - [At date tokens](#at-date-tokens)
    - [time](#time)
    - [date](#date)
    - [increment](#increment)
    - [now](#now)
    - [month](#month)
    - [weekday](#weekday)
    - [period](#period)
- [Final notes](#final-notes)

## Installation

**At-date** requires Python 3.4 or higher.

You can install package using pip:

```bash
pip install atdate
```

Or with pipenv:

```bash
pipenv install atdate
```

If you want to use latest unreleased version use the  code from master branch:

```bash
git clone git@github.com:destag/at-date.git
cd at-date/
python setup.py install
```

## Guide

### Basic Usage

To start using **at-date** import **parse** function and provide valid at date string.

```python
>>> from atdate import parse

>>> parse('noon next day')
datetime.datetime(2018, 10, 11, 12, 0)

>>> parse('now + 8 hours')
datetime.datetime(2018, 10, 10, 15, 42, 24)
```

Or you can use **AtDateParser** object.

```python
>>> from atdate import AtDateParser

>>> parser = AtDateParser()
>>> parser.execute('now + 8 hours')
datetime.datetime(2018, 10, 10, 15, 42, 24)
```

### Function parse

Parses string in at date format to valid datetime object.

Arguments:

- at_date_string ([str](https://docs.python.org/3/library/stdtypes.html?highlight=str#str)): Valid at date string.

Returns:

- [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime-objects): Date and time to which string has been parsed.

### At date string

Valid at date string consists of tokens which can be in order:

tokens|example
---|---
time|17:32
time date|17:32 11/22/2033
time increment|17:32 next day
time date increment|17:32 11/22/2033 next day
date|11/22/2033
date increment|11/22/2033 next month
now|now
now increment|now next day

### At date tokens

These are valid formats for at date string tokens.

#### time

Format for describing time.

format|example
---|---
\[00-23\] \[00-59\]|1732
\[0-23\] : \[0-59\]|17:32
\[00-12\] \[00-59\] \[am\|pm\]|0532 pm
\[0-12\] : \[0-59\] \[am\|pm\]|5:32 pm
\[noon\|midnight\]|noon

#### date

Format for describing date.

format|example
---|---
\[[month](#month)\]\[1-31\]|october 27
\[1-12\] / \[1-31\]|10/27
\[1-12\] / \[1-31\] / \[0-9999\]|10/27/2006
\[1-12\] . \[1-31\]|10.27
\[1-12\] . \[1-31\] . \[0-9999\]|10.27.2006

#### increment

Format for describing time incrementation.

format|example
---|---
next \[[period](#period)\]|next month
\+ \[0-9999\] \[[period](#period)\]|\+ 12 minutes

#### now

Format for this token is literally `now`.

Returns actual date and time.

#### month

Month name is case insensitive. You can use whole name or shortcut. All months with shortcuts are listed in table.

name|shortcut
---|---
january|jan
february|feb
march|mar
april|apr
may|may
june|jun
july|jul
august|aug
september|sep
october|oct
november|nov
december|dec

#### weekday

Weekday name is case insensitive. You can use whole name or shortcut. All weekdays with shortcuts are listed in table.

name|shortcut
---|---
monday|mon
tuesday|tue
wednesday|wed
thursday|thu
friday|fri
saturday|sat
sunday|sun

#### period

Format for describing period of time. Can end with s. All possible formats are listed in table.

name|s
---|---
minute|minutes
hour|hours
day|days
week|weeks
month|months
year|years

## Final notes

Thank you for using 
