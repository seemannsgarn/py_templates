# **kwargs =    parameter that will pack all arguments into a dictionary
#               useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    print('Hello',end=' ')
    for key,value in kwargs.items():
        print(value,end=' ')

hello(title='Doctor',first='Sheldon',middle='Lee',last='Cooper')