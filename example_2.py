n = 4
m = 6
matrix = []
mx = -100
for i in range(n):
    matrix.append([int(j) for j in '1 2 3 4 5'.split()])
print(matrix)
for j in range(n):
    for k in range(m):
        print(matrix[j][k])
        if mx < matrix[j][k]:
            pass
            # mx = f'{k} {j}'
print()
print(matrix)
