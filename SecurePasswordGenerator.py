# Подключаем модуль random

import random

# Строковые константы

DIGITS = 0123456789
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'

chars = ''    # Переменная chars = '', которая содержит все символы, которые могут быть в генерируемом пароле.

# Опредеялем переменные пользовательского ввода

amount_pass = input('Укажите количество паролей для генерации: ')
len_pass = input('Укажите длину одого пароля: ')
digit_pass = input('В пароле должны быть цифры?: ')
low_case_pass = input('Включать строчные буквы?: ')
up_case_pass = input('Включать прописные буквы? ')
chs_pass = input('Вкючать символы: "!#$%&*+-=?@^_."? : ')
ambchrs_pass = input('Вкючать неоднозначные символы: "il1Lo0O"? : ')
