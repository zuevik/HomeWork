import unittest
import os
from programs_from_homework6_to_test import to_change_information_in_two_binaryes

class TestBinaryChanger(unittest.TestCase):
    #creating of temporary file
    def setUp(self):
        with open('file1.bin', 'wb') as f1:
            f1.writelines('')
        with open('file2.bin', 'wb') as f2:
            f2.writelines('')
    #deleting of temporary files
    def tearDown(self):
        if os.path.exists('file1.bin'):
            os.remove('file1.bin')
        if os.path.exists('file2.bin'):
            os.remove('file2.bin')

    def run_test(self, input_list1, input_list2):

        expected_output = [bytes(input_list2), bytes(input_list1)]
        to_change_information_in_two_binaryes(input_list1, input_list2)


        #checking of values quantity in the lists
        if len(input_list1) < 1 or len(input_list2) < 1:
            raise ValueError


        #checking of the highest and lowest value in the list
        for i in input_list1 and input_list2:
            if i < 0 or i > 256:
                raise ValueError

        with open('file1.bin', 'rb') as f1:
            coded_bin1 = f1.read()
        with open('file2.bin', 'rb') as f2:
            coded_bin2 = f2.read()

        self.assertEqual(coded_bin1, expected_output[0])
        self.assertEqual(coded_bin2, expected_output[1])


    def test_case_1(self):                          #general test 1
        input_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        input_list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        self.run_test(input_list1, input_list2)


    def test_case_2(self):                          #general test 2
        input_list1 = [0, 0, 0]
        input_list2 = [1, 1, 1]
        self.run_test(input_list1, input_list2)

    def test_case_3(self):                          #test with no values
        input_list1 = []
        input_list2 = []
        with self.assertRaises(ValueError):
            self.run_test(input_list1, input_list2)

    def test_case_4(self):                          #check lowest barier
        input_list1 = [-1, 0, 1]
        input_list2 = [1, 2, 3]
        with self.assertRaises(ValueError):
            self.run_test(input_list1, input_list2)

    def test_case_5(self):                             #check highest barier
        input_list1 = [257, 256, 255]
        input_list2 = [1, 2, 1]
        with self.assertRaises(ValueError):
            self.run_test(input_list1, input_list2)



if __name__ == '__main__':
    unittest.main()


