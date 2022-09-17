# 8
# 17
# 33
# 56
# 70
# 66
# 50
# 20
# 38
# 1400
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
num = int(input())
flag = False
for i in range(len(lst)):
    for j in lst[i:]:
        if lst[i] * j == num:
            flag = True

if flag:
    print('ДА')
else:
    print('НЕТ')