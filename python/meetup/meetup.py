from datetime import date
from calendar import Calendar, day_name
from itertools import zip_longest


def meetup(year, month, week, day_of_week):
    weekday = list(day_name).index(day_of_week)
    month_weeks = get_month(year, month)
    week_number = get_week_number(week, month_weeks, weekday)

    try:
        day = next(day[0] for day in month_weeks[week_number] if day and day[1] == weekday)

        return date(year, month, day)
    
    except IndexError:
        raise MeetupDayException("Week number not found.")


def get_month(year, month):
    weeks_in_month = Calendar().monthdays2calendar(year, month)
    flattened_dates = [day for week in weeks_in_month for day in week if day[0] != 0]
    formatted_dates = list(zip_longest(*(iter(flattened_dates),) * 7, fillvalue=""))

    return formatted_dates


def get_week_number(week, weeks, day_of_week):
    if week == "teenth":
        for days in weeks:
            if any(day[1] == day_of_week for day in days if day[0] in range(13, 20)):
                return weeks.index(days)

    elif week == "last":
        for days in reversed(weeks):
            if any(day[1] == day_of_week for day in days if day):
                return weeks.index(days)

    else:
        return int(week[:-2]) - 1


class MeetupDayException(Exception):
    forgiveness = "I was forced to create this class on a script level due to the test class importing it."
