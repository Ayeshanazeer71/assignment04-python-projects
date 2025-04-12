def main():
    try:
        
        num: float = float(input("Type a number to see its square: "))

        square: float = num ** 2

        
        print(f"{num} squared is {square}")

    except ValueError:
        print("Error: Please enter a valid number.")


main()
