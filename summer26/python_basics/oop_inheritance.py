#inheritance = allows a class to inherit attributes and methods from another class 
#              helps with code reusebility and extensibility 
#              class child (Parent)  aka sub class (super class)

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")    


class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

dog=Dog("tom")
cat=Cat("whiskey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()



#multiple inheritance = inherit from more than parent class
#                       C(A, B)

#multilevel inheritance = inherit from a parent which inherits from another parent
#                       C(B) <- B(A) <- A

class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):                      #multiple inheritance 
    pass                                        #bigger fish can prey on smaller fish 


rabbit= Rabbit("bugs")
hawk= Hawk("eyed")
fish=Fish("nemo")

rabbit.flee()
fish.flee()
fish.hunt()
rabbit.eat()