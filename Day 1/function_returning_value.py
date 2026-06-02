# function_returning_value.py

def get_details():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    return name, age, course


def print_details(name, age, course):
    print("\n--- Admission Details ---")
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)


# Function call
name, age, course = get_details()
print_details(name, age, course)

Output Example
Enter Name: XXX
Enter Age: 18
Enter Course: B.Tech AI

--- Admission Details ---
Name   : XXX
Age    : 18
Course : B.Tech AI
