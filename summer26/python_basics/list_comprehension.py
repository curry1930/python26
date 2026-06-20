#list_copmprehension = a consice way to create lists in python 
#                      compact and easier to read than the traditional loops 
#                      syntax=[expression for value in iterable if condition]

#this is the tradional method we use 
#double=[]
#for i in range(1,11):
#    double.append(i*2)
#print(double) 

#using list comprehension
#double=[expression for value in iterable if condition]
#double=[i*2 for i in range(1,11)]
#triples=[j*3 for j in range(1,11)]
#squares=[pow(k,2) for k in range(1,11)]


#fruits=["apple","banana","orange","mango"]
#fruit_capital=[fruit.upper() for fruit in fruits]
#fruit_chars=[first_char[0] for first_char in fruits]
#print(fruit_chars)


#to have a condition
number=[1,-2,-3,0,4,5,3,-4]
posi_num=[num for num in number if num>=0] 
neg_num=[neg_num for neg_num in number if neg_num<0]
even_num=[even_num for even_num in number if even_num%2==0  and even_num>0]
odd_num=[odd_num for odd_num in number if odd_num%2!=0  and odd_num>0]
print(odd_num)