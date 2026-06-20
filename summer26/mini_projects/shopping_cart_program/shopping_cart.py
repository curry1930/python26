#SHOPPING CART

foods=[]
prices=[]

while True:
    food=input("Enter the food you want to buy (q for quit):")
    if food.lower() == "q":
        break
    else:
        price=float(input("Enter the price of the food: ₹"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----") 

for food in foods:
    print(food, end=" ")

print()

total=0 
for price in prices:
    total=total+price 

print(f"Your Total Bill is:{total}")         


