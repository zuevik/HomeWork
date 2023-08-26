#1
import timeit



def factorial_generator():
    n = 1
    result = 1
    while True:
        yield result
        n += 1
        result *= n


t = timeit.Timer(lambda: list(factorial_generator() for i in range(10)))
execution_time = t.timeit(number=1000)
print("Время выполнения: {:.6f} секунд".format(execution_time))




def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)

print(factorial_rec(10))
t = timeit.Timer(lambda: factorial_rec(10))
print('Время выполнения рекурсии: ', t.timeit(number = 1000), 'секунд')






def factorial_func(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial_func(10))



b = timeit.Timer(lambda: factorial_func(10))
print('Время выполнения кода: ', b.timeit(number = 1000), 'секунд')



#2
def typed(type):
    def decorator(func):
        def wrapper(*args):
            converted_args = []
            for arg in args:
                if type == 'str':
                    arg = str(arg)
                elif type == 'int':
                    arg = int(arg)
                elif type == 'float':
                    arg = float(arg)
                converted_args.append(arg)
            return func(*converted_args)
        return wrapper
    return decorator




@typed(type = 'str')
def add_two_symbols(a, b):
    return a + b


add_two_symbols("3", 5)
add_two_symbols(5, 5)
add_two_symbols('a', 'b')




@typed(type = 'int')
def add_three_symbols(a, b, с):
    return a + b + с


add_three_symbols(5, 6, 7)
add_three_symbols("3", 5, 0)
add_three_symbols(0.1, 0.2, 0.4)


l1 = add_two_symbols("3", 5)
l2 = add_two_symbols(5, 5)
l3 = add_two_symbols('a', 'b')
l4 = add_three_symbols(5, 6, 7)
l5 = add_three_symbols("3", 5, 0)
l6 = add_three_symbols(0.1, 0.2, 0.4)
print(l1, l2, l3, l4, l5, l6)


#3
