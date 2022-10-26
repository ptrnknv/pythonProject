def read_csv():
    with open('/home/petr/Downloads/data.csv', 'r', encoding='utf-8') as file:
        res = []
        keys = [el.rstrip() for el in file.readline().split(',')]
        for values in file.readlines():
            value = [el.rstrip() for el in values.split(',')]
            res.append(dict(zip(keys, value)))
        return res


print(read_csv())

# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

# [{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]

