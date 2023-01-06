from addition import additionn as jog
def multipication(*args):
    
    add = 1
    for i in args:
        add *=i
    return(f'{jog(*args)} multipication is: {add}')

#print(jog(10,2,3,4,5))
print(multipication(10,2,3,4,5))