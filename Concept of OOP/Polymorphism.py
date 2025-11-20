class InkPrinter:
    def print_document(self):
        return "Printing using ink..."

class LaserPrinter:
    def print_document(self):
        return "Printing using laser..."

printers = [InkPrinter(), LaserPrinter()]
for prnt in printers:
    print(prnt.print_document())
