from programs_from_homework6_to_test import square_in_file
import unittest
import os

class File_works(unittest.TestCase):

    def setUp(self):
        with open('text', 'w') as file:
            file.write('')

    def tearDown(self):
        if os.path.exists('text'):
            os.remove('text')



# Test 1
    def test_square_in_file(self):
        square_in_file(1, 2, 3)
        with open('text', 'r') as file:
            result = list(map(float, file.readlines()))
        expected = [1.0, 4.0, 9.0]
        self.assertEqual(result, expected)



#Test 2
    def test_too_low_amount_of_numbers(self):
        with self.assertRaises(ValueError):
            square_in_file(1, 2)



#Test 3
    def test_of_negative_numbers(self):
        square_in_file(-1, -2, -3)
        with open('text', 'r') as file:
            result = list(map(float, file.readlines()))
        expected = [1.0, 4.0, 9.0]
        self.assertEqual(result, expected)



#Test 4
    def test_with_one_letter_instead_of_a_number(self):
        with self.assertRaises(ValueError):
            square_in_file(1, 2, 'i')



#Test 5
    def test_with_no_numbers(self):
        with self.assertRaises(ValueError):
            square_in_file()




if __name__ == '__main__':
    unittest.main()



