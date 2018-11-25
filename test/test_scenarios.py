"""Module contains scenarios for tests.

All scenarios are stored in dict, which keys are parser rules eg. 'now increment'.
Each parser rule is dict with keys that are user stories.
Test cases are in format [test_string, start_time, expected_time].

"""

scenarios_dict = {
    'noon': {
        'before_noon': ['noon', '2000-01-02 03:04:05', '2000-01-02 12:00:00'],
        'day_change': ['noon', '2000-01-02 13:04:05', '2000-01-03 12:00:00'],
        'month_change': ['noon', '2000-01-31 13:04:05', '2000-02-01 12:00:00'],
        'year_change': ['noon', '2000-12-31 13:04:05', '2001-01-01 12:00:00'],
    },
    'midnight': {
        'midnight': ['midnight', '2000-01-02 03:04:05', '2000-01-03 00:00:00'],
        'month_change': ['midnight', '2000-01-31 13:04:05', '2000-02-01 00:00:00'],
        'year_change': ['midnight', '2000-12-31 13:04:05', '2001-01-01 00:00:00'],
    },
    'now': {
        'now': ['now', '2000-01-02 03:04:05', '2000-01-02 03:04:05'],
    },
    'now increment': {
        'next_minute': ['now next minute', '2000-01-02 03:04:05'],
    },
}
