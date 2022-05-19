number = input("input number : ")

if number :
    number = int(number)
    if (number > 0):
        print(f"{number} is positive number")
    elif number == 0:
        print ("this is 0")
    else:
        print(f"{number} is negative")
else:
    print("enter the value")