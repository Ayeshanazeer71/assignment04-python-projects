def main():
    print("Welcome to Number Doubling Game!")
    
    # Get starting number from user
    start_num = int(input("Please enter a starting number: "))
    original = start_num
    steps = 0
    
    # Double the number until 100 or more
    while start_num < 100:
        start_num = start_num + start_num  # Different way to double
        steps += 1
        print(f"Step {steps}: {start_num}")
    
    print(f"\nYour number {original} was doubled {steps} times to reach {start_num}")

# Run the program
if __name__ == '__main__':
    main()