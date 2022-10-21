x = int(input("input number one : "))
y = int(input("input number two : "))
z = int(input("input number three : "))

if (x > y and x > z):
    print (f"{x} is largest number")
elif(y > x and y > z):
    print(f"{y} is largest number")
else:
    print(f"{z} is largest number")