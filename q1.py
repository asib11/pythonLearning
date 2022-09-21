import random

def encrypt(original, key=None):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if key is None:
        l = list(alpha)
        random.shuffle(l)
        key = ''.join(l)
    new = []
    for letter in original:
        if letter == ' ':
            new.append(letter)
        else:
            new.append(key[alpha.index(letter)])
    return [''.join(new), key]



def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))


def encryption(string, key):
    encrypt_text = []
    for i in range(len(string)):
        if string[i] !=' ':
            x = (ord(string[i]) + ord(key[i])) % 26
            x += 65
            encrypt_text.append(chr(x))
        elif string[i] == ' ':
            encrypt_text.append(string[i])

    return ("".join(encrypt_text))

e = encrypt(input('user input:'), None)
print('mono encrypted message: '+ str(e))
print('poly input:'+str(e[0]))
string = str(e[0]).upper()
#string=string
keyword = input("Enter poly secret key: ").upper()
#keyword=keyword
key = generateKey(string, keyword)
encrypt_text = encryption(string, key)
print("Poly Encrypted message:", encrypt_text.lower())
