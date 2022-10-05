def calculation(a,b,c):
    return a+b+c
print(calculation(10,6,5))

#clean code

def mistake(x):
    if x%2 == 0:
        return 'even'
    return 'odd'  #no need to use else
print(mistake(4))
print(mistake(7))

#other made mistake

def array(number):
    total = 1
    for i in number:
        total *=i
       # return total "if you write code here, you just retun value 1st list of index"
    return total
print(array([1,2,3,4,5]))