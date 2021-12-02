# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

champ_pool = list()
while champ := input("What is your champ pool: ") != "quit":
champ_pool.append(champ)


# print(a := True)