


import random

choices = ["rock" , "paper" , "scrissors"]

user = input("Rock, Paper, or Scissors? ").strip().lower()
computer = random.choice(choices)

print(f"Coumputer: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")