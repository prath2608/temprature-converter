import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    # Game loop
    while True:
        # Prompt the user to input their guess
        guess = int(input("Guess the number (between 1 and 100): "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts to win the game.")
            break

# Call the function to start the game
guessing_game()
