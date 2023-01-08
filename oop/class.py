# Define Bank Account Below:
class BankAccount:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0.0
    
    def deposit(self,money):
        self.balance += money
        return self.balance
    def withdraw(self,money):
        self.balance -= money
        return self.balance

name = BankAccount('asib')
print(name.balance)
print(name.deposit(20.5))
print(name.withdraw(5))
print(name.owner,name.balance)

