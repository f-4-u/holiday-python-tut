#!/usr/bin/env python3

"""_summary_
Initialize an empty list.
Prompt the user to input 10 numbers and add them to the list.
Print the list.
Remove the first and last numbers from the list.
Print the list after removal.
Find and print the maximum and minimum numbers in the list.
Calculate and print the sum and average of the numbers.
Sort and print the list in ascending order.
Sort and print the list in descending order. # Googlen
Enter 10 numbers:
1: 5
2: 8
3: 3
4: 12
5: 7
6: 9
7: 2
8: 10
9: 4
10: 6

Original list:
[5, 8, 3, 12, 7, 9, 2, 10, 4, 6]

List after removing first and last elements:
[8, 3, 12, 7, 9, 2, 10, 4]

Maximum number: 12
Minimum number: 2
Sum of numbers: 55
Average of numbers: 6.88

List in ascending order:
[2, 3, 4, 7, 8, 9, 10, 12]

List in descending order:
[12, 10, 9, 8, 7, 4, 3, 2]
"""

# 10,17,7,3,9,5,6,4,8,2,1,11,15


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
            print(f"You provided {len(numbers_list)
                                  } numbers. The entries are truncated after the 10th number ({numbers_list[10]}).")
            numbers_list = numbers_list[:10]

        # Ensure we now have exactly ten numbers
        if len(numbers_list) == 10:
            break
        else:
            print("There was an error in the input process. Let's try again.")

    return numbers_list


def remove_first_and_last(numbers):
    if len(numbers) >= 2:
        print(f"Remove the first and last  numbers of from the list ({numbers[0]}, {numbers[-1]})")
        numbers = numbers[1:-1]  # Remove the first and last element
    else:
        print("Error: The list must have at least two elements to remove the first and last.")
    return numbers


def calculate_statistics(numbers):
    # Sort the numbers
    sorted_numbers = sorted(numbers)

    # Print sorted numbers
    print(f"Sorted Numbers: {sorted_numbers}")

    # Print lowest and highest number
    print(f"Lowest Number: {sorted_numbers[0]}")
    print(f"Highest Number: {sorted_numbers[-1]}")

    # Calculate sum and average
    total_sum = sum(sorted_numbers)
    average = total_sum / len(sorted_numbers)

    # Print sum and average
    print(f"Sum of the numbers: {total_sum}")
    print(f"Average of the numbers: {average}")

    # Print list in ascending order (already sorted)
    print("List in ascending order:", sorted_numbers)

    # Print list in descending order
    print("List in descending order:", sorted_numbers[::-1])


if __name__ == "__main__":
    numbers = get_numbers()
    print(f"Received numbers: {numbers}")

    # Remove the first and last elements
    numbers = remove_first_and_last(numbers)
    print(f"Removed first and last entry: {numbers}")

    # Calculate and print statistics
    calculate_statistics(numbers)
