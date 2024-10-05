import random


def guessGame():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    flag = True
    while flag == True:
        try:
            # Get player's guess
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            x = input("Do you want play again press y/n ")
            if(x.lower() == "y"):
                secret_number = random.randint(1, 100)
                attempts = 0
                continue
            else:
                flag = False
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
