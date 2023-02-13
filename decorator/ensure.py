from functools import wraps

def use_first_args(value):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                return f'first args needs to be {value}'
            return fn(*args, **kwargs)
        return wrapper
    return inner

@use_first_args(10)
def summation(x, y):
    return x+y

print(summation(10, 20))
print(summation(20, 10))