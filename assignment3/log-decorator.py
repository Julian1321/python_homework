from functools import wraps

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        with open("decorator.log", "a") as file:
            file.write(f"Function: {func.__name__}\n")
            file.write(f"Arguments: {args}\n")
            file.write(f"Keyword arguments: {kwargs}\n")
            file.write(f"Return value: {result}\n")
            file.write("_______________________\n")

        return result

    return wrapper

@logger_decorator
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3))