import operations

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a number.")

def get_operation():
    operation_choices = ["1", "2", "3", "4", "5"]
    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice in operation_choices:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def main():
    while True:
        print("\\nWelcome to the Calculator App!")
        print("Please select an operation")
        print("1. Addition\\n2. Subtraction\\n3. Multiplication\\n4. Division\\n5. Quit")

        choice = get_operation()

        if choice == 5:
            print("Goodbye! Thanks for using the Calculator App.")
            break
        
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == 1:
                result = operations.add(num1, num2)
                operation = "+"
            elif choice == 2:
                result = operations.subtract(num1, num2)
                operation = "-"
            elif choice == 3:
                result = operations.multiply(num1, num2)
                operation = "*"
            elif choice == 4:
                result = operations.divide(num1, num2)
                operation = "/"

            print(f"Result: {num1} {operation} {num2} = {result}")

        except ValueError as e:
            print(e)

        if input("Do you want to perform another calculation? (yes/no); ").lower() != "yes":
            print("Goodbye! Thanks for using the Calculator App.")
            break

if __name__ == "__main__":
    main()

