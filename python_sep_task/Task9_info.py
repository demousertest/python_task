def create_account():
    user_Id = input("Enter User ID :- ")
    user_name = input("Enter User Name :- ").title()
    amount = int(input("Enter Total amount : "))
    password = input("Enter new account Password : ")
    user_details = (user_Id, user_name, amount)
    return user_details, password

user_acc_val, pass_val = create_account()
print(f"your account successfully created {user_acc_val[1]}")

def amount_tans(args):
    user_list = list(args)
    for i in range(len(user_list)):
        if type(user_list[i]) == int:
            while True:
                tnsf = input("enter transfer amount : ")
                if tnsf.isdigit():
                    tnsf = int(tnsf)
                    break
                else:
                    print("You Enter the wrong value")
            if user_list[i]> tnsf:
                user_list[i] = user_list[i] - tnsf

    print(user_list)
    return tuple(user_list)



auth_pass = input("Enter your pin ")
while True:
    
    if pass_val != auth_pass:
        print("You had entered a wrong password")
        break
    elif pass_val == auth_pass:
        print("Your Initial Amount is :- ", user_acc_val)
        new_bln = amount_tans(user_acc_val)
        while True:
            print("new balance", new_bln)
            re_attemp = input("Do you want to continue Yes/No :- ")

            if re_attemp.lower() == 'no':
                print("thank you for transaction")
                break
            elif re_attemp.lower() == 'yes':
                new_bln = amount_tans(new_bln)
                print(f"After Transaction completed {new_bln}")
                
        break
                
            
