#!/usr/bin/env python3

# Function to convert kilograms to pounds
def kg_to_lbs(weight_kg):
    return weight_kg * 2.20462

# Function to convert pounds to kilograms
def lbs_to_kg(weight_lbs):
    return weight_lbs / 2.20462

# Collect weight input from the user
weight = float(input("Enter your weight: "))

# Collect unit input from the user (k for kilograms, l for pounds)
unit = input("Is the weight in kilograms (k) or pounds (l)? ").strip().lower()

# Convert and display the weight in the other unit
if unit == 'k':
    weight_in_pounds = kg_to_lbs(weight)
    print(f"Your weight in pounds is: {weight_in_pounds:.2f} lbs")
elif unit == 'l':
    weight_in_kilograms = lbs_to_kg(weight)
    print(f"Your weight in kilograms is: {weight_in_kilograms:.2f} kg")
else:
    print("Invalid input. Please enter 'k' for kilograms or 'l' for pounds.")
