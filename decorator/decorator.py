def calculation(a, b):
    def sum():
        return a+b
    print( 'done')
    return sum
def square(x):
    return x*x
    
ok = calculation(20,square(2))
print(ok())
