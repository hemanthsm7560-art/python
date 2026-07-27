class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("area of a circle=", 3.14 * self.radius * self.radius)


c = Circle(5)

c.area()
