#Number Guessing Game
import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_answer=True

print()
print("WELCOME TO NUMBER GUESSING GAME")
print("===============================")

while is_answer:
    guess=input("Enter your guess:")
    if guess.isdigit():
        guess=int(guess)
        guesses +=1
        if guess<lowest_num or guess>highest_num:
            print("Your guess is INVALID!")
            print(f"Your guess should be between {lowest_num} & {highest_num}.")
        elif guess<answer:
            print("Your guess is lower than the numberr")
            print("GO HIGH!!")

        elif guess>answer:
            print("Your guess is higher than the number")
            print("GO LOW!!")
   
        else:
            print(f"CORRECT the number was {answer}")  
            print(f"It took you {guesses} to guesses to reach the correct number")  
            is_answer = False 

    else:
        print("Your guess is INVALID!")
        print(f"Your guess should be between {lowest_num} & {highest_num}.")
       