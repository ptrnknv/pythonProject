import csv
from collections import namedtuple
from datetime import datetime

with open('meetings.csv', 'r', encoding='utf8') as file:
    guests = sorted(csv.DictReader(file), key=lambda x: (datetime.strptime(x['meeting_date'], '%d.%m.%Y'),
                                                         datetime.strptime(x['meeting_time'], '%H:%M')))
    for guest in guests:
        Guest = namedtuple('Guest', ['surname', 'name'])
        temp = Guest(guest['surname'], guest['name'])
        print(*temp)
