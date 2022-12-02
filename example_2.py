from zipfile import ZipFile


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'


with ZipFile('desktop.zip', 'r') as zip_file:
    for info in zip_file.infolist():
        crumbs = info.filename.rstrip('/').split('/')
        size = info.file_size
        unit = convert_bytes(size)
        print(f"{'  ' * (len(crumbs)-1)}{crumbs[-1]}{' ' + unit if int(unit.split()[0]) > 0 else ''}")
