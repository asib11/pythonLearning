text = input("enter a string :")
key =int(input("key number :"))
ascii_values = [ord(character) for character in text]
encrypted=[]

for i in ascii_values:
    if i==32:
        encrypted += chr(i)
    elif i>=65 and i<=90:
        encrypted += [chr(((i)+key-65)% 26+65)]
    else:
       encrypted += [chr(((i)+key-97)% 26+97)] 
print(''.join(encrypted)) 