# Получение данных от пользователя

text = input('Введите текст: ')
direction = input('c = зашифровать; d = дешивровать: ')
shift = int(input('Введите сдвиг шифрования: '))

# Определение переменных

eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
rus_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


# Функция шифрует нужный символ

def ciphered_letter(alpha, letter, shift):
    index_letter_alpha = alpha.find(letter)
    if direction == 'c' or direction == 'с':
        index_letter_alpha -= len(alpha)
    else:
        return alpha[index_letter_alpha - shift]
    return alpha[index_letter_alpha + shift]


# Функция шифрования

def cipher(text, shift):
    ciphered = ''
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                if text[i] in rus_upper:
                    ciphered += ciphered_letter(rus_upper, text[i], shift)
                else:
                    ciphered += ciphered_letter(eng_upper, text[i], shift)
            else:
                if text[i] in rus_lower:
                    ciphered += ciphered_letter(rus_lower, text[i], shift)
                else:
                    ciphered += ciphered_letter(eng_lower, text[i], shift)
        else:
            ciphered += text[i]

    return ciphered

print(cipher(text, shift))

# Функция возвращает сдвиг по количеству символов в слове

# def shift_by_word(text):
#     splitted_text = text.split()
#     shifts = []
#     for el in splitted_text:
#         word = ''
#         for c in el:
#             if c.isalpha():
#                 word += c
#         shifts.append(len(word))
#
#     return shifts

# text = 'Day, mice. "Year" is a mistake!'
# shifts = shift_by_word(text)
# text = text.split()
# result = []
#
# for i in range(len(shifts)):
#     result.append(cipher(text[i], shifts[i]))
#
# print(' '.join(result))

# print(cipher('Day, mice. "Year" is a mistake!', 1))
# Gdb, qmgi. "Ciev" ku b tpzahrl!