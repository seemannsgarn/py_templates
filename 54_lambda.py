# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, bit only has one expression,
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# ---------it's the same-----------

# def doudble(x):
#     return x * 2
# print(doudble(2))

# double = lambda x: x * 2
# print(double(2))

# -----------examples---------------
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False
print(age_check(77))