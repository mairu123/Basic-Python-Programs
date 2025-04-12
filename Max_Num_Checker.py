def get_max_number(numbers):
    return max(numbers)

while True:
    try:
        count = input(" How many numbers do you want to compare? ").strip()

        while not count.isdigit() or int(count) <= 1:
            print(" Please enter a valid number greater than 1.")
            count = input(" How many numbers do you want to compare? ").strip()

        count = int(count)
        numbers = []

        for i in range(count):
            while True:
                try:
                    num = float(input(f" Enter number {i+1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print(" Invalid input. Please enter a numeric value (e.g., -3.5, 0, 7).")

        maximum = get_max_number(numbers)
        print(f"\n The maximum number among the entered values is: {maximum}")

    
        print("\ Do you want to try again?")
        print("1. Yes")
        print("2. No")
        choice = input(" Enter your choice (1 or 2): ")

        while choice not in ['1', '2']:
            print("❗ Invalid choice. Please enter 1 to continue or 2 to exit.")
            choice = input(" Enter your choice (1 or 2): ")

        if choice == '2':
            print(" Exiting the program. See you next time!")
            break

    except Exception as e:
        print(f"❗ Unexpected error occurred: {e}")
