# Updating_removing.py
# Program to demonstrate updating and removing elements in list and tuple

# ----- List Example -----
fruits = ["apple", "banana", "cherry", "mango"]
print("Original List:", fruits)

# Update element
fruits[1] = "blueberry"
print("After Updating:", fruits)

# Remove element
fruits.remove("cherry")
print("After Removing:", fruits)

# ----- Tuple Example -----
numbers = (10, 20, 30, 40)
print("\nOriginal Tuple:", numbers)

# Tuples are immutable → cannot update/remove directly
# Convert to list for modification
temp_list = list(numbers)

# Update element
temp_list[2] = 300
print("Tuple after Updating:", tuple(temp_list))

# Remove element
temp_list.remove(20)
print("Tuple after Removing:", tuple(temp_list))

"""
Original List: ['apple', 'banana', 'cherry', 'mango']
After Updating: ['apple', 'blueberry', 'cherry', 'mango']
After Removing: ['apple', 'blueberry', 'mango']

Original Tuple: (10, 20, 30, 40)
Tuple after Updating: (10, 20, 300, 40)
Tuple after Removing: (10, 300, 40)
"""
