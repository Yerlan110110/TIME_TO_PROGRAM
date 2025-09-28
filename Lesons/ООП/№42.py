from math import pi
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(pi * self.radius ** 2)
a = Circle(5)
a.area()
    

    
