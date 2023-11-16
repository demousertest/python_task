import copy

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 21}
]

print(f"before apply shallow copy \n {students}")


shallow_copy = copy.copy(students)
shallow_copy[0]['name'] = "Ashish"
shallow_copy[0]['age'] = 26
print(f"after apply shallow copy \n {students}")
print(shallow_copy)

print("after append value in shallow copy object")
shallow_copy.append({"name": "harish", "age": 28})
print(shallow_copy)
print(students)