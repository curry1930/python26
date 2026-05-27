num=int(input("enter no btw 1 to 10"))

while num<1 or num>10:
    print("num is not valid")
    num=int(input("enter no btw 1 to 10"))
print(f"{num} is valid!")    