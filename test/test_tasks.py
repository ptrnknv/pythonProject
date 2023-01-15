import pytest
import os
from zipfile import ZipFile

list_files = os.listdir('/home/petr/Desktop/PycharmProjects/pythonProject/answers')
list_zip = list(filter(lambda x: x.lower().endswith(".zip"), list_files))
if list_zip:
    # Чтение содержимого архива
    zip_with_test = list_zip[0]
    with ZipFile(zip_with_test) as zip_file:
        files = zip_file.namelist()
        # Распределение на тесты и ответы к тестам
        test_code = list(filter(lambda x: not x.endswith(".clue"), files))
        test_answer = list(filter(lambda x: x.endswith(".clue"), files))


@pytest.mark.parametrize('matrix, expected_results', test_code)
def test_matrix_to_dict(matrix):
    assert
