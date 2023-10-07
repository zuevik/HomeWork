import pytest
from for_testing import square_in_file

@pytest.fixture
def temporary_file_edit(tmp_path):
    file_path = tmp_path / 'temporary_file.txt'
    with open(file_path, 'w') as file:
        file.write('1\n2\n3\n')
    return file_path



def test_square_in_file(temporary_file_edit, tmp_path):
    square_in_file(1, 2, 3, file_path=temporary_file_edit)

    with open(temporary_file_edit, 'r') as file:
        result = list(map(float, file.readlines()))

    assert result == [1.0, 4.0, 9.0]


def test_square_in_file_with_2_numbers_value_Error(temporary_file_edit, tmp_path):
    with pytest.raises(ValueError):
        square_in_file(file_path=temporary_file_edit)



def test_square_in_file_with_no_numbers(temporary_file_edit, tmp_path):
    with pytest.raises(ValueError):
        square_in_file(file_path=temporary_file_edit)


def test_square_in_file_with_float_numbers(temporary_file_edit, tmp_path):
    square_in_file(1.5, 2.5, 3.5, file_path=temporary_file_edit)

    with open(temporary_file_edit, 'r') as file:
        result = list(map(float, file.readlines()))

    assert result == [2.25, 6.25, 12.25]

def test_square_with_lost_number(temporary_file_edit, tmp_path):
    with pytest.raises(ValueError):
        square_in_file(1, 'i', 3, file_path=temporary_file_edit)





if __name__ == '__main__':
    pytest.main()



C:/Users/zuevi/PycharmProjects/HomeWork(18)/HomeWork(18)/test_file_of_task_3.py:44





