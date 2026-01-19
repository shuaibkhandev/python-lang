print("This Lecture is on OOP in Python.")


# class Car():
#     industry = 'Toyota'

#     def __init__(self, carName, carColor):
#         self.carName = carName
#         self.carColor = carColor
#         print("making new car..")
    
#     def hello(self):
#         print("Welcome to Toyota Company", self.industry)


# car1 = Car("Marcedes", 'Black');
# print(car1.carName, car1.carColor)
# car1.hello()

# car2 = Car("Range Rover", 'Grey');
# print(car2.carName, car2.carColor)


class Student():

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        # print(self.marks1, self.marks2, self.marks3)
    @staticmethod
    def hello():
        print("Hello World")
    
    def average(self):
        return (self.marks1 + self.marks2 + self.marks3)/3

s1 = Student("Hashir", 97, 94, 98)
# print(s1.average())
s1.hello()


