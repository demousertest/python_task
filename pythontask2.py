import re

def validate_email(email):
    pattern = r"^[A-Za-z0-9.]+@[A-Za-z]+\.[a-z]{3}"
    return re.match(pattern, email)

def write_email(email):
    with open("email.txt", 'a') as email_file:
        email_file.write(email + "\non")

def read_email():
    with open('email.txt', 'r') as read_email:
        email_val = read_email.read().splitlines()
        return email_val

def all_func():
    while True:
        while True:
            user_input = input("enter email address (Yes/No) : ").lower()
            if user_input=='no' or user_input=='yes':
                print(f"you enter : {user_input}")
                break
            else:
                print("Please Enter Yes or No")
        
        if user_input=="no":
            emails = read_email()
            for i in emails:
                print(i, end='\n')
            break
        elif user_input=="yes":
            email= input("enter email : ")
            if validate_email(email):
                write_email(email)
            else:
                print(f'Email is not Vaild : {email}')  



all_func()