class Human:
    def eat(self):
        print('Human eat food')

class Zombie(Human):
    def eat(self):
        print('Zombie eat human meat')

zombie = Zombie()
zombie.eat()
