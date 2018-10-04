from datetime import datetime, timedelta

from lark import Lark, Transformer
from dateutil.relativedelta import relativedelta

from .atdate_format import format_string


class AtDateParser:
    def __init__(self):
        self.parser = Lark(format_string, start='timespec')

    def execute(self, string_to_parse):
        transformer = AtDateTransformer()
        tree = self.parser.parse(string_to_parse.lower())
        new_tree = transformer.transform(tree)

        next_time_run = new_tree if isinstance(new_tree, datetime) else new_tree.children[-1]

        if next_time_run < transformer.now:
            raise ValueError

        return next_time_run


class AtDateTransformer(Transformer):
    _month_name_to_month_number = {
        "jan": 1, "january": 1,
        "feb": 2, "february": 2,
        "mar": 3, "march": 3,
        "apr": 4, "april": 4,
        "may": 5,
        "jun": 6, "june": 6,
        "jul": 7, "july": 7,
        "aug": 8, "august": 8,
        "sep": 9, "september": 9,
        "oct": 10, "october": 10,
        "nov": 11, "november": 11,
        "dec": 12, "december": 12
    }

    def __init__(self):
        super().__init__()
        self.now = datetime.now()
        self.datetime_params = {
            'year': self.now.year,
            'month': self.now.month,
            'day': self.now.day,
            'hour': self.now.hour,
            'minute': self.now.minute,
            'second': self.now.second,
            'microsecond': 0
        }

    def _now(self, matches):
        return self.now

    def _hr24clock_hr_min(self, matches):
        hour = int(matches[0][:2])
        minute = int(matches[0][2:] or 0)
        next_day = self._check_if_next_day(hour, minute)
        self.datetime_params['day'] += next_day
        self.datetime_params['hour'] = hour
        self.datetime_params['minute'] = minute
        self.datetime_params['second'] = 0
        return datetime(**self.datetime_params)

    def _hr24clock_hour_minute(self, matches):
        hour = int(matches[0])
        minute = int(matches[1])
        next_day = self._check_if_next_day(hour, minute)
        self.datetime_params['day'] += next_day
        self.datetime_params['hour'] = hour
        self.datetime_params['minute'] = minute
        self.datetime_params['second'] = 0
        return datetime(**self.datetime_params)

    def _wallclock_hr_min_am_pm(self, matches):
        am_pm = matches[1]
        hour = int(matches[0][:2]) % 12 + 12 * int(am_pm == 'pm')
        minute = int(matches[0][2:] or 0)
        next_day = self._check_if_next_day(hour, minute)
        self.datetime_params['day'] += next_day
        self.datetime_params['hour'] = hour
        self.datetime_params['minute'] = minute
        self.datetime_params['second'] = 0
        return datetime(**self.datetime_params)

    def _wallclock_hour_minute_am_pm(self, matches):
        am_pm = matches[2]
        hour = int(matches[0]) % 12 + 12 * int(am_pm == 'pm')
        minute = int(matches[1])
        next_day = self._check_if_next_day(hour, minute)
        self.datetime_params['day'] += next_day
        self.datetime_params['hour'] = hour
        self.datetime_params['minute'] = minute
        self.datetime_params['second'] = 0
        return datetime(**self.datetime_params)

    def _noon(self, matches):
        next_day = timedelta(days=self._check_if_next_day(12, 0))
        self.datetime_params['hour'] = 12
        self.datetime_params['minute'] = 0
        self.datetime_params['second'] = 0
        dt = datetime(**self.datetime_params)
        return dt + next_day

    def _midnight(self, matches):
        next_day = timedelta(days=1)
        self.datetime_params['hour'] = 0
        self.datetime_params['minute'] = 0
        self.datetime_params['second'] = 0
        dt = datetime(**self.datetime_params)
        return dt + next_day

    def _month_name_day_number(self, matches):
        month = self.__class__._month_name_to_month_number[matches[0]]
        day = int(matches[1])
        next_year = self._check_if_next_year(month, day)
        self.datetime_params['day'] = day
        self.datetime_params['month'] = month
        self.datetime_params['year'] += next_year
        return datetime(**self.datetime_params)

    def _month_number_day_number(self, matches):
        month, day = map(int, matches)
        next_year = self._check_if_next_year(month, day)
        self.datetime_params['day'] = day
        self.datetime_params['month'] = month
        self.datetime_params['year'] += next_year
        return datetime(**self.datetime_params)

    def _month_number_day_number_year_number(self, matches):
        month, day, year = map(int, matches)
        self.datetime_params['day'] = day
        self.datetime_params['month'] = month
        self.datetime_params['year'] = year
        return datetime(**self.datetime_params)

    def _day_number_month_number(self, matches):
        day, month = map(int, matches)
        next_year = self._check_if_next_year(month, day)
        self.datetime_params['day'] = day
        self.datetime_params['month'] = month
        self.datetime_params['year'] += next_year
        return datetime(**self.datetime_params)

    def _day_number_month_number_year_number(self, matches):
        day, month, year = map(int, matches)
        self.datetime_params['day'] = day
        self.datetime_params['month'] = month
        self.datetime_params['year'] = year
        return datetime(**self.datetime_params)

    def _next(self, matches):
        inc_period = matches[0] if matches[0].endswith('s') else matches[0] + 's'
        dt = datetime(**self.datetime_params)
        ret = relativedelta(**{inc_period: 1})
        return dt + ret

    def _inc_number(self, matches):
        inc_number = int(matches[0])
        inc_period = matches[1] if matches[1].endswith('s') else matches[1] + 's'
        return datetime(**self.datetime_params) + timedelta(**{inc_period: inc_number})

    def _check_if_next_day(self, hour, minute):
        return int(self.now.hour > hour or (self.now.hour == hour and self.now.minute > minute))

    def _check_if_next_year(self, month, day):
        return int(self.now.month > month or (self.now.month == month and self.now.day > day))
