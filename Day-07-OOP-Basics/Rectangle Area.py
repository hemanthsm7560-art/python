class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("area=", self.length * self.breadth)


r = Rectangle(10, 5)

r.area()
