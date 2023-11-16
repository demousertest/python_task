def write_fun():
    text_val = input("Enter file text value :- ")
    with open("test.txt", 'w') as new_file:
        new_file.write(text_val)
        print("text file ready to read now")


def read_file():
    print("Read function calling..")
    with open("test.txt", "r") as read_new_file:
        file_text = read_new_file.read()
        print(file_text)



# @read_file
def edit_fun():
    update_value = input("Enter Update Text value :- ")
    with open("test.txt", "+a") as update_file:
        update_file.write(update_value)
        print("update is completed")
    read_file()    



