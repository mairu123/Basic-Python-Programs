# Creating a dictionary with multiple person profiles
profiles = {}

# Ask how many profiles the user wants to add
try:
    num_profiles = int(input("How many profiles do you want to add? "))
    
    if num_profiles <= 0:
        print(" Please enter a number greater than 0.")
    else:
        for i in range(num_profiles):
            name = input(f"Enter name for profile {i + 1}: ").strip()
            while name == "":
                print(" Name cannot be empty.")
                name = input(f"Please re-enter name for profile {i + 1}: ").strip()
            
            age = input(f"Enter age for {name}: ").strip()
            while not age.isdigit():
                print(" Age must be a valid number.")
                age = input(f"Please re-enter age for {name}: ").strip()
            
            occupation = input(f"Enter occupation for {name}: ").strip()
            while occupation == "":
                print(" Occupation cannot be empty.")
                occupation = input(f"Please re-enter occupation for {name}: ").strip()

            # Add profile to the dictionary
            profiles[name] = {'Age': int(age), 'Occupation': occupation}
        
        # Print all profiles
        print("\n All profiles added:")
        for name, details in profiles.items():
            print(f"\nName: {name}")
            for key, value in details.items():
                print(f"{key}: {value}")

except ValueError:
    print(" Invalid input! Please enter a valid number.")
