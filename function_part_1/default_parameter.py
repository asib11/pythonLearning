def name(first='oh',last = 'no'):
    return f'your name is {first} {last}'

print(name())
print(name(last ='ahmed',first ='asib'))

x = input('your 1st input: ')
y = input('your 2nd input: ')

print(name(y,x))

def power(num,power=2):
    return num**power

print(power(4,5))
print(power(5))