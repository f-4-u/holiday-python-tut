#!/usr/bin/env python3

"""_summary_
Initialize two lists with at least 5 words each.
Convert the lists to sets to remove any duplicate words.
Print the original sets of words.
Find and print the union of the two sets.
Find and print the intersection of the two sets.
Find and print the difference between the first set and the second set.
Find and print the difference between the second set and the first set.

# output

List 1: ['apple', 'banana', 'cherry', 'date', 'elderberry']
List 2: ['banana', 'date', 'fig', 'grape', 'apple']

Set 1: {'apple', 'banana', 'cherry', 'date', 'elderberry'}
Set 2: {'banana', 'date', 'fig', 'grape', 'apple'}

Union: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape'}
Intersection: {'banana', 'date', 'apple'}
Difference (Set 1 - Set 2): {'cherry', 'elderberry'}
Difference (Set 2 - Set 1): {'fig', 'grape'}
"""

# Initialize two lists
list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
list2 = ['banana', 'date', 'fig', 'grape', 'apple']

# Convert lists to sets to remove duplicates
set1 = set(list1)
set2 = set(list2)

# Print original sets
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Find and print the union of the two sets
union_set = set1.union(set2)
print(f"Union: {union_set}")

# Find and print the intersection of the two sets
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")

# Find and print the difference between the sets
difference_set1_to_set2 = set1.difference(set2)
print(f"Difference (Set 1 - Set 2): {difference_set1_to_set2}")

difference_set2_to_set1 = set2.difference(set1)
print(f"Difference (Set 2 - Set 1): {difference_set2_to_set1}")
