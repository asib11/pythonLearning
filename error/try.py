def division(a,b):
    try:
        result = a/b
    except ZeroDivisionError as err:
        print('0 is not allow')
        print(err)
    except TypeError as err:
        print('a or b must be ints or float')
        print(err)
    else:
        print(result)

division(1,2)
division(0,1)
division(1,0)
division(1,'a')