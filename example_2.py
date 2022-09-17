s = 'ОООООООООО'
count = 0
res = 0

for c in s:
    if c == 'Р':
        count += 1
        if res < count:
            res = count
    else:
        count = 0

print(res)


