n = 6
f1, f2, f3 = 1, 1, 1

for i in range(n):
    print(f1)
    f1, f2, f3 = f2, f3, f1 + f2 + f3

