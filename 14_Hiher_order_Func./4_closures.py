# A closure is a nested function that captures and remembers values from its enclosing scope (non-global variables) even after the outer function has finished executing.
def outer_func(msg):
    # This variable is enclosed
    message = msg
    
    def inner_func():
        print(message)
    
    return inner_func

my_func = outer_func("Hello, World!")
my_func()  # Output: Hello, World! (remembers 'message')
print()
# example
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20