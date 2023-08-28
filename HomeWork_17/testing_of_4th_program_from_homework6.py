from HomeWork_17.programs_from_homework6_to_test import to_change_information_in_two_binaryes
import unittest
import os
import struct


class testOfBinariesChanger(unittest.TestCase):

    def setUp(self):
        with open('file1.bin', 'wb') as f1:
            f1.writelines('')
        with open('file2.bin', 'wb') as f2:
            f2.writelines('')

    def tearDown(self):
        if os.path.exists('file1.bin'):
            os.remove('file1.bin')
        if os.path.exists('file2.bin'):
            os.remove('file2.bin')

    def test_to_change_information_in_two_binaryes(self):
        list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

        to_change_information_in_two_binaryes(list_1, list_2)

        with open('file1.bin', 'rb') as f1:
            coded_bin1 = f1.read()
        with open('file2.bin', 'rb') as f2:
            coded_bin2 = f2.read()

        length_lst_1 = len(list_1)
        length_lst_2 = len(list_2)

        x = str(length_lst_1) + 'B'
        y = str(length_lst_2) + 'B'

        uncoded_bin1 = struct.unpack(x, coded_bin1)
        uncoded_bin2 = struct.unpack(y, coded_bin2)

        expected_1 = tuple(list_2)
        expected_2 = tuple(list_1)

        self.assertEqual(expected_1, uncoded_bin1)
        self.assertEqual(expected_2, uncoded_bin2)

    if __name__ == '__main__':
        unittest.main()
