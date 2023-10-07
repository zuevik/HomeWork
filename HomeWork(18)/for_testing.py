#3
def square_in_file(*args, file_path='text'):
    with open(file_path, "w") as file:
        for i in args:
            file.write(str(i) + '\n')

    with open(file_path, 'r') as file:
        numbers = list(map(float, file.readlines()))
    if len(numbers) < 3:
        raise ValueError
    squares = list(map(lambda x: x ** 2, numbers))

    with open(file_path, 'w') as file:
        for square in squares:
            file.write(str(square) + '\n')





# 4
def to_change_information_in_two_binaryes(list_1, list_2, name_of_first_file="file1.bin", name_of_second_file="file2.bin"):
    with open(name_of_first_file, "wb") as f1:
        arr_1 = bytearray(list_1)
        f1.write(arr_1)
    with open(name_of_second_file, "wb") as f2:
        arr_2 = bytearray(list_2)
        f2.write(arr_2)

    file1 = name_of_first_file
    file2 = name_of_second_file


    with open(file1, 'rb') as f1:
        data1 = f1.read()


    with open(file2, 'rb') as f2:
        data2 = f2.read()


    with open(file2, 'wb') as f2:
        f2.write(data1)

    with open(file1, 'wb') as f1:
        f1.write(data2)

    print(data2)



