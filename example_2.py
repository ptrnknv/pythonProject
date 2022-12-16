from calendar import day_name
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
days = {i: d for i, d in enumerate(map(str.title, day_name), 1)}


def get_weekday(number):
    try:
        if type(number) != int:
            raise TypeError('Аргумент не является целым числом')
        elif number not in range(1, 8):
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
        else:
            return days[number]
    except TypeError as errT:
        raise errT
    except ValueError as errV:
        raise errV


try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
