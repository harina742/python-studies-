#              Notes
"""
  List	                    Tuple
Mutable	                  Immutable
Uses append()	            Cannot use append()
[ ]	                      ( )
Can modify items	        Cannot modify items
"""


#Adding Elements in a List
def add_item(my_list, item):
    my_list.append(item)
    return my_list

fruits = ["Apple", "Banana"]

new_item = input("Enter a fruit: ")

result = add_item(fruits, new_item)

print("Updated List:", result)

"""
Output
Enter a fruit: Mango
Updated List: ['Apple', 'Banana', 'Mango']
"""
#Adding Elements in a Tuple
#Since tuples are immutable, we create a new tuple.

def add_item(my_tuple, item):
    return my_tuple + (item,)

fruits = ("Apple", "Banana")

new_item = input("Enter a fruit: ")

result = add_item(fruits, new_item)

print("Updated Tuple:", result)
"""Output
Enter a fruit: Mango
Updated Tuple: ('Apple', 'Banana', 'Mango')"""
