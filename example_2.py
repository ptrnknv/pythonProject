from datetime import datetime


def fill_up_missing_dates(dates: list[str]) -> list[str]:
    ls = [datetime.strptime(date, '%d.%m.%Y').toordinal() for date in dates]
    return sorted([datetime.fromordinal(el).strftime('%d.%m.%Y') for el in range(min(ls), max(ls) + 1)])


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))
