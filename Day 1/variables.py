# College Admission using Variables and Functions

def get_details():
    print("---- College Admission Form ----")
    
    # variables (runtime input)
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    course = input("Enter Course Applied For: ")
    department = input("Enter Department: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    
    # return all variables as a dictionary
    return name, age, gender, course, department, email, phone


def print_details(name, age, gender, course, department, email, phone):
    print("\n---- ADMISSION DETAILS ----")
    print("Name       :", name)
    print("Age        :", age)
    print("Gender     :", gender)
    print("Course     :", course)
    print("Department :", department)
    print("Email      :", email)
    print("Phone      :", phone)
    print("----------------------------")


def main():
    # get values from user
    name, age, gender, course, department, email, phone = get_details()
    
    # display values
    print_details(name, age, gender, course, department, email, phone)


# run program
if __name__ == "__main__":
    main()
