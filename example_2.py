from math import factorial


def pascal(n):
    list = []
    for i in range(n + 1):
        m = factorial(n) / (factorial(i) * factorial(n - i))
        list.append(int(m))

    return list


for i in range(int(input())):
    print(pascal(i))
# [1, 3, 3, 1]
