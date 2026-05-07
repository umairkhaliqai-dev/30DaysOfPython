# Errors detected during execution are called Exceptions. try...except blocks are used to catch and handle these errors, preventing the program from crashing abruptly. 
# You can use else (runs if no error) and finally (always runs).
# Example: Division by zero handling
try:
    numerator = 10
    denominator = int(input("Enter a number to divide 10: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division successful.")
finally:
    print("Execution finished.")