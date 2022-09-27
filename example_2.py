n, m = [int(i) for i in input().split()]
board1 = [input().split() for _ in range(n)]
board2 = [input().split() for _ in range(n)]
total = board = [['0'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        total[i][j] = int(board1[i][j]) + int(board2[i][j])

for row in total:
    for col in row:
        print(str(col), end=' ')
    print()