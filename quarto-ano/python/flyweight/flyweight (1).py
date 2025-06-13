from abc import ABC,abstractmethod
from memory_profiler import profile 

ITERATIONS = 100000

class Geometry(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Geometry):
    def __init__(self,color,radius):
        self.color = color
        self.radius = radius
    def draw(self):
        print(f"Drawing a {self.color} circle of radius {self.radius}m")

class Square(Geometry):
    def __init__(self,color,side):
        self.color = color
        self.side = side
    def draw(self):
        print(f"Drawing a {self.color} square of sides {self.side}m")

class Rectangle(Geometry):
    def __init__(self,color,height,width):
        self.color = color
        self.height = height
        self.width = width
    def draw(self):
        print(f"Drawing a {self.color} rectangle of {self.height}x{self.width}m")

class Triangle(Geometry):
    def __init__(self, color, height, base):
        self.color = color
        self.height = height
        self.base = base
    def draw(self):
        print(f"Drawing a {self.color} triangle of base {self.base}m and height {self.height}m")


## FLYWEIGHT

class Color:
    def __init__(self, color):
        self.color = color

class ColorFactory:
    _colors = {}
    @staticmethod
    def get_color(color_name):
        if color_name not in ColorFactory._colors:
            ColorFactory._colors[color_name] = Color(color_name)
        return ColorFactory._colors[color_name]

class CircleFW(Geometry):
    def __init__(self,color,radius):
        self.color = ColorFactory.get_color(color)
        self.radius = radius
    def draw(self):
        print(f"Drawing a {self.color} circle of radius {self.radius}m")

class SquareFW(Geometry):
    def __init__(self,color,side):
        self.color = ColorFactory.get_color(color)
        self.side = side
    def draw(self):
        print(f"Drawing a {self.color} square of sides {self.side}m")

class RectangleFW(Geometry):
    def __init__(self,color,height,width):
        self.color = ColorFactory.get_color(color)
        self.height = height
        self.width = width
    def draw(self):
        print(f"Drawing a {self.color} rectangle of {self.height}x{self.width}m")

class TriangleFW(Geometry):
    def __init__(self, color, height, base):
        self.color = ColorFactory.get_color(color)
        self.height = height
        self.base = base
    def draw(self):
        print(f"Drawing a {self.color} triangle of base {self.base}m and height {self.height}m")


@profile
def test_standard():
    shapes = []
    for i in range(ITERATIONS):
        shapes.append(Circle("red",10))
        shapes.append(Square("red",10))
        shapes.append(Rectangle("red",10,10))
        shapes.append(Triangle("red",10,10))

@profile
def test_flyweigth():
    shapes = []
    for i in range(ITERATIONS):
        shapes.append(CircleFW("red",10))
        shapes.append(SquareFW("red",10))
        shapes.append(RectangleFW("red",10,10))
        shapes.append(TriangleFW("red",10,10))

if __name__ == "__main__":
    test_standard()
    test_flyweigth()