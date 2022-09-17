# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

n = int(input())
lst = [input() for i in range(n)]
res = []
total = []

for i in range(len(lst)):
    search = ['a', 'n', 't', 'o', 'n']
    for c in lst[i]:
        if c == search[0]:
            res.append(search.pop(0))
        if not search:
            total.append(i+1)
            res = []
            break

print(*total)

