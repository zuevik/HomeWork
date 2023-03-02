#Variables 1.0
def vard():
    var_int = 10
    var_float = 8.4
    var_str = 'No'
    var_big = var_int * 3.5
    var_int / var_float
    var_big / var_float
    var_str = 'No' * 2 + 'Yes' * 3
    print('var_int :', var_int)
    print('var_float:', var_float)
    print('var_str:', var_str)
    print('var_big:', var_big)
vard()

# Strings
# Задание 1
def outta(x):
    str_eight = x
    lnth = len(str_eight)
    print(str_eight, ';', str_eight[0], str_eight[lnth-1], str_eight[2], str_eight[lnth-3], 'String length:', lnth)
outta('How are you?')

# Задание 2
def stren(str_ten):
    lnth2 = len(str_ten)
    str_center = lnth2 // 2
    print(str_ten, '/ String length:', )
    print(str_ten[0:8], '/', str_ten[(str_center-1):(str_center+3)], "/", str_ten[3:lnth2:3], "/", str_ten[::-1], "/")
stren('benzodiazepines')
# Задание 3
def cams(str_name):
    f = str_name.rfind('name')
    str_name = str_name[0:f] + "Artiom"
    print(str_name)
cams("my name is name")

# Задание 4
def test_tring(x):
    print('index cof "w" is', x.find("w"))
    print('There are', x.count('l'), 'letters "l".')
    print('"Hello" at the beginning:', x.startswith('Hello'))
    print('"qwe" at the end:', x.startswith('qwe'))


test_tring('Hello world!')


# Lists
# Задания 1-6
def printer(x, y):
    print('2nd element of the 1st list:', x[1])
    y[len(y)-1] = 444
    print('2nd list:', y)
    list_both = x + y
    print('common list:', list_both)
    list_both_new = list_both[0:5] + list_both[(len(list_both) - 4):(len(list_both))]
    print(list_both_new)
    list_both_new.extend([8, 153])
    print("final list:", list_both_new)
printer([1, 3, 4, 9, 5, 6, 17, 16, 2, 7], [21, 35, 68, 8, 44, 96, 13, 71, 64, 47])

# Задания 7-8
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


print('united list:', c)

# Логические операции
def frid(d, e):
    print('__and__')
    print(d < e and (e - d) > 0)
    print(d < e and d > 0)
    print(d > e and (e * d) == 0)
    print(d == e and (e - d) > 0)
    print('__or__')
    print(d < e or e > 0)
    print(d < e or d != 0)
    print(d > e or e <= 0)
    print(d == e or (e - d) < 0)
    str_logic = 'Python'
    print('__and__or___string')
    print(len(str_logic) < 7 and str_logic[0] == 'P')
    print(str_logic[0] == str_logic[len(str_logic)-1] or str_logic == 7)
frid(6, 18)

# Dictionaries
def schooler(school):
    print("School:", school)
    print("In the group '5к' there are", school.get("5к"), "pupils.")
    school["1а"] = 31
    school["7в"] = 27
    school["9г"] = 28
    school["2ж"] = 27
    school["6г"] = 26
    school.pop("5к")
    print("Changes at school:", school)
schooler({"1а": 32, "1б": 27, "2б": 30, "3и": 29, "5к": 26, "6а": 31, "7в": 25, "8д": 28, "9г": 24, "10в": 22})

# Преобразование типов
# Задания 1-3
def rob(x):
    x = x.split()
rob('Robin Singh')
rob('I love arrays they are my favorite')

def merger(x):
    list_a = x
    list_a = ' '.join(list_a)
    print(list_a)
merger(['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite'])

def naming(x, y, z):
    name = z
    place_a = x
    place_b = y
    print('Привет,', name, '! Добро пожаловать в', place_a, place_b)
naming('Minsk', 'Belarus', 'Ivan Ivanou')


# Задание 4
def tenner(x):
    list_ten = x
    print(list_ten)
    list_ten.insert(2, 'ты')
    list_ten.pop(6)
    print(list_ten)
tenner(['съешь', 'же', 'ещё', 'этих', 'мягких', 'французских', 'булок', 'да', 'выпей', 'чаю'])

# Задание 5
def merger_1(a, b):
    ab = a | b
    print(ab)
merger_1({'a': 1, 'b': 2, 'c': 3}, {'c': 3, 'd': 4, 'e': 5})

# Условия
num_one = 8
if num_one > 0:
    num_one +=1
print(num_one)

list_three = [5, 89, -4]
i = 0
for item in list_three:
    if item > 0:
        i += 1
print('Positive numbers:', i)

# Задание 3
def gem(x):
    year = x
    if (year % 400 != 0) and (year % 100 == 0):
        print (year, 'не високосный год')
    elif (year % 4 == 0):
        print (year, 'високосный год')
    else:
        print (year, 'не високосный год')
gem(700)

# задание 4
def weekday(x):
    if x == 1:
        print('monday')
    elif x == 2:
        print('tuesday')
    elif x == 3:
        print('wensday')
    elif x == 4:
        print('thursday')
    elif x == 5:
        print('friday')
    elif x == 6:
        print('sunday')
    elif x == 7:
        print('saturday')
weekday(5)

# Задание 5
def converter(x,  y):
    if x == 1:
        print(y)
    elif x == 2:
        d = y / 1000000
        print(d)
    elif x == 3:
        d = y / 1000
        print(d)
    elif x == 4:
        d = y * 1000
        print(d)
    elif x == 5:
        d = y / 100
        print(d)
converter(5, 5000000)


# Цикл for
# Задания 1-2
def ranger_v2(A, B):
    total_sum = 0
    for i in range(A, B+1):
        total_sum += i
    print(total_sum)
ranger_v2(6, 15)


def ranger_v3(A, B):
    if A < 0:
        A = 1
    total_sum = 0
    for i in range(A, B+1):
        total_sum += i
    print(total_sum)
ranger_v3(-2, 15)

# Задание 3
def calculator():
    prod_nums = 1
    sum_min_nums = 0
    minus_count = 0
    for i in range(10):
        num = int(input('Ввести число: '))
        if num < 0:
            sum_min_nums += 1
            minus_count += num
        elif num > 0:
            prod_nums *= num
        print('Произведение чисел', prod_nums)
        print('Сумма отрицательных', sum_min_nums)
        print('Кол-во отрицательных', minus_count)
calculator()

# Задание 4
plywacze = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17
}

best_czas = 99

for plywacz, czas in plywacze.items():
    if best_czas is None or czas < best_czas:
        best_czas = czas

print(f'Лучший результат заплыва среди 6 участников: ', best_czas)


# Цикл while
# Задание 1
def conter_v2(N):
    home = 1
    i = 0
    while i < N:
        i += 1
        home *= i
    print(home)
conter_v2(5)
#2
def surface(x):
    year = 0
    S1 = x
    S2 = x
    while S2 < S1 * 9:
        year += 1
        S2 *= 3
        S1 *= 2
    print(year)
surface(1)

# Задание 3
def liczer(n):

    count = 0
    sum_liczb = 0

    while n > 0:
        liczba = n % 10
        count += 1
        sum_liczb += liczba
        n //= 10

    print(f'Кол-во цифр', {count})
    print(f'Сумма цифр', {sum_liczb})
liczer(29103481)

# Задание 4
def age(x, y):
    year = 0
    N = x
    M = y
    while M > N * 2 :
        year += 1
        N += 1
        M += 1
    print(f'Кол-во прошедших лет', {year})
    print(f'Возраст спиногрыза', {N})
    print(f'Возраст деда', {M})
age(7, 57)



