#!/usr/bin/env python3

# Initialize the list of Greek gods
greek_gods = [
    "Hera", "Poseidon", "Demeter", "Athena",
    "Apollo", "Artemis", "Ares", "Aphrodite", "Hephaestus",
    "Hermes", "Hestia", "Dionysus", "Hades", "Persephone"
]

# Print the initial list of Greek gods
print(greek_gods)

# Print the first element
print(greek_gods[0])

# Change the second element to "Zeus"
greek_gods[1] = "Zeus"
print(greek_gods[1])

# Print the second and third elements
print(greek_gods[1:3])

# Print the last element
print(greek_gods[-1])

# Initialize a mixed-type list
list = ["String", 100, 1.5, True]

# Append a new element to the list
list.append("List")
print(list)

# Insert elements at specific positions
list.insert(1, "blue")
list.insert(6, "blue")
print(list)

# Extend the list with elements from greek_gods
list.extend(greek_gods)
print(list)

# Remove the first occurrence of "blue"
list.remove("blue")
print(list)

# Remove the last element
list.pop()
print(list)

# Remove the element at index 5
list.pop(5)
print(list)

# Delete the first element
del list[0]
print(list)

# Clear all elements from the list
list.clear()
print(list)

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
for name in greek_gods:
    print(name)

# Print each name from index 4 to the end
for i in range(4, len(greek_gods)):
    print(f"{i}: {greek_gods[i]}")

# Notice about specific index pattern printing
print("NOTICE: Starting from index 6, printing every 3rd Greek god:")
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
print("NOTICE: Default ASCII sort - Uppercase letters come before lowercase letters, so 'hErmes' appears after 'hera', but both are at the end of the sorted list.\n"
      "Also, numbers come before letters, so 'H3phaestus' appears before 'Hades'.")
print(greek_gods)

# Sort the list ignoring case sensitivity
greek_gods.sort(key=str.lower)
print("NOTICE: Case-insensitive sort - The list is sorted ignoring case sensitivity.")
print(greek_gods)


# Initialize list1 with some integers
list1 = [1, 2, 3]

# Create list2 as a reference copy of list1
list2 = list1  # This is a reference copy (list2 is an alias)

# Create list3 as a deep copy of list1
list3 = list1.copy()  # This is a deep copy

# Print the initial state of all lists
print(f"List 1: {list1}, List 2: {list2}, List 3: {list3}")

# Append different strings to list1 and list2
list1.append("appended to L1")
list2.append("appended to L2")

# Print the state of all lists after appending to list1 and list2
print(f"List 1: {list1}, List 2: {list2}, List 3: {list3}")

# Create list4 by concatenating list1 and list3
list4 = list1 + list3

# Print the state of all lists after creating list4
print(f"List 1: {list1}, List 2: {list2}, List 3: {list3}, List 4: {list4}")

# Append a string to list3
list3.append("appended to L3")

# Print the final state of all lists
print(f"List 1: {list1}, List 2: {list2}, List 3: {list3}, List 4: {list4}")
