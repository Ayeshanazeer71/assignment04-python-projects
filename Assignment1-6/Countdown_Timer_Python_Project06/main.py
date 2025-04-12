import time

def countdown_timer(seconds: int) -> None:
    """Simple Countdown Timer in MM:SS format."""
    if seconds <= 0:
        print("⛔ Please enter a valid positive number of seconds.")
        return

    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            print(f"{mins:02}:{secs:02}", end="\r")  # Overwrite same line
            time.sleep(1)  # Pause for 1 second
            seconds -= 1
        
        print("⏰ Time's up!")
    
    except KeyboardInterrupt:
        print("\n⏹ Countdown stopped by user.")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter countdown time in seconds: "))
        countdown_timer(user_input)
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
