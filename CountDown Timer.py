import time
def start_countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print(" Time's up!")
while True:
    try:
        seconds = int(input("\n Enter the countdown time in seconds: "))
        if seconds <= 0:
            print("Please enter a positive number for seconds.")
            continue
        start_countdown(seconds) 
        print("\n🔁 Do you want to start another countdown?")
        print("1. Yes")
        print("2. No")
        choice = input(" Enter your choice (1 or 2): ")
        if choice != '1':
            print(" Exiting the countdown timer. Goodbye!")
            break
    except ValueError:
        print("❗ Invalid input! Please enter a valid integer.")
