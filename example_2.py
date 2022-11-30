from zipfile import ZipFile
from functools import reduce


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    total_size = reduce(lambda acc, x: acc + x.file_size, info, 0)
    total_size_compressed = reduce(lambda acc, x: acc + x.compress_size, info, 0)
    print(f'Объем исходных файлов: {total_size} байт(а)')
    print(f'Объем сжатых файлов: {total_size_compressed} байт(а)')

