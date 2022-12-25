def error_detected(name, age):
    if type(name) is not str:
        raise TypeError('text must be string')
    if type(age) is not int:
        raise TypeError('age must be integer')
    print(f'my name {name} and age is {age}')


error_detected('asib',25)
#error_detected(25,'asib')
error_detected('asib',25.5)
