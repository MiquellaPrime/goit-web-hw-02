from datetime import datetime, date, timedelta

DATE_FORMAT = "%d.%m.%Y"


def string_to_date(date_string: str) -> date:
    return datetime.strptime(date_string, DATE_FORMAT).date()


def date_to_string(date: datetime) -> str:
    return date.strftime(DATE_FORMAT)


def find_next_weekday(start_date: date, weekday: int) -> date:
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday: date) -> date:
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday
