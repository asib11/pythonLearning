def make_function(fn):
    def wrapper():
        print('Hello Asib')
        fn()
        print('well done')
    return wrapper

@make_function # if you use this you will not need to define veriable
def tell():
    print('give me my money')

tell()

