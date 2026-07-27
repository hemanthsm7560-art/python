class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show(self):
        print("account holder:", self.name)
        print("Balance:", self.balance)


account = Bankaccount("hemanth", 5000)

account.deposit(1000)

account.show()
