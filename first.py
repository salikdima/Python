'''n = int(input('Enter number:\n'))

x = int(555//3*(2+345)**7-345+n)

print(x)
'''


'''
import math
x = -3.55
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))

'''
'''n = int(input("Enter time(sec):\n"))

x = str(n/60*10)
y = str(x)
print(y)

'''

first_name = 'Dima'
last_name = 'Karchik'
print('Hello,{first} {last}'.format
    (
    first = first_name,
    last = last_name,
    ))


temp_string = 'abcdefghijp'
print(temp_string.replace('b', 'c').replace('j', 'c').replace('d', 'c').replace('e', 'c'))