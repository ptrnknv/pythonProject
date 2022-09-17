n = '1 2 3 4 5'.split()

for i in range(0, len(n) - 1, 2):
        n[i], n[i+1] = n[i+1], n[i]

print(*n)