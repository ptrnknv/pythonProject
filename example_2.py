from collections import namedtuple
import itertools as it

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

weight_limit = int(input())
mx_price = 0
res = []
for i in range(len(items)):
    for j in it.combinations(items, i):
        total_mass = 0
        total_price = 0
        name = ''
        for el in j:
            total_mass += el.mass
            total_price += el.price
            name = el.name
        if total_mass <= weight_limit:
            if total_price > mx_price:
                mx_price = total_price
                res.append(j)
                print(total_mass)
                print(total_price)

for i in res:
    print(sorted(i))
if res:
    for el in sorted(res[-1]):
        print(el.name)
else:
    print('Рюкзак собрать не удастся')
