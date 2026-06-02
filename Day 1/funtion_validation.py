# function_validation.py

def get_details():
    name = input("Enter Name: ")

    age = int(input("Enter Age: "))
    while age < 17:
        print("Age must be 17 or above.")
        age = int(input("Enter Age: "))

    course = input("Enter Course: ")

    phone = input("Enter Phone Number: ")
    while len(phone) != 10 or not phone.isdigit():
        print("Invalid phone number. Enter 10 digits.")
        phone = input("Enter Phone Number: ")

    return name, age, course, phone


def print_details(name, age, course, phone):
    print("\n--- Admission Details ---")
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)
    print("Phone  :", phone)


name, age, course, phone = get_details()
print_details(name, age, course, phone)
