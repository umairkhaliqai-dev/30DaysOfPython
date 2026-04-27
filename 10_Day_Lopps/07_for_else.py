# The else block runs only if the loop completes normally (i.e., was not stopped by a break).
# Example: Search for a number
search_for = 5
for i in range(3):  # Loop runs 0,1,2
    if i == search_for:
        print("Found!")
        break
else:
    print(f"{search_for} not found in range.")  # <-- This will execute
# Output: 5 not found in range.

