from functools import wraps

def document(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''i am wrapper'''
        print(f'this is a document of {func.__doc__}')
        print(f'i call its {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@document
def multi(x,y):
    '''multipy two number'''
    return x*y

print(multi(10,5))
print(multi.__doc__)
help(multi)