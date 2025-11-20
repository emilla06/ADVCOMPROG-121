#Shape Area
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(4)
rect = Rectangle(5, 7)
print("Circle Area:", circle.area())
print("Rectangle Area:", rect.area())



#Employee Payment
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate


class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

hourly = HourlyEmployee("Emi", 50, 100)
salaried = SalariedEmployee("Cath", 50000)

print("Hourly Employee Pay:", hourly.calculate_pay())
print("Salaried Employee Pay:", salaried.calculate_pay())
