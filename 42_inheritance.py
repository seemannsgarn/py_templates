class Human:

    alive = True

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

class Anime_boy(Human):

    def watch_anime(self):
        print("This boy is watching anime")

class Redneck(Human):

    def drink(self):
        print("This animal is drinking")


anime_boy = Anime_boy()
redneck = Redneck()

print(anime_boy.alive)
# print(anime_boy.watch_anime())
# print(redneck.drink())
