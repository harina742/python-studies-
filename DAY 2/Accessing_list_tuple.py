# Accessing_list_tuple.py

# List
fruits_list = ["Apple", "Banana", "Mango"]

print("Accessing List Elements")
print(fruits_list[0])
print(fruits_list[1])
print(fruits_list[2])

# Tuple
fruits_tuple = ("Apple", "Banana", "Mango")

print("\nAccessing Tuple Elements")
print(fruits_tuple[0])
print(fruits_tuple[1])
print(fruits_tuple[2])

"""Output
Accessing List Elements
Apple
Banana
Mango

Accessing Tuple Elements
Apple
Banana
Mango"""

#Using User Input
fruits = ["Apple", "Banana", "Mango"]

index = int(input("Enter index (0-2): "))

print("Element:", fruits[index])
"""Notes
Index starts from 0
First element → list[0]
Second element → list[1]
Third element → list[2]
Same syntax is used for both List and Tuple."""
