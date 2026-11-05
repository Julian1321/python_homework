from functools import wraps

def type_converter(type_of_output):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return type_of_output(result)
        return wrapper
    return decorator


@type_converter(str)
def return_int():
    return 123


@type_converter(int)
def return_string():
    return "hello"

if __name__ == "__main__":
    print(return_int())
    print(type(return_int()))

    try:
        print(return_string())
    except ValueError as e:
        print("ValueError caught:", e)