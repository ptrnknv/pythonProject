import csv
import json


with open('playgrounds.csv', 'r', encoding='utf8') as file, open('addresses.json', 'w', encoding='utf8') as outer:
    res = {}
    for line in csv.DictReader(file, delimiter=';'):
        res[line['AdmArea']] = res.get(line['AdmArea'], {})
        res[line['AdmArea']][line['District']] = res[line['AdmArea']].get(line['District'], []) + [line['Address']]
    print(json.dumps(res, indent='   ', ensure_ascii=False))

