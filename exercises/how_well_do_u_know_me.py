#!/usr/bin/env python3
import random

thm_rank = 7706

# Function to generate options around a given number


def generate_options(given_number, num_options=5):
    options = []
    options.append(str(given_number))  # Convert the given_number to string

    for _ in range(num_options - 1):
        # Generate a random number near the given number
        random_number = random.randint(given_number - 50, given_number + 50)
        # Ensure the random number is unique and not already in options
        while str(random_number) in options:
            random_number = random.randint(given_number - 50, given_number + 50)
        options.append(str(random_number))

    # Shuffle the options to randomize the order
    random.shuffle(options)

    return options


# Define questions, answers, and options as a list of dictionaries
questions = [
    {"question": "Do I like", "answer": "dogs", "options": ["dogs", "cats", "elephants", "penguins"]},
    {"question": "Do I prefer", "answer": "coffee", "options": ["tea", "coffee", "juice"]},
    {"question": "Is my favorite color", "answer": "grey", "options": [
        "white", "grey", "black", "blue", "green", "red"]},
    {"question": "Which OS do I prefer", "answer": "linux", "options": ["Linux", "BSD", "MacOS", "Windows"]},
    {"question": "Which OSI Layer am I", "answer": "network", "options": [
        "Physical", "Data Link", "Network", "Transport", "Session", "Presentation", "Application"]},
    {"question": "Which is my preferred Firewall OS:", "answer": "opnsense",
        "options": ["Cisco Catalyst", "OPNsense", "pfSense"]},
    {"question": "How many VLANs are in my Network:", "answer": "12", "options": generate_options(12, 5)},
    {"question": "What's my THM rank:", "answer": str(thm_rank), "options": generate_options(thm_rank, 5)},
]

# Function to ask questions and check answers


def ask_questions(questions):
    correct_count = 0
    total_questions = len(questions)

    for q in questions:
        print(f"{q['question']} {', '.join(q['options'])}?")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == q['answer'].lower():
            correct_count += 1
            print("Correct!\n")
        else:
            print(f"Wrong. The correct answer is {q['answer']}.\n")

    # Calculate percentage of correct answers
    correct_percentage = (correct_count / total_questions) * 100

    # Print result message based on percentage of correct answers
    print(f"You got {correct_count} out of {total_questions} correct.")
    print(f"Your score: {correct_percentage:.2f}%")

    if correct_percentage == 100:
        print("Excellent! You got all the answers correct!")
    elif correct_percentage >= 75:
        print("Great job! You got most of the answers correct.")
    elif correct_percentage >= 50:
        print("Good effort! You got more than half of the answers correct.")
    else:
        print("Keep trying! You'll get better with practice.")


# Collect input from the user
wanna_play = input("Do you want to play a game? [Y/n] ").strip().lower()

# Convert input to boolean with default value True
start_game = True if wanna_play in ['', 'y', 'yes'] else False

# Conditional to check if the game should start
if start_game:
    print("Nice! Let's start ;-)")
    # Start asking questions
    ask_questions(questions)
else:
    print("Too bad =( Maybe later ....")
