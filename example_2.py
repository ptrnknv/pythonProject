list = [2, 5, 7, 4, 3]
target = 12

for i in range(len(list)):
    for j in range(i, len(list) - i):
        if list[i] + list[j] == target:
            print(i, j)