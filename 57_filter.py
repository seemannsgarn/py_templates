# filter() = creates a collection of elements from an iterable for which a function returns
#
# filter(function, iterable)

friends = [ ("Sheldon",33),
            ("Leonard",34),
            ("Radge",32),
            ("Howard",31),
            ("Penny",30) ]

age = lambda data:data[1] >= 32

adult = list(filter(age, friends))
print(adult)