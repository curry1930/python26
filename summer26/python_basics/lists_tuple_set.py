# collection = single "variable" used to store multiple values
#Lists = [] ordered and changeable(mutable), duplicated OK
#Sets = {} unordered and immutable, but add/remove Ok, NO duplicates
#Tuples = () ordered and unchangeable, duplicates OK, FASTER

#fruits=["apple", "orange", "banana", "watermelon"]

#print(fruits)
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))  #prints lenght of list
#print("pineapple" in fruits) #check for pineapple in list and returns boolean

#for fruit in fruits:
    #print(fruit)

#fruits[1]="pineapple"   #removes orange and adds pineapple on index 1

#fruits.append("pineapple")  #appends pineapple in list
#fruits.remove("watermelon")  #removes watermelon from the list
#fruits.insert(1,"litchi")    #inserts a element on a specific index
#fruits.sort()                  #sorts alphabetically or numerically based on the list
#fruits.reverse()                #reverses the list
#fruits.clear()                 #removes every elements from the string 

#print(fruits.index("orange"))    #returns the index of element
#print(fruits.count("banana"))    #counts no of elements
#print(fruits)



#SET   #set is unordered we cant print indexes because elements are not in order 
       #everytime we print the set it will be in diffrent order   
fruits={"apple", "orange", "banana", "watermelon"}

#print(fruits)
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))  #prints lenght of set
#print("pineapple" in fruits) #check for pineapple in set and returns boolean

#fruits.add("pineapple")
#fruits.remove("pineapple")
#fruits.pop()
#fruits.clear()
#print(fruits)

for fruit in fruits:
    print(fruit)


#TUPLES 

fruits=("apple", "orange", "banana", "watermelon")

#print(fruits)
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))  #prints lenght of tuple
#print("pineapple" in fruits) #check for pineapple in tuple and returns boolean

#print(fruits.index("apple"))  #prints index of an element
#print(fruits.count("apple"))   #counts the no of apple in tuple