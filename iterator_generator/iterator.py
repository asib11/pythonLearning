def make_for(iterator, func):
    iterator = iter(iterator)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

square= lambda x: print(x**2)

make_for('lol',print)
make_for([1,2,3,4],square)