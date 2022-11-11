from datetime import datetime


def is_available_date(booked_dates, book_date):
    pattern = '%d.%m.%Y'
    splitted_book = [datetime.strptime(date, pattern).toordinal() for date in book_date.split('-')]
    if len(splitted_book) > 1:
        splitted_book = range(splitted_book[0], splitted_book[1] + 1)
    for el in booked_dates:
        splitted_booked = [datetime.strptime(date, pattern).toordinal() for date in el.split('-')]
        if len(splitted_booked) > 1:
            splitted_booked = range(splitted_booked[0], splitted_booked[1] + 1)
        if set(splitted_book) & set(splitted_booked):
            return False
    return True




dates = ['04.11.2021', '05.11.2021-09.11.2021']  # True
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']  # False
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']  # False
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '12.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '09.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '15.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '17.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # True
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']  # False
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))

dates = ['14.09.2022-14.10.2022']  # False
some_date = '20.09.2022'
print(is_available_date(dates, some_date))

dates = ['14.09.2022-14.10.2022']  # True
some_date = '14.11.2022'
print(is_available_date(dates, some_date))

dates = ['14.09.2022-14.10.2022']  # True
some_date = '15.11.2022-16.11.2022'
print(is_available_date(dates, some_date))

dates = ['14.09.2022-14.10.2022']  # False
some_date = '14.09.2022-22.09.2022'
print(is_available_date(dates, some_date))
