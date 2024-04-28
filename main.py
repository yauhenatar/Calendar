from config import *


def get_leap_year(year: int) -> bool:
    return True if year % 4 == 0 else False


def get_february_days() -> int:
    year = int(input('Enter year:\n'))
    return DAYS_COUNT['February'][1] if get_leap_year(year) else DAYS_COUNT['February'][0]


def get_days_count() -> int:
    needed_month = input('Enter month:\n').capitalize()
    if needed_month == 'February':
        return get_february_days()
    else:
        return DAYS_COUNT[needed_month] if needed_month in list(DAYS_COUNT) else get_days_count()


if __name__ == '__main__':
    print(get_days_count())