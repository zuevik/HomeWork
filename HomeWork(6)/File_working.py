

# # 1
#
# with open('text', "r") as file:
#     content = file.read()
#     numbers = list(map(float, content.split()))
# if len(numbers) <= 3:
#     print("Ошибка: файл содержит менее четырех чисел")
# else:
#     print(f"Первый элемент: {numbers[0]}")
#     print(f"Второй элемент: {numbers[1]}")
#     print(f"Предпоследний элемент: {numbers[-2]}")
#     print(f"Последний элемент: {numbers[-1]}")
#
#
#
# # 2
# with open('text_1', 'r') as file:
#     text_of_file = file.read()
#     words = text_of_file.strip(',')
#
#     numbers = []
#     for word in words:
#         if word.strip().isdigit():
#             numbers.append(int(word))
#
#     even_numbers = [x for x in numbers if x % 2 == 0]
#     odd_numbers = [x for x in numbers if x % 2 == 1]
#
# with open('even_txt', 'w') as even_file:
#     for x in even_numbers:
#         even_file.write(str(x) + '\n')
#
# with open('odd_numbers', "w") as odd_file:
#     for x in odd_numbers:
#         odd_file.write(str(x) + '\n')
#
#


# 3
def square_in_file(*args):
    with open('text', "w") as file:
        for i in args:
            file.write(str(i) + '\n')

    with open('text', 'r') as file:
        numbers = list(map(float, file.readlines()))

    squares = list(map(lambda x: x ** 2, numbers))

    with open('text', 'w') as file:
        for square in squares:
            file.write(str(square) + '\n')

square_in_file(1, 2, 3)

# # 4
# with open("file1.bin", "wb") as f1:
#     num_1 = [45, 1, 100, 23]
#     arr_1 = bytearray(num_1)
#     f1.write(arr_1)
# with open("file2.bin", "wb") as f2:
#     num_2 = [6, 11, 14]
#     arr_2 = bytearray(num_2)
#     f2.write(arr_2)
#
# file1 = "file1.bin"
# file2 = "file2.bin"
#
#
# with open(file1, 'rb') as f1:
#     data1 = f1.read()
#
#
# with open(file2, 'rb') as f2:
#     data2 = f2.read()
#
#
# with open(file2, 'wb') as f2:
#     f2.write(data1)
#
# with open(file1, 'wb') as f1:
#     f1.write(data2)
