#Animal Inheritance
class Animal:
    def speak(self, speak):
        print("their sounds")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

Dog().speak()
Cat().speak()



#Vehicle Class
class Vehicle:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

class Car(Vehicle):
    def __init__(self, brand, fuel, doors):
        Vehicle.__init__(self, brand, fuel)
        self.doors = doors

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print(f"The {self.brand} car is driving... Fuel left: {self.fuel}")
        else:
            print(f"The {self.brand} car has no fuel left!")

my_car = Car("Ford", 5, 4)
my_car.drive()
my_car.drive()
my_car.drive()
