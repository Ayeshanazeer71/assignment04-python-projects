# Number Doubling Game

## Description
The **Number Doubling Game** is a simple Python program that takes a starting number as input from the user and keeps doubling it until it reaches or exceeds 100. The program also tracks and displays the number of steps taken to reach this threshold.

## How It Works
1. The program welcomes the user and prompts them to enter a starting number.
2. It then continuously doubles the number and prints each step.
3. The process continues until the number reaches or exceeds 100.
4. Finally, the program displays how many times the number was doubled to reach the final value.

## Code Explanation
- `main()`: This function handles the main logic of the game.
  - It prints a welcome message.
  - It takes an integer input from the user.
  - It initializes the `steps` counter to track the number of doublings.
  - A `while` loop runs, doubling the number and incrementing the step counter until the number is 100 or more.
  - Each step's result is printed.
  - The final message displays the original number, the number of times it was doubled, and the final result.
- The program is executed only if it is run directly (`if __name__ == '__main__':`).

## Example Run
```
Welcome to Number Doubling Game!
Please enter a starting number: 5
Step 1: 10
Step 2: 20
Step 3: 40
Step 4: 80
Step 5: 160

Your number 5 was doubled 5 times to reach 160
```

## Requirements
- Python 3.x

## How to Run
1. Save the script as `number_doubling.py`.
2. Open a terminal and navigate to the script location.
3. Run the command:
   ```
   python number_doubling.py
   ```

## Notes
- If a number greater than 100 is entered initially, the program will immediately display the result without performing any doubling steps.
- Negative numbers and non-numeric inputs will cause errors; adding validation can improve user experience.

