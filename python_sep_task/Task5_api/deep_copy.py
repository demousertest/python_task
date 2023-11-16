import copy

students = [
    {"name": "hemant", "age": 20},
    {"name": "hitesh", "age": 22},
    {"name": "mohit", "age": 21}
]
print(f"before apply deep copy \n {students}")

deep_copy = copy.deepcopy(students)
deep_copy[0]['name'] = "Ashish"
deep_copy[0]['age'] = 26

print(f"after apply deep copy \n {students}")

print(deep_copy)
