#!/usr/bin/env python3

# Tuple definition
tupel = ("apple", "banane", "cherry")

# Accessing elements in a tuple (not mutable)
# tupel[1] = 1  # This will report an error because tuples are immutable

# Printing tuple and its length
print("\nTuple and its length:")
print(tupel, len(tupel))  # Output: ('apple', 'banane', 'cherry') 3

# Creating a tuple with a single element (note the comma)
tupel2 = ("apple")
print("\nSingle element without a comma (treated as a string):")
print(tupel2, type(tupel2))  # Output: apple <class 'str'>

# Correct way to create a tuple with a single element
tupel2 = ("apple",)
print("\nSingle element with a comma (treated as a tuple):")
print(tupel2, type(tupel2))  # Output: ('apple',) <class 'tuple'>

# Unpacking a tuple into variables
tupel = ("apple", "banane", "cherry", "mango", "kiwi")
(a, b, *c) = tupel
print("\nUnpacking a tuple into variables (a, b, *c):")
print(a, b, c, type(c))  # Output: apple banane ['cherry', 'mango', 'kiwi'] <class 'list'>

# Unpacking with variable length lists
(a, *b, c) = tupel
print("\nUnpacking with variable length lists (a, *b, c):")
print(a, b, c, type(b))  # Output: apple ['banane', 'cherry', 'mango'] kiwi <class 'list'>

# Concatenating tuples
tupel = tupel * 2
print("\nConcatenating the tuple with itself:")
print(tupel)  # Output: ('apple', 'banane', 'cherry', 'mango', 'kiwi', 'apple', 'banane', 'cherry', 'mango', 'kiwi')

# Adding tuples together
tupel = tupel + tupel2
print("\nAdding a single-element tuple to the original tuple:")
print(tupel)  # Output: ('apple', 'banane', 'cherry', 'mango', 'kiwi', 'apple', 'banane', 'cherry', 'mango', 'kiwi', 'apple')
