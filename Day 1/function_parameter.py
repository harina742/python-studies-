# function_parameter.py

def print_details(name, age, course):
    print("\n--- Admission Details ---")
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)

# Getting input from user
name = input("Enter Name: ")
age = input("Enter Age: ")
course = input("Enter Course: ")

# Passing values as parameters
print_details(name, age, course)

Example Output
Enter Name:XXX
Enter Age: 18
Enter Course: AI & DS

--- Admission Details ---
Name   : XXX
Age    : 18
Course : AI & DS
