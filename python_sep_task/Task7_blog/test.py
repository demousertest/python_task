import json

l1= [{'Name': 'Hitesh'}, {'Age': '26'}, {'City': 'Bangalore'}, {'Pincode': '560095'}]
with open("test1.txt", "w") as file:
    json.dump(l1,file)
    # file.write(l1)


with open("test1.txt", 'r') as file1:
    test = file1.read()
    print(test)