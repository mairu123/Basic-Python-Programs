# program that take two numbers from user and prints the even number with in the specific range

def print_even_numbers(start, end):
    # condition for correct input of range , must be sequenced
    if start > end:
        print(" The start number should be less than the end number.")
        return
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)
while True:
    try:
        # Take start and end numbers as input from the user
        start = int(input("\n Enter the start number of the range: "))
        end = int(input(" Enter the end number of the range: "))
        # condition added for negative input
        if start < 0 or end < 0:
            print(" Negative numbers are not allowed. Please enter positive numbers.")
            continue
        print(f"\n Printing even numbers from {start} to {end}:")
        print_even_numbers(start, end)
        # for continue execution
        print("\n Do you want to run the loop again?")
        print("1. Yes")
        print("2. No")
        choice = input(" Enter your choice (1 or 2): ")
        if choice != '1':
            print(" Exiting the program. Goodbye!")
            break
    except ValueError:
        print(" Invalid input! Please enter valid integers for start and end.")
