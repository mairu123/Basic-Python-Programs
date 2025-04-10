height = 5

print("Left-Aligned Triangle:")
for i in range(1, height + 1):
    print("*" * i)

print("\nRight-Aligned Triangle:")
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * i)

print("\nCenter-Aligned Triangle:")
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1))

