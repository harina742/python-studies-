✅ ex1.py (Get User Input)
# ex1.py

name = input("Enter Name: ")
age = input("Enter Age: ")
course = input("Enter Course: ")

print("\nStudent Details")
print("Name :", name)
print("Age :", age)
print("Course :", course)
✅ ex2.py (Using Functions)
# ex2.py

def get_details():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    return name, age, course

def print_details(name, age, course):
    print("\nStudent Details")
    print("Name :", name)
    print("Age :", age)
    print("Course :", course)

name, age, course = get_details()
print_details(name, age, course)
