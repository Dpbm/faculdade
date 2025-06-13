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

class GeometricForms:
    def __init__(self):
        self.forms = []
    def add_form(self, form):
        self.forms.append(form)
    def draw_all(self):
        for form in self.forms:
            form.draw()


## FLYWEIGHT

class Color:
    def __init__(self, color):
        self.color = color

class ColorFactory:
    _colors = {}
    
    @classmethod
    def get_color(cls, color):
        if color not in cls._colors:
            cls._colors[color] = Color(color)
        return cls._colors[color]

class CircleFW(Geometry):
    def __init__(self,color,radius):
        self.color = ColorFactory.get_color(color)
        self.radius = radius
    def draw(self):
        print(f"Drawing a {self.color.color} circle of radius {self.radius}m")

class SquareFW(Geometry):
    def __init__(self,color,side):
        self.color = ColorFactory.get_color(color)
        self.side = side
    def draw(self):
        print(f"Drawing a {self.color.color} square of sides {self.side}m")

class RectangleFW(Geometry):
    def __init__(self,color,height,width):
        self.color = ColorFactory.get_color(color)
        self.height = height
        self.width = width
    def draw(self):
        print(f"Drawing a {self.color.color} rectangle of {self.height}x{self.width}m")

class TriangleFW(Geometry):
    def __init__(self, color, height, base):
        self.color = ColorFactory.get_color(color)
        self.height = height
        self.base = base
    def draw(self):
        print(f"Drawing a {self.color.color} triangle of base {self.base}m and height {self.height}m")


@profile
def default_implementation():
    print("=====Testing Default implementation=====")
    forms = GeometricForms()

    for _ in range(ITERATIONS):
        for form,color in zip((Circle, Square), ("red", "yellow")):
            forms.add_form(form(color, 10))
        
        for form,color in zip((Rectangle, Triangle), ("blue", "gray")):
            forms.add_form(form(color, 10, 10))

@profile
def default_implementation_only_circles():
    print("=====Testing Default implementation (Only circles)=====")
    forms = GeometricForms()
    for _ in range(ITERATIONS):
        forms.add_form(Circle("green", 10))
        


@profile
def flyweight_version():
    print("=====Testing Flyweight implementation=====")
    forms = GeometricForms()

    for _ in range(ITERATIONS):
        for form,color in zip((CircleFW, SquareFW), ("red", "yellow")):
            forms.add_form(form(color, 10))
        
        for form,color in zip((RectangleFW, TriangleFW), ("blue", "gray")):
            forms.add_form(form(color, 10, 10))

@profile
def flyweight_version_only_circles():
    print("=====Testing Flyweight implementation (Only Circles)=====")
    forms = GeometricForms()

    for _ in range(ITERATIONS):
        forms.add_form(CircleFW("purple", 10))



if __name__ == "__main__":
    default_implementation()
    flyweight_version()

    default_implementation_only_circles()
    flyweight_version_only_circles()


# TEST SETTING A DIFFERENT FLYWEIGHT FOR NUMBERS