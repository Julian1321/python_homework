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
def say_hello():
    print("Hello!")


@logger_decorator
def check_numbers(*args):
    print("Numbers:", args)
    return True


@logger_decorator
def get_decorator(**kwargs):
    print("Keyword arguments:", kwargs)
    return logger_decorator


if __name__ == "__main__":
    say_hello()
    check_numbers(1, 2, 3)
    get_decorator(name="Julian", course="Python")