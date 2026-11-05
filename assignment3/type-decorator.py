from functools import wraps

def type_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [int(arg) for arg in args]
        
        new_kwargs = {
            key: int(value)
            for key, value in kwargs.items()
        }

        return func(*new_args, **new_kwargs)

    return wrapper

@type_decorator
def add_numbers(a, b):
    return a + b

print(add_numbers("5", "3"))