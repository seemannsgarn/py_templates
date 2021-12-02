# list comprehension =    a way to create a new list with less syntax
#                         can mimic certain lambda functions, easier to read
#                         list = [expression for item in iterable]
#                         list = [expression for item in iterable if conditional]
#                         list = [expression if/else for item in iterable if conditional]

# --------------examples------------------------------------------------------
# squares = []                # create an empty list
# for i in range(1,11):       # create a for loop
#     squares.append(i * i)   # define what each loop iteration should do
# print(squares)
#
# squares = [i * i for i in range(1,11)]
# print(squares)
#
# a = ['frya ' * i for i in range(1,5)]
# print(a)
# -----------------------------------------------------------------------------

students = [100,90,80,70,60,50,40,30,20,10,0]
# passed_students = list(filter(lambda x: x >= 60, students))
# passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "DICK" for i in students]
print(passed_students)


