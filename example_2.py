from datetime import datetime


def choose_plural(amount, declensions):
    last_dig = amount % 10
    last_two = amount % 100
    if 4 < last_two < 21:
        return f'{amount} {declensions[2]}'
    elif 5 > last_dig > 1:
        return f'{amount} {declensions[1]}'
    elif last_dig == 1:
        return f'{amount} {declensions[0]}'

    return f'{amount} {declensions[2]}'


def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60


pattern = '%d.%m.%Y %H:%M'
release = datetime.strptime('08.11.2022 12:00', pattern)
inp = datetime.strptime(input(), pattern)
res = release - inp
hours, minutes = hours_minutes(res)
declensions =  {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"), 2: ("минута", "минуты", "минут")}
if hours == 0:
    print(f'До выхода курса осталось: {choose_plural(res.days, declensions[0])}')
elif res.days == 0:
    if minutes == 0:
        print(f'До выхода курса осталось: {choose_plural(hours, declensions[1])}')
    elif hours == 0:
        print(f'До выхода курса осталось: {choose_plural(minutes, declensions[2])}')
    else:
        print(f'До выхода курса осталось: {choose_plural(hours, declensions[1])} и {choose_plural(minutes, declensions[2])}')
elif inp > release:
    print('Курс уже вышел!')
else:
    if hours == 0:
        print(f'До выхода курса осталось: {choose_plural(res.days, declensions[0])}')
    else:
        print(f'До выхода курса осталось: {choose_plural(res.days, declensions[0])} и {choose_plural(hours, declensions[1])}')
