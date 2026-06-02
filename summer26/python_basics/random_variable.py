import random

low=1
high=20

#print(random.randint(low,high))  # returns a random int btw low and high 
#print(random.random(low,high))   #will return error bc random.random dont take any arguments
#print(random.random())            #returns a random floating no

#options=("rock","paper","scissors")
#print(random.choice(options))     #randomly chooses an option from options 

cards=["2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(cards)              #shuffles the elements of the list 
print(cards)