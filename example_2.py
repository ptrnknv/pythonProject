import json


def is_correct_json(string: str):
    try:
        json.loads(string)
        return True
    except:
        return False


data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))
print(is_correct_json('number = 17'))
data = '''{
        "beegeek": 2018,
        "stepik": 2013
       }'''

print(is_correct_json(data))
data = '''{
        "beegeek": 2018,
        ("Timur", "Guev"): 29,
        ("Artur", "Harisov"): 20,
        "stepik": 2013
       }'''

print(is_correct_json(data))
print(is_correct_json('99999'))
data = '''{
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Artur', 'Harisov'): 20,
        'stepik': 2013
       }'''

print(is_correct_json(data))
data = '''{
        'beegeek': 2018,
        'stepik': 2013
       }'''

print(is_correct_json(data))
