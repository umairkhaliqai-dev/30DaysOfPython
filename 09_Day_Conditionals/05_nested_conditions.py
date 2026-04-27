# Core idea: Place an if statement inside another if statement.


is_weekend = True
has_homework = False
if is_weekend:
    if has_homework:
        print("Do homework first, then relax.")
    else:
        print("Relax, it's the weekend!")  # This runs