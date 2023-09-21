import math
class shape:
    def area(self):
        pass
class Square(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

class Triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (0.5 * self.base * self.height)

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (math.pi * self.radius * self.radius)
    
class main():
    value = input("Are you ready for play : Yes/No ").lower()
    while value != 'no':
        while True:
            select_num = int(input("Enter 1 for Square, 2 for Triangle, 3 for circle : "))
            if select_num < 4 and select_num > 0:
                print(f"You have selected : {select_num}")
                break
            else:
                print("Enter number only 1,2, and 3")

        if select_num == 1:
            length_val = int(input("Enter square length values : "))
            width_val = int(input("Enter square width values : "))
            result  = Square(length_val, width_val)
            print(f"Square Area is : {result.area()}")
        elif select_num == 2:
            base_val = int(input("Enter Triangle base values : "))
            height_val = int(input("Enter Triangle height values : "))
            result = Triangle(base_val,height_val)
            print(f"Triangle Area is : {result.area()}")
        else:
            radius_val = int(input("Enter radius Values : "))
            result = Circle(radius_val)
            print(f"Circle Area is : {result.area()}")
        value = input("Do you want to continue : (Yes/No) ")
main()