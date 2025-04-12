# Countdown Program

## Introduction
This is a simple Python program that performs a countdown from **10 to 1** and then prints **"Liftoff!"** at the end. It demonstrates the use of a `for` loop and basic Python syntax.

## How It Works
- The `main()` function contains a `for` loop that starts from `10` and decreases to `1` using `range(10, 0, -1)`.
- Each number is printed on the same line with a space between them.
- After the countdown, the program prints **"Liftoff!"**.
- The `if __name__ == '__main__':` condition ensures that the script runs only when executed directly, not when imported as a module.

## Code
```python
def main():
    # Use a for loop to count down from 10 to 1
    for i in range(10, 0, -1):
        print(i, end=" ")
    
    # Print "Liftoff!" after the countdown
    print("Liftoff!")

# This line ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
```

## How to Run the Code
1. Make sure you have Python installed (Python 3 recommended).
2. Save the code in a file named `countdown.py`.
3. Open a terminal or command prompt and navigate to the file location.
4. Run the command:
   ```sh
   python countdown.py
   ```
5. You will see the following output:
   ```
   10 9 8 7 6 5 4 3 2 1 Liftoff!
   ```

## Best Practices Followed
- **Function Usage**: The countdown logic is inside a `main()` function for better structure.
- **Proper Looping**: A `for` loop with `range()` is used to count down efficiently.
- **Readability**: The `end=" "` argument ensures numbers appear on the same line.
- **Standard Execution Check**: `if __name__ == '__main__':` ensures modularity.

## Conclusion
This is a beginner-friendly Python script demonstrating loops, function definition, and execution control. Modify it to count down from a different number or customize the message! 🚀

