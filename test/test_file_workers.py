from my_func.file_workers import read_from_file


def test_read_from_file():
    test_data = ['Black goat\n', 'Pink goat\n']
    assert read_from_file('test_file.txt') == test_data


def test_read_from_file1():
    test_data = ['Black goat\n', 'Pink goat\n']
    assert read_from_file('test_file.txt') == test_data
