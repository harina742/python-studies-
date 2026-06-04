#CREATE — One Report as a Dictionary
# Create a dictionary to store one student's report
report = {
    "name": "Harina",
    "roll_no": 101,
    "department": "CSE (AI & ML)",
    "marks": {"Python": 85, "IoT": 80, "ML": 78}
}
print("Report Created:", report)

#READ — Access Specific Fields
# Access individual fields
print("Name:", report["name"])
print("Python Marks:", report["marks"]["Python"])


# Update marks
report["marks"]["Python"] = 90
print("Updated Python Marks:", report["marks"]["Python"])

# Delete a field
del report["department"]
print("After Deletion:", report)

#List of Dictionaries — Multiple Reports
# Store multiple student reports
reports = [
    {"name": "Harina", "roll_no": 101, "marks": {"Python": 90, "IoT": 80}},
    {"name": "Anu", "roll_no": 102, "marks": {"Python": 85, "IoT": 75}},
    {"name": "Ravi", "roll_no": 103, "marks": {"Python": 88, "IoT": 82}}
]

# Display all reports
for r in reports:
    print(r["name"], "→ Python:", r["marks"]["Python"])
  
#Function That Creates a Report Dictionary
def create_report(name, roll_no, python, iot):
    return {
        "name": name,
        "roll_no": roll_no,
        "marks": {"Python": python, "IoT": iot}
    }

new_report = create_report("Harina", 101, 92, 85)
print("Generated Report:", new_report)
