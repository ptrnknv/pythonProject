s = 'home sweet Home sweet.'.split()
s = [el.lower().strip('.,!?:;-') for el in s]
total = {}

for i in range(len(s)):
    total[s[i]] = total.get(s[i], 0) + 1

res = {}

for el in total.items():
    #print(el)
    if el[1] == min(total.values()):
        res[el[0]] = el[1]

print(sorted(res)[0])


