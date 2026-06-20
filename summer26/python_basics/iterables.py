#iterable= an object/collection that can return its elements one at a time,
#          allowing it to be iterated over in a loop 

#iteration can be done in lists,tuples,dictionary,sets,string etc

#number=(1,2,3,4,5)
#for i in number:
#    print(i)

#number=(1,2,3,4,5)
#for i in reversed(number):
#    print(i)



#membership operator = used to test weather a value or variable is found in a sequence
#                      strin, list, tuple, set or dictionary 
#                      1. in 
#                       2. not in

#word="abhinav"

#guess=input("guess the word in the secret word!!")
#if guess in word:
#    print(f"wallah! {guess} is in the secret word")
#else:
#    print(f"{guess} is not found in the secret word")    


grades={"abhi":"B",
        "sam":"A"}

student=input("enter students name:")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found!!")