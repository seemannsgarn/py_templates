# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

name = 'Erkul'      # global scope (available inside & outside inside this  functions)

def dispay_name():
    name = 'Puaro'  # local scope (available only inside this function)
    print(name)

dispay_name()
print(name)