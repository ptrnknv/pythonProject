import json


with open('food_services.json', 'r', encoding='utf8') as file:
    catering, biggest = {}, {}
    for line in json.load(file):
        catering[line['District']] = catering.get(line['District'], 0) + 1
        biggest[line['OperatingCompany']] = biggest.get(line['OperatingCompany'], 0) + 1
catering_max = max(catering, key=lambda x: catering[x])
biggest_max = max(biggest, key=lambda x: biggest[x] if x != '' else 0)
print(f'{catering_max}: {catering[catering_max]}')
print(f'{biggest_max}: {biggest[biggest_max]}')

