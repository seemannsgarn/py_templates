
# Python will assign the __name__ variable a value of '__main__' if it's the initial module being run
# **********************************************
#   if __name__== '__main__'
# **********************************************

# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__
import module_two
print(__name__)
print(module_two.__name__)