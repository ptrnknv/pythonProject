# 1
# 6
# 36
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
num = int(input())
flag = False
for i in range(len(lst)):
    for j in lst[i+1:]:
        print(lst[i:])
        if lst[i] * j == num:
            flag = True

if flag:
    print('ДА')
else:
    print('НЕТ')