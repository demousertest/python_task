import random
import string

username_length = int(input("Enter length of username :- "))


def generate_username(length):
    characters = string.ascii_letters + string.digits
    while True:
        username = ''.join(random.choice(characters) for _ in range(length))    
        yield username
    # return username

num_usernames = int(input("Enter number of username :- "))

used_usernames = set()

for _ in range(num_usernames):
    while True:
        new_username = next(generate_username(username_length))
        if new_username not in used_usernames:
            used_usernames.add(new_username)
            print("Generated Username:", new_username)
            break
print(used_usernames)