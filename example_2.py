inp = '3 4'.split()
n = int(inp[0])
m = int(inp[1])
matrix = []

for i in range(n):
    for j in range(m):
        matrix.append(['.'] * m)

for i in range(n):
    for j in range(m):
        if i % 2 !=0:
            if j % 2 != 0:
                matrix[i][j] = '*'
        else:
            if j % 2 == 0:
                matrix[i][j] = '*'

for k in range(n):
    print(*matrix[k], end='')
    print()