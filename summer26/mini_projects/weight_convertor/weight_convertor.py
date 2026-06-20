#Python Weight Convertor

weight=float(input("Enter your weight: "))
unit=input("Enter unit (lbs/kgs): ")

if unit == "kgs":
    weight *= 2.205
    print(f"Your weight is {round(weight,3)}lbs ")
elif unit == "lbs":
    weight /= 2.205
    print(f"Your weight is {round(weight,3)}kgs ")    
else:
    print(f"{unit} entered is INVALID!!")

    
