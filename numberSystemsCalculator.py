
# Функция переводит из любой системы в 10 по параметру base

def trans_to_10(num, base):
    if base == 16:
        num = define_num(num)
    res = 0
    num = num[::-1]
    for i in range(len(num)):
        res += int(num[i]) * base ** i
    return res


# Функция переводит из 16 в 10

def define_num(num):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lst = []
    for c in num:
        if c.isalpha():
            for i in range(len(letters)):
                if letters.find(c) == i and i <= 10:
                    lst.append(str(i + 10))
        else:
            lst.append(c)
    return lst


# Функция переводит из 10 в любую другую систему по параметру base

def from_10_to_base(num, base=2):
    res = ''
    while num:
        num, d = divmod(num, base)
        sd = str(d) if d < 10 else str(chr(ord('A')+d-10))
        res = sd + res
    return res


def num_to(num):
    print(bin(num)[2:])
    print(oct(num)[2:])
    print(hex(num)[2:].upper())


num_to(int(input('Введите десятичное число: ')))
