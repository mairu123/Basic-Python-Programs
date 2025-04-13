# storing name of movies by taking user input
# use of data structure list 
try:
    count = int(input("How many movies do you want to store? "))
    
    if count <= 0:
        print(" Please enter a number greater than 0.")
    else:
        movies = []
        for i in range(1, count + 1):
            name = input(f"Enter name of movie {i}: ").strip()
            while name == "":
                print(" Movie name cannot be empty.")
                name = input(f"Please re-enter name of movie {i}: ").strip()
            movies.append(name)

        # statement will show all movies of users with indexes
        print("\n🎬 Your Movie List:")
        index = 1
        for movie in movies:
            print(f"{index}. {movie}")
            index += 1

except ValueError:
    print(" Invalid input! Please enter a valid number.")
