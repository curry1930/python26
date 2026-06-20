# object = a "bundle" of related attributes (variables) and methods (function)
#         ex. phone, cup, book 
#         you need a "class" to to create many object

# class= (blueprint) used to design the structure and layout of the object 
 
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print(f"you drive the {self.model}")      

    def stop(self):
        print(f"you stop the {self.model}") 

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")       


car1=Car("BMW",2026,"blue",False)     

#print(car1.model)                      # "." is attribute access operator
#print(car1.year)
#print(car1.color)
#print(car1.for_sale)

car1.drive()
car1.stop()
car1.describe()




#class variables = shared among all instances of the class
#                  defined outside the constructor 
#                  allow you to share data among all objects created from that class

#instance variable = defined inside of the constructor 

class Student:

    class_year=2026                      #class variable
    num_student=0                        #class variable

    def __init__(self,name,age):
        self.name=name                   #instance variable 
        self.age=age                     #instance variable 
        Student.num_student += 1

student1=Student("abhinav",21)
student2=Student("sam",20)

print(student1.name)
print(student1.age)
print(Student.class_year)                #calling class variable from the class itself Student.class_year

print(f"i had {Student.num_student} batchmates in my class of {Student.class_year}")
print(student1.name)
print(student2.name)

