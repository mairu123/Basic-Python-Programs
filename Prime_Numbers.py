def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
try:
    limit = int(input("Enter a number greater than 1: "))
    if limit <= 1:
        print(" Please enter a number greater than 1.")
    else:
        print(f"\nPrime numbers from 1 to {limit} are:")
        for i in range(1, limit + 1):
            if is_prime(i):
                print(i, end=' ')
except ValueError:
    print(" Invalid input. Please enter a valid integer.")
