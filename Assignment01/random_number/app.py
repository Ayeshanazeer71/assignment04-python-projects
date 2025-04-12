import random

def guess_number():
    number = random.randint(10, 50)
    print("I am thinking of a number between 10 and 50...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
            if guess == number:
                print(f"🎉 Congrats! The number was {number}.")
                break
            print("Too low!" if guess < number else "Too high!")
        except ValueError:
            print("❌ Please enter a valid number!")

if __name__ == "__main__":
    guess_number()
