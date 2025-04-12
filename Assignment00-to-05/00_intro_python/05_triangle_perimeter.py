def main():
    
    try:
        side1: float = float(input("What is the length of side 1? "))
        side2: float = float(input("What is the length of side 2? "))
        side3: float = float(input("What is the length of side 3? "))

    
        perimeter: float = side1 + side2 + side3

        print(f"The perimeter of the triangle is {perimeter}")

    except ValueError:
        print("Error: Please enter a valid number for all sides.")

main()
