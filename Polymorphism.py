from abc import ABC, abstractmethod


class shapes:
    @abstractmethod
    def area(self):
        pass

class circle(shapes):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius * 3.14 ** 2


class square(shapes):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class triangle(shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.height * self.base *0.33

cal = [circle(3), square(4), triangle(6, 7)]
for shapes in cal:
    print(f"{shapes.area():.1f}cm square")
