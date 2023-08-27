from From_HW6 import square_in_file
import unittest
import os

class File_works(unittest.TestCase):

    def setUp(self):
        with open('text', 'w') as file:
            file.write('')

    def tearDown(self):
        if os.path.exists('text'):
            os.remove('text')

    def test_square_in_file(self):
        square_in_file(1, 2, 3)
        with open('text', 'r') as file:
            result = list(map(float, file.readlines()))
        expected = [1.0, 4.0, 9.0]
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()



