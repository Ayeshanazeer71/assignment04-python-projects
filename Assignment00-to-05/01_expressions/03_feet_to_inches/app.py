 # Conversion factor: 12 inches in 1 foot
INCHES_IN_FOOT = 12  # This constant defines how many inches are there in 1 foot.

def main():
    try:
        feet = float(input("Enter number of feet: "))  # Step 1: Take input from the user in feet and convert it to float.
        print(f"That is {feet * INCHES_IN_FOOT} inches!")  # Step 2: Convert feet to inches and print the result.
    except ValueError:
        print("Please enter a valid number.")  # If the user enters an invalid input, this message will be shown.

if __name__ == "__main__":
    main()  # Step 3: When the script is run directly, the main() function will be called.
