import csv


def condense_csv(file_name, id_name):
    dt = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in csv.reader(file):
            dt[line[0]] = dt.get(line[0], []) + [[line[1], line[2]]]
    ls = []
    for el in dt.items():
        temp = {id_name: el[0]}
        for data in el[1]:
            temp[data[0]] = data[1]
        ls.append(temp)

    with open('condensed.csv', 'w', encoding='utf-8') as file:
        columns = ls[0].keys()
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(ls)


condense_csv('data.csv', id_name='ID')
