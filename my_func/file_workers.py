def read_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()
