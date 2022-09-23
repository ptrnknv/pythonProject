n = 3
m = 4
board = [['0'] * m for _ in range(n)]
last = 0

for i in range(n):
    for j in range(1, m + 1):
        last += 1
        board[i][j-1] = last

for row in board:
    for col in row:
        print(str(col).ljust(3), end='')
    print()