#Basic Calculator Using python
# Program for perfoming Basic Mathematical Calculations

def perform_operation(num1, num2, operation):
    if operation == 'add':
        print("Sum of the two numbers is:", num1 + num2)
        return True
    elif operation == 'sub':
        print("Subtraction of the two numbers is:", num1 - num2)
        return True
    elif operation == 'mul':
        print("Multiplication of the two numbers is:", num1 * num2)
        return True
    elif operation == 'div':
        if num2 == 0:
            print("Division by zero is not allowed.")
            return False
        else:
            print("Division of the two numbers is:", num1 / num2)
            return True
    else:
        print(" Invalid operation! Please choose from: add, sub, mul, div.")
        return False


while True:
    try:
        num1 = int(input("\n Enter your first number: "))
        num2 = int(input(" Enter your second number: "))

        # continuues loop intil the correct input has been taken
        while True:
            print("\nChoose operation:")
            print("add - Addition")
            print("sub - Subtraction")
            print("mul - Multiplication")
            print("div - Division")
            operation = input(" Enter operation: ").lower()

            if perform_operation(num1, num2, operation):
                break  # break the loop if the input value is valid

        # Ask if the user wants to perform another calculation
        print("\n🔁 Do you want to perform another calculation?")
        print("1. Yes")
        print("2. No")
        choice = input(" Enter your choice (1 or 2): ")

        if choice != '1':
            print(" Exiting the calculator. Have a great day!")
            break

    except ValueError:
        print(" Invalid input! Please enter valid integers.")
