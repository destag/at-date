from datetime import datetime

import pytest
from freezegun import freeze_time

import atdate
from .test_scenarios import scenarios_dict


def test_at_date_has_parse_attribute():
    assert hasattr(atdate, 'parse')


def test_at_date_has_atdateparser_attribute():
    assert hasattr(atdate, 'AtDateParser')


def test_parse_return_datetime_object():
    test_string = 'noon'
    result = atdate.parse(test_string)
    assert isinstance(result, datetime)


@pytest.mark.parametrize('test_string,start_time,expected_time', [
    pytest.param(
        test_params[0], test_params[1], test_params[2],
        id='{} {}'.format(scenario_name, test_name))
    for scenario_name, scenario in scenarios_dict.items()
    for test_name, test_params in scenario.items()
])
def test_at_date_parser(test_string, start_time, expected_time):
    expected_dt = datetime.strptime(expected_time, '%Y-%m-%d %H:%M:%S')
    with freeze_time(start_time):
        result = atdate.parse(test_string)
        assert result == expected_dt


@freeze_time('2000-01-02 03:04:05')
def test_at_now_next_minute_change_minute():
    test_string = 'now next minute'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 3, 5, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_at_now_next_minutes():
    test_string = 'now next minutes'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 3, 5, 5, 0)


@freeze_time('2000-01-02 03:59:05')
def test_at_now_next_minute_change_hour():
    test_string = 'now next minute'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 4, 0, 5, 0)


@freeze_time('2000-01-02 23:59:05')
def test_at_now_next_minute_change_day():
    test_string = 'now next minute'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 3, 0, 0, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_at_now_next_hour():
    test_string = 'now next hour'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 4, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_at_now_next_day():
    test_string = 'now next day'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 3, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_at_now_next_week():
    test_string = 'now next week'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 9, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_at_now_next_month():
    test_string = 'now next month'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 2, 2, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_at_now_next_year():
    test_string = 'now next year'
    result = atdate.parse(test_string)
    assert result == datetime(2001, 1, 2, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_month_number_day_number():
    test_string = '05/20'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 5, 20, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_month_name_day_number():
    test_string = 'May 20'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 5, 20, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_month_number_day_number_year_number():
    test_string = '05/20/2003'
    result = atdate.parse(test_string)
    assert result == datetime(2003, 5, 20, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_day_number_month_number():
    test_string = '20.05'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 5, 20, 3, 4, 5, 0)


@freeze_time('2000-01-02 03:04:05')
def test_day_number_month_number_year_number():
    test_string = '20.05.2003'
    result = atdate.parse(test_string)
    assert result == datetime(2003, 5, 20, 3, 4, 5, 0)


@freeze_time('2000-07-02 03:04:05')
def test_inc_period():
    test_string = '02.07.2000 +1days'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 3, 3, 4, 5, 0)


@freeze_time('2000-07-02 03:04:05')
def test_hr24clock_hr_min():
    test_string = '1401'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 2, 14, 1, 0, 0)


@freeze_time('2000-07-02 03:04:05')
def test_hr24clock_hour_minute():
    test_string = '14:01'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 2, 14, 1, 0, 0)


@freeze_time('2000-07-02 03:04:05')
def test_wallclock_hr_min_am_pm():
    test_string = '0201 pm'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 2, 14, 1, 0, 0)


@freeze_time('2000-07-02 03:04:05')
def test_wallclock_hour_minute_am_pm():
    test_string = '02:01 pm'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 2, 14, 1, 0, 0)


@freeze_time('2000-07-02 03:04:05')
def test_next_month_without_now():
    test_string = 'next month'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 8, 2, 3, 4, 5, 0)


@freeze_time('2000-07-02 03:04:05')
def test_plus_one_day_without_now():
    test_string = '+1days'
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 3, 3, 4, 5, 0)
