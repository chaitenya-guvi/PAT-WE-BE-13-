class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2



class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "tHIS SHAPE IS A Rectangle MADE BY CHAITENYA"

shapes = [Circle(5), Rectangle(4, 6)]

for s in shapes:
    print(s)
    print(f"Area of shape : {s.area()}")
