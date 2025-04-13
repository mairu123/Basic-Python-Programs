# This program uses list data structure to store and then removes duplicates by using sets

# Ask the user how many elements they want to add
try:
    num_elements = int(input("How many elements do you want to add? "))
    
    if num_elements <= 0:
        print(" Please enter a number greater than 0.")
    else:
        input_list = []

        # Take input from the user for each element with error handling
        for i in range(num_elements):
            while True:
                try:
                    element = int(input(f"Enter element {i + 1}: "))
                    input_list.append(element)
                    break  # Exit the loop if the input is valid
                except ValueError:
                    print(" Invalid input! Please enter a valid integer for element.")

        # Dictionary to store the frequency of each number
        frequency = {}

        # Count occurrences of each number
        for number in input_list:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1

        # Display the repetition count
        for number, count in frequency.items():
            if count > 1:
                print(f"Number {number} is repeated {count} times.")

        # Remove duplicates by converting the list to a set
        unique_list = list(set(input_list))

        # Display the list after removing duplicates
        print("\nList after removing duplicates:", unique_list)

except ValueError:
    print(" Invalid input! Please enter a valid integer for the number of elements.")
