
n = int(input())

matrix = [input().split() for i in range(n)]
has = []
samp = []
flag = False

for i in range(n):
    c, r, m, s = 0, 0, 0, 0
    lastC = c
    lastR = r
    for j in range(n):
        c += int(matrix[j][i])
        r += int(matrix[i][j])
        m += int(matrix[i][j])
        s += int(matrix[i][n - j - 1])
        has.append(int(matrix[i][j]))

    if c == r and m == s and r == m and c == s:
        flag = True
    else:
        flag = False
        break

for i in range(min(has), n ** 2 + 1):
    samp.append(i)
has.sort()
if has == samp and flag:
    print('YES')
else:
    print('NO')