# higher order function = a function that either:
#                         1. accepts a function as an argument
#                             or
#                         2. returns a function
#                         (In python, functions are also treated as objects)

# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def fck(func):
#     text = func("FuCK yOu")
#     print("==============")
#     print(text)
#     print("==============")
#
#
# fck(loud)

# def divisor(x):
#     def divident(y):
#         return y/x
#     return divident
#
# divide = divisor(3)
# print(divide(9))

def text(text):
    def name(x):
        return text * x
    return name

result = text("You are awesome! ")
print(result(2))