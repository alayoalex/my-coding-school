def to_uppercase(func):
    """Convert to uppercase and return to uppercase."""
    # Adding this line, will call passed function to get text
    text = func()
    if not isinstance(text, str):
        raise TypeError("Not a string type")
    return text.upper()

def say():
    return "welcome"

@to_uppercase
def hello():
    return "hello"

#print(say())
#print(hello())

#print(to_uppercase(say))
#print(hello())