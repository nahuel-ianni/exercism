def leap_year(year):
    check1 = (year % 4) == 0 and (year % 100) != 0
    check2 = (year % 100) == 0 and (year % 400) == 0

    return check1 or check2
