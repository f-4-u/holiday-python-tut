#!/usr/bin/env python3

# Define a dictionary mapping numbers 0 to 9 to their respective words
numbers_to_words = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}


def translateNumberToWords(number):
    worded = []  # Initialize an empty list to store word representations

    # Iterate through each character (digit) in the input number string
    for digit in number:
        # Convert the character (digit) to integer and get its word representation
        worded.append(numbers_to_words[int(digit)])

    # Join the list of word representations into a single string
    return ' '.join(worded)


def main():
    user_input = input("Give a number: ")
    worded_number = translateNumberToWords(user_input)
    print(f"Given Number: {user_input} spelled out as: {worded_number}")


if __name__ == "__main__":
    main()
