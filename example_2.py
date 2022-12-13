from collections import Counter
import csv
import json

total = Counter()
for i in '1234':
    with open(f'quarter{i}.csv', 'r', encoding='utf8') as file:
        _, *reader = csv.reader(file)
    for product, *amount in reader:
        total.update({product: sum(map(int, amount))})
result = 0
with open('prices.json', 'r', encoding='utf8') as file:
    for k, v in json.load(file).items():
        result += total[k] * v

print(result)
