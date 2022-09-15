# Подключаем модуль random

from random import choice, shuffle


# Функция генерирующая пароли

def generate_password(length, chars):
    password = ''
    i = 0
    count = 1
    while i <= length - count:
        for j in range(len(chars)):
            password += choice(chars[j])
            count += 1

    password = list(password)
    shuffle(password)

    return ''.join(password)


# Строковые константы

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'
AMBIGUOUS = 'il1Lo0O'

chars = []    # Переменная chars = '' - содержит все символы, которые могут быть в генерируемом пароле.

# Опредеялем переменные пользовательского ввода

amount_pass = int(input('Укажите количество паролей для генерации: '))
len_pass = int(input('Укажите длину одного пароля: '))
digit_pass = input('В пароле должны быть цифры?: y = "yes"; for "no" press any key ').strip()
low_case_pass = input('Включать строчные буквы?: y = "yes"; for "no" press any key ').strip()
up_case_pass = input('Включать прописные буквы? y = "yes"; for "no" press any key ').strip()
chs_pass = input('Вкючать символы: "!#$%&*+-=?@^_."? : y = "yes"; for "no" press any key ').strip()
ambchrs_pass = input('Искючать неоднозначные символы: "il1Lo0O"? : y = "yes"; for "no" press any key ').strip()

# Добавляем необходимые символы

if digit_pass == 'y':
    chars.append(DIGITS)
if low_case_pass == 'y':
    chars.append(LOWERCASE_LETTERS)
if up_case_pass == 'y':
    chars.append(UPPERCASE_LETTERS)
if chs_pass == 'y':
    chars.append(PUNCTUATION)
if ambchrs_pass == 'y':  # Удаляем ненужные символы
    for i in range(len(chars) - 1):
        for c in AMBIGUOUS:
            chars[i] = chars[i].replace(c, '')

passwords = []

for _ in range(amount_pass):
    passwords.append(generate_password(len_pass, chars))

print(passwords)
