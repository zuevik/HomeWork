s1 = 'Hello'
s2 = ' '
s3 = 'World'
s4 = '!'
str = s1 + s2 + s3 + s4
print(str)
print(str[0])
str2 = str.replace(' ', '-')
print(str2)
str3 = s2 + s1 + s2
print(str3)
str4 = str3.lstrip(' ')
str5 = str4.rstrip(' ')
print(str5, end='.')
if s1 == str5:
    print('True')






