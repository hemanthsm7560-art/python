class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"Student name: {self.name}, age: {self.age}"

    def is_adult(self):
        return self.age >= 18


name = input("enter your name:")
age = int(input("enter your age:"))
student = student(name, age)

print(student.describe())
print(student.is_adult())
