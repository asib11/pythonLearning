def get_number(func):
    def wrapper(*args , **kwargs):
        return func(*args,**kwargs)
    return wrapper

@get_number
def single_name(name):
    print(f'my nick name is {name}')

@get_number
def full_name(first_name, last_name):
    print(f'my first name is {first_name} and last  name is {last_name}.')

single_name('aSib')
full_name('asib', 'ahmed')