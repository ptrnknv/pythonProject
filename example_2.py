n = '489 483 43 2 3 84 1 4 3 2 5 4 3 13'.split()
last = [n.pop()]
a = input().split()

print(*[a[-1]] + a[:-1])
print(n)
print(last)