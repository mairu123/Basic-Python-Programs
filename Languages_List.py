# This program uses list data structure to save languages known by user and adds  more to it

# Initial set of known languages
languages = {"Python", "Java", "C++", "JavaScript"}

print(" Languages I know before adding:", languages)

# Ask how many languages user wants to add
try:
    count = int(input("How many languages do you want to add? "))
    
    if count <= 0:
        print(" Please enter a number greater than 0.")
    else:
        # Loop to add languages
        for i in range(count):
            new_language = input(f"Enter language {i + 1}: ").strip()
            
            # Validation: check if input is not empty
            while new_language == "":
                print(" Language name cannot be empty.")
                new_language = input(f"Please enter a valid language for {i + 1}: ").strip()

            # Add the new language to the set
            languages.add(new_language)

        print(" Updated set of languages I know:", languages)

except ValueError:
    print(" Invalid input! Please enter a valid number.")

