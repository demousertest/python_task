class ATM_notes:
    def amount_fun(self):
        while True:
            notes = [500,200,50]
            amount = input('Enter total amount : ')
            if amount.isdigit() and int(amount) % min(notes)==0:
                amount = int(amount)
                break
            else:
                print("Please Type a valid interger number which is multiple of 50,200, and 500 ")
        note1 = 0
        note2 = 0
        note3 = 0
        while True:
            if amount >=500:
                note1 +=1
                amount -=500
            else:
                break
        while True:
            if amount >=200:
                note2 +=1
                amount -=200
            else:
                break
        while True:
            if amount >=50:
                note3 +=1
                amount -=50
            else:
                break
        return {
            "500" :note1,
            "200" :note2,
            "50" : note3
        }
    

class continue_cancel__:
     def re_ask(self):
        while True:
            print(ATM_notes.amount_fun(self))
            select_option = input("Please enter the option you want to continue/cancel : ")
            try:
                if select_option.lower() == 'cancel':
                    print("Transaction Done")
                    break
                elif select_option.lower() == 'continue':
                    continue
                else:
                    raise ValueError("Invalid option. Please enter 'continue' or 'cancel'.")
            except ValueError as e:
                print(e)
obj = continue_cancel__()
print(obj.re_ask())