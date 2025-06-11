import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")

    while True:
        choice = input("Enter choice (1-7) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif choice == '5':
                print(f"Result: {math.pow(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            if num >= 0:
                print(f"Result: {math.sqrt(num)}")
            else:
                print("Error: Square root of negative number is not defined.")

        elif choice == '7':
            num = float(input("Enter number: "))
            if num > 0:
                print(f"Result: {math.log(num)}")
            else:
                print("Error: Logarithm of non-positive number is not defined.")

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    scientific_calculator()