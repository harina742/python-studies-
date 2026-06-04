# movies_dict.py
# Dictionary + User Input Validation

movies = {
    "vijay": ["Ghilli","Thuppakki","Mersal","Master","Leo","Kaththi","Pokkiri","Theri","Bigil","Sarkar"],
    "ajith": ["Mankatha","Billa","Viswasam","Vedalam","Yennai Arindhaal","Valimai","Veeram","Citizen","Dheena","Aarambam"],
    "surya": ["Ghajini","Singam","Ayan","Soorarai Pottru","Vaaranam Aayiram","24","Jai Bhim","Kaakha Kaakha","Etharkkum Thunindhavan","Vel"],
    "dhanush": ["Asuran","VIP","Karnan","Thiruchitrambalam","Raanjhanaa","Maari","Polladhavan","Pudhupettai","Velaiilla Pattadhari","Captain Miller"]
}

def get_top_movies(actor, x):
    if actor not in movies:
        return f"Error: Unknown actor!"
    elif x < 1 or x > 10:
        return f"Error: Please enter a number between 1 and 10."
    else:
        result = [f"{i+1}. {movies[actor][i]}" for i in range(x)]
        return f"\nHere are the top {x} super hit movies of {actor.title()}:\n" + "\n".join(result)

# ---- Main Program ----
if __name__ == "__main__":
    x = int(input("Please enter top x number (1-10): "))
    actor = input("Please enter the actor name: ").lower()
    output = get_top_movies(actor, x)
    print(output)

"""
Sample Run 1 — Valid Actor
Code
Please enter top x number (1-10): 5
Please enter the actor name: Vijay

Here are the top 5 super hit movies of Vijay:
1. Ghilli
2. Thuppakki
3. Mersal
4. Master
5. Leo

Sample Run 2 — Unknown Actor
Code
Please enter top x number (1-10): 5
Please enter the actor name: Rajini

Error: Unknown actor!

Sample Run 3 — Invalid Number
Code
Please enter top x number (1-10): 12
Please enter the actor name: Ajith

Error: Please enter a number between 1 and 10.

Concepts Used:

Dictionary → stores actors and their movies

List → each actor’s movies stored as a list

For Loop → prints top x movies

if‑else Validation → checks actor validity and number range

User Input → input() for interactive program"""
