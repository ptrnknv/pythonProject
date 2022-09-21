n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j]

for k in range(n):
    print(*matrix[k], end='')
    print()