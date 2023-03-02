# # 1
# g = (lambda x: 'Hello' + ' ' + x)
# print(g('Artiom'))
#
# # 2
# list_n = ['Artiom', 'Olga', 'Gleb', 'Wojtek', 'Mateusz', 'Oliwia']
# g = list(map(lambda element: f'Hello, {element}', list_n))
# print(g)

#1
n = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


!!!!!!!!!!!!!!!def my_generator(n):
    i = 0
    while n < i:
        yield i
        i * -1

my_generator(n)