
# Class
# Attributes of an object is called properties
# Actions of an object is called methods

class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name, "plays tennis")
        elif self.occupation == "Actor":
            print(self.name, "shoots a film")

    def speaks(self):
        print(self.name, "says how are you?")

Tom = Human("Tom Cruise", "Actor")
Tom.do_work()
Tom.speaks()

Maria = Human("Maria Sharapova", "Tennis Player")
Maria.do_work()
Maria.speaks()


# INHERITANCE - Is used to inherit attributes of another class


class Vehicle:
    def general_usage(self):
        print("The general usage: transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm a motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")

car = Car()
car.specific_usage()

mcycle = MotorCycle()
mcycle.specific_usage()

# isinstance() function tells if an object is an instance of a specific class or not
print(isinstance(car, Car), ": the object is an instance")

# issubclass() function tells if an object is a subclass of a specific class or not
print(issubclass(Car, Vehicle))


# MULTIPLE INHERITANCE

class Father():
    def skills(self):
        print("Father: gardening, programming")

class Mother():
    def skills(self):
        print("Mother: cooking, art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: sport","writing")


child = Child()
child.skills()