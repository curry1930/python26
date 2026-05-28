name=input("enter your full name: ")
phone_no=input("enter your phone number: ")

# result = len (name)
# result = name. find("o")
#result = name.rfind("q") #if q is not in the entered name then it will show -1
#name = name. capitalize() only first letter capital 
# name = name. upper () #make everything in caps
# name = name. lower () #lowers everything
# result = name.isdigit() # will check for numbers
#result = name. isalpha() # will check for alphabets 
#result=name.isalnum() #this is to check for both alphabets and numbers


#result=phone_no.count("-")
result=phone_no.replace("-","*")

print(result)


#for more methods or revising these methods we can do this command print(help(str))
