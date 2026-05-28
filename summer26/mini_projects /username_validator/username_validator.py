# Username Validator in Python

while True:
    username = input("Enter your username:")

    if len(username) < 4 or len(username) > 12:
        print("Username must be between 4 and 12 characters!!")

    elif " " in username:
        print("Username should not contain any spaces!!")

    elif username[0].isdigit():
        print("Username must not start with a digit!!")

    elif not username.isalnum():
        print("Only alphabets and numbers are allowed!!")

    else:
        print(f"Your username is: {username}")
        break
 

