
months_days = {
    1:31,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

is_leap_year = lambda year : (((year % 400 == 0) and (year % 100 == 0)) or
                             ((year % 4   == 0) and (year % 100 != 0)))
check_february = lambda year, month, day: (((    is_leap_year(year)) and (day <= 29) and (day > 0)) or 
                                           ((not is_leap_year(year)) and (day <= 28) and (day > 0)))


valid_month = lambda month : month >= 1 and month <= 12
valid_year  = lambda year : year >= 0
valid_day   = lambda day, year, month:  check_february(year, month, day) if month == 2 else ((day <= months_days[month]) and (day > 0)) 
                                        

def valid_date(year, month, day):

    return (
            valid_month(month) and 
            valid_day(day, year, month) and 
            valid_year(year)
        )
