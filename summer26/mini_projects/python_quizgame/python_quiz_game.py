#Python Quiz Game

questions=(("How many players play basketball match:"),
           ("Who just won the champions league:"),
           ("Which team does Curry play for:"),
           ("Which sport does Virat Kohli play:"),
           ("Which does not require a BALL:"))

answers=(("A.10","B.12","C.14","D.8"),
         ("A.Arsenal","B.PSG","C.Barcelona","D.Real Madrid"),
         ("A.Lakers","B.Spurs","C.OKC","D.Warriors"),
         ("A.Basketball","B.Tennis","C.Cricket","D.Football"),
         ("A.Basketball","B.Swimming","C.Cricket","D.Football"))

correct_ans=["A","B","D","C","B"]
guesses=[]
score=0

question_no=0

for que in questions:
    print("---------------------------")
    print(que)
    for ans in answers[question_no]:
        print(ans)

    guess=input("Enter your ANS(A,B,C,D):").upper()
    guesses.append(guess)
    if guess==correct_ans[question_no]:
        print("CORRECT!!")
        score+=1
    else:
        print("INCORRECT!!")    

      
    question_no +=1
    
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("          RESULT         ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

print("YOUR GUESS ")
for i in guesses:
    print(i,end=" ") 
print()
print("CORRECT ANS ")
for i in correct_ans:
    print(i,end=" ")  
print()    

print(f"You have scored {score} out of {len(questions)}")      
percentage=int(score/len(questions)*100)

print(f"YOUR RESULT IS:{percentage}%")      
if percentage>= 90:
    print("Excellent")
elif percentage >= 75:
    print("Good")
else:
    print("Needs Practice")    
          


    
