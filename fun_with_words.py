#!/usr/bin/env python3

"""_summary_
Initialize an empty list.
Prompt the user to input 10 words and add them to the list.
Print the list.
Remove a word specified by the user from the list.
Print the list after removal.
Find and print the longest and shortest words in the list.
Count and print the occurrences of each word.
Sort and print the list alphabetically.
Print the list in reverse alphabetical order.
# Output

Enter 10 words:
1: apple
2: banana
3: cherry
4: date
5: elderberry
6: fig
7: grape
8: honeydew
9: kiwi
10: lemon

Original list:
['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

Enter a word to remove: fig

List after removing 'fig':
['apple', 'banana', 'cherry', 'date', 'elderberry', 'grape', 'honeydew', 'kiwi', 'lemon']

Longest word: elderberry
Shortest word: date

Word occurrences:
apple: 1
banana: 1
cherry: 1
date: 1
elderberry: 1
grape: 1
honeydew: 1
kiwi: 1
lemon: 1

List in alphabetical order:
['apple', 'banana', 'cherry', 'date', 'elderberry', 'grape', 'honeydew', 'kiwi', 'lemon']

List in reverse alphabetical order:
['lemon', 'kiwi', 'honeydew', 'grape', 'elderberry', 'date', 'cherry', 'banana', 'apple']


Sample input for comma seperated input
other, trench, refuse, illusion, ambiguity, woman, half, jockey, rate, have, eliminate
dog, dog, dog, cat, cat, mule, mouse, elefant, tiger, shark
"""

def get_words():
    while True:
        user_input = input("Enter 10 words, either one by one or comma-separated: ").strip()

        if ',' in user_input:
            # Split by comma and strip extra spaces, then split by any whitespace to handle any excess spaces
            words_list = [word.strip() for word in user_input.split(',') if word.strip()]
        else:
            words_list = []

            # Prompt the user to provide each word individually
            for i in range(10):
                word = input(f"Provide word {i + 1}: ").strip()
                words_list.append(word)

        # Validate and process the input
        if len(words_list) == 10:
            # Validate each word is a non-empty string
            if all(isinstance(word, str) and word for word in words_list):
                return words_list
            else:
                print("Error: All inputs must be non-empty strings.")
        else:
            print("Error: Please provide exactly 10 words.")


def find_longest_and_shortest_words(words_list):
    if not words_list:
        return None, None

    # Initialize variables to store longest and shortest words
    longest_words = []
    shortest_words = []

    # Determine the length of the longest and shortest words
    max_length = max(len(word) for word in words_list)
    min_length = min(len(word) for word in words_list)

    # Find all words with the longest length
    for word in words_list:
        if len(word) == max_length:
            longest_words.append(word)

    # Find all words with the shortest length
    for word in words_list:
        if len(word) == min_length:
            shortest_words.append(word)

    return longest_words, shortest_words


def main():
    # Get 10 words from the user
    words_list = get_words()

    # Print the words with their respective indices
    print("\nYou provided the following words:")
    for idx, word in enumerate(words_list, start=1):
        print(f"Word {idx}: {word}")

    # Find and print longest and shortest words
    longest_words, shortest_words = find_longest_and_shortest_words(words_list)

    if longest_words:
        print(f"\nLongest word(s) ({len(longest_words)} words with length {len(longest_words[0])}):")
        for longest_word in longest_words:
            print(f"- {longest_word}")

    if shortest_words:
        print(f"\nShortest word(s) ({len(shortest_words)} words with length {len(shortest_words[0])}):")
        for shortest_word in shortest_words:
            print(f"- {shortest_word}")

    # Count and print the occurrences of each word
    word_count = {}

    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("\nWord occurrences:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    # Sort and print the list alphabetically
    sorted_list = sorted(words_list)
    print("\nList in alphabetical order:")
    print(sorted_list)

    # Print the list in reverse alphabetical order
    reverse_sorted_list = sorted(words_list, reverse=True)
    print("\nList in reverse alphabetical order:")
    print(reverse_sorted_list)

if __name__ == "__main__":
    main()
