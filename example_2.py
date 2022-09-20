n = int(input())
m = int(input())
matrix = []
for i in range(n):
    temp = [input() for _ in range(m)]
    matrix.append(temp)

for j in range(len(matrix)):
    print(*matrix[j])
print()
matrix = []
for i in range(m):
    temp = [input() for _ in range(n)]
    matrix.append(temp)

for j in range(len(matrix)):
    print(*matrix[j])