#Concession Stand 

menu={"popcorn":450,
      "cheese popcorn":550,
      "nachos":350,
      "cheese nachos":450,
      "pizza":600,
      "pepsi":150,
      "coke":150,}

print("~~~~~~~~~~~~~~~~~~~~~~")
print("         MENU         ")
print("~~~~~~~~~~~~~~~~~~~~~~")
for key, value in menu.items():
    print(f"{key:15}:{value:.2f}")
print("~~~~~~~~~~~~~~~~~~~~~~")

cart=[]
total=0 

while True:
    order=input("Select your items from the menu(q to quit):").lower()
    if order == "q":
        break
    elif menu.get(order) is not None:
        cart.append(order)
    else:
        print(f"{order} is not in the menu")    

for order in cart:
    total = total + menu.get(order)
    print(order,end=" ")

print()
print(f"Your total bill is:₹{total}")