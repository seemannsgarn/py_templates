# multiple inheritance = when a child class is derived from than one parent class

class Prey:
    def flee(self):
        print(f'{self} is running')

class Predator:
    def hunt(self):
        print(f'{self} is hunting')

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()