# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map (function, iterable)

store = [   ("dick", 20.00),
            ("black dick", 25.00),
            ("pussy", 50.00),
            ("matador 5 DVD", 10.00)
        ]

to_rubles = lambda data: (data[0],data[1] * 69,37)

store_rubles = list(map(to_rubles, store))

for i in store_rubles:
    print(i)


