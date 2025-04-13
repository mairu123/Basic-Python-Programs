# This program takes user input and stores cordiantes in tuple
# Basic Program that uses tuple dafta structure
def get_coordinate(Axis):
    while True:
        try:
            value = int(input(f"Enter {Axis} coordinate: "))
            return value
        except ValueError:
            print(f" Invalid input! Please enter a valid number for {Axis}.")

# main program 
print(" Enter the 3D coordinates (X, Y, Z):")

x = get_coordinate("X")
y = get_coordinate("Y")
z = get_coordinate("Z")

coordinates = (x, y, z)  # tuple to store values

print("\n Your coordinates stored in a tuple are:", coordinates)
