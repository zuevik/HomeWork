import pytest
from for_testing import to_change_information_in_two_binaryes
import os

#1
test_sets = [
    ([12, 13, 14, 15, 16, 17, 18, 19], [1, 2, 3, 4, 5, 6, 7]),
    ([12, 13, 14, 15, 16, 17, 18, 19], [1, 2, 3, 4, 5, 6, 7]),
    ([12, 13, 18, 19], [5, 6, 7]),
    ([1, 2, 3], [5, 6, 7]),
    ([1, 2, 3], [3, 4, 5])
]


@pytest.mark.parametrize("x, y", test_sets)
def test_of_changing_inf_between_two_binaries(x, y):
    with open('file_1.bin', 'wb') as f1:
        f1.write(b'')

    with open('file_2.bin', 'wb') as f2:
        f2.write(b'')

    to_change_information_in_two_binaryes(x, y, 'file_1.bin', 'file_2.bin')

    with open('file_1.bin', 'rb') as f1_read:
        info_from_first_file = f1_read.read()

    with open('file_2.bin', 'rb') as f2_read:
        info_from_second_file = f2_read.read()

    assert info_from_first_file == bytes(y)
    assert info_from_second_file == bytes(x)














