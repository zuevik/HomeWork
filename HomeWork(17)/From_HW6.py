# def square_in_file(*args):
#     with open('text', "w") as file:
#         for i in args:
#             file.write(str(i) + '\n')
#
#     with open('text', 'r') as file:
#         numbers = list(map(float, file.readlines()))
#
#     squares = list(map(lambda x: x ** 2, numbers))
#
#     with open('text', 'w') as file:
#         for square in squares:
#             file.write(str(square) + '\n')
# square_in_file(1, 2, 3)



# 4
def to_change_information_in_two_binaryes(list_1, list_2):
    with open("file1.bin", "wb") as f1:
        arr_1 = bytearray(list_1)
        f1.write(arr_1)
    with open("file2.bin", "wb") as f2:
        arr_2 = bytearray(list_2)
        f2.write(arr_2)

    file1 = "file1.bin"
    file2 = "file2.bin"


    with open(file1, 'rb') as f1:
        data1 = f1.read()


    with open(file2, 'rb') as f2:
        data2 = f2.read()


    with open(file2, 'wb') as f2:
        f2.write(data1)

    with open(file1, 'wb') as f1:
        f1.write(data2)

    print(data2)



