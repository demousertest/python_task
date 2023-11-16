from read_edit import read_file, write_fun, edit_fun
import os
try:
    while True:
        ter_task = input("do you want to terminate execution Yes/No: ")
        if ter_task.lower() == 'yes':
            break

        file_value = "./test.txt"
        if os.path.exists(file_value):
            del_file = input("1 file is present do you want to delete it? yes/no :- ")
            if del_file.lower() == "yes":
                os.remove('test.txt')
            else:
                read_file()
                print("\n"*2)
                edit_fun()
        else:
            print("no")
            write_fun()
except ValueError as err:
    print(err)

