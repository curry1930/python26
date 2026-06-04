#positional arguments= normal arguments which is passed when calling the function
#eg.   def happy_birthday(name):         this is called a parameter
            #print(f"Happy birthday {name}")
#        happy_birthday("Abhinav")       this is  positional arg

#parameter= a parameter is passed when we declare a func


#default arguments= A default value for certain parameters
#                   default is used when that argument is omitted
#                   makes ur function more flexible, it can reduce the no of arguments 
# eg.      def net_price(list_price,discount=0,tax=0.05):     #default argument
#               return list_price*(1-discount)*(1+tax)
#          print(net_price(500))
#          print(net_price(500,.10))                   #this will work as a parameter is passed is the
#                                                        place of discount


#keyword argument= an argument preceded by an identifier 
#                  helps with readability
#                  order of argument doesnt matter
#eg.      def hello(greeting, title, first, last):
#             print(f"{greeting} {title} {first} {last}")
#         hello("Hello", title="Mr.", first= "Spongebob", last= "Squarepants")


#### positional arguments must always come first, followed by keyword arguments

#def num_count():
#    for i in range(1,11):
#        print(i)
#num_count()        

#arbitrary arguments
# *args     =allows you to pass multiple non key arguments
# **kwargs  =allows you to multiple key arguments 
#             * is unpacking operator 

def add(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add(1,10491,812,8914))  
#*args passes the value as a tuple


def address(**kwargs):
    for i in kwargs.values():
        print(i,end=" ")
        
print(address(street="007 strt.", city="Bangalore", state="Karnataka", zip="390022"))        
#**kwargs passes the vaule of parameter as a tuple 

