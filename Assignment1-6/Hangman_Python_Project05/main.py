import random

def choose_word():
    """Pick a random word for the game."""
    return random.choice(["python", "coding", "developer", "debug", "script"])

def display_word(word, guessed):
    """Show word progress with guessed letters."""
    return " ".join(letter if letter in guessed else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed, lives = set(), 6

    print("🎮 Welcome to Hangman! Guess the word.")
    
    while lives:
        print("\nWord:", display_word(word, guessed))
        print(f"Lives: {lives}")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("🚨 Enter only a single valid letter!")
            continue
        if guess in guessed:
            print("⚠️ You already guessed that letter!")
            continue

        guessed.add(guess)
        if guess not in word:
            lives -= 1
            print(f"❌ '{guess}' is incorrect!")
        
        if all(letter in guessed for letter in word):
            print(f"\n🎉 You won! The word was: {word}")
            break
    else:
        print(f"\n💀 Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
