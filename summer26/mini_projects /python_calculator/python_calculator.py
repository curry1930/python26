#Python Calculator

operator=input("Enter an operator (+,-,*,/): ")

a=float(input("Enter first operand: "))
b=float(input("Enter second operand: "))

if operator == "+":
    addition=a+b
    print(f"You are doing addition!!")
    print(f"Addition of two numbers is: {addition}")
elif operator == "-":
    subtraction=a-b
    print(f"You are doing subtraction!!")
    print(f"Subtraction of two numbers is: {subtraction}")
elif operator == "*":
    multiplication=a+b
    print(f"You are doing multiplication!!")
    print(f"Multiplication of two numbers is: {multiplication}")
elif operator == "+":
    division=a/b
    print(f"You are doing division!!")
    print(f"Division of two numbers is: {division}")   
else:
    print(f"{operator} is INVALID!")         
        
