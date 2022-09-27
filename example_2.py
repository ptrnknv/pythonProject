n = int(input())
board = [input().split() for _ in range(n)]
matrix = [[int(x) for x in input().split()] for i in range(n)]
res = [['0'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        res[i][j] = board[j][i]

for row in res:
    for col in row:
        print(str(col), end=' ')
    print()

for i in range(8):
    for j in range(8):
        if i == y and j == x:
            matrix[i][j] = 'N'
        inx = (x - j) * (y - i)
        if inx == 2 or inx == -2:
            matrix[i][j] = '*'