# Snake, Water, Gun game in Python

import random

def game():
    choices = ["Snake", "Water", "Gun"]
    computer = random.choice(choices)

    user = input("Enter your choice (Snake/Water/Gun): ").capitalize()
    while user not in choices:
        user = input("Invalid input. Enter your choice (Snake/Water/Gun): ").capitalize()

    print(f"\nComputer chose {computer} and you chose {user}.\n")

    if user == computer:
        return "It's a tie!"
    if (user == "Snake" and computer == "Gun") or (user == "Water" and computer == "Snake") or (user == "Gun" and computer == "Water"):
        return "You win!"
    return "You lose!"

print(game())