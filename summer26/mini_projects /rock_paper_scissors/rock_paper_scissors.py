import random

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOM TO ROCK, PAPER AND SCISSORS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

running = True
options=("rock","paper","scissors")

while running:
    player=input("Enter an option:").lower()
    computer=random.choice(options)

    while player not in options:
        print("You have entered a invalid option!!")
        print("Select options from rock, paper, scissors!!")
        player=input("Enter an option:")
    print(f"Player:{player}")
    print(f"computer:{computer}")

    if player==computer:
        print("THATS A TIE")
        print("TRY AGAIN")
    elif player == "rock" and computer=="scissors":
        print("YOU WON!!")
    elif player == "paper" and computer=="rock":
        print("YOU WON!!")
    elif player == "scissors" and computer=="paper":
        print("YOU WON!!")        
    else:
        print("YOU LOST!!")
        print("TRY AGAIN")  
    play_again=input("Do you want to play again? (y for yes & n for no):").lower()
    if not play_again == "y":
        running = False

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("THANK YOU FOR PLAYING OUR GAME")

        


