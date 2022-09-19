s = 'f g g g d r t'.split()
repeated = []
lst = [s[0]]

for i in range(1, len(s)):
    print(lst)
    if s[i-1] != s[i]:
        lst.append([s[i]])
    else:
        lst[-1].append(s[i])

print(lst)
