class student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("student name:", self.name)


s1 = student("Hemanth")
s1.display()
