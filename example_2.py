numbers = {
    1: '.,?!:',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
    0: ' ',
}

s = list('Hello, World!'.upper())

for i in range(len(s)):
    for number in numbers.items():
        for j in range(len(number[1])):
            if s[i] == number[1][j]:
                print(str(number[0])*(j+1), end='')
