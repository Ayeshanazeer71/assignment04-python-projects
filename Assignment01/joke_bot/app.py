def tell_joke():
    """Ask user input and respond accordingly."""
    user_input = input("What do you want? ").strip().lower()
    
    if user_input == "joke":
        print("😂 Why did the developer go broke? Because he used up all his cache!")
    else:
        print("🙃 Sorry, I can only tell jokes!")

# Run the function
if __name__ == "__main__":
    tell_joke()
