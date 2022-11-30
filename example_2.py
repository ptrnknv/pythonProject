import json


with open('food_services.json', 'r', encoding='utf8') as file:
    type_of_catering = {}
    for line in json.load(file):
        type_of_catering[line['TypeObject']] = type_of_catering.get(line['TypeObject'], []) + [(line['Name'], line['SeatsCount'])]

for catering in sorted(type_of_catering):
    mx = max(type_of_catering[catering], key=lambda x: x[1])
    print(f'{catering}: {mx[0]}, {mx[1]}')
