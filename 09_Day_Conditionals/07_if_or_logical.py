# Core idea: At least one condition connected by or must be True.
is_teacher = False
is_admin = True
if is_teacher or is_admin:
    print("You have access to gradebook.")  # is_admin is True