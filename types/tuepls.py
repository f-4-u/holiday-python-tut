#!/usr/bin/env python3

# Tuple definition
tupel = ("apple", "banane", "cherry")

# Accessing elements in a tuple (not mutable)
# tupel[1] = 1  # This will report an error because tuples are immutable

# Printing tuple and its length
print(tupel, len(tupel))

# Creating a tuple with a single element (note the comma)
tupel2 = ("apple")
print(tupel2, type(tupel2))  # This will be treated as a string, not a tuple

# Correct way to create a tuple with a single element
tupel2 = ("apple",)
print(tupel2, type(tupel2))  # This is a tuple with one element

# Unpacking a tuple into variables
tupel = ("apple", "banane", "cherry", "mango", "kiwi")
(a, b, *c) = tupel
print(a, b, c, type(c))  # a and b are individual elements, c is a list containing the remaining elements

# Unpacking with variable length lists
(a, *b, c) = tupel
print(a, b, c, type(b))  # a is the first element, b is a list containing the middle elements, c is the last element

# Concatenating tuples
tupel = tupel * 2
print(tupel)  # The tuple is repeated

# Adding tuples together
tupel = tupel + tupel2
print(tupel)  # tupel2 is added to tupel
