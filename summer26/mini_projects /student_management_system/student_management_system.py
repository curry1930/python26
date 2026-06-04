students={"John":99,
          "Danny":85,
          "Sam":87,
          "Robert":59,
          "Fred":73}

adding = True
while adding:
    student=input("Enter student name you want to add in the system:").capitalize()
    if student.isdigit():
        print("Please enter a valid name!")
        continue
    marks=float(input("Enter students marks:"))
    students.update({student:marks})
    ask=input("Do you want to add more students(y for yes n for n):").lower()
    if not ask=="y":
        adding=False

for keys,value in students.items():
    print(f"{keys:10}:{value:.2f}")
print(f"Total students: {len(students)}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO PARENTS TEACHERS MEETING") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for student in students:
    name=input("Enter students name:").capitalize()
    if students.get(name) is None:
        print("INVALID ENTRY!!")
    else:
        print(f"{name} has scored {students.get(name)} marks")
    ask=input("Do you want to search again(y/n):").lower()
    if not ask == "y":
        break

       
print("THANK YOU ")
