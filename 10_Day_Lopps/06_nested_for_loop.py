# A loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.
for row in range(3):          # Outer loop
    for col in range(3):      # Inner loop
        print(f"({row},{col})", end=" ")
    print()  # New line after each row
# Output: (0,0) (0,1) (0,2)
#         (1,0) (1,1) (1,2)
#         (2,0) (2,1) (2,2)
