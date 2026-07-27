class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print("Name=:", self.name)
        print("Salary=:", self.salary)


e = Employee("hemanth", "2500000")

e.details()
