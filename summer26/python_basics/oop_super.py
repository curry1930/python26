#super() = Function used in a child class to call methods from a parent class (superclass)
#          Allows you to extend the functionality to the inherited methods 

import math

class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"it is {self.color} colored and {"filled" if self.is_filled else "not filled"}")   

class Circle(Shape):
    def __init__(self,shape,color,is_filled,radius):
        super().__init__(color,is_filled)               #constructor from the parent class
        self.shape=shape
        self.radius=radius

    def describe(self):
        super().describe()
        print(f"it is a {self.shape} with area of {math.pi * pow(self.radius,2)}")    

class Square(Shape):
    def __init__(self,shape,color,is_filled,length,):
        super().__init__(color,is_filled)
        self.shape=shape
        self.length=length


class Triangle(Shape):
    def __init__(self,shape,color,is_filled,length,height):
        super().__init__(color,is_filled)
        self.shape=shape
        self.length=length
        self.height=height


circle=Circle("circle","red",True,5)
square=Square("square","blue",False,5)

print(circle.shape)
print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()
