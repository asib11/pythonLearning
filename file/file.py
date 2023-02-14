'''old technique
file = open('read.txt', 'r')
print(file.read())
print(file.readline())
print(file.readlines())
file.close()'''

with open('read.txt') as file:
    print(file.read())
    print(file.readline())
    print(file.readlines()) 
