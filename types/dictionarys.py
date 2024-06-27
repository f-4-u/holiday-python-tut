#!/usr/bin/env python3

# Define a dictionary with key-value pairs
# Dictionaries are ordered (from Python 3.7+), changeable, and do not allow duplicate keys (duplicated key will overwrite)
my_dict = {
    'yulicee': 21756832454,
    'eisi2k': 327467335,
    'f4u': 1774325342534,
    'f4u': 0,  # Duplicated key 'f4u' will overwrite the previous value
}

# Print the value associated with the key 'eisi2k'
print("\nValue associated with the key 'eisi2k':")
print(my_dict['eisi2k'])  # Output: 327467335

# Print the length of the dictionary
print("\nLength of the dictionary:")
print(len(my_dict))  # Output: 3, as 'f4u' is considered once due to duplicate key overwriting

# Define another dictionary 'dict2'
dict2 = {
    'brand': 'ford',
    'electric': False,
    'year': 1964,
    'colors': ['red', 'white', 'blue']
}

# Access and print specific values from 'dict2'
print("\nAccessing specific values in 'dict2':")
print(dict2['brand'])  # Output: 'ford'
print(dict2.get('year'))  # Output: 1964

# Print keys and values of 'dict2'
print("\nKeys and values of 'dict2':")
print(dict2.keys())  # Output: dict_keys(['brand', 'electric', 'year', 'colors'])
print(dict2.values())  # Output: dict_values(['ford', False, 1964, ['red', 'white', 'blue']])

# Modify a value in 'dict2'
dict2['year'] = 2024
print("\nUpdated values of 'dict2' after modification:")
print(dict2.values())  # Output: dict_values(['ford', False, 2024, ['red', 'white', 'blue']])

# Update 'year' back to 1964 in 'dict2'
dict2.update({'year': 1964})
print("\nRestored 'year' to 1964 in 'dict2':")
print(dict2.values())  # Output: dict_values(['ford', False, 1964, ['red', 'white', 'blue']])

# Print items (key-value pairs) of 'dict2'
print("\nItems (key-value pairs) in 'dict2':")
# Output: dict_items([('brand', 'ford'), ('electric', False), ('year', 1964), ('colors', ['red', 'white', 'blue'])])
print(dict2.items())

# Remove a specific key-value pair from 'dict2'
dict2.pop('brand')
print("\nDictionary 'dict2' after removing 'brand':")
print(dict2)  # Output: {'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# Remove and return an arbitrary key-value pair from 'dict2'
dict2.popitem()
print("\nDictionary 'dict2' after popping an item:")
print(dict2)  # Output: {'electric': False, 'year': 1964}

# Delete a specific key from 'dict2'
del dict2['year']
print("\nDictionary 'dict2' after deleting 'year':")
print(dict2)  # Output: {'electric': False}

# Clear all elements from 'dict2'
dict2.clear()
print("\nDictionary 'dict2' after clearing all elements:")
print(dict2)  # Output: {}

# Create a shallow copy of 'dict2' and assign it to 'dict3'
dict3 = dict2.copy()
print("\nShallow copy of 'dict2' assigned to 'dict3':")
print(dict3)  # Output: {}

# Define a nested dictionary 'myFamily'
myFamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    },
}

# Access and print nested values from 'myFamily'
print("\nAccessing nested values in 'myFamily':")
print(myFamily['child1']['name'])  # Output: 'Emil'
