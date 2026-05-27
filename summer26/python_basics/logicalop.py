#logical operators = evaluate multiple conditions (or, and, not)
#or = at least one condition must be True
#and = both conditions must be True
#not = inverts the condition (not False, not True)


#conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#Print or assign one of two values based on a condition
#X if condition else Y
#temp=21
#weather= "HOT" if temp>=25 else "COLD"
#print(weather)

user_role="guest"
access_level="give full access" if user_role=="admin" else "access not granted"
print(access_level)