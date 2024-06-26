#!/usr/bin/env python3
import random
import requests
from bs4 import BeautifulSoup

user_rank = None
api_url = "https://tryhackme.com/api/discord/user/f4u"

# getting a user's THM rank
def get_thm_rank():

    # Send a GET request to fetch the JSON content
    response = requests.get(api_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON content
        data = response.json()

        # Extract the user rank
        user_rank = data.get('userRank', 'Rank not found')

        return user_rank
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return 0

# Get the user's THM rank
user_rank = get_thm_rank()

# Check if the user's THM rank is 0 or None
if user_rank == 0 or user_rank is None:
    print("Couldn't get THM Rank! Force quit =(")
    exit()
else:
    # Collect input from the user
    wanna_play = input("Do you want to play a game? [Y/n] ").strip().lower()

    # Convert input to boolean with default value True
    start_game = True if wanna_play in ['', 'y', 'yes'] else False

    # Define the OSI layers
    osi_layers = [
        "Physical", "Data Link", "Network", "Transport",
        "Session", "Presentation", "Application"
    ]

    # Function to generate a list of numbers up to a given maximum
    def generate_numbers_list(max_num):
        return [str(i) for i in range(1, max_num + 1)]

    # Function to generate options around a given number
    def generate_options(given_number, num_options=5):
        options = []
        options.append(str(given_number))  # Convert the given_number to string

        for _ in range(num_options - 1):
            # Generate a random number near the given number
            random_number = random.randint(given_number - 10, given_number + 10)
            # Ensure the random number is unique and not already in options
            while str(random_number) in options:
                random_number = random.randint(given_number - 10, given_number + 10)
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
        {"question": "What's my favorite food", "answer": "sushi",
            "options": ["pizza", "sushi", "ice cream", "broccoli"]},
        {"question": "What hobby do I enjoy", "answer": "coding",
            "options": ["coding", "painting", "dancing", "knitting"]},
        {"question": "What happened during my most embarrassing moment", "answer": "spilled coffee",
            "options": ["fell in public", "forgot my lines", "spilled coffee", "lost my keys"]},
        {"question": "Which TV show is my favorite", "answer": "Breaking Bad", "options": [
            "The IT Crowd", "Game of Thrones", "Breaking Bad", "Stranger Things"]},
        {"question": "What annoys me the most", "answer": "slow internet", "options": [
            "loud chewing", "slow internet", "messy rooms", "traffic jams"]},
        {"question": "Who's my favorite superhero", "answer": "Iron Man",
            "options": ["Spider-Man", "Batman", "Wonder Woman", "Iron Man"]},
        {"question": "Where's my dream vacation destination", "answer": "Japan",
            "options": ["Japan", "Hawaii", "Cuba", "Australia"]},
        {"question": "What's my favorite season", "answer": "summer",
            "options": ["summer", "winter", "spring", "autumn"]},
        {"question": "What's my go-to comfort food", "answer": "fried chicken",
            "options": ["macaroni and cheese", "chocolate cake", "fried chicken", "ice cream"]},
        {"question": "What skill do I wish I had", "answer": "speaking any language fluently", "options": [
            "playing the guitar", "speaking any language fluently", "drawing", "cooking gourmet meals"]},
        {"question": "What's my most used emoji", "answer": "xD", "options": ["xD", "=D", ":-D", "-.-\""]},
        {"question": "What's my favorite board game", "answer": "Scrabble",
            "options": ["Monopoly", "Scrabble", "Catan", "Chess"]},
        {"question": "If I could have any superpower, what would it be", "answer": "teleportation",
            "options": ["invisibility", "super strength", "teleportation", "mind reading"]},
        {"question": "What's my favorite genre of music", "answer": "techno",
            "options": ["rock", "pop", "hip-hop", "techno"]},
        {"question": "What's my biggest fear", "answer": "public speaking",
            "options": ["spiders", "heights", "public speaking", "darkness"]},
        {"question": "Which OS do I prefer", "answer": "Linux", "options": ["Linux", "BSD", "MacOS", "Windows"]},
        {"question": "Which OSI Layer am I", "answer": "Network", "options": osi_layers},
        {"question": "Which is my preferred Firewall OS:", "answer": "OPNsense",
            "options": ["Cisco Catalyst", "OPNsense", "pfSense"]},
        {"question": "How many VLANs are in my Network:", "answer": "12", "options": generate_numbers_list(20)},
        {"question": "What's my THM rank:", "answer": str(user_rank), "options": generate_options(user_rank)},
    ]

    # Function to ask questions and check answers
    def ask_questions(questions):
        correct_count = 0
        total_questions = len(questions)

        for q in questions:
            print(f"{q['question']}: {', '.join(q['options'])}?")
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

    # Conditional to check if the game should start
    if start_game:
        print("Nice! Let's start ;-)")
        # Start asking questions
        ask_questions(questions)
    else:
        print("Too bad =( Maybe later ....")
