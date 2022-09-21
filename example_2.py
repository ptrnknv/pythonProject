n = 4
m = 6
matrix = []

for i in range(1, m + 1):
    matrix.append([i * j for j in range(n)])
for j in range(n):
    for k in range(m):
        print(str(matrix[k][j]).ljust(3), end='')
    print()
