# Taking input for the keys list
try:
    num_keys = int(input("How many keys do you want to enter? "))
    keys = []
    
    for i in range(num_keys):
        while True:
            key = input(f"Enter key {i + 1}: ")
            keys.append(key)
            break

    # Taking input for the values list
    values = []
    
    for i in range(num_keys):
        while True:
            try:
                value = input(f"Enter value for key {keys[i]}: ")
                values.append(value)
                break
            except ValueError:
                print(" Invalid input! Please enter a valid value.")

    # Creating the dictionary using zip
    my_dict = dict(zip(keys, values))

    # Display the resulting dictionary
    print("\nCreated Dictionary:", my_dict)

except ValueError:
    print(" Invalid input! Please enter a valid integer.")
