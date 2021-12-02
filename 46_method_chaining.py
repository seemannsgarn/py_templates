# method chaining = calling multiple methods sequentially each call performs an action
#                   on the same object and returns self

class Name_class:

    def write_first_letter(self):
        print("F")
        return self
    def write_second_letter(self):
        print("U")
        return self
    def write_third_letter(self):
        print("C")
        return self
    def write_fourth_letter(self):
        print("K")
        return self

item = Name_class()

item.write_first_letter( )
item.write_second_letter()
item.write_third_letter()
item.write_fourth_letter()