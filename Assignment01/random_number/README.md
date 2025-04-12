# Guess the Number Game

## 📌 Overview
This is a simple number guessing game built in Python. The program generates a random number between **10 and 50**, and the user has to guess the correct number. After each incorrect guess, the program provides feedback if the guess is **too high** or **too low**.

## 🚀 How It Works
1. The program generates a **random number between 10 and 50**.
2. The user enters a guess.
3. If the guess is incorrect:
   - The program provides a hint: **"Too low!"** or **"Too high!"**
   - The user is asked to guess again.
4. If the guess is correct:
   - The program prints a **congratulatory message** and exits.
5. If the user enters an invalid input (e.g., letters or symbols), the program shows an **error message** and asks for a valid number.

## 📂 File Structure
```
|-- guess_number.py   # Main Python script
|-- README.md         # This documentation file
```

## 🛠️ Requirements
- Python 3.x

## ▶️ How to Run the Program
1. Make sure Python is installed on your system.
2. Open a terminal or command prompt and navigate to the folder containing `guess_number.py`.
3. Run the program using:
   ```sh
   python guess_number.py
   ```
4. Follow the on-screen instructions to play the game.

## ✨ Features
✅ Generates a **random number between 10 and 50**
✅ Provides hints (**Too low! / Too high!**)
✅ Handles invalid inputs gracefully
✅ Uses a **while loop for continuous guessing**
✅ **Breaks** when the correct number is guessed

## 📌 Example Output
```
I am thinking of a number between 10 and 50...
Enter a guess: 20
Too low!

Enter a guess: 40
Too high!

Enter a guess: 30
🎉 Congrats! The number was 30.
```

## 🤝 Contributing
If you want to improve this project, feel free to submit a pull request!

## 📜 License
This project is free to use and modify.

