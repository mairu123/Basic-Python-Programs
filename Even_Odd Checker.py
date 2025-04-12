#Even or odd checker
# Program takes input from user and tells wether it is even or odd number

def check_even_odd(number):
    # Check condition  that number is zero or negative
    if number <= 0:
        print(" The number must be positive and non-zero.")
        return False
    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f" {number} is an Odd number.")
    return True

while True:
    try:
        number = int(input("\n Enter a positive number to check if it is even or odd: "))
        # Handle negative number or zero input
        if number <= 0:
            print(" Invalid input! The number must be positive and non-zero. Please try again.")
            continue

        # Call function to check even or odd
        if check_even_odd(number):
            # Ask user if they want to continue
            print("\n Do you want to check another number?")
            print("1. Yes")
            print("2. No")
            choice = input(" Enter your choice (1 or 2): ")

            if choice != '1':
                print(" Exiting the program. Goodbye!")
                break
        else:
            continue  # If number is invalid (negative or zero), ask again

    except ValueError:
        print(" Invalid input! Please enter a valid integer.")
