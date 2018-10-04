format_string = """
?timespec: time
         | time date
         | time increment
         | time date increment
         | nowspec
         | nowspec increment
time: HR24CLOCK_HR_MIN                            -> _hr24clock_hr_min
    | HR24CLOCK_HOUR ":" MINUTE                   -> _hr24clock_hour_minute
    | WALLCLOCK_HR_MIN AM_PM                      -> _wallclock_hr_min_am_pm
    | WALLCLOCK_HOUR ":" MINUTE AM_PM             -> _wallclock_hour_minute_am_pm
    | "noon"                                      -> _noon
    | "midnight"                                  -> _midnight
date: MONTH_NAME DAY_NUMBER                       -> _month_name_day_number
    | MONTH_NUMBER "/" DAY_NUMBER                 -> _month_number_day_number
    | MONTH_NUMBER "/" DAY_NUMBER "/" YEAR_NUMBER -> _month_number_day_number_year_number
    | DAY_NUMBER "." MONTH_NUMBER                 -> _day_number_month_number
    | DAY_NUMBER "." MONTH_NUMBER "." YEAR_NUMBER -> _day_number_month_number_year_number
increment: "next" INC_PERIOD                      -> _next
         | "+" INC_NUMBER INC_PERIOD              -> _inc_number
nowspec: "now"                                    -> _now
INC_PERIOD: "minutes" | "minute"
          | "hours" | "hour"
          | "days" | "day"
          | "weeks" | "week"
          | "months" | "month"
          | "years" | "year"
MONTH_NAME: "january" | "jan"
          | "february" | "feb"
          | "march" | "mar"
          | "april" | "apr"
          | "may"
          | "june" | "jun"
          | "july" | "jul"
          | "august" | "aug"
          | "september" | "sep"
          | "october" | "oct"
          | "november" | "nov"
          | "december" | "dec"
DAY_NAME: "monday" | "mon"
        | "tuesday" | "tue"
        | "wednesday" | "wed"
        | "thursday" | "thu"
        | "friday" | "fri"
        | "saturday" | "sat"
        | "sunday" | "sun"
DAY_NUMBER: /\b([0-3][0-9]|[0-9])\b/
MONTH_NUMBER: /\b([1-9]|0[1-9]|1[0-2])\b/
YEAR_NUMBER: /\b[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9]\b/
INC_NUMBER: /\b([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\b/
HR24CLOCK_HR_MIN: /\b(([0-1][0-9]|2[0-3])[0-5][0-9])|([0-1][0-9]|2[0-3])|[0-9]\b/
HR24CLOCK_HOUR: /\b([0-1][0-9]|2[0-3])|[0-9]\b/
WALLCLOCK_HR_MIN: /\b((0[1-9]|1[0-2])[0-5][0-9])|(0[1-9]|1[0-2])|[1-9]\b/
WALLCLOCK_HOUR:  /\b(0[0-9]|1[0-2])|[0-9]\b/
MINUTE: /\b[0-5][0-9]|[0-9]\b/
AM_PM: "am" | "pm"
%import common.WORD
%import common.NUMBER
%import common.WS
%ignore WS
"""