#argument unpack
def calculations(*args):
    total = 0
    for i in args:
        total += i
    return total

num = [1,2,32,13,4,6,7]
print(f'total sum is: {calculations(*num)}')

#keyword unpack

def dictionary_make(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} is my choice {value}')

dic = dict(asib = 14, hamza = 'gai', opu =10 )
print(dictionary_make(**dic))

# name parameter,*args, default parameter, **kwargs

def display_info(a, b, *args, instructor="asib", **kwargs):
   return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, 4, last_name="prema", job="coding"))