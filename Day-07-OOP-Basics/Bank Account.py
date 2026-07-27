class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show(self):
        print("Balance:", self.balance)


b = Bank(5000)

b.deposit(60000)
b.withdraw(5000)

b.show()
