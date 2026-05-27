#Compound Interest Calculator 

principle =0
rate =0
time =0

while principle <=0:
    principle=float(input("Enter principle amount: "))
    if principle <=0:
        print("Principle amount entered in INVALID!!")

while rate <=0:
    rate=float(input("Enter interest rate: "))
    if rate <=0:
        print("Interest rate entered in INVALID!!")

while time <=0:
    time=float(input("Enter time(years): "))
    if time <=0:
        print("Interest rate entered in INVALID!!")

Total=principle * pow((1+rate/100),time)
print(f"Total Amount after {time}(years):₹{round(Total,3)}")