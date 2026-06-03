movies = {
    "vijay": [
        "Ghilli",
        "Thuppakki",
        "Mersal",
        "Master",
        "Leo",
        "Kaththi",
        "Pokkiri",
        "Theri",
        "Bigil",
        "Sarkar"
    ],

    "ajith": [
        "Mankatha",
        "Billa",
        "Viswasam",
        "Vedalam",
        "Yennai Arindhaal",
        "Valimai",
        "Veeram",
        "Citizen",
        "Dheena",
        "Aarambam"
    ],

    "surya": [
        "Ghajini",
        "Singam",
        "Ayan",
        "Soorarai Pottru",
        "Vaaranam Aayiram",
        "24",
        "Jai Bhim",
        "Kaakha Kaakha",
        "Etharkkum Thunindhavan",
        "Vel"
    ],

    "dhanush": [
        "Asuran",
        "VIP",
        "Karnan",
        "Thiruchitrambalam",
        "Raanjhanaa",
        "Maari",
        "Polladhavan",
        "Pudhupettai",
        "Velaiilla Pattadhari",
        "Captain Miller"
    ]
}

x = int(input("Please enter top x number (1-10): "))
actor = input("Please enter the actor name: ").lower()

if actor not in movies:
    print("Error: Unknown actor!")
elif x < 1 or x > 10:
    print("Error: Please enter a number between 1 and 10.")
else:
    print(f"\nHere are the top {x} super hit movies of {actor.title()}")

    for i in range(x):
        print(f"{i+1}. {movies[actor][i]}")
"""
Sample Output
Please enter top x number (1-10): 5
Please enter the actor name: Vijay

Here are the top 5 super hit movies of Vijay

1. Ghilli
2. Thuppakki
3. Mersal
4. Master
5. Leo
Unknown Actor
Please enter top x number (1-10): 5
Please enter the actor name: Rajini

Error: Unknown actor!
Concepts Used
List
Dictionary
For Loop
if-else Validation
User Input (input())
"""
