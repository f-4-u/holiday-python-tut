#!/usr/bin/env python3

# Create a set using curly braces {}
set = {'apple', 'banana', 'cherry', 'eggplant', 'lemon'}

# Create a new set with duplicate values (duplicates are automatically removed)
newset = {'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry'}

# Print the type of 'set' (should output 'set')
print(type(set))

# Print the contents of both sets
print(set)      # Output: {'apple', 'banana', 'cherry', 'eggplant', 'lemon'}
print(newset)   # Output: {'apple', 'banana', 'cherry'}

# Check if 'banana' is in the set
print('banana' in set)      # Output: True

# Check if 'banana' is not in the set
print('banana' not in set)  # Output: False

# Add 'orange' to the newset
newset.add('orange')
print(newset)   # Output: {'apple', 'banana', 'cherry', 'orange'}

# Update 'set' with elements from 'newset'
set.update(newset)
print(set)      # Output: {'apple', 'banana', 'cherry', 'eggplant', 'lemon', 'orange'}

# Remove 'banana' from 'set'
set.remove('banana')
print(set)      # Output: {'apple', 'cherry', 'eggplant', 'lemon', 'orange'}

# Attempt to remove 'hello' (not in set, raises KeyError)
# set.remove('hello')

# Discard 'hello' (not in set, no error raised)
set.discard('hello')
print(set)      # Output: {'apple', 'cherry', 'eggplant', 'lemon', 'orange'}

# Discard 'apple' from 'set'
set.discard('apple')
print(set)      # Output: {'cherry', 'eggplant', 'lemon', 'orange'}

# Remove and return an arbitrary item from 'set'
set.pop()
print(set)      # Output: {'eggplant', 'lemon', 'orange'}

# Remove and return an arbitrary item from 'set', assign to variable 'x'
x = set.pop()
print(set, x)   # Output: {'lemon', 'orange'} eggplant
