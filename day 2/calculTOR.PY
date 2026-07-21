from abc import ABC, abstractmethod


class a(ABC):
    @abstractmethod
    def add(self, x, y):
        pass

    @abstractmethod
    def sub(self, x, y):
        pass

    @abstractmethod
    def mul(self, x, y):
        pass

    @abstractmethod
    def div(self, x, y):
        pass


class Calculator(a):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y


print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice = int(input("enter your choice(1-4):"))

a = float(input("enter first number:"))
b = float(input("enter second number:"))

calculator = Calculator()

if choice == 1:
    print("answer=", calculator.add(a, b))
elif choice == 2:
    print("answer=", calculator.sub(a, b))
elif choice == 3:
    print("answer=", calculator.mul(a, b))
elif choice == 4:
    print("answer=", calculator.div(a, b))
else:
    print("invalid choice")
