# 1
print(round(-1.6))
print(round(2.99))

# 2
str1 = ('www.my_site.com#about')
print(str1.replace('#', '/'))

# 3
str2 = ('stroka')
print(str2.replace('oka', 'ing'))

# 4
str_1 = 'Ivan'
str_2 = ' '
str_3 = 'Ivanou'

str_4 = str_1 + str_2 + str_3
print(str_3, str_1)

# 5
str_5 = (' Ivan Ivanou ')
print(str_5[1:-1])

# 6`
dict = {'1A': '25', '1B': '22', '1C': '26', '2A': '21', '2B': '28', '2C': '27', '3A': '24', '3B': '25', '3C': '29',
        '3D': '30'}
school = dict

# 7
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1])

# 8
if __name__ == '__main__':
    str_6 = 'employ'
    str_7 = 'employment'
    if str_7.__contains__(str_6):
        print("Contains")
    else:
        print("Does not contain")

# 9
x = "My name is Agent Smith"
print(x[1])
print(x[3:18:3])

# 10
if __name__ == '__main__':
    b = [1, 5, 2, 9, 2, 9, 1, 1, 1]

    unique = {x for x in b if b.count(x) % 2 == 1}
    print(unique)

    print("another method")
    for i in b:
        if b.count(i) % 2 != 0:
            print(i)
