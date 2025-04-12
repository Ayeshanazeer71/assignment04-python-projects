import random  # Importing random module to generate a secret number

def guess_the_number():  # Function to handle the guessing game
    secret_number = random.randint(1, 70)  # Generating a random number between 1 and 100
    
    while True:
        try:
            guess = int(input("Enter your guess: "))  # Taking user input and converting it to an integer
            
            if guess < secret_number:
                print("Too low! Try again.")  # Hint if guess is too low
            elif guess > secret_number:
                print("Too high! Try again.")  # Hint if guess is too high
            else:
                print("Congratulations! You guessed the right number.")  # Correct guess message
                break  # Exit loop when the correct number is guessed
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # Handling non-numeric input

guess_the_number()  # Calling the function to start the game
