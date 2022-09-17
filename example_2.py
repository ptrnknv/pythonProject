s = 'тимур'
strng = s + ' запретил букву'
b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
     'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
count = 0
has = ''
alph = ''

for j in range(len(strng)):
    if strng[j] not in has:
        has += strng[j]
        count += 1

for i in range(len(b)):
    for c in has:
        if b[i] == c:
            alph += c

for i in range(count-1):
    if strng[1:3] == '  ':
        strng = strng[0:1] + strng[2:]
    print(strng, alph[i])
    strng = strng.replace(alph[i], '')

