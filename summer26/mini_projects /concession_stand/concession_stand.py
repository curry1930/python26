menu={"popcorn":350,
      "pizza":750,
      "cold drink":250,
      "nachos":500,
      "cheese popcorn":450,
      "cheese nachos":600,}
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("          MENU          ")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

cart=[]
total=0

for item,price in menu.items():
    print(f"{item:15}:₹{price:.2f}")

print("~~~~~~~~~~~~~~~~~~~~~~~~")    

while True:
    order=input("Select your item from the menu (q to QUIT):").lower()
    if order == "q":
        break
    elif menu.get(order) is not None:
        cart.append(order)

for order in cart:
    total += menu.get(order)
    print(order,end=" ")

print()
print(f"Your Total amount is:₹{total}")


