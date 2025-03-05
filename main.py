import random

print("Welcome to the Game. This is a number guessing game!\nYou got 5 attempts to guess the number between 50 and 100. Let's start the game!")

# Random number generate karna
number_to_guess = random.randint(50, 100)  # randint inclusive hota hai

chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    try:
        my_guess = int(input("Please enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number between 50 and 100.")
        continue

    if my_guess == number_to_guess:
        print(f"Congratulations! The number was {number_to_guess}, and you found it in {guess_counter} attempts.")
        break
    elif my_guess < number_to_guess:
        print("Your guess is too low, try again!")
    else:
        print("Your guess is too high, try again!")

# Agar player 5 attempts me nahi jeeta
if my_guess != number_to_guess:
    print(f"Oops! You ran out of attempts. The correct number was {number_to_guess}. Better luck next time!")
