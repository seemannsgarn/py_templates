class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color


car_1 = Car()
motorcycle_1 = Motorcycle()

change_color(car_1,"red")
change_color(motorcycle_1,"black")

print(car_1.color)
print(motorcycle_1.color)