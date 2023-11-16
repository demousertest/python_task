import string
import matplotlib.pyplot as plt
string1 = "this is the sample text to count string and plot string"
letters = string.ascii_letters
d1 = {}
for i in letters:
    if i not in d1 and i !=" " and i.isalpha() and i in string1:
        d1[i.lower()] = string1.count(i.lower())
    else:
        d1[i.lower()] =string1.count(i.lower())
print(d1)
category = list(d1.keys())
values = list(d1.values())

plt.bar(category, values)
plt.show()