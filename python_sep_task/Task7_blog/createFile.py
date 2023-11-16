def write_fun():
    text_val = input("Enter file text value :- ")
    with open("test.txt", 'w') as new_file:
        new_file.write(text_val)
        print("text file ready to read now")

write_fun()
