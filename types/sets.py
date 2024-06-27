#!/usr/bin/env python3

# Create a set using curly braces {}
my_set = {'apple', 'banana', 'cherry', 'eggplant', 'lemon'}

# Create a new set with duplicate values (duplicates are automatically removed)
new_set = {'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry'}

# Print the type of 'set' (should output 'set')
print("\nThe type of 'my_set' is:")
print(type(my_set))  # Output: <class 'set'>

# Print the contents of both sets
print("\nContents of 'my_set':")
print(my_set)        # Output: {'apple', 'banana', 'cherry', 'eggplant', 'lemon'}
print("\nContents of 'new_set':")
print(new_set)       # Output: {'apple', 'banana', 'cherry'}

# Check if 'banana' is in the set
print("\nCheck if 'banana' is in 'my_set':")
print('banana' in my_set)       # Output: True

# Check if 'banana' is not in the set
print("\nCheck if 'banana' is not in 'my_set':")
print('banana' not in my_set)   # Output: False

# Add 'orange' to the new_set
print("\nAdd 'orange' to 'new_set':")
new_set.add('orange')
print(new_set)       # Output: {'apple', 'banana', 'cherry', 'orange'}

# Update 'my_set' with elements from 'new_set'
print("\nUpdate 'my_set' with elements from 'new_set':")
my_set.update(new_set)
print(my_set)        # Output: {'apple', 'banana', 'cherry', 'eggplant', 'lemon', 'orange'}

# Remove 'banana' from 'my_set'
print("\nRemove 'banana' from 'my_set':")
my_set.remove('banana')
print(my_set)        # Output: {'apple', 'cherry', 'eggplant', 'lemon', 'orange'}

# Attempt to remove 'hello' (not in set, raises KeyError)
# print("\nAttempt to remove 'hello' from 'my_set':")
# my_set.remove('hello')

# Discard 'hello' (not in set, no error raised)
print("\nDiscard 'hello' from 'my_set' (no error if not present):")
my_set.discard('hello')
print(my_set)        # Output: {'apple', 'cherry', 'eggplant', 'lemon', 'orange'}

# Discard 'apple' from 'my_set'
print("\nDiscard 'apple' from 'my_set':")
my_set.discard('apple')
print(my_set)        # Output: {'cherry', 'eggplant', 'lemon', 'orange'}

# Remove and return an arbitrary item from 'my_set'
print("\nRemove and return an arbitrary item from 'my_set':")
my_set.pop()
print(my_set)        # Output: {'eggplant', 'lemon', 'orange'}

# Remove and return an arbitrary item from 'my_set', assign to variable 'x'
print("\nRemove and return an arbitrary item from 'my_set', assign to variable 'x':")
x = my_set.pop()
print(my_set, x)     # Output: {'lemon', 'orange'} eggplant

# Create two sets and perform union operation
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
print("\nUnion of 'set1' and 'set2':")
set3 = set1.union(set2)
print(set3)          # Output: {'a', 'b', 'c', 1, 2, 3}

# Another way to perform the union operation
print("\nAnother way to perform the union of 'set1' and 'set2':")
set4 = set1 | set2
print(set4)          # Output: {'a', 'b', 'c', 1, 2, 3}

# Union of multiple sets (duplicates removed)
print("\nUnion of multiple sets (duplicates removed):")
myset = set1.union(set2, set2, set3, set3)
print(myset)         # Output: {'a', 'b', 'c', 1, 2, 3}

# Union and intersection operations with a set and a tuple

# Define a set
t = {'a', 'b', 'c'}

# Define a tuple
y = ('a', 2, 'h')

# Perform union of a set 't' and a tuple 'y'
print("\nUnion of a set 't' and a tuple 'y':")
z = t.union(y)
print(z)  # Output: {'a', 'b', 'c', 2, 'h'}

# Perform intersection of the set 't' and the union result 'z'
z = t & z
print("Intersection of set 't' and the union result 'z':")
print(z)  # Output: {'a', 'b', 'c'}

# Perform intersection of a set 't' and a tuple 'y'
print("\nIntersection of a set 't' and a tuple 'y':")
w = t.intersection(y)
print(w)  # Output: {'a'}

# Update 'z' with the intersection of 't'
z.intersection_update(t)
print("Intersection update of 'z' with set 't':")
print(z)  # Output: {'a', 'b', 'c'}

# Difference between set 't' and tuple 'y'
set1 = t.difference(y)
print("Difference between set 't' and tuple 'y':")
print(set1)  # Output: {'b', 'c'}

# Difference between set 't' and set 'z'
set1 = t - z
print("Difference between set 't' and set 'z':")
print(set1)  # Output: set() (empty set since z is same as t)

# Update 'set1' with the difference from tuple 'y'
set1.difference_update(y)
print("Difference update of 'set1' with tuple 'y':")
print(set1)  # Output: set() (already empty set)

# Symmetric difference between set 't' and tuple 'y'
set2 = t.symmetric_difference(y)
print("Symmetric difference between set 't' and tuple 'y':")
print(set2)  # Output: {2, 'b', 'h', 'c'}
