import random  # Importing random module for generating random characters
import string  # Importing string module to use alphabets, digits, and special characters

def generate_password(length):  # Function to generate a password of given length
    characters = string.ascii_letters + string.digits + string.punctuation  # Defining characters to be used in the password
    password = ''.join(random.choices(characters, k=length))  # Selecting random characters and forming the password
    return password  # Returning the generated password

try:
    num_passwords = int(input("Enter the number of passwords: "))  # Taking input for number of passwords to generate
    password_length = int(input("Enter the length of each password: "))  # Taking input for length of each password
    
    if num_passwords > 0 and password_length > 0:
        print("\nGenerated Passwords:")
        for i in range(num_passwords):  # Loop to generate multiple passwords
            print(f"Password {i + 1}: {generate_password(password_length)}")
    else:
        print("Please enter a positive number!")  # Handling invalid input
except ValueError:
    print("Invalid input! Please enter a number.")  # Handling non-numeric input
