format_string = r'''
?timespec: time
         | time date
         | time increment
         | time date increment
         | date
         | date increment
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
         | "+" INT INC_PERIOD                     -> _inc_number
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
DAY_NUMBER: /([0-3][0-9]|[0-9])/
MONTH_NUMBER: /([1-9]|0[1-9]|1[0-2])/
YEAR_NUMBER: /[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9]/
HR24CLOCK_HR_MIN: /(([0-1][0-9]|2[0-3])[0-5][0-9])|([0-1][0-9]|2[0-3])|[0-9]/
HR24CLOCK_HOUR: /([0-1][0-9]|2[0-3])|[0-9]/
WALLCLOCK_HR_MIN: /((0[1-9]|1[0-2])[0-5][0-9])|(0[1-9]|1[0-2])|[1-9]/
WALLCLOCK_HOUR:  /(0[0-9]|1[0-2])|[0-9]/
MINUTE: /[0-5][0-9]|[0-9]/
AM_PM: "am" | "pm"
%import common.INT
%import common.WS
%ignore WS
'''
