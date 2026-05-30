rows=int(input("enter no of rows:"))
columns=int(input("enter no of columns:"))
symbol=input("enter a symbol:")

for i in range(rows):
    for j in range (columns):
        print(symbol,end="")
    print()    