user_profile = {}

for i in range(0, 4):
    input_field = input("Enter Field Name: ").title()
    input_val = input("Enter Field Value: ").title()
    user_profile[input_field] = input_val

print(user_profile)

def edit_profile(args):
    input_field = input("Enter Update Field Name: ").title()
    input_val = input("Enter Update Field Value: ").title()
    args[input_field] = input_val
    return args

while True:
    ip_val = input("Enter 'Yes' if you want to Edit the Profile: ").title()
    if ip_val == 'Yes':
        edit_profile(user_profile)
        print(user_profile)
    elif ip_val == 'No':
        print("Thanks for your selection.")
        break
    else:
        print("Your Selection is not correct")
