# You can stack multiple decorators on top of a single function. They are applied from the bottom up (the one closest to the function runs first).

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello"

print(text())  # Output: <b><i>Hello</i></b>