# Flight Booking System

flights = {
    "AI101": {"source": "Delhi", "dest": "Mumbai", "seats": 5, "price": 5500},
    "AI102": {"source": "Mumbai", "dest": "Delhi", "seats": 8, "price": 5200},
    "6E201": {"source": "Bangalore", "dest": "Chennai", "seats": 3, "price": 3200},
    "6E202": {"source": "Chennai", "dest": "Bangalore", "seats": 4, "price": 3100},
    "UK301": {"source": "Delhi", "dest": "Kolkata", "seats": 2, "price": 6000},
    "UK302": {"source": "Kolkata", "dest": "Delhi", "seats": 6, "price": 6200},
    "SG401": {"source": "Hyderabad", "dest": "Pune", "seats": 10, "price": 4000},
    "SG402": {"source": "Pune", "dest": "Hyderabad", "seats": 7, "price": 4100},
    "QP501": {"source": "Ahmedabad", "dest": "Delhi", "seats": 5, "price": 3500},
    "QP502": {"source": "Delhi", "dest": "Ahmedabad", "seats": 9, "price": 3600}
}

def search_flights(source, dest):
    """Search flights based on source and destination"""
    available = []
    for code, details in flights.items():
        if details["source"].lower() == source.lower() and details["dest"].lower() == dest.lower():
            available.append((code, details))
    return available

def book_flight(code, seats_requested):
    """Book seats if available"""
    if code in flights:
        if flights[code]["seats"] >= seats_requested:
            flights[code]["seats"] -= seats_requested
            print(f"\n✅ Booking Confirmed!")
            print(f"Flight: {code}")
            print(f"Seats Booked: {seats_requested}")
            print(f"Total Price: ₹{flights[code]['price'] * seats_requested}")
            print(f"Remaining Seats: {flights[code]['seats']}")
        else:
            print("\n❌ Not enough seats available!")
    else:
        print("\n❌ Invalid flight code!")

def main():
    source = input("Enter Source Airport: ")
    dest = input("Enter Destination Airport: ")

    results = search_flights(source, dest)

    if results:
        print("\nAvailable Flights:")
        for code, details in results:
            print(f"{code} | Seats: {details['seats']} | Price: ₹{details['price']}")
        
        code = input("\nEnter Flight Code to Book: ")
        seats_requested = int(input("Enter number of seats to book: "))
        book_flight(code, seats_requested)
    else:
        print("\n❌ No flights available for this route.")

# Run the program
main()

"""
Key Concepts Used
Dictionary operations: storing and updating flight details.

Functions: search_flights(), book_flight(), main() for modular design.

User input: input() for source, destination, flight code, and seats.

Validation: checking seat availability before booking.

Updating dictionary: subtracting booked seats from available seats."""

#Example Run
"""Code
Enter Source Airport: Delhi
Enter Destination Airport: Mumbai

Available Flights:
AI101 | Seats: 5 | Price: ₹5500

Enter Flight Code to Book: AI101
Enter number of seats to book: 3

✅ Booking Confirmed!
Flight: AI101
Seats Booked: 3
Total Price: ₹16500
Remaining Seats: 2"""
