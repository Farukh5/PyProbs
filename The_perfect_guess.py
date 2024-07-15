import random

def guess_the_number():
    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    number_of_guesses = 0
    guess = None

    print("Welcome to 'The Perfect Guess' game!")
    print("I have selected a number between 1 and 10.")
    print("Try to guess the number!")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        number_of_guesses += 1

        if guess < number_to_guess:
            print("Higher number please.")
        elif guess > number_to_guess:
            print("Lower number please.")
        else:
            print(f"Congratulations! You've guessed the number in {number_of_guesses} attempts.")

# Run the game
guess_the_number()
