from datetime import datetime

from freezegun import freeze_time

import atdate


def test_at_date_has_parse_attribute() -> None:
    assert hasattr(atdate, "parse")


def test_at_date_has_atdateparser_attribute() -> None:
    assert hasattr(atdate, "AtDateParser")


def test_parse_return_datetime_object() -> None:
    test_string = "noon"
    result = atdate.parse(test_string)
    assert isinstance(result, datetime)


@freeze_time("2000-01-02 03:04:05")
def test_at_noon_before_noon() -> None:
    test_string = "noon"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 12, 0, 0, 0)


@freeze_time("2000-01-02 13:04:05")
def test_at_noon_after_noon() -> None:
    test_string = "noon"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 3, 12, 0, 0, 0)


@freeze_time("2000-01-31 13:04:05")
def test_at_noon_month_change() -> None:
    test_string = "noon"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 2, 1, 12, 0, 0, 0)


@freeze_time("2000-12-31 13:04:05")
def test_at_noon_year_change() -> None:
    test_string = "noon"
    result = atdate.parse(test_string)
    assert result == datetime(2001, 1, 1, 12, 0, 0, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_midnight() -> None:
    test_string = "midnight"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 3, 0, 0, 0, 0)


@freeze_time("2000-01-31 13:04:05")
def test_at_midnight_month_change() -> None:
    test_string = "midnight"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 2, 1, 0, 0, 0, 0)


@freeze_time("2000-12-31 13:04:05")
def test_at_midnight_year_change() -> None:
    test_string = "midnight"
    result = atdate.parse(test_string)
    assert result == datetime(2001, 1, 1, 0, 0, 0, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_now() -> None:
    test_string = "now"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_now_next_minute_change_minute() -> None:
    test_string = "now next minute"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 3, 5, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_now_next_minutes() -> None:
    test_string = "now next minutes"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 3, 5, 5, 0)


@freeze_time("2000-01-02 03:59:05")
def test_at_now_next_minute_change_hour() -> None:
    test_string = "now next minute"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 4, 0, 5, 0)


@freeze_time("2000-01-02 23:59:05")
def test_at_now_next_minute_change_day() -> None:
    test_string = "now next minute"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 3, 0, 0, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_now_next_hour() -> None:
    test_string = "now next hour"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 2, 4, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_now_next_day() -> None:
    test_string = "now next day"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 3, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_now_next_week() -> None:
    test_string = "now next week"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 1, 9, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_now_next_month() -> None:
    test_string = "now next month"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 2, 2, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_at_now_next_year() -> None:
    test_string = "now next year"
    result = atdate.parse(test_string)
    assert result == datetime(2001, 1, 2, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_month_number_day_number() -> None:
    test_string = "05/20"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 5, 20, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_month_name_day_number() -> None:
    test_string = "May 20"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 5, 20, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_month_number_day_number_year_number() -> None:
    test_string = "05/20/2003"
    result = atdate.parse(test_string)
    assert result == datetime(2003, 5, 20, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_day_number_month_number() -> None:
    test_string = "20.05"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 5, 20, 3, 4, 5, 0)


@freeze_time("2000-01-02 03:04:05")
def test_day_number_month_number_year_number() -> None:
    test_string = "20.05.2003"
    result = atdate.parse(test_string)
    assert result == datetime(2003, 5, 20, 3, 4, 5, 0)


@freeze_time("2000-07-02 03:04:05")
def test_inc_period() -> None:
    test_string = "02.07.2000 +1days"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 3, 3, 4, 5, 0)


@freeze_time("2000-07-02 03:04:05")
def test_hr24clock_hr_min() -> None:
    test_string = "1401"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 2, 14, 1, 0, 0)


@freeze_time("2000-07-02 03:04:05")
def test_hr24clock_hour_minute() -> None:
    test_string = "14:01"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 2, 14, 1, 0, 0)


@freeze_time("2000-07-02 03:04:05")
def test_wallclock_hr_min_am_pm() -> None:
    test_string = "0201 pm"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 2, 14, 1, 0, 0)


@freeze_time("2000-07-02 03:04:05")
def test_wallclock_hour_minute_am_pm() -> None:
    test_string = "02:01 pm"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 2, 14, 1, 0, 0)


@freeze_time("2000-07-02 03:04:05")
def test_next_month_without_now() -> None:
    test_string = "next month"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 8, 2, 3, 4, 5, 0)


@freeze_time("2000-07-02 03:04:05")
def test_plus_one_day_without_now() -> None:
    test_string = "+1days"
    result = atdate.parse(test_string)
    assert result == datetime(2000, 7, 3, 3, 4, 5, 0)


@freeze_time("2000-07-02 03:04:05")
def test_isodate() -> None:
    test_string = "2011-09-22"
    result = atdate.parse(test_string)
    assert result == datetime(2011, 9, 22, 3, 4, 5, 0)


@freeze_time("2000-07-02 03:04:05")
def test_time_date() -> None:
    test_string = "12:24 01.02.2011"
    result = atdate.parse(test_string)
    assert result == datetime(2011, 2, 1, 12, 24, 0, 0)


@freeze_time("2000-07-02 03:04:05")
def test_isodatetime() -> None:
    test_string = "2011-09-22T11:44"
    result = atdate.parse(test_string)
    assert result == datetime(2011, 9, 22, 11, 44, 0, 0)


@freeze_time("2000-07-02 03:04:05")
def test_isodatetime_without_t() -> None:
    test_string = "2011-09-22 11:44"
    result = atdate.parse(test_string)
    assert result == datetime(2011, 9, 22, 11, 44, 0, 0)
