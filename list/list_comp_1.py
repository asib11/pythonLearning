item = [1,2,3,4,5,6]

square = [i*i for i in item]
print (square)

name = ['cow','ox','elephent','goat']
uppername =[names.upper() for names in name]
print(uppername)

multipy = [j*10 for j in range(10)]
print(multipy)

string_number = [str(num) for num in item]
print(string_number)

result = ['even' if num%2 ==0 else 'odd' for num in item]
print (result)