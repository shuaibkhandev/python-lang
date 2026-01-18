print("This Lecture is on OOP in Python.")


class Car():
    def __init__(self, carName, carColor):
        self.carName = carName
        self.carColor = carColor
        print("making new car..")

car1 = Car("Marcedes", 'Black');
print(car1.carName, car1.carColor)

car2 = Car("Range Rover", 'Grey');
print(car2.carName, car2.carColor)