lst = [i for i in 'a b c d e f g h i j k l m n'.split()]
n = 3
res = []
temp = []
shift = 0

for i in range(shift, n):
    for j in range(i, len(lst), n):
        temp.append(lst[j])
        shift += 1

    res.append(temp)
    temp = []

print(res)