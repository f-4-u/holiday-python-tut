#!/usr/bin/env python3

from datetime import datetime

# Function to calculate birth year based on age


def calculate_birth_year(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    return birth_year


# Collecting inputs from the user
surname = input("Enter your surname: ")
first_name = input("Enter your first name: ")
age = int(input("Enter your age: "))
height_cm = float(input("Enter your height (in cm): "))

# Input options for student status with default value 'No'
student_status_input = input("Are you a student? (y/n/yes/no, default is 'No'): ").strip().lower()
if student_status_input in ['yes', 'y']:
    student_status = True
else:
    student_status = False

# Calculate birth year
birth_year = calculate_birth_year(age)

# Convert height from cm to meters
height_m = height_cm / 100

# Output the results
print("\n--- User Details ---")
print(f"Name: \t\t\t{first_name} {surname}")
print(f"Birth Year: \t\t{birth_year} ({age}y)")
print(f"Height: \t\t{height_m:.2f} meters")
print(f"Student Status: \t{'Yes' if student_status else 'No'}")
