# loop_enumerate.py
# Program to demonstrate enumerate() with list and tuple

"""enumerate() adds a counter to an iterable (list, tuple, etc.).
Syntax:
python
enumerate(iterable, start=0)
You can also start counting from a custom number:
python
for i, v in enumerate(fruits, start=1):
    print(i, v)"""

# List example
fruits = ["apple", "banana", "cherry"]
print("Enumerating List:")
for index, value in enumerate(fruits):
    print(index, "→", value)

# Tuple example
print("\nEnumerating Tuple:")
numbers = (10, 20, 30, 40)
for index, value in enumerate(numbers):
    print(index, "→", value)
