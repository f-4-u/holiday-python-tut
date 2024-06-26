#!/usr/bin/env python3

while True:
    calc = input("Provide your calculation (+, -, *, /): ").strip()

    # Check if the user wants to exit
    if calc.lower() == 'no' or calc.lower() == 'n':
        print("Goodbye!")
        break

    # Evaluate the calculation
    try:
        result = eval(calc)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

    # Ask if the user wants to perform another calculation
    new_calc = input("Do you want to perform another calculation? (yes/no) [yes]: ").strip().lower() or 'yes'
    if new_calc != 'yes' and new_calc != 'y':
        print("Goodbye!")
        break

print("Thank you for using the calculator!")
