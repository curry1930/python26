#ATM simulator 
menu=["To check account balance - ENTER:1",
      "To deposit money - ENTER:2",
      "To withdraw money - ENTER:3",
      "To check transaction history - ENTER:4",
      "To exit - ENTER:5"]
balance=1000
history=[]
running=True
for i in menu:
    print(i,end=" ")
    print()
while running:

    enter=int(input("Enter a specific from the menu:"))
    if enter==1:
        print(f"Your account balance is:₹{balance}")
    elif enter==2:
        deposit=int(input("Enter amount to be deposited:₹"))
        if deposit<=0:
            print("INVALID AMOUNT!!")
        else:    
            print(f"You have deposited ₹{deposit} into your bank account!!")
            balance += deposit
            history.append(f"You deposited ₹{deposit}")
    elif enter==3:
        while True:
            withdraw=int(input("Enter amount to be withdrawn:₹"))
            if withdraw>balance:
                print("You cannot withdraw more than balance")
                print(f"Your current account balance is:₹{balance}")
            elif withdraw<0:
                print("You cannot withdraw negative money.") 
            else:
                print(f"You have withdrawn ₹{withdraw} from your bank account!!")  
                balance -= withdraw
                history.append(f"You withdrew ₹{withdraw}") 
                break   
            
            
    elif enter==4:
        for i in history:
            print(i,end=" ") 
            print()        
    elif enter==5:
        print("Thank you for using our ATM!!!")
        running=False     
    else:
        print("INVALID ENTRY!!")      



