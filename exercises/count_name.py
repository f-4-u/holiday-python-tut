#!/usr/bin/env python3

name = input("What's your name? ")

name_length = len(name)

if name_length <= 3:
    print("Your name should atleast longer, than three characters")
elif name_length > 20:
    print("You have a really long ... name")
else:
    print(f"Hello {name}")
