import random  # Importing random module to generate random numbers

def guess_number():  # Function to guess the user's number
    print("Think of a number between 10 and 50, and I will guess it.")
    
    while True:
        try:
            guess = random.randint(10, 50)  # Generating a random number between 10 and 50
            print(f"Is your number {guess}? (yes/higher/lower)")
            
            user_input = input().strip().lower()  # Taking user input and converting it to lowercase
            
            if user_input == "yes":
                print("Yay! I guessed it! 🎉")
                break  # Exiting the loop when the correct number is guessed
            elif user_input not in ["higher", "lower"]:
                print("Please enter a valid response (yes/higher/lower).")  # Handling invalid inputs
        except Exception as e:
            print(f"An error occurred: {e}")  # Catching any unexpected errors

guess_number()  # Calling the function to start the game
