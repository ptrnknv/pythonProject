def print_matrix(matrix, n, width=1):
  for r in range(n):
    for c in range(n):
      print(str(matrix[r][c]).ljust(width), end=' ')
    print()


n = 3
matrix = []
c = 1
for r in range(1, n + 1):
  row = []
  for i in range(c, c + n):
    row.append(i)
    c = i + 1
  matrix.append(row)

print_matrix(matrix, n)
