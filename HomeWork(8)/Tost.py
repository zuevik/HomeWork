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












