from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))
max_len = []
total = 0
for ingredient, amount in sorted(order.items()):
    ingredient_string = f'{ingredient.ljust(len(max(order, key=len)))} x {amount}'
    print(ingredient_string)
    max_len.append(len(ingredient_string))
    total += ingredients[ingredient] * amount
total_string = f'ИТОГ: {total}р'
max_len.append(len(total_string))
print(''.ljust(max(max_len), '-'), total_string, sep='\n')
