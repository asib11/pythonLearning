def calculations(*args):
    total = 0
    for i in args:
        total += i
    return total
print(f'total sum is: {+calculations(10,2,4,5,3,56)}') #its a tuple

def combine_words(string,**kwargs):  #its a dictionary
    if 'prefix' in kwargs:
        return kwargs['prefix']+string
    elif 'suffix' in kwargs:
        return string+kwargs['suffix']
    return string

print(combine_words('man', prefix = 'wo'))
print(combine_words('man', suffix = 'kind'))
print(combine_words('asib'))