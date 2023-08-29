# import unittest
# import os
#
# numbers = (1.4, 1.5, 1.6, 3.0)
#
#
# def process_numbers(input_filename, output_filename):
#     with open('text', "w") as file:
#         for i in numbers:
#             file.write(str(i) + '\n')
#
# with open('text', 'r') as file:
#     our_numbers = list(map(float, file.readlines()))
#
# squares = list(map(lambda x: x ** 2, our_numbers))
#
# with open('text', 'w') as file:
#     for square in squares:
#         file.write(str(square) + '\n')
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
#
# def process_numbers(input_filename, output_filename):
#     with open(input_filename, 'r') as file:
#         numbers = list(map(float, file.readlines()))
#
#     squares = list(map(lambda x: x ** 2, numbers))
#
#     with open(output_filename, 'w') as file:
#         for square in squares:
#             file.write(str(square) + '\n')
#
# class TestProcessNumbers(unittest.TestCase):
#     def test_square_calculation(self):
#         input_filename = 'test_input.txt'
#         output_filename = 'test_output.txt'
#
#         with open(input_filename, "w") as file:
#             for i in (1.4, 1.5, 1.6):
#                 file.write(str(i) + '\n')
#
#         process_numbers(input_filename, output_filename)
#
#         with open(output_filename, 'r') as file:
#             result_squares = list(map(float, file.readlines()))
#
#         expected_squares = [x ** 2 for x in (1.4, 1.5, 1.6)]
#
#         self.assertEqual(result_squares, expected_squares, "Ошибка в расчете квадратов чисел")
#
#         # Очистка временных файлов
#         os.remove(input_filename)
#         os.remove(output_filename)
#
# if __name__ == '__main__':
#     unittest.main()





a = 'b'
print(3*a)