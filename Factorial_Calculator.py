# Factorial Calculator
# This program takes input from user and returns its factorial
def calculate_factorial(number):
    # Check if the number is negative or zero
    if number < 0:
        print(" Factorial is not defined for negative numbers. Please enter a positive integer.")
        return None
    elif number == 0:
        return 1  # By  Math rules that factorial of zero is 1
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial
while True:
    try:
        number = int(input("\n Enter a positive integer to calculate its factorial: "))
        # check for  negative number or zero input
        if number < 0:
            print(" Factorial is not defined for negative numbers. Please try again with a positive integer.")
            continue
        # Call function to calculate factorial
        factorial = calculate_factorial(number)
        if factorial is not None:
            print(f" The factorial of {number} is: {factorial}")
        # To take new input 
        print("\nDo you want to calculate the factorial of another number?")
        print("1. Yes")
        print("2. No")
        choice = input(" Enter your choice (1 or 2): ")
        if choice != '1':
            print(" Exiting the program. Goodbye!")
            break
    except ValueError:
        print(" Invalid input! Please enter a valid integer.")
