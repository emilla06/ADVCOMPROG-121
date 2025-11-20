class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance= balance
        
    def deposit(self, amount):
        self.balance += amount
        print (f"{self.owner} deposited Php {amount}. New balance: Php{self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew Php{amount}. Remaining balance: Php {self.balance}")
        else:
            print("Insuficient funds!")

amount1= BankAccount("Emi", 1000)
amount1.deposit(500)
amount1.withdraw(300)
amount1.withdraw(10000)
