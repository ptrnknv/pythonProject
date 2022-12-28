from string import ascii_lowercase as asc, digits as dg


def verification(login, password, success, failure):
    dt = {
        lambda x: x in asc or x in asc.upper(): 'в пароле нет ни одной буквы',
        lambda x: x in asc.upper(): 'в пароле нет ни одной заглавной буквы',
        lambda x: x in asc: 'в пароле нет ни одной строчной буквы',
        lambda x: x in dg: 'в пароле нет ни одной цифры'
    }
    for f in dt:
        if not any((f(l) for l in password)):
            return failure(login, dt[f])
    success(login)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)