n = '6 5 8 79 8 57 69'.split()
count = 0
for i in range(len(n) - 1):
    if n[i] < n[i+1]:
        count += 1

print(count)