from zipfile import ZipFile
import json


def is_correct_json(string: str):
    try:
        json.loads(string)
        return True
    except:
        return False


with ZipFile('data.zip', 'r') as zip_file:
    arsenal = []
    for info in zip_file.infolist():
        with zip_file.open(info.filename, 'r') as file:
            reader = file.read().decode('utf-8', errors='ignore')
            if is_correct_json(reader):
                reader = json.loads(reader)
                if reader['team'] == 'Arsenal':
                    arsenal.append((reader['first_name'], reader['last_name']))
print(*sorted([name + ' ' + last for name, last in arsenal]), sep='\n')
