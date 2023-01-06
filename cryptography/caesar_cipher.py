import pdb
text = input('input a string: ')
key = int(input('input a key: '))
convert_ascii = []
encrypted = []
pdb.set_trace()
for c in text:
    convert_ascii.append(ord(c)) 
#print(convert_ascii) my name is asib
for i in convert_ascii:
    if i==32:
        encrypted += chr(i)
    elif i>=65 or i<=90:
        encrypted += chr(((i)+key-65)%26+65)
    elif i>=97 or i<=122:
        encrypted += chr(((i)+key-97)%26+97)
print(encrypted)
print(f"encrypted: {''.join(encrypted)}")

decrypted = []
for j in encrypted:
    if j==' ':
        decrypted +=j
    else:
        decrypted += chr((ord(j)-key-97)%26+97)
print(f"decrypted: {''.join(decrypted)}")