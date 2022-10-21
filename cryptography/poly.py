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


'''def decryption(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i])) % 26
        x += 65
        orig_text.append(chr(x))
    return ("".join(orig_text))'''

string = input("Enter the message: ").upper()
keyword = input("Enter secret key: ").upper()
key = generateKey(string, keyword)
encrypt_text = encryption(string, key)
print("Encrypted message:", encrypt_text)
#print("Decrypted message:", decryption(encrypt_text, key))