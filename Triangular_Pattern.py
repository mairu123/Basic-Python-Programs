# Program for drawing the triangular pattern of * by taking input from user 
# Program uses a draw_triangle function that includes simple and nested loop 
def draw_triangle(height, position):
    if position.lower() == "left":
        for i in range(1, height + 1):
            print("*" * i)
        return True
    elif position.lower() == "right":
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            stars = "*" * i
            print(spaces + stars)
        return True
    elif position.lower() == "top":
        for i in range(height, 0, -1):
            print("*" * i)
        return True
    else:
        print(" Invalid position! Please choose 'top', 'left', or 'right'.")
        return False
while True:
    try:
        height = int(input("\n Enter the height of the triangle: "))   
        # Asks for position until its valid
        while True:
            position = input(" Enter the position (top, left, right): ")
            if draw_triangle(height, position):
                break  # will stop the loop if the input is correct
        # contiue or asks user to perform or execute again
        print("\n🔁 Do you want to draw another triangle?")
        print("1. Yes")
        print("2. No")
        choice = input(" Enter your choice (1 or 2): ")
        if choice != '1':
            print("👋 Exiting the program. Goodbye!")
            break
    except ValueError:
        print(" Please enter a valid number for height.")
