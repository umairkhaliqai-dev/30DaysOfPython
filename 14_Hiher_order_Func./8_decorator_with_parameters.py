# If the original function takes arguments, the wrapper function inside the decorator must accept *args and **kwargs to pass those arguments correctly to the original function.
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')

def smart_divide(func):
    def wrapper(a, b):
        print(f"Dividing {a} by {b}")
        if b == 0:
            print("Cannot divide by zero!")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    return a / b

print(divide(10, 2))  # Output: Dividing 10 by 2 \n 5.0
print(divide(5, 0))   # Output: Dividing 5 by 0 \n Cannot divide by zero!