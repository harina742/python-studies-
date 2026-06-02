# Simple College Admission using Variables

def get_details():
    print("---- College Admission Form ----")
    
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")
    
    return name, age, course, phone


def print_details(name, age, course, phone):
    print("\n---- ADMISSION DETAILS ----")
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)
    print("Phone  :", phone)


def main():
    name, age, course, phone = get_details()
    print_details(name, age, course, phone)


main()
