# Задание 1
def f(x, y):
    print(round(x))
    print(round(y))
    return


f(2.99, -1.6)

# Задание 2
str = 'www.my_site.com#about'
replace_values = {'#': '/'}


def replacing(str, replace_values):
    for i, j in replace_values.items():
        str = str.replace(i, j)
    return str


print(replacing(str, replace_values))


# Задание 3
def add(a, b):
    print(a + b)


add('stroka', 'ing')


# Задание 4
def repl(x, y):
    y + ' ' + x
    print(y + ' ' + x)


repl('Ivan', 'Ivanou')


# Задание 5
def cut_spaces(s):
    s = s.strip()
    return s


s = '           Ivan Ivanou '
s = cut_spaces(s)
print(s)

# Задание 6

school = {'1A': '25', '1B': '22', '1C': '26', '2A': '21', '2B': '28', '2C': '27', '3A': '24', '3B': '25', '3C': '29',
          '3D': '30'}


def merging(x, y):
    lst_str = y
    lst_num = x
    print(dict(zip(lst_num, lst_str)))


merging(['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C', '3D'], [25, 22, 26, 21, 28, 27, 24, 25, 29, 30])


# Задание 7
def intersept(a):
    print(a[1])


intersept([1, 2, 3, 4, 5, 6, 7, 8, 9])


# Задание 8
def checking(a, b):
    str = a
    str2 = b
    print(str in str2)


checking('employ', 'employment')


# Задание 9
def sign(x):
    print(x[1])
    print(x[3:18:3])


sign("My name is Agent Smith")


# Задание 10

def extr(b):
    print('Extra number')
    for i in b:
        if b.count(i) % 2 != 0:
            print(i)


extr([1, 5, 2, 9, 2, 9, 1, 1, 1])
