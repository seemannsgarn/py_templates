# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments

def add(*something):
    sum = 0
    for i in something:
        sum += i
    return sum

print(add(123,334,54,67,89,65))