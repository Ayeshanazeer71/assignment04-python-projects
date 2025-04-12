import random

def guess_the_number():
    number = random.randint(1, 99)
    print("Guess a number between 1 and 99.")

    while (guess := int(input("Your guess: "))) != number:
        print("Too low!" if guess < number else "Too high!")

    print(f"🎉 Correct! The number was {number}.")

if __name__ == "__main__":
    guess_the_number()
