# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# ----------------------------------------------------------------------------------

# socks_in_shop = {"red socks":10,"black socks":15,"yellow socks":23,"blue socks":18}
# socks_in_shop_in_rubles = {key : (value) * 69 for (key,value) in socks_in_shop.items()}
# print(socks_in_shop_in_rubles)

# ----------------------------------------------------------------------------------

# dictionary = {'Ironman':'Marver',
#               'Batman':'DC Comics',
#               'Hulk':'Marvel',
#               'Superman':'DC Comics',
#               'Captain America':'Marvel',
#               'Joker':'DC Comics'}
#
# DC_dictionary = {key: value for (key,value) in dictionary.items() if value == 'DC Comics'}
# print(DC_dictionary)

# ----------------------------------------------------------------------------------

# socks_in_shop = {"red socks":10,"black socks":15,"yellow socks":23,"blue socks":18}
# socks_description = {key: ("Low price" if value <= 15 else "High price") for (key,value) in socks_in_shop.items()}
# print(socks_description)

# ----------------------------------------------------------------------------------
def check_price(value):
    if value >= 15:
        return "HIGH"
    else:
        return "LOW"
socks_in_shop = {"red socks":10,"black socks":15,"yellow socks":23,"blue socks":18}
socks_descrip = {key: check_price(value) for (key,value) in socks_in_shop.items()}
print(socks_descrip)
