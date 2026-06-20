# Static methods = A method that belongs to a class rathen than any object from that class (instance)
#                  Usually used for general utility functions 
# 
# Instance methods = Best for operations on instances of the class (objects)
#                    An instance method works on a specific object.
# Static methods = Best for utility functions that do not need access to class data
#                  A static method belongs to the class but doesn't need any object data. 


class Employee:

    def __init__(self, name, position):
        self.name=name
        self.position=position 

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer"]
        return position in valid_positions   
    
print(Employee.is_valid_position("Manager"))




# Class methods = Allow operations related to the class itself 
#                 Take (cls) as the first parameter, which represents the class itself 

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name=name
        self.gpa=gpa
        Student.count += 1
        Student.total_gpa += gpa

    #Instance method
    def get_info(self):
        return f"{self.name} : {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total no. of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average gpa of students is:{cls.total_gpa / cls.count}"

    
student1 = Student("Abhinav", 7.2)
student2 = Student("Sam", 7.8)

print(student1.get_info())
print(student2.get_info())
print(Student.get_count())
print(Student.get_avg_gpa())




# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built in operations
#                 They allow developers to define or customize the behaviour of objects

class Books:

    def __init__(self, title, author, no_of_pages):
        self.title = title
        self.author = author
        self.no_of_pages = no_of_pages
    
    #dunder string 
    def __str__(self):
        return f"'{self.title}' is by {self.author}"    #prints a string representation of the object 
                                                        #if this method wasnt used we would get the
                                                        #address of the object when printing print(book1)

    #dunder equal
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    #dunder less than
    def __lt__(self, other):
        return self.no_of_pages < other.no_of_pages 

    #dunder greater than
    def __gt__(self, other):
        return self.no_of_pages > other.no_of_pages

    #dunder addition
    def __add__(self, other):
        return self.no_of_pages + other.no_of_pages 

    #dunder contains
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author   

    #dunder get_item                      
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "no_of_pages":
            return self.no_of_pages
        else:
            print(f"Key '{key}' was not found")
                

book1 = Books("Harry Potter", "J.K. Rowling", 289)                                                        
book2 = Books("Harry Potter", "J.K. Rowling", 400)

print(book1)
print(book1 == book2)
print(book1 < book2)
print(book1 + book2)
print("Harry" in book1)
print(book1['author'])




# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefits : Add additional logic when read, write, or delete attributes
#             Gives you getter(to write), setter(to read) and deleter(to delete) method

class Rectangle:

    def __init__(self, length, width):
        self._length = length              #_length means this is protected (private attribute)
        self._width = width

    @property
    def length(self):
        return f"{self._length:.1f}cm"  
    
    @property
    def width(self):
        return f"{self._width:.1f}cm" 
    
    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self._length = new_length
        else:
            print("length must be greater than zero")

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than zero")  

    @length.deleter
    def length(self):
        del self._length
        print("length is deleted") 


    @width.deleter
    def width(self):
        del self._width
        print("width is deleted")                  



rectangle=Rectangle(3,4)        

rectangle.width=-5
print(rectangle.length)
print(rectangle.width)

del rectangle.length
del rectangle.width




# Decorator = A function that extends the behaviour of another function 
#             without modifying the base function 
#             Pass the base function as an argument to the decorator

def add_sprinkles(func):                       # this is blueprint the create a decorator 
    def wrapper():
        print("You added sprinkles 🎊")
        func()
    return wrapper    

@add_sprinkles        
def get_ice_cream():
    print("Here's your ice cream 🍨")
    
get_ice_cream()