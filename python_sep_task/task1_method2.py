import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

def main():
    shapes = {
        1: Rectangle,
        2: Triangle,
        3: Circle,
    }

    while True:
        select_num = int(input("Enter 1 for Rectangle, 2 for Triangle, 3 for Circle, or 0 to exit: "))
        
        if select_num == 0:
            break

        if select_num in shapes:
            shape_class = shapes[select_num]
            params = shape_class.__init__.__code__.co_varnames[1:]
            values = [int(input(f"Enter {param} value: ")) for param in params]
            result = shape_class(*values)
            print(f"{shape_class.__name__} Area is: {result.area()}")
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 0 to exit.")

main()

