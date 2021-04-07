import test as ts

name = input('Enter your name: ')

while name == '':
    name = input('Enter your name: ')

print(ts.sum_names(name))
