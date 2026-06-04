 
# Save report data to a text file
with open("report.txt", "w") as file:
    file.write(str(report))
print("Report saved to text file.")

#Read All Reports from File
# Read data back from text file
with open("report.txt", "r") as file:
    content = file.read()
print("File Content:\n", content)

#Save as JSON

import json
# Save multiple reports as JSON
with open("reports.json", "w") as json_file:
    json.dump(reports, json_file, indent=4)
print("Reports saved as JSON.")

#Load from JSON
# Load reports back from JSON file
with open("reports.json", "r") as json_file:
    loaded_reports = json.load(json_file)

print("Loaded Reports:")
for r in loaded_reports:
    print(r["name"], "→ IoT:", r["marks"]["IoT"])

"""
Save to a Text File
text
Report saved to text file.
(A file named report.txt will be created containing the dictionary data.)

Read All Reports from File
text
File Content:
{'name': 'Harina', 'roll_no': 101, 'department': 'CSE (AI & ML)', 'marks': {'Python': 85, 'IoT': 80, 'ML': 78}}
(This shows the content read back from report.txt.)

Save as JSON
text
Reports saved as JSON.
(A file named reports.json will be created with neatly formatted JSON data.)

Example content inside reports.json:

json
[
    {
        "name": "Harina",
        "roll_no": 101,
        "marks": {"Python": 90, "IoT": 80}
    },
    {
        "name": "Anu",
        "roll_no": 102,
        "marks": {"Python": 85, "IoT": 75}
    },
    {
        "name": "Ravi",
        "roll_no": 103,
        "marks": {"Python": 88, "IoT": 82}
    }
]
Load from JSON
text
Loaded Reports:
Harina → IoT: 80
Anu → IoT: 75
Ravi → IoT: 82
✨ Summary

report.txt → stores plain text version of one dictionary.

reports.json → stores structured data for multiple reports.

Reading and loading confirm that data is correctly saved and retrieved."""
