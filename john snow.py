# 1
print(round(-1.6))
print(round(2.99))

# 2
str1 = 'www.my_site.com#about'
print(str1.replace('#', '/'))


# 3
str2 = 'stroka'
str3 = 'ing'
str4 = str2 + str3
print(str4)

# 4
str_1 = 'Ivan Ivanou'
b = str_1.split(' ')
print(b[1] + ' ' + b[0])


# 5
# str1 = 'Ivan'
# str2 = ' '
# str3 = 'Ivanou'
# str3 = s2 + s1
# str4 = str3.lstrip(' ')
# str5 = str4.rstrip(' ')
# print(str5, end='.')

# 6`
school = {'1A': '25', '1B': '22', '1C': '26', '2A': '21', '2B': '28', '2C': '27', '3A': '24', '3B': '25', '3C': '29',
        '3D': '30'}

# 7
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1])

# 8
str = 'employ'
str2 = 'employment'
print(str in str2)


# 9
x = "My name is Agent Smith"
print(x[1])
print(x[3:18:3])

# 10
#  b = [1, 5, 2, 9, 2, 9, 1, 1, 1]
#
#     unique = {x for x in b if b.count(x) % 2 == 1}
#     print(unique)
#
#     print("another method")
#     for i in b:
#         if b.count(i) % 2 != 0:
#             print(i)
