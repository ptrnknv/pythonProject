from zipfile import ZipFile


with ZipFile('workbook.zip') as zip_file:
    print(min([((info.compress_size / info.file_size) * 100, info.filename) for info in zip_file.infolist() if not info.is_dir()], key=lambda x: x[0])[1].split('/')[1])

