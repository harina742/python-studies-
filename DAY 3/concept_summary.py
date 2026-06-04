"""Dictionaries
Definition: A dictionary in Python is a collection of key–value pairs.

Structure:

python
movies = {
    "vijay": ["Ghilli", "Leo", "Master"],
    "ajith": ["Billa", "Mankatha"]
}
Keys → "vijay", "ajith"

Values → lists of movies

Conceptual Role:

Acts like a lookup table: you give a key (actor name) and instantly get the value (list of movies).

Useful when data is naturally mapped (e.g., actor → movies, student → marks).

Operations:

Access: movies["vijay"]

Update: movies["vijay"].append("New Movie")

Delete: del movies["ajith"]

Validation: if actor in movies:

File Handling
Definition: File handling allows programs to store and retrieve data permanently outside of runtime.

Modes:

"w" → Write (creates/overwrites file)

"r" → Read (opens existing file)

"a" → Append (adds new content without overwriting)

Conceptual Role:

Ensures persistence: results don’t vanish when the program ends.

Bridges between program memory (RAM) and permanent storage (disk).

Operations:

Write to Text File:

python
with open("output.txt", "w") as f:
    f.write("Hello World")
Read from Text File:

python
with open("output.txt", "r") as f:
    print(f.read())
JSON Handling:

json.dump() → saves structured data (dictionary/list) into a .json file.


json.load() → loads structured data back into Python.

Conceptually, JSON is a portable format — readable by humans and machines, widely used in APIs and databases."""
