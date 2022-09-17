t, r = input(), input()
var = ['камень', 'бумага', 'Спок', 'ножницы', 'ящерица']

if t == r:
    print('ничья')
elif t == 'камень':
    if r in ['ножницы', 'ящерица']:
        print('Тимур')
    else:
        print('Руслан')
elif t == 'бумага':
    if r in ['Спок', 'камень']:
        print('Тимур')
    else:
        print('Руслан')
elif t == 'Спок':
    if r in ['ножницы', 'камень']:
        print('Тимур')
    else:
        print('Руслан')
elif t == 'ножницы':
    if r in ['ящерица', 'бумага']:
        print('Тимур')
    else:
        print('Руслан')
elif t == 'ящерица':
    if r in ['Спок', 'бумага']:
        print('Тимур')
    else:
        print('Руслан')
