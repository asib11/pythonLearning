key_matrix = [[0] * 4 for i in range(4)] 
message_list = [[0] for i in range(4)] 
cipher_matrix = [[0] for i in range(4)] 

def get_key(key): 
    k = 0
    for i in range(4): 
        for j in range(4): 
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1
 
def encrypt(message_list): 
    for i in range(4): 
        for j in range(1): 
            cipher_matrix[i][j] = 0
            for x in range(4): 
                cipher_matrix[i][j] += (key_matrix[i][x] * message_list[x][j]) 
            cipher_matrix[i][j] = cipher_matrix[i][j] % 26
  
def HillCipher(message, key): 

    get_key(key) 
    for i in range(4): 
        message_list[i][0] = ord(message[i]) % 65
    encrypt(message_list) 

    CipherText = [] 
    for i in range(4): 
        CipherText.append(chr(cipher_matrix[i][0] + 65)) 
    print("Ciphertext: ", "".join(CipherText)) 


if __name__ == "__main__":
    message = "WARR"
    key = "SDTMOFGYBNQKURPW"
    HillCipher(message, key) 
