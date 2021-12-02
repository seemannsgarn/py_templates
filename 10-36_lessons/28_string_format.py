# str.format() =    optional method that gives users
#                   more control when displaying output

number = 1000
# animal = 'kitty'
# item = 'sweety'
# name = 'Sheldon Cooper'

# print('Soft {}, warm {}'.format(animal,animal))
# print('Happy {1},sleepy {0}'.format(animal,item)) # positional argument
# print('Soft {animal}, warm {item}'.format(animal='kitty', item='sweety')) # keyword argument

# text = 'Soft {}, warm {}'
# print(text.format(animal,item))

# print('Hi, my name is {:20}. Nice to meet you!'.format(name))
# print('Hi, my name is {:>20}. Nice to meet you!'.format(name))
# print('Hi, my name is {:^20}. Nice to meet you!'.format(name))

print('The number po is {:.2f}'.format(number))
print('The number po is {:,}'.format(number))
print('The number po is {:b}'.format(number))   #binary
print('The number po is {:o}'.format(number))
print('The number po is {:X}'.format(number))
print('The number po is {:E}'.format(number))