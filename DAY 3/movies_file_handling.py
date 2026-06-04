# movies_file_handling.py
# Save and Load Movie Results using File Handling + JSON

import json
from movies_dict import get_top_movies

# Example run
x = 5
actor = "vijay"
output = get_top_movies(actor, x)

# ---- Save to Text File ----
with open("movies_output.txt", "w") as file:
    file.write(output)
print("Movie list saved to movies_output.txt")

# ---- Read from Text File ----
with open("movies_output.txt", "r") as file:
    content = file.read()
print("\nReading from text file:\n", content)

# ---- Save to JSON ----
movie_data = {"actor": actor, "top_x": x, "movies": output.split("\n")[1:]}  # skip header line
with open("movies_output.json", "w") as json_file:
    json.dump(movie_data, json_file, indent=4)
print("\nMovie list saved to movies_output.json")

# ---- Load from JSON ----
with open("movies_output.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("\nLoaded from JSON:")
print("Actor:", loaded_data["actor"])
print("Top Movies:", loaded_data["movies"])

"""

Console Output
Code
Movie list saved to movies_output.txt

Reading from text file:
Here are the top 5 super hit movies of Vijay:
1. Ghilli
2. Thuppakki
3. Mersal
4. Master
5. Leo

Movie list saved to movies_output.json

Loaded from JSON:
Actor: vijay
Top Movies: ['1. Ghilli', '2. Thuppakki', '3. Mersal', '4. Master', '5. Leo']

movies_output.txt (created file content)
Code
Here are the top 5 super hit movies of Vijay:
1. Ghilli
2. Thuppakki
3. Mersal
4. Master
5. Leo

movies_output.json (created file content)
json
{
    "actor": "vijay",
    "top_x": 5,
    "movies": [
        "1. Ghilli",
        "2. Thuppakki",
        "3. Mersal",
        "4. Master",
        "5. Leo"
    ]
}"""
