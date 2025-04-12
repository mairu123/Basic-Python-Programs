# Simple Sign up And Login program
# Function for signing up (creating a new account)
def sign_up():
    print("\n Sign up - Create your new account")
    username = input(" Enter your username: ")
    password = input(" Enter your password: ")
    return username, password

# Function for logging in
def login(existing_username, existing_password):
    username = input("\n Enter your username: ")
    
    # Check if username is correct
    if username != existing_username:
        print(" Username is invalid.")
        return False

    password = input(" Enter your password: ")
    
    # Check if password is correct
    if password != existing_password:
        print(" Password is wrong.")
        return False
    
    print(" Login successful! Welcome to your account.")
    return True

while True:
    try:
        print("\nWelcome! Please choose an option:")
        print("1. Sign In (Create a new account)")
        print("2. Login (Use an existing account)")
        choice = input(" Enter your choice (1 or 2): ")

        if choice == '1':
            # for signup
            stored_username, stored_password = sign_up()

            print("\nYour account has been created successfully!")
            print("Please log in to continue.")

            # Login after sign up
            if login(stored_username, stored_password):
                break  # Will stops if the login is sucessful

        elif choice == '2':
            # Login process
            if login(stored_username, stored_password):
                break  # Will stops if the login is sucessful
        else:
            print(" Invalid choice. Please choose option 1 or 2.")
        # For Continue
        print("\n Do you want to continue?")
        print("1. Yes")
        print("2. No")
        continue_choice = input(" Enter your choice (1 or 2): ")
        if continue_choice != '1':
            print(" Exiting the program. Goodbye!")
            break
    except Exception as e:
        print(f" Something went wrong: {e}. Please try again.")
