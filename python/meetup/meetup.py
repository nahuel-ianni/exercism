from datetime import date
from calendar import Calendar
from itertools import zip_longest


def meetup(year, month, week, day_of_week):
    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

    month_weeks = get_month(year, month)
    week_number = get_week_number(week, month_weeks, weekdays.get(day_of_week))

    try:
        day = next(day[0] for day in month_weeks[week_number] if day and day[1] == weekdays.get(day_of_week))

        return date(year, month, day)
    
    except IndexError:
        raise MeetupDayException("Week number not found.")


def get_month(year, month):
    weeks_in_month = Calendar().monthdays2calendar(year, month)
    flattened_dates = [day for week in weeks_in_month for day in week if day[0] != 0]
    formatted_dates = list(zip_longest(*(iter(flattened_dates),) * 7, fillvalue=""))

    return formatted_dates


def get_week_number(week, weeks, day_of_week):
    if week.isdigit():
        return int(week) - 1

    elif week == "teenth":
        for days in weeks:
            if any(day[1] == day_of_week for day in days if day[0] in range(13, 20)):
                return weeks.index(days)
        
        raise MeetupDayException("Week number not found.")

    elif week == "last":
        for days in reversed(weeks):
            if any(day[1] == day_of_week for day in days if day):
                return weeks.index(days)
        
        raise MeetupDayException("Week number not found.")

    else:
        return int(week[:-2]) - 1


class MeetupDayException(Exception):
    forgiveness = "I was forced to create this class on a script level due to the test class importing it."
