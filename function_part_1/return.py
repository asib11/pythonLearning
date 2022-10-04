from random import random
def coin():
    if random()> 0.5:
        return 'heads'
    else:
        return 'tails'
print(coin())

#same name of function call below, its overwright