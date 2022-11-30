import csv
import json
from datetime import datetime


with open('exam_results.csv', 'r', encoding='utf8') as file, open('best_scores.json', 'w', encoding='utf8') as outer:
    temp = {}
    for student in sorted(csv.DictReader(file), key=lambda x: (int(x['score']), datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S')), reverse=True):
        temp[student['email']] = temp.get(student['email'], student)
    res = []
    for el in sorted(temp):
        temp[el]['best_score'] = int(temp[el].pop('score'))
        res.append(temp[el])
    json.dump(res, outer, indent='   ')

