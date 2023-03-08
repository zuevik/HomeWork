# 1
g = (lambda x: 'Hello' + ' ' + x)
print(g('Artiom'))

# 2
list_n = ['Artiom', 'Olga', 'Gleb', 'Wojtek', 'Mateusz', 'Oliwia']
g = list(map(lambda element: f'Hello, {element}', list_n))
print(g)


# 2

def my_generator(x):
    for num in x:
        if num < 0:
            num_new = num * -1
            yield num_new
        else:
            num_new = num
            yield num_new


x = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_numbers = list(my_generator(x))
print(new_numbers)


# 3
def sentencer(n):
    word = n.split(' ')
    for i in word:
        try:
            if i != 'the':
                yield len(i)
        except TypeError:
            yield None
            print(f"TypeError: '{i}' is not a string")


n = "the quick brown fox jumps over the lazy dog"
word_lengths = list(sentencer(n))
print(word_lengths)


# 4
def encode(v_original, step):
    v_lower = 'abcdefghijklmnopqrstuvwxyz'
    v_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v_final = ''
    i = 0
    while i < len(v_original):
        if v_original[i] in v_lower:
            k = v_lower.find(v_original[i])
            k += step
            if k >= len(v_lower):
                k = k - len(v_lower)
            v_final += v_lower[k]
        elif v_original[i] in v_upper:
            k = v_upper.find(v_original[i])
            k += step
            if k >= len(v_upper):
                k = k - len(v_upper)
            v_final += v_upper[k]
        else:
            v_final += v_original[i]
        i += 1
    print(v_final)


encode('awake', 5)


def decode(v_original, step):
    v_lower = 'abcdefghijklmnopqrstuvwxyz'
    v_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v_final = ''
    i = 0
    while i < len(v_original):
        if v_original[i] in v_lower:
            k = v_lower.find(v_original[i])
            k -= step
            if k >= len(v_lower):
                k = k - len(v_lower)
            v_final += v_lower[k]
        elif v_original[i] in v_upper:
            k = v_upper.find(v_original[i])
            k -= step
            if k >= len(v_upper):
                k = k - len(v_upper)
            v_final += v_upper[k]
        else:
            v_final += v_original[i]
        i += 1
    print(v_final)


decode('fbfpj', 5)
