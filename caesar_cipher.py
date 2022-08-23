text = input("enter a string :")
shift =int(input("shift number :"))
ascii_values = []
result=[]
for character in text:
    ascii_values.append(ord(character))
for i in ascii_values:
    if i==32:
        result += chr(i)
    elif i>=65 and i<=90:
        result += [chr((((i)+shift-65)% 26)+65)]
    else:
       result += [chr((((i)+shift-97)% 26)+97)] 
print(''.join(result))