def main():
    try:
     num1 = (input("Enter first number:"))
     num1 = int(num1)

     num2 = (input("Enter Second number:"))
     num2 = int(num2)
     total = num1 + num2 
     print(f"{num1} + {num2} = {total}")

    except ValueError:
     print("Please enter a  number")
main()