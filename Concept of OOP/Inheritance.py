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
