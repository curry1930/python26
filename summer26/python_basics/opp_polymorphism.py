#polymmorphism = greek word that mean "have many forms or faces"
#               poly = many
#               morph = forms

#               Two ways to achieve polymorphism 
#               1. inheritance = An object could be treated of the same type of the parent class
#               2. "Duck typing" = object must have necessary attributes/methods

from abc import ABC, abstractmethod
import math

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi * self.radius ** 2   
        
class Square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        return self.length ** 2   

class Triangle(Shape):
    def __init__(self,length,height):
        self.length=length
        self.height=height

    def area(self):
        return self.length * self.height * 0.5   

class Pizza(Circle):
    def __init__(self, radius, toppings):
        super().__init__(radius)
        self.toppings=toppings

shapes = [Circle(3),Square(4),Triangle(5,6), Pizza(11,"chicken")]    

for shape in shapes:
    print(f"{shape.area():.2f}cm²")



#"Duck Typing" = Another way to achieve polymorphism besides inheritance
#                Object must have the minimum necessary attributes/methods
#                "If it looks like a duck and quaks like a duck, it must be a duck "    