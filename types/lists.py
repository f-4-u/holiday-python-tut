#!/usr/bin/env python3

# Initialize the list of Greek gods
greek_gods = [
    "Hera", "Poseidon", "Demeter", "Athena",
    "Apollo", "Artemis", "Ares", "Aphrodite", "Hephaestus",
    "Hermes", "Hestia", "Dionysus", "Hades", "Persephone"
]

# Print the initial list of Greek gods
print("\nInitial list of Greek gods:")
# Output: ['Hera', 'Poseidon', 'Demeter', 'Athena', 'Apollo', 'Artemis', 'Ares', 'Aphrodite', 'Hephaestus', 'Hermes', 'Hestia', 'Dionysus', 'Hades', 'Persephone']
print(greek_gods)

# Print the first element
print("\nFirst element in the list of Greek gods:")
print(greek_gods[0])  # Output: 'Hera'

# Change the second element to "Zeus"
greek_gods[1] = "Zeus"
print("\nSecond element after changing to 'Zeus':")
print(greek_gods[1])  # Output: 'Zeus'

# Print the second and third elements
print("\nSecond and third elements:")
print(greek_gods[1:3])  # Output: ['Zeus', 'Demeter']

# Print the last element
print("\nLast element in the list of Greek gods:")
print(greek_gods[-1])  # Output: 'Persephone'

# Initialize a mixed-type list
mixed_list = ["String", 100, 1.5, True]

# Append a new element to the list
mixed_list.append("List")
print("\nMixed list after appending 'List':")
print(mixed_list)  # Output: ['String', 100, 1.5, True, 'List']

# Insert elements at specific positions
mixed_list.insert(1, "blue")
mixed_list.insert(6, "blue")
print("\nMixed list after inserting 'blue' at positions 1 and 6:")
print(mixed_list)  # Output: ['String', 'blue', 100, 1.5, True, 'List', 'blue']

# Extend the list with elements from greek_gods
mixed_list.extend(greek_gods)
print("\nMixed list after extending with elements from 'greek_gods':")
# Output: ['String', 'blue', 100, 1.5, True, 'List', 'blue', 'Hera', 'Zeus', 'Demeter', 'Athena', 'Apollo', 'Artemis', 'Ares', 'Aphrodite', 'Hephaestus', 'Hermes', 'Hestia', 'Dionysus', 'Hades', 'Persephone']
print(mixed_list)

# Remove the first occurrence of "blue"
mixed_list.remove("blue")
print("\nMixed list after removing the first occurrence of 'blue':")
# Output: ['String', 100, 1.5, True, 'List', 'blue', 'Hera', 'Zeus', 'Demeter', 'Athena', 'Apollo', 'Artemis', 'Ares', 'Aphrodite', 'Hephaestus', 'Hermes', 'Hestia', 'Dionysus', 'Hades', 'Persephone']
print(mixed_list)

# Remove the last element
mixed_list.pop()
print("\nMixed list after removing the last element:")
# Output: ['String', 100, 1.5, True, 'List', 'blue', 'Hera', 'Zeus', 'Demeter', 'Athena', 'Apollo', 'Artemis', 'Ares', 'Aphrodite', 'Hephaestus', 'Hermes', 'Hestia', 'Dionysus', 'Hades']
print(mixed_list)

# Remove the element at index 5
mixed_list.pop(5)
print("\nMixed list after removing the element at index 5:")
# Output: ['String', 100, 1.5, True, 'List', 'Hera', 'Zeus', 'Demeter', 'Athena', 'Apollo', 'Artemis', 'Ares', 'Aphrodite', 'Hephaestus', 'Hermes', 'Hestia', 'Dionysus', 'Hades']
print(mixed_list)

# Delete the first element
del mixed_list[0]
print("\nMixed list after deleting the first element:")
# Output: [100, 1.5, True, 'List', 'Hera', 'Zeus', 'Demeter', 'Athena', 'Apollo', 'Artemis', 'Ares', 'Aphrodite', 'Hephaestus', 'Hermes', 'Hestia', 'Dionysus', 'Hades']
print(mixed_list)

# Clear all elements from the list
mixed_list.clear()
print("\nMixed list after clearing all elements:")
print(mixed_list)  # Output: []

# Delete the variable greek_gods
del greek_gods
# print(greek_gods)  # This would raise an error because greek_gods is deleted

# Reinitialize the list of Greek gods
greek_gods = [
    "Zeus", "Hera", "Poseidon", "Demeter", "Athena",
    "Apollo", "Artemis", "Ares", "Aphrodite", "Hephaestus",
    "Hermes", "Hestia", "Dionysus", "Hades", "Persephone"
]

# Print each name in greek_gods
print("\nPrinting each name in the reinitialized list of Greek gods:")
for name in greek_gods:
    print(name)

# Print each name from index 4 to the end
print("\nPrinting each name from index 4 to the end in Greek gods list:")
for i in range(4, len(greek_gods)):
    print(f"{i}: {greek_gods[i]}")

# Notice about specific index pattern printing
print("\nNOTICE: Starting from index 6, printing every 3rd Greek god:")
for i in range(6, len(greek_gods), 3):
    print(f"{i}: {greek_gods[i]}")

# Reinitialize the list with mixed-case names and numbers
greek_gods = [
    "Zeus", "hera", "Poseidon", "Demeter", "Athena",
    "Apollo", "artemis", "Ares", "Aphrodite", "H3phaestus",
    "hErmes", "Hestia", "Dionysus", "Hades", "Persephone"
]

# Sort the list based on ASCII values (default behavior)
greek_gods.sort()
print("\nNOTICE: Default ASCII sort - Uppercase letters come before lowercase letters, so 'hera' appears after 'hErmes', but both are at the end of the sorted list.\n"
      "Also, numbers come before letters, so 'H3phaestus' appears before 'Hades'.")
# Output: ['Apollo', 'Aphrodite', 'Ares', 'Athena', 'Demeter', 'Dionysus', 'H3phaestus', 'Hades', 'Hera', 'Hestia', 'Poseidon', 'Zeus', 'artemis', 'hErmes', 'hera']
print(greek_gods)

# Sort the list ignoring case sensitivity
greek_gods.sort(key=str.lower)
print("\nNOTICE: Case-insensitive sort - The list is sorted ignoring case sensitivity.")
# Output: ['Aphrodite', 'Apollo', 'Ares', 'artemis', 'Athena', 'Demeter', 'Dionysus', 'H3phaestus', 'Hades', 'Hera', 'hErmes', 'Hestia', 'hera', 'Poseidon', 'Zeus']
print(greek_gods)

# Initialize list1 with some integers
list1 = [1, 2, 3]

# Create list2 as a reference copy of list1
list2 = list1  # This is a reference copy (list2 is an alias)

# Create list3 as a deep copy of list1
list3 = list1.copy()  # This is a deep copy

# Print the initial state of all lists
print("\nInitial state of list1, list2, and list3:")
# Output: List 1: [1, 2, 3], List 2: [1, 2, 3], List 3: [1, 2, 3]
print(f"List 1: {list1}, List 2: {list2}, List 3: {list3}")

# Append different strings to list1 and list2
list1.append("appended to L1")
list2.append("appended to L2")

# Print the state of all lists after appending to list1 and list2
print("\nState of list1, list2, and list3 after appending to list1 and list2:")
# Output: List 1: [1, 2, 3, 'appended to L1', 'appended to L2'], List 2: [1, 2, 3, 'appended to
print(f"List 1: {list1}, List 2: {list2}, List 3: {list3}")
