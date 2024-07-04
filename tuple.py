#tuple
student=("broo",22,"male")
print(student.count("broo"))
print(student.index("male"))
for x in student:
    print(x)
if "broo" in student:
    print("broo is here")