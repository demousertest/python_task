import re

email_pattern = r'[a-zA-Z0-9.]+@[a-zA-Z.]+\.[a-z|A-Z]{2,3}'
with open('./test.txt', 'r') as text:
    text_val = text.read()

    email_addresses = re.findall(email_pattern, text_val)

    for email in email_addresses:
        print(email)
