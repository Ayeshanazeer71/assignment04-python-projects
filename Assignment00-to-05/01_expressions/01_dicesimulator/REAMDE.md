# 🎲 Dice Rolling Game in Python

Hello everyone!  
This is a simple Python program I made to roll two dice three times and show the total each time. 😊

## 💡 What this program does:
- It rolls two dice.
- Each dice gives a random number between 1 and 6.
- It adds both numbers and shows the total.
- It does this 3 times in a row.

## 🧠 Why I made this:
I’m learning Python and trying to understand how functions, variables, and loops work.  
In this code, I also explored how variable scope works — you’ll see a variable called `die1 = 25` in the `main()` function just to show it’s different from the dice rolled inside `roll_dice()` function.

## 🧾 How it works:
1. We import the `random` module to get random numbers.
2. We define a function `roll_dice()` that rolls 2 dice and prints their values and total.
3. In the `main()` function, we:
   - Set a variable `die1 = 25` just to show variable scope.
   - Call `roll_dice()` three times using a loop.
4. The program starts when `main()` is called.

## ▶️ How to run:
Just run the Python file using any Python interpreter.

```bash
python dice_game.py


🎯 Output Example:

die1 in main() starts as: 25
Rolled: 3 and 5, Total: 8
Rolled: 6 and 2, Total: 8
Rolled: 1 and 4, Total: 5
die1 in main() is: 25


✅ What I learned:
How to use functions

How for loops work

How to generate random numbers

Understanding variable scope

Thanks for reading! 🌟
This is just the beginning of my Python journey 🐍✨
