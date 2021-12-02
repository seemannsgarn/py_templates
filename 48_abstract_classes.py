# Prevents a user from creating an object of that class
# +compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract class = a method that has a declatation bot does not have an implementation.

# основная идея абстрактных классов в том что они не дают создавать объекты этого класса

from abc import ABC,abstractmethod

class Humanoid(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def death(self):
        pass

class Liveman(Humanoid):
    def go(self):
        print("This liveman is walking. ")

    def death(self):
        print("Liveman can die")

class Deadman(Humanoid):
    def go(self):
        print("This deadman is walking")

    def death(self):
        print("Deadman can't die!")

humanoid = Humanoid()
liveman = Liveman()
deadman = Deadman()

humanoid.go()
humanoid.death()
liveman.go()
deadman.go()