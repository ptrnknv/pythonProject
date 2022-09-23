xy = 'f3'
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
matrix = []
for i in range(8):
    for j in range(8):
        point = '.'
        matrix.append([point] * 8)

for i in range(8):
    for j in range(8):
        if i == y and j == x:
            matrix[i][j] = 'N'
        inx = (x - j) * (y - i)
        if inx == 2 or inx == -2:
            matrix[i][j] = '*'


for k in range(8):
    print(*matrix[k], end='')
    print()