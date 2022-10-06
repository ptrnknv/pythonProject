s = 'name age x x2 j k l name x y k j e a x name number'.split()
result = {}

for i in range(len(s)):
    result[i] = result.get(s[i], s[i]) + f'_{s[:i].count(s[i])}'
for el in result.items():
    if '_0' in el[1]:
        result[el[0]] = el[1][:-2]

print(*result.values())

