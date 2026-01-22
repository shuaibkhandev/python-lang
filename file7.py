print("This Lecture is on OOP in Python.\n")


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


# class Student():

#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
#         # print(self.marks1, self.marks2, self.marks3)
#     @staticmethod
#     def hello():
#         print("Hello World")
    
#     def average(self):
#         return (self.marks1 + self.marks2 + self.marks3)/3

# s1 = Student("Hashir", 97, 94, 98)
# # print(s1.average())
# s1.hello()


# class ABL_Account():

#     def __init__(self, user_name, password):
#         greeting = "Welcome to Allied Bank Limited"
#         print(greeting)
#         self.user_name = user_name
#         self.__password = password
    
#     def reset_pass(self, new_password):
#         print("old pass is", self.__password)
#         self.__password = new_password
#         print("new pass is", self.__password)


# acc1 = ABL_Account("Shuaib Khan", '123123')
# acc1.reset_pass("Admin#123")



# Inheritance

# class Car:
#     def __init__(self):
#         pass

#     @staticmethod
#     def start():
#         print("Car Started..")

#     @staticmethod
#     def stop():
#         print("Car Stopped..")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("Prius")

# print("Car Name is", car1.name)
# car1.start()
# car1.stop()



# Polymorphism

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNum(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, obj2):
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img
        return Complex(newReal, newImg)


num1 = Complex(3,5);
# num1.showNum()
num2 = Complex(4,7);
# num2.showNum()
# num3 = num1.addNum(num2)
# num3.showNum()

num3 = num1 + num2;
num3.showNum()