from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from os import name


class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        print("name:", self.name)
        print("marks:", self.marks)

        if self.marks >= 35:
            print("result:, pass")

        else:
            print("result: fail")


name = input("enter student name:")
marks = int(input("enter student marks:"))

s = student(name, marks)

s.result()
