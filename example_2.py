from zipfile import ZipFile
from datetime import datetime


with ZipFile('workbook.zip') as zip_file:
     print(*sorted(map(lambda x: x.filename.split('/')[1] if len(x.filename.split('/')) > 1 else x.filename, filter(
            lambda x: datetime(2021, 11, 30, 14, 22, 0) < datetime(*x.date_time) and not x.is_dir(), zip_file.infolist()))),
           sep='\n')

