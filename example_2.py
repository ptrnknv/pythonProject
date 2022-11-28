import csv


def key_func(grade):
    num, letter = grade.split('-')
    return int(num), letter


with open('student_counts.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
    rows = list(reader)
with open('sorted_student_counts.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
