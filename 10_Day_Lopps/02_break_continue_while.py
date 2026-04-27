# break: Exits the loop immediately.
num = 0
while num < 3:
    num += 1
    if num == 2:
        break  # Loop stops here
    print(f"Break ex: {num}")  # Only prints 1'

print()
# continue: Skips the rest of the code for the current iteration and jumps to the next.

num = 0
while num < 3:
    num += 1
    if num == 2:
        continue  # Skips print for 2
    print(f"Continue ex: {num}")  # Prints 1, 3