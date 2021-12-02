# sort() method     = used with lists
# sort() function   = used with iterables

# adcs = ("Tristana", "Ashe", "Caitlyn", "Miss Fortune", "Jinx", "Ezreal", "Sivir")
#
# sorted_adcs = sorted(adcs, reverse=True)
#
# for i in sorted_adcs:
#     print(i)

# my_cars = [ ("BMW", "E", 1992),
#             ("Geely Emgrand", "D", 2015 ),
#             ("Nissan Quashkai", "C-SUV", 2010)]

my_cars = ( ("BMW", "E", 1992),
            ("Geely Emgrand", "D", 2015 ),
            ("Nissan Quashkai", "C-SUV", 2010))

# grade = lambda grade: grade[1]
year = lambda year: year[2]
# my_cars.sort(key=year,reverse=True)
sorted_cars = sorted(my_cars,key=year)

for i in sorted_cars:
    print(i)