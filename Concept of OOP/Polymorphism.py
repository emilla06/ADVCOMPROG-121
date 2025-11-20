#Printer
class InkPrinter:
    def print_document(self):
        return "Printing using ink..."

class LaserPrinter:
    def print_document(self):
        return "Printing using laser..."

printers = [InkPrinter(), LaserPrinter()]
for prnt in printers:
    print(prnt.print_document())



#Duck Typing
def make_it_speak(animal):
    animal.speak()

class Bird:
    def speak(self):
        print("Chirp! Chirp!")

class Robot:
    def speak(self):
        print("Beep! boop!")

make_it_speak(Bird())
make_it_speak(Robot())
