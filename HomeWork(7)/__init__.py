# 1
g = (lambda x: 'Hello' + ' ' + x)
print(g('Artiom'))

# 2
list_n = ['Artiom', 'Olga', 'Gleb', 'Wojtek', 'Mateusz', 'Oliwia']
g = list(map(lambda element: f'Hello, {element}', list_n))
print(g)
