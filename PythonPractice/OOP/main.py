from car import Car
from boat import Boat
from plane import Plane


def main():
    car1 = Car("Ford", "Mustang")
    boat1 = Boat("Ibiza", "Touring 20")
    plane1 = Plane("Boeing", "747")
    
    for x in (car1, boat1, plane1):
        print(x.brand)
        print(x.model)
        x.move()

main()
