# Object Oriented Programming
# Define a class
class Car:
    # class attributes
    wheels= 4
    vendor="cfao"


    # constructer method
    # instance attributes
    def __init__(self, color, make, year):
        self.color= color
        self.make= make
        self.year= year
        
        
    def describe(self):
       print(f"This is a {self.color}, {self.make}, {self.year}.")


    def drive(self,task):
        print(f"This is a {self.color}, {self.make}, {self.year}. I {task}")   

# instantiate an object
# car1= Car("Beige", "Benz", 1998)
# car1.drive("Drive smoothly.")
# print(car1.color)
# print(car1.make)
# print(car1.year)

# print(car1.describe())


# Inheritance : Aclass takes on the methods and attributes of another class
class Car:
    def __init__(self, color, make, year):
        self.color= color
        self.make= make
        self.year= year
    def describe(self):
       print(f"This is a {self.color}, {self.make}, {self.year}.")


# A subclass 
class ElectricCar(Car):
    def __init__(self, color, make, year, battery):
        super().__init__(color, make, year)
        self.battery= battery

    def describe_electric(self):
        print(f"This is a {self.color}, {self.make}, {self.year} with a {self.battery} battery")    
        


car1= ElectricCar("Red", "Subaru", 2021, 1500)
# print(car1.describe())
# print(car1.describe_electric())
car1.describe()
car1.describe_electric()
