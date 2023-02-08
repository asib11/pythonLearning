def summation(max):
    n=0
    while n <= max:
        yield n
        n +=2
sum = summation(6)
add = 0
for i in sum:
    add +=i
print(add)