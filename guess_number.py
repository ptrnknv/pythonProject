from random import randint


def is_valid(num):
    if num.isdigit() and 0 < int(num) < 101:
        return True
    return False


print('Добро пожаловать в числовую угадайку')

if input('Сыграем? y = да ') == 'y':

    rnd = randint(1, 100)
    count = 0

    while True:

        user_n = input('Вводи число: ')

        if is_valid(user_n):
            user_n = int(user_n)
            count += 1
            if user_n == rnd:
                print('Вы угадали, поздравляем!')
                print(f'Число ваших попыток: {count}')
                if input('Сыграем ещё? y = да ') == 'y':
                    count = 0
                    rnd = randint(1, 100)
                else:
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    break
            elif user_n > rnd:
                print('Слишком много, попробуйте еще раз')
            elif user_n < rnd:
                print('Слишком мало, попробуйте еще раз')
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
