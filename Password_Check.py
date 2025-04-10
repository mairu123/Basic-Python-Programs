correct_password = "UmairRiaz123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Please Enter Your Password:   ")
    if password == correct_password:
        print("Password is Correct! Access Granted.")
        break
    else:
        attempts += 1
        if attempts == max_attempts:
            print("Maximum Attempts Exceeded. Access Denied.")
        else:
            print(f"Incorrect Password. You have {max_attempts - attempts} attempt(s) left.")
