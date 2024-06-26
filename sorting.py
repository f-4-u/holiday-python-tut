#!/usr/bin/env python3

# 10,7,3,9,5,6,4,7,4,8,2,1,11,15

def get_numbers():
    while True:
        user_input = input("Give ten numbers, comma separated: ")
        numbers_list = user_input.split(",")

        # Attempt to convert the input strings to integers
        try:
            numbers_list = [int(number) for number in numbers_list]
        except ValueError:
            print("Error: Please ensure all inputs are integers.")
            continue

        # Check if the user provided exactly ten numbers
        if len(numbers_list) < 10:
            print(f"You provided {len(numbers_list)} numbers. Please add {10 - len(numbers_list)} more numbers.")
            additional_input = input(f"Provide {10 - len(numbers_list)} more numbers, comma separated: ")
            additional_numbers = additional_input.split(",")
            try:
                additional_numbers = [int(number) for number in additional_numbers]
                numbers_list.extend(additional_numbers)
            except ValueError:
                print("Error: Please ensure all additional inputs are integers.")
                continue

        # Cut off extra numbers if the user provided more than ten
        if len(numbers_list) > 10:
            print(f"You provided {len(numbers_list)} numbers. The entries are truncated after the 10th number ({numbers_list[10]}).")
            numbers_list = numbers_list[:10]

        # Ensure we now have exactly ten numbers
        if len(numbers_list) == 10:
            break
        else:
            print("There was an error in the input process. Let's try again.")

    return numbers_list


numbers = get_numbers()

print(f"reviced numbers: {numbers}")

# Remove the first and last elements
if len(numbers) >= 2:
    numbers.pop(0)  # Remove the first element
    numbers.pop()   # Remove the last element
else:
    print("Error: The list must have at least two elements to remove the first and last.")

print(f"removed first and last entry: {numbers}")
numbers.sort()
print(f"Sorted Number: {numbers}")
print(f"Lowest Number: {numbers[0]}")
print(f"Highest Number: {numbers[-1]}")

# Calculate sum and average
total_sum = sum(numbers)
average = total_sum / len(numbers)

# Print sum and average
print(f"Sum of the numbers: {total_sum}")
print(f"Average of the numbers: {average}")

# Print list in ascending order
print("List in ascending order:", sorted(numbers))

# Print list in descending order
print("List in descending order:", sorted(numbers, reverse=True))
