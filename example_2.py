ls = [input().split('@')[0] for _ in range(int(input()))]
dt = {}
for el in ls:
    if el[-1].isdigit():
        dt[el[:-1]] = dt.get(el[:-1], []) + [el[-1]]
    else:
        dt[el] = dt.get(el, [])
for _ in range(int(input())):
    inp = input()
    if inp in dt.keys():
        dt[inp].append(int(dt[inp][-1])+1 if dt[inp] else 1)
        print(inp + str(int(dt[inp][-1])) + '@beegeek.bzz' if dt[inp] else inp + '1' + '@beegeek.bzz')
    else:
        dt[inp] = []
        print(inp + '@beegeek.bzz')
