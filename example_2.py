def get_value(dt, key):
    if key in dt:
        return dt[key]
    for k, v in dt.items():
        if isinstance(v, dict):
            value = get_value(v, key)
            if value is not None:
                return value




data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))
