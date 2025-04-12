def main():
    try:
        animal = input("What's your favorite animal? ")  

        
        if not animal.isalpha():
            raise ValueError("Error: Invalid input! Please enter a valid animal name.")  

        print(f"My favorite animal is also {animal}!") 
    
    except ValueError as e:
        print(e)  
main()
