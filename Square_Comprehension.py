# Taking input from the user for the number of elements
while True:
    try:
        num_elements = int(input("How many numbers do you want to square? "))
        if num_elements <= 0:
            print(" Please enter a number greater than 0.")
        else:
            break  # Exit the loop if the input is valid
    except ValueError:
        print(" Invalid input! Please enter a valid integer for the number of elements.")

input_list = []

# Take input from the user for each element with error handling
for i in range(num_elements):
    while True:
        try:
            element = int(input(f"Enter number {i + 1}: "))
            input_list.append(element)
            break  # Exit the loop if the input is valid
        except ValueError:
            print(" Invalid input! Please enter a valid integer for element.")

# List comprehension to calculate the square of each number
square_list = [x ** 2 for x in input_list]

# Display the result
print("\nList of squares:", square_list)
